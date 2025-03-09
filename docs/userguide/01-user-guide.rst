================
Tool Usage Guide
================
This guide provides everything you need to get started with the tool, whether you're a casual user or 
a developer looking to integrate it into your workflow. This tool is built with flexibility and offers multiple interaction methods to suit your needs.

A step-by-step guide
--------------------
The tool provides users with four distinct methods of interaction:

1. Web Interface: Access and utilize the tool directly through our online web tool.
2. Command-Line Interface (CLI): Leverage the full functionality of the tool via the command-line tool
3. Source Code Deployment: Download the source code and deploy the tool on a local server for complete control and customization
4. API: Integrate the tool's features programatically through  API for automated workflows and system integration


1. How to Use the Web Interface
-------------------------------

To use the Allelic-Cas-OFFinder web tool, your system must meet the following requirements for operating systems and web browsers.

- Supported Operating Systems:
        - Windows
        - macOS
        - Linux
- Supported web browsers:
        - Google Chrome
        - Mozilla Firefox
        - Microsoft Edge
        - Safari


To get started, navigate to https://crispr.pnucolab.com/ and explore the platform's features. A Sample VCF file is provided for new users, which can be easily downloaded by clicking on the link. This sample file serves as a great starting point for familiarizing yourself with the tool's capabilities.
The platform's default settings include:

    - Target Genome: Homo sapiens (GRCh38/hg38) - Human
    - PAM Type: SpCas9 from Streptococcus pyogenes: 5'-NRG-3
    - Query Sequence: CAGCAACTCCAGGGGGCCGC
    - Mismatches: 3
After downloading the sample VCF file, click "Submit" to process it with the default parameters and wait until the result is available. 
For more customized analysis, users have the option to upload their own VCF file (Supported file formats: [e.g., .vcf, .vcf.gz (gzipped and bgzipped file)]) and select from a range of parameters to tailor the analysis to their specific needs. For faster execution, upload a VCF file that contains a limited number of chromosomes, like 2 or 3. The User can follow the steps below to select a few chromosomes from a VCF file.

  
Unzip if it is zipped:


.. code-block:: bash

    gunzip Sample.vcf.gz

bgzip the VCF File


.. code-block:: bash

    bgzip -c Sample.vcf > Sample.vcf.gz

Index bgzip VCF File


.. code-block:: bash

    tabix -p vcf Sample.vcf.gz

Filter a Few Chromosomes VCF data (Not Mandatory but better for faster processing time)


.. code-block:: bash

    bcftools view -r chr6,chr10 Sample.vcf.gz -o Output.vcf.gz
 

Make sure the above tools are installed on your machine. After all these steps, your VCF file is ready to be uploaded for processing. 

These default settings provide a solid foundation for analysis, but the ability to customize parameters ensures that users can adapt the tool to their unique research requirements.
Once the analysis is complete, the results will be ready. The users can download the results if they want. 

Our tool is designed to deliver a smooth user experience. If an issue arises, we provide clear and actionable error messages to help the user resolve any problems.

Common Error messages and Solutions
-----------------------------------

1. Your file is not phased VCF file.
    -  What It Means: This occurs when you upload not pahsed vcf file. 
    -  What to Do: Ensure your VCF file is phased. You can use GATK, Octopus, or other variant callers to prepare a phased VCF file. 
2. Your file is multi-sample vcf file.
    -  What It Means: This happens when you upload multiple sample VCF file.
    -  What to Do: Please make sure that your VCF file contains only a single sample. Our web tool accepts only phased single sample vcf file to identify on-target and potential 
       off-target sites in the entire individual genome. 


2. How to Use the Command-line Interface
----------------------------------------

Cas-OFFinder is built upon OpenCL to identify potential off-target sites of CRISPR/Cas-derived RNA-guided endonucleases (RGENs).
An OpenCL device is essential for optimal functionality.


Create your environment:


.. code-block:: bash

   conda create -n crispr



Download requirements.txt and vcf-cas-offinder.py from the command-line interface directory and install all dependencies using the command:


.. code-block:: bash

  pip install —no-cache-dir -r requirements.txt


Download the Cas-OFFinder binary file from https://github.com/pnucolab/variant-aware-Cas-OFFinder/blob/main/backend/cas-offinder in the same directory with vcf-cas-offinder.py:

  

install the vcflib package using conda, execute the following command:


.. code-block:: bash

  conda install -c bioconda vcflib=1.0.3 tabixpp=1.1.0


Download the chromosome FASTA files for any target organism. You can find one using the links below, or you can use any other sources:

    - For Vertebrates


        .. code-block:: bash
        
           https://ftp.ensembl.org/pub/

 
    - For Plants

        .. code-block:: bash
                
                  https://ftp.ensemblgenomes.ebi.ac.uk/pub/plants/
         

Extract all FASTA files into a directory. Index the extracted reference genome within the same directory

.. code-block:: bash
        
           samtools faidx ref.genome # replace ref.genome with tha actual name of the extracted reference genome 


Ensure that the “+x” flag is added to the input_vcf_file and the target organism’s reference genome directory.

Now, the new Cas-OFFinder pipeline can run with:


.. code-block:: bash
        
          ./vcf-cas-offinder.py -i input_vcf_file_path -r reference_genome_path -t target_sequence_input_file_name -d device_id 



For device_id you can use G, C or A
     - G represents using GPU devices, while C stands for CPUs. A represents accelerators. 
     - If you have multiple GPU or CPU IDs, you can specify them as G0 for GPU device ID 0 and G1 for ID 1 to limit the number of devices used. 
For a short help, try running 


.. code-block:: bash
        
          ./vcf-cas-offinder.py -h 


.. code-block:: bash
        
  usage: vcf-cas-offinder.py [-h] -i INPUT -r REF_PATH -t QUERY_INPUT -d DEVICE_ID

  Identify potential off-target sites based on VCF files.

  options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Path to the input VCF (Phased and single sample) file
  -r REF_PATH, --ref_path REF_PATH
                        Path to the target organism reference genome
  -t QUERY_INPUT, --query_input QUERY_INPUT
                        target sequence in the target organism genome (input.txt file)
  -d DEVICE_ID, --device_id DEVICE_ID
                        device_id(s): C for CPU and G for GPU, G0 for GPU device id=0


You should create an input.txt file in the same directory with vcf-cas-offinder. 

 An example of an input file:


.. code-block:: bash
        
      NNNNNNNNNNNNNNNNNNNNGG
      GTGAAATCTAAGTGTAGAGNNN 2
      TTGTGAAATCTAAGTGTAGNNN 2
      CTTCACAATTATTCGCCCANNN 2
      GGGCGAATAATTGTGAAGGNNN 2
      CTTACAGAAACACCTGTTANNN 2
      AGATTCAAGAATTGGTACGNNN 2
      AACCTTCAGTTAGTCGCTANNN 2
      CACCATAGCGACTAACTGANNN 2
      AGCTCAGGAAGGCCCTCATNNN 2

- The first line indicates the desired pattern, including the PAM site.
- The remaining lines are the query sequences and maximum mismatch numbers, separated by spaces.
- The length of the desired pattern and the query sequences should be the same.

Now you can run vcf-Cas-OFFinder as follows (using GPUs):


.. code-block:: bash
        
      ./vcf-cas-offinder.py -i /home/user/Documents/vcf_files/bgzipresultcm334.vcf.gz -r /home/user/genome/pepper_ref/GCA_000512255.2_ASM51225v2_genomic.fa -t input.txt -d G1


- Replace the file paths with the actual file path. 

Sample results are shown below.


.. image:: https://github.com/pnucolab/variant-aware-Cas-OFFinder/blob/main/docs/images/Screenshot%202025-03-07%20231028.png
   :alt: Example Image
   :width: 400px
   :align: center



- 0 after the colon in the second column represents allele 1, and 1 represents allele 2 for each chromosome. In the example shown above, CVCM334_CM008455, CVCM334_CM008456, etc, are chromosome identifiers found in the allelic fasta files. 



3. How to deploy Source Code on local machines
----------------------------------------------


If the user wants to deploy on local machines, please follow the following steps.

1. Create a directory
2. Download frontend, backend, Caddyfile, and docker-compose.yml source codes to the directory
3. Download Cas-offinder from https://github.com/pnucolab/variant-aware-Cas-OFFinder/blob/main/backend/cas-offinder and make it executable:


   .. code-block:: bash
        
          chmod +x cas-offinder 

4. Run the following command to build from the docker-compose file:


   .. code-block:: bash
        
           docker compose build


5. After building, run the following command to start the services


   .. code-block:: bash
        
           docker compose up -d





