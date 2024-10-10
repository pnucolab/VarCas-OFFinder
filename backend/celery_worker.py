from celery_app import celery_task
import os
import subprocess
from fastapi import UploadFile, File
import time
from datetime import datetime
from io import StringIO
import pandas as pd
from target_genome import Target_Genome, ref_paths
from concurrent.futures import ThreadPoolExecutor
import re
import duckdb


@celery_task.task
def off_target(ticket,output_file_name, file_name, output_vcf, ref_path,  pam_line, target_line):
     time.sleep(5)
     con = duckdb.connect("task_time.db")
     con.execute("CREATE TABLE IF NOT EXISTS task_times (id VARCHAR, created_at TIMESTAMP, finished_at TIMESTAMP)")

     created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
     '''with open(output_file_name+'startt', 'w') as file:
          file.write(created_at)'''
     
     allelic_off_target_files = [] 
     tab_index = ['tabix', '-p', 'vcf', output_vcf]
     tab_result = subprocess.run(['tabix', '-p', 'vcf', file_name], stdout=subprocess.DEVNULL, stderr=subprocess.PIPE,text=True )
     errmessage = tab_result.stderr
     if "is not BGZF" in errmessage:
          if ".gz" in file_name:
               subprocess.run(['gunzip', file_name])
               unzip_file = file_name[:-3]
               subprocess.run(["bgzip", "-c", unzip_file], stdout=open(output_vcf, "wb"))
               subprocess.run(tab_index, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
               
          else:
           subprocess.run(["bgzip", "-c", file_name], stdout=open(output_vcf, "wb"))
           subprocess.run(['tabix', '-p', 'vcf', output_vcf], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
     

     vcfallelic = ["vcfallelicprimitives", output_vcf]
     norm = ["bcftools", "norm", "-m-"]
     vcfcreatemulti = ["vcfcreatemulti"]
     bgzip = ["bgzip", "-c"]
     result_file = "output_"+output_vcf
     bcftools_index = ["bcftools", "index", result_file]
     with open(result_file, 'wb') as output_file:
           vcfallelic_process = subprocess.Popen(vcfallelic, stdout=subprocess.PIPE)
           norm_process = subprocess.Popen(norm, stdin=vcfallelic_process.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
           vcfcreatemulti_process = subprocess.Popen(vcfcreatemulti, stdin=norm_process.stdout, stdout=subprocess.PIPE)
           bgzip_process = subprocess.Popen(bgzip, stdin=vcfcreatemulti_process.stdout, stdout=output_file)
     bgzip_process.communicate()
     subprocess.run(bcftools_index, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
     tab_index2 = ['tabix', '-p', 'vcf', result_file]
     subprocess.run(tab_index2, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
     vcf2tsv_cmd = ['vcf2tsv', result_file]
     result  = subprocess.run(vcf2tsv_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text = True)
     output = result.stdout
     output_file = StringIO(output)
     dtype = {
       'INFO': str,
       'FORMAT': str,
      }   
     df = pd.read_csv(output_file, sep ='\t', dtype=dtype, low_memory=False)
     unique_s = df['#CHROM'].unique()
     unique_s_str = [str(item) for item in unique_s]
     """if re.search(r'\bpepper\b', ref_path):
          chrom_id = 'CM'
     elif re.search(r'\b(?:dempsey|human38|human19)\b', ref_path):
          chrom_id = 'chr'"""
     parent_directory = ref_path
     components = parent_directory.split(os.sep)
     first_two_components = os.sep.join(components[:3])
     fai_files = [f for f in os.listdir(first_two_components) if f.endswith('.fai')]
     if fai_files:
          for fai_file in fai_files:
               fai_file_path = os.path.join(first_two_components, fai_file)
               with open(fai_file_path, 'r') as file:
                    lines = file.readlines()
                    if len(lines) >= 2:
                         chrom_id = lines[1][:2] 
                    else:
                         chrom_id = 'ch'     
     chrom_item = [item for item in unique_s_str if chrom_id in item or item[0].isdigit()]
     for column_name in chrom_item:
         command = ["bcftools", "view", result_file, column_name ]
         output = f"{output_vcf}{column_name}.vcf"
         with open(output, 'w') as output:
               process = subprocess.Popen(command, stdout=output)
               process.communicate()
     input_files = [output_vcf+item + '.vcf' for item in chrom_item]
     allfastafiles = output_vcf+'.fasta'     
     def process_input_file(input_file):
           vcf2fasta_cmd = ['vcf2fasta', '-f', ref_path, '-p', allfastafiles, '-n', 'NAN', input_file]
           subprocess.run(vcf2fasta_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
           time.sleep(2)  
     def process_input_files(input_files):
          for input_file in input_files:
               process_input_file(input_file)
     
     process_input_files(input_files)    
         
     fasta_files = [f for f in os.listdir() if f.startswith(allfastafiles)]
     combined_content = ''
     query_input = output_vcf+'_input.txt'
     for i in range(len(fasta_files)):
            target_path = "/app/"+fasta_files[i]+"\n"
            
            with open(query_input, "w") as file:
                 pass   

            with open(query_input, "w") as file:
                file.write(target_path)
                file.write(pam_line)
            with open(query_input, 'r') as file:
                  lines = file.readlines()
                  lines[2:] = target_line
            with open(query_input, 'w') as file:
                  for line in lines:
                       file.write(line)
            off_target_output = fasta_files[i]+'.txt'

            off_target_allele = ['/app/cas-offinder', query_input, 'G0', off_target_output] # G0 -GPU id 0
            subprocess.run(off_target_allele, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            allelic_off_target_files.append(off_target_output)
          
            with open(off_target_output, 'r') as file: 
                     combined_content += file.read()
            
     '''with open(output_file_name, 'w') as file:
          file.write(combined_content) ''' 

     file_content = combined_content
     db_con = duckdb.connect("off_target_result.db")
     db_con.execute("""
     CREATE TABLE IF NOT EXISTS off_target_result (
     id VARCHAR ,
     content TEXT
     )
     """)
     id_no = output_file_name
     db_con.execute("INSERT INTO off_target_result (id, content) VALUES (?, ?)", (id_no, file_content))
     result_df = db_con.execute("SELECT * FROM  off_target_result").fetchdf()
     pd.set_option('display.max_colwidth', None)
     #print(result_df)
     db_con.close()

     finished_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
     '''with open(output_file_name+'endt', 'w') as file:
          file.write(finished_at)'''
     string_id = ticket
     con.execute("INSERT INTO task_times (id, created_at, finished_at) VALUES (?, ?, ?)", (string_id, created_at, finished_at))
     dft = con.execute("SELECT * FROM task_times").fetchdf()
     #print(dft)
     con.close()

     files_to_erase =  allelic_off_target_files + fasta_files + input_files + [query_input]
    
     for file in files_to_erase:
           os.remove(file)
     
     files_to_clear = [file_name, output_vcf]
     for file in files_to_clear:
          if os.path.exists(file):
               os.remove(file)
     indexed_files = [f for f in os.listdir() if f.startswith(f'output_{file_name}')]
     for file in indexed_files:
          if os.path.exists(file):
               os.remove(file)
     
     return  {'success': True, 'created_at':created_at, 'finished_at': finished_at}