from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import os, uuid
from celery_worker import off_target
from typing import Text
from fastapi.responses import PlainTextResponse
from enum import Enum
from pam import Pam
from target_genome import Target_Genome


app = FastAPI()
origins = [
    "http://10.125.218.100:5175",
  ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

task_id_lists = []
tasks = {}


@app.post('/cas_offinder_tasks', tags = ["cas_offinder"])
async def cas_offfinder(Target_Genome: Target_Genome, Pam: Pam,
                       job_title: str=Query(default="", title="Job Title"),
                       email:str=Query(default="", title="Email"),
                       query_seq: str=Query(default="CAGCAACTCCAGGGGGCCGC", title="Query Sequences without PAM from 5' to 3'"),
                       mismatches: int=Query(ge=0, le=9, default=0, title="Maximum number of mismatches between gRNA and the target genome"),
                       dna_bulge : int=Query(ge=0, le=4, default=0, title="Maximum DNA_Bulge size"),
                       rna_bulge: int=Query(ge=0, le=4, default=0, title="Maximum DNA_Bulge size")):
  task_id = str(uuid.uuid4())
  output_file_name = str(task_id) + 'output'
  summary_file_name = str(task_id) + 'summary'
  
  if Target_Genome == 'Homo sapiens (GRCh38/hg38) - Human':
      Target_Genome = 'human'
  if Target_Genome == 'Homo sapiens (hg19) - Human':
      Target_Genome = 'human1'
  if Target_Genome == 'Mus musculus (mm10) - Mouse':
      Target_Genome = 'mm10'
  if Target_Genome == 'Bos taurus (bosTau7) - Cow':
      Target_Genome = 'bosTau7'
  if Target_Genome == 'Canis familiaris (canFam3) - Dog':
      Target_Genome = 'canFam3'
  if Target_Genome == 'Rattus norvegicus (rn5) - Rat':
      Target_Genome = 'rn5'
  if Target_Genome == 'Sus scrofa (susScr11) - Pig':
      Target_Genome = 'susScr11'  
  if Target_Genome == 'Danio rerio (danRer7) - Zebrafish':
      Target_Genome = 'danRer7'
  if Target_Genome == 'Macaca mulatta(rheMac3) - Monkey':
      Target_Genome = 'rheMac3'
  if Target_Genome == 'Xenopus tropicalis (JGI 4.2/xenTro3) - Western clawed frog':
      Target_Genome = 'JGI42'  
  if Target_Genome == 'Xenopus tropicalis (JGI 7.1) - Western clawed frog':
      Target_Genome = 'JGI71'
  if Target_Genome == 'Xenopus laevis (JGI 7.1) - African clawed frog':
      Target_Genome = 'JGI71A'
  if Target_Genome == 'Cricetulus griseus (v1.0) - Chinese Hamster':
      Target_Genome = 'Cv10'  
  if Target_Genome == 'Xenopus tropicalis (JGI 8.0) - Western clawed frog':
      Target_Genome = 'JGI80'
  if Target_Genome == 'Xenopus tropicalis (JGI 9.0) - Western clawed frog':
      Target_Genome = 'JGI90'
  if Target_Genome == 'Xenopus laevis (JGI 9.1) - African clawed frog':
      Target_Genome = 'JGI91' 
  if Target_Genome == 'Macaca fascicularis (5.0) - Crab-eating macaque':
      Target_Genome = 'macaca50'
  if Target_Genome == 'Danio rerio (GRCz10) - Zebrafish':
      Target_Genome = 'GRCz10'
  if Target_Genome == 'Rattus norvegicus (Rnor 6.0) - Rat':
      Target_Genome = 'Rnor60'  
  if Target_Genome == 'Equus caballus (EquCab2) - Horse':
      Target_Genome = 'EquCab2'
  if Target_Genome == 'Oryctolagus cuniculus (OryCun2) - Rabbit':
      Target_Genome = 'OryCun2'
  if Target_Genome == 'Mesocricetus auratus (MesAur1.0) - Golden hamster':
      Target_Genome = 'MesAur10'  
  if Target_Genome == 'Felis catus (6.2) - Cat':
      Target_Genome = 'Felis62'
  if Target_Genome == 'Mochrtus ochrogaster (AHZW01) - Prairie vole':
      Target_Genome = 'AHZW01'
  if Target_Genome == 'Bos taurus (bosTau8) - Cow':
      Target_Genome = 'bosTau8'  
  if Target_Genome == 'Callithrix jacchus (calJac3) -marmoset':
      Target_Genome = 'calJac3'
  if Target_Genome == 'Pimephales promelas (SOAPdenovo v. 2) - fathead minnow':
      Target_Genome = 'SOAPdenovov2'
  if Target_Genome == 'ovis_aries (Oar_v3.1) - sheep':
      Target_Genome = 'Oarv31' 
  if Target_Genome == 'Chlorocebus_sabeus (AQIB01) - green monkey':
      Target_Genome = 'AQIB01'
  if Target_Genome == 'Gallus gallus (Galgal4) - Chicken':
      Target_Genome = 'Galga14'
  if Target_Genome == 'Oreochromis niloticus (ASM185804v2)':
      Target_Genome = 'ASM1858804v2'  
  if Target_Genome == 'Capra hircus (ARS1) - goat':
      Target_Genome = 'ARS1'
  if Target_Genome == 'Peromyscus maniculatus (Pman_1.0) - North American deer mouse':
      Target_Genome = 'Pman10'
  if Target_Genome == 'Macaca mulatta (Mmul_8.0.1) - Monkey':
      Target_Genome = 'Muml801'  
  if Target_Genome == 'Cricetulus griseus (CriGri_1.0) - Chinese hamster':
      Target_Genome = 'CriGri10'
  if Target_Genome == 'Cavia porcellus (Cavpor3.0) - guinea pig':
      Target_Genome = 'Cavpor30'
  if Target_Genome == 'Danio rerio (GRCz11) - zebrafish':
      Target_Genome = 'GRCz11'  
  if Target_Genome == 'Anas platyrhynchos (BGI_duck_1.0) - duck':
      Target_Genome = 'BGIduk10'
  if Target_Genome == 'Salmo salar (ICSASG_v2) -Atlantic salmon':
      Target_Genome = 'ICSASGv2'
  if Target_Genome == 'Cyprinus carpio (common carp genome)':
      Target_Genome = 'commoncarp' 
  if Target_Genome == 'Oncorhynchus tshawytscha (Otsh_v1.0) - Chinook salmon':
      Target_Genome = 'Otshv10'
  if Target_Genome == 'Human Mitochondria genome (NC_012920.1)':
      Target_Genome = 'NC012920'
  if Target_Genome == 'BalbC/J mouse Mitochondria genome (AJ512208.1)':
      Target_Genome = 'AJ512208'  
  if Target_Genome == 'Bos taurus (ARS UCD1.2)':
      Target_Genome = 'ARSUCD12'
  if Target_Genome == 'Paralichthys olivaceus (Flounder_ref_guided_V1.0':
      Target_Genome = 'Flounderrefguidedv10'
  if Target_Genome == 'Myotis lucifugus (Myoluc2.0)':
      Target_Genome = 'Myoluc20'  
  if Target_Genome == 'Rousettus aegyptiacus (Raegyp2.0':
      Target_Genome = 'Raegyp20'
  if Target_Genome == 'Tree shrew (TS_20 long-read)':
      Target_Genome = 'TS20longread'
  if Target_Genome == 'Ambystoma mexicanum (ASM291563v2) -axolotl':
      Target_Genome = 'ASM291563v2'  
  if Target_Genome == 'Gallus gallus (GRCg6a) - chicken':
      Target_Genome = ' GRCg6a'
  if Target_Genome == 'Ictalurus punctatus (IpCoco_1.2)':
      Target_Genome = 'IPCoco12'
  if Target_Genome == 'Mustela putorius furo (MusPutFur1.0) - Ferret':
      Target_Genome = 'Musputfur10' 
  if Target_Genome == 'Erinaceus_europaeus (GCF_000296755.1)':
      Target_Genome = 'GCF0002967551'
  if Target_Genome == 'Macaca mulatta (Mmul_10)':
      Target_Genome = 'Mmul10'
  if Target_Genome == 'Macaca fascicularis (Macaca_fascicularis_5.0)':
      Target_Genome = 'Macacafascicularis50'  
  if Target_Genome == 'Pagrus major (Pmaj_1.0)':
      Target_Genome = 'Pmaj10'
  if Target_Genome == 'Petromyzon_marinus':
      Target_Genome = 'Petromyzon'
  if Target_Genome == 'Homo sapiens (CHM13 T2T v1.1) - Human':
      Target_Genome = 'CHM13T2Tv11'  
  if Target_Genome == 'Ovis aries (ARS-UI_Ramb_v2.0) - Sheep':
      Target_Genome = 'ARSUIRambv20'
  if Target_Genome == 'Equus caballus (EquCab3.0) - horse':
      Target_Genome = 'EquCab30'
  if Target_Genome == 'Epinephelus coioides () - Orange-spotted grouper':
      Target_Genome = 'Epinephelus'  
  if Target_Genome == 'Anabas testudineus (fAnaTes1.2) - Climbing perch':
      Target_Genome = 'fAnaTes12'
  if Target_Genome == 'Bubalus bubalis (NDDB_SH_1)':
      Target_Genome = 'NDDBSH1'
  if Target_Genome == 'Sus scrofa (Large white v1 from ensembl) - pig':
      Target_Genome = 'Largewhitev1' 
  if Target_Genome == 'Homo sapiens (T2T_CHM13v2) - Human':
      Target_Genome = 'T2TCHM13v2'
  if Target_Genome == 'Salmo salar (USDA_NASsal_1.1) - Atlantic salmon':
      Target_Genome = 'USDANASsal11'
  if Target_Genome == 'Vulpes lagopus (ASM1834538v1) - Arctic fox':
      Target_Genome = 'ASM1834538v1'  
  if Target_Genome == 'Takifugu rubripes (fTakRub1.3 from ENA)':
      Target_Genome = 'fTakRub13'
  if Target_Genome == 'Macaca nemestrina (Mnem_1.0)':
      Target_Genome = 'Mnem10'
  if Target_Genome == 'Eptesicus fuscus (EptFus1.0) - Big brown bat':
      Target_Genome = 'EptFus10'  
  if Target_Genome == 'Oncorhynchus mykiss (USDA_OmykA_1.1) - rainbow trout':
      Target_Genome = 'USDAOmykA11'
  if Target_Genome == 'Pteropus alecto (ASM32557v1) - Black flying fox':
      Target_Genome = 'ASM32557v1'
  if Target_Genome == 'Macaca fascicularis (6.0) - Crab-eating macaque':
      Target_Genome = 'Macaca60'  
  if Target_Genome == 'Dicentrarchus labrax - (European seabass)':
      Target_Genome = 'Europeanseabass'
  if Target_Genome == 'Equus asinus (ASM1607732v2) - Ass':
      Target_Genome = 'ASM1607732v2'
  if Target_Genome == 'Mus musculus (mm9) - Mouse':
      Target_Genome = 'mm9' 
  if Target_Genome == 'Gallus gallus (Gallus_gallus-5.0) - Chicken':
      Target_Genome = 'Gallus50' 

  file_path = '/home/abyot/projects/cas_offinder/genome/' + Target_Genome 
  with open('input.txt', 'w') as f:
      f.write(file_path + '/' + '\n')  
  replace_dict = {
          'A': 'N',
          'T': 'N',
          'G': 'N',
          'C': 'N'
       }
  pam_seq = query_seq
  for old_str, new_str in replace_dict.items():
        pam_seq = pam_seq.replace(old_str, new_str)
  if Pam == "SpCas9 from streptococcus pyogenes: 5'-NGG-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NGG'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNN'+' ' + str(mismatches))
  if Pam == "SpCas9 from Streptococcus pyogenes: 5'-NRG-3' (R = A or G)":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NRG'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNN'+' ' + str(mismatches))
  if Pam == "StCas9 from Streptococcus thermophilus: 5'-NNAGAAW-3' (W = A or T)":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNAGAAW'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNNNNN'+' ' + str(mismatches))
  if Pam == "NmCas9 from Neisseria meningitidis: 5'-NNNNGMTT-3' (M = A or C)":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNNNGMTT'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNNNNNN'+' ' + str(mismatches))
  if Pam == "FnCpf1 from Francisella: 5'-KYTV-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'KYTV'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))
  if Pam == "SaCas9 from Staphylococcus aureus: 5'-NNGRRT-'3 (R=A or G)":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNGRRT'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNNNN'+' ' + str(mismatches))
  if Pam == "CjCas9 from Campylobacter jejuni: 5'-NNNVRYAC-3' (V = G or C or A, R = A or G, Y = C or T)":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNNVRYAC'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNNNNNN'+' ' + str(mismatches))
  if Pam == "AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTN-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'TTTN'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))
  if Pam == "AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTV-3' (V = G or C or A)":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'TTTV'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))
  if Pam == "FnCpf1 from Francisella: 5'-TTN-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'TTN'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNN'+' ' + str(mismatches))
  if Pam == "SpCas9 from Streptococcus pasteurianus: 5'-NNGTGA-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNGTGA'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNNNN'+' ' + str(mismatches))
  if Pam == "SaCas9 from Staphylococcus aureus: 5'-NNNRRT-'3 (R=A or G)":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNNRRT'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNNNN'+' ' + str(mismatches))
  if Pam == "VRER SpCas9 from Streptococcus pyogenes: 5'-NGCG-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NGCG'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))
  if Pam == "VQR SpCas9 from Streptococcus pyogenes: 5'-NGA-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NGA'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNN'+' ' + str(mismatches))
  if Pam == "XCas9 3.7 (TLIKDIV SpCas9) from Streptococcus pyogenes: 5'-NGT-3'":
       with open('input.txt', 'a') as f:
           f.write(pam_seq + 'NGT'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNN'+' ' + str(mismatches))
  if Pam == "":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + ''+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NN'+' ' + str(mismatches))
  if Pam == "XCas9 3.7 (TLIKDIV SpCas9) from Streptococcus pyogenes: 5'-NG-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NG'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NN'+' ' + str(mismatches))
  if Pam == "BhCas12b from Bacillus hisashii: 5'-TTN-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'TTN'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNN'+' ' + str(mismatches))
  if Pam == "BhCas12b v4 from Bacillus hisashii: 5'-ATTN-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'ATTN'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))
  if Pam == "":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + ''+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NN'+' ' + str(mismatches))
  if Pam == "BhCas12b v4 from Bacillus hisashii: 5'-DTTN-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'DTTN'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))
  if Pam == "Spy-macCas9 from Streptococcus pyogenes and Streptococcus macacae: 5'-NAAN-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NAAN'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))
  if Pam == "RR AsCpf1 from Acidaminococcus: 5'-TYCV-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'TYCV'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))
  if Pam == "Nme2Cas9 from Neisseria meningitidis: 5'-NNNNCC-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNNNCC'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNNNN'+' ' + str(mismatches))
  if Pam == "CcCas9 from Clostridium cellulolyticum: 5'-NNNNGNA-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNNNGNA'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNNNNN'+' ' + str(mismatches))
  if Pam == "RVR AsCpf1 from Acidaminococcus: 5'-TATV-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'TATV'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))
  if Pam == "":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + ''+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNN'+' ' + str(mismatches))
  if Pam == "MAD7 nuclease: 5'-YTTV-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'YTTV'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))
  if Pam == "Complementary SpCas9 from Streptococcus pyogenes: 5'-NCC-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NCC'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNN'+' ' + str(mismatches))


  if Pam == "ThermoCas9 from Geobacillus thermodenitrificans T1: 5'-NNNNCNR-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNNNCNR'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNNNNN'+' ' + str(mismatches))


  if Pam == "ThermoCas9 from Geobacillus thermodenitrificans T1: 5'-NNNNCNAA-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNNNCNAA'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNNNNN'+' ' + str(mismatches))


  if Pam == "SpRY Cas9 from Streptococcus pyogenes: 5'-NNN-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNN'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNN'+' ' + str(mismatches))
  if Pam == "SpRY Cas9 from Streptococcus pyogenes: 5'-NNN-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNN'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNN'+' ' + str(mismatches))

  if Pam == "SpRY Cas9 from Streptococcus pyogenes: 5'-NRN-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NRN'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNN'+' ' + str(mismatches))


  if Pam == "SpCas9 Variant from Streptococcus pyogenes: 5'-NGC-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NGC'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNN'+' ' + str(mismatches))


  if Pam == "Cas12f1 from Acidibacillus sulfuroxidans: 5'-TTTR-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'TTTR'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))


  if Pam == "Cas12f1 from Acidibacillus sulfuroxidans: 5'-NTTR-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NTTR'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))
  if Pam == "DpbCasX (Cas12e) from Deltaproteobacteria: 5'-TTCN-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'TTCN'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))          
  if Pam == "SpCas9 Variant (TAT.P5-1) from Streptococcus pyogenes: 5'-NRTH-3' (R=G or A, H=A or C orT)":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NRTH'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))          
  if Pam == "SpCas9 from Staphylococcus Auricularis: 5'-NNGG-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNGG'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))          
  if Pam == "St3Cas9 from Streptococcus Thermophilus: 5'-NGGNG-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NGGNG'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNNN'+' ' + str(mismatches))          
  if Pam == "Frcas9 from Faecalibaculum rodentium: 5'-NRTA-3' for target (R=A or G)":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NRTA'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))          
  if Pam == "Frcas9 from Faecalibaculum rodentium: 5'-NNNA-3'":
       with open('input.txt', 'a') as f:
            f.write(pam_seq + 'NNNA'+' '+ str(dna_bulge)+ ' '+ str(rna_bulge)+'\n' + query_seq  + 'NNNN'+' ' + str(mismatches))


  tasks[task_id] = output_file_name, summary_file_name
  rofftarget=off_target.apply_async([output_file_name,summary_file_name], task_id=task_id)
  ticket = task_id
  task_id_lists.append(ticket)
  return {'message': 'excution started', 'task id lists': task_id_lists}



@app.get('/result', tags = ['result_status'])
async def result(ticket:str):
  result_summary = off_target.AsyncResult(ticket)
  if ticket in task_id_lists:
        status = result_summary.state
        existance = 'task_id exists'
        results= tasks.get(ticket)
  else:
        status = ' No Result '
        existance = 'No such task_id'
        results=""
#result.info
  return { 'status': status, 'Result File Names': results}




@app.get('/summary',  response_class =  PlainTextResponse, tags = ['result_summary'])
async def summary(summary_file_name: str):




  try:
   with open(summary_file_name, 'r') as file:
      content = file.read()
      #return content
      return content
  except FileNotFoundError:
      error_message = f'the file {summary_file_name[1]} cound not be found.'
      return error_message
