#!/usr/bin/env python
import argparse
import subprocess
from datetime import datetime
from io import StringIO
import pandas as pd
import os
import time

def compress_and_index(file_path, ref_path, query_input, device_id):

  created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
  file_name = os.path.basename(file_path)
  uploadedfile = ''
  combined_content = file_name+'_off_target_result.txt'
  try:
    with open(file_path, "rb") as file: 
        contents = file.read()
    with open(file_name, 'wb') as file_content:
        file_content.write(contents)
  except FileNotFoundError:
        print ('file not found')
  except Exception as e:
        print(f"An error occurred: {e}")
  output_vcf = file_name if file_name.endswith(".gz") else f"{file_name}.gz"
  single_multi_sample = subprocess.run(
                    ["bcftools", "query", "-l", output_vcf], 
                    capture_output=True,
                    text=True,
                    check=True
                )  
  num_samples = len(single_multi_sample.stdout.splitlines())
  if num_samples ==1:
    tabix_result = subprocess.run(
        ['tabix', '-p', 'vcf', file_name],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True
    )
    if "is not BGZF" in tabix_result.stderr:
        if file_name.endswith(".gz"):
            print("File is gzipped but not BGZF. Decompressing and recompressing...")
            subprocess.run(['gunzip', file_name])
            uncompressed_file = file_name[:-3]
            subprocess.run(["bgzip", "-c", uncompressed_file], stdout=open(output_vcf, "wb"))
        else:
            print("File is not compressed. Compressing with BGZF...")
            subprocess.run(["bgzip", "-c", file_name], stdout=open(output_vcf, "wb"))
        
        subprocess.run(['tabix', '-p', 'vcf', output_vcf], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("File is compressed and indexed.")
    else:
        print(f"File is indexed.")
    
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
    first_two_components = os.sep.join(ref_path.split(os.sep)[:-1])
    fai_files = [f for f in os.listdir(first_two_components) if f.endswith('.fai')]
    chrom_id = next((open(os.path.join(first_two_components, f)).readlines()[1][:2] for f in fai_files if len(open(os.path.join(first_two_components, f)).readlines()) >= 2), '')
    chrom_item = [item for item in unique_s_str if chrom_id in item]
    print (f'chrom_id {chrom_id}')
    print (f'chrom_item {chrom_item}')
    err_response = ''
    
    
    if  not chrom_item:
             err_response = "Error: #CHROM name mismatch between your vcf file and target organism reference genome.\
                Please make sure you select the right target organism or modify #CHROM name in your indexed reference genome \
                and try again. Visit Ensembl website to check chromosomes name of your target organism reference genome."
    
    if chrom_item:
      for column_name in chrom_item:
         command = ["bcftools", "view", result_file, column_name ]
         output = f"{output_vcf}{column_name}.vcf"
         with open(output, 'w') as output:
               process = subprocess.Popen(command, stdout=output)
               process.communicate() 
      input_files = [output_vcf+item + '.vcf' for item in chrom_item]
      allfastafiles = output_vcf+'.fasta'
      print('Fasta file generation...')
      def process_input_file(input_file):
         global error_message
         try:  
           vcf2fasta_cmd = ['vcf2fasta', '-f', ref_path, '-p', allfastafiles, '-n', 'NAN', input_file]
           subprocess.run(vcf2fasta_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE, check = True, text=True)
           time.sleep(2)
         except subprocess.CalledProcessError as e:
            stderr_message = e.stderr.strip()
            if 'not phased' in stderr_message:
                error_message = 'Error: your vcf file is not phased. Only Phased and single sample vcf is allowed.'
            elif 'unable to find FASTA index' in stderr_message:
                error_message = 'Error: Wrong target organism selection.'
            else:
                error_message = f'Error: {stderr_message}'    

      def process_input_files(input_files):
          for input_file in input_files:
               process_input_file(input_file)
     
      process_input_files(input_files)
  
    fasta_files = [f for f in os.listdir() if f.startswith(allfastafiles)]
      
    allelic_off_target_files = [] 
     
    for i in range(len(fasta_files)):
            target_path = "./"+fasta_files[i]
            with open(query_input, 'r') as file:
                lines = file.readlines()
                
            if lines and lines[0].startswith('./'):
               lines = lines[1:]
    
            
            lines.insert(0, target_path + '\n')
    
            
            with open(query_input, 'w') as file:
                file.writelines(lines)
            
            
            off_target_output = fasta_files[i]+'.txt'

            off_target_allele = ['./cas-offinder', query_input, device_id, off_target_output] # G0 -GPU id 0
            subprocess.run(off_target_allele, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            allelic_off_target_files.append(off_target_output)
    try:
        with open(combined_content,'w') as  outfile:
            for file in allelic_off_target_files:
                with open(file, 'r') as infile:
                    outfile.write(infile.read())
        print(f'off_target result:{combined_content}')
                            
    except FileNotFoundError:
                 uploadedfile = f"Error: {output_vcf} is not phased VCF file. Only Phased and single sample vcf is allowed." 
    files_to_erase =  allelic_off_target_files + fasta_files + input_files
    for file in files_to_erase:
         try:
           os.remove(file)
         except FileNotFoundError:
           single_multi_sample = subprocess.run(
                    ["bcftools", "query", "-l", output_vcf], 
                    capture_output=True,
                    text=True,
                    check=True
                )  
           num_samples = len(single_multi_sample.stdout.splitlines())
           if num_samples != 1:
               uploadedfile = f"Error: {output_vcf} is multi-sample file with {num_samples} samples. \
                      Only Phased and single sample vcf is allowed."
              
           else:
               if err_response =='':
                  if error_message !='':
                      uploadedfile = error_message
                  else:
                     uploadedfile = f"Error: {output_vcf} is not phased VCF file. Only Phased and single sample vcf is allowed."  
               else:
                 uploadedfile = err_response
    
    indexed_files = [f for f in os.listdir() if f.startswith(f'output_{file_name}') or f.endswith('.tbi')]
    for file in indexed_files:
          if os.path.exists(file):
               os.remove(file)
    files_to_clear = [file_name, output_vcf]
    for file in files_to_clear:
          if os.path.exists(file):
               os.remove(file)
  else:
    uploadedfile = f"Error: {output_vcf} is multi-sample file with {num_samples} samples. Only Phased and single sample vcf is allowed." 
  finished_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
  return {'result status': {uploadedfile}, 'created at': {created_at}, 'finished at': {finished_at}}

def main():
    parser = argparse.ArgumentParser(description="Identify potential off-target sites based on VCF files.")
    parser.add_argument('-i', '--input', type=str, required=True, help="Path to the input VCF (Phased and single sample) file")
    parser.add_argument('-r', '--ref_path', type=str, required=True, help="Path to the target organism reference genome")
    parser.add_argument('-t', '--query_input', type = str, required = True,  help = "target sequence in the target organism genome (input.txt file)")
    parser.add_argument('-d', '--device_id', type=str, required=True, help="device_id(s): C for CPU and G for GPU, G0 for GPU device id=0")
    args = parser.parse_args()
    output_vcf = compress_and_index(args.input, args.ref_path, args.query_input, args.device_id)
    print(f"status: {output_vcf}")
    
    
    print("Completed.")

if __name__ == "__main__":
    main()
