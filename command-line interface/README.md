# Variant Aware Cas-OFFinder pipeline
## The new Cas-OFFinder pipeline

Cas-OFFinder is a highly efficient and adaptable program built upon OpenCL that identifies potential off-target sites of CRISPR/Cas-derived RNA-guided endonucleases (RGENs).
Cas-OFFinder is not limited by the number of mismatches and accommodates variations in the protospacer-adjacent motif (PAM) sequences recognized by Cas9, which is the crucial protein component in RNA-guided endonucleases (RGENs).
An OpenCL device is essential for optimal functionality.
This newly designed pipeline incorporates Single Nucleotide Polymorphisms (SNPs) into the search criteria for both on-target and potential off-target sites. This tool addresses specific challenges encountered when relying solely on reference genomes for predicting on-target potential off-target sites. Reference genomes are typically generated from the genetic material of a limited number of individuals, resulting in a representation that often falls short of capturing the complete genetic diversity within a species. Our platform empowers users to identify potential off-target sites by incorporating a reference genome and individual genetic variants. 
This tool is available in both web and command-line interfaces. The Cas-OFFinder web tool is user-friendly, and the entire website has undergone a renovation, transitioning from the previous interface at CRISPR RGEN Tools (rgenome.net) to a new one based on cutting-edge web technologies such as SvelteKit, FastAPI, Celery, duckdb, and Redis to enhance the user experience.

## Usage
- Download requirements.txt and vcf-cas-offinder.py and Install all dependencies listed in the requirements.txt file using the command:
   ```
   pip install —no-cache-dir -r requirements.txt
   ```
- Download the Cas-OFFinder binary file and extract and save it in the same directory with vcf-cas-offinder.py
  ```
  https://github.com/snugel/cas-offinder/releases/tag/2.4.1
  ```
- To install the vcflib package using conda, execute the following command:
  ```
   conda install -c bioconda vcflib=1.0.3 tabixpp=1.1.0
  ```
- Then, download the chromosome FASTA files for any target organism. You can find one using the links below or you can use any other sources: 
    - For Vertebrates
      ```
      https://ftp.ensembl.org/pub/
      ```
    - For Plants
      ```
      https://ftp.ensemblgenomes.ebi.ac.uk/pub/plants/
      ```
- Extract all FASTA files into a directory and index them within the same directory.
   ```
   samtools faidx ref.genome
   ```
- Ensure that the “+x” flag is added to the input_vcf_file, and the target organism’s reference genome directory.
- Now, the new Cas-OFFinder pipeline can run with:
  ```
  ./vcf-cas-offinder.py -i input_vcf_file_path -r reference_genome_path -t target_sequence_input_file_name -d device_id
  ```
   G represents using GPU devices, while C stands for CPUs. If you have multiple GPU or CPU IDs, you can specify them as G0 for GPU device ID 0 and G1 for ID 1 to limit the number    of devices used.
- For a short help, try running ./vcf-cas-offinder.py -h
  ```
  ./vcf-cas-offinder.py -h
  ```
