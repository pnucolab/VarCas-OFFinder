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

To get started, simply navigate to https://crispr.pnucolab.com/ and begin exploring the platform's features. For new users, a Sample VCF file is provided, which can be easily downloaded by clicking on the link. This sample file serves as a great starting point for familiarizing yourself with the tool's capabilities.
The platform's default settings include:

    - Target Genome: Homo sapiens (GRCh38/hg38) - Human
    - PAM Type: SpCas9 from Streptococcus pyogenes: 5'-NRG-3
    - Query Sequence: CAGCAACTCCAGGGGGCCGC
    - Mismatches: 3
After downloading the sample VCF file, the user can click "Submit" to process it with the default parameters and wait until the result is available. 
For more customized analysis, users have the option to upload their own VCF file (Supported file formats: [e.g., .vcf, .vcf.gz (gzipped and bgzipped file)]) and select from a range of parameters to tailor the analysis to their specific needs. For faster execution, upload a VCF file that contains limited chromosomes, like 2 or 3. See the steps below.

  
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

Cas-OFFinder is a highly efficient and adaptable program built upon OpenCL that identifies potential off-target sites of CRISPR/Cas-derived RNA-guided endonucleases (RGENs).
An OpenCL device is essential for optimal functionality.


Create your environment:


.. code-block:: bash

   conda create -n crispr

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
