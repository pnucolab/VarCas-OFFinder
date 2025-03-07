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

============================
How to Use the Web Interface
============================

This intuitive platform operates directly within your web browser from anywhere at any time.

To get started, simply navigate to https://crispr.pnucolab.com/ and begin exploring the platform's features. For new users, a Sample VCF file is provided, which can be easily downloaded by clicking on the link. This sample file serves as a great starting point for familiarizing yourself with the tool's capabilities.

For more customized analysis, users have the option to upload their own VCF file (Supported file formats: [e.g., .vcf, .vcf.gz (gzipped and bgzipped file)]) and select from a range of parameters to tailor the analysis to their specific needs. The platform's default settings include:

Target Genome: Homo sapiens (GRCh38/hg38) - Human
PAM Type: SpCas9 from Streptococcus pyogenes: 5'-NRG-3
Query Sequence: CAGCAACTCCAGGGGGCCGC
Mismatches: 3
These default settings provide a solid foundation for analysis, but the ability to customize parameters ensures that users can adapt the tool to their unique research requirements.
Once the analysis is complete, the results will be ready. The users can download the results if they want. 

Our tool is designed to deliver a smooth user experience. If an issue arises, we provide clear and actionable error messages to help the user resolve any problems.

Common Error messages and Solutions
-----------------------------------

1.  Your file is not phased VCF file.
    - What It Means: This occurs when you upload not pahsed vcf file. 
    - What to Do: Ensure your VCF file is phased. You can use GATK, Octopus, or other variant callers to prepare a phased VCF file. 
2. Your file is multi-sample vcf file.
    - What It Means: This happens when you upload multiple sample VCF file.
    - What to Do: Please make sure that your VCF file contains only a single sample. Our web tool accepts only phased single sample vcf file to identify on-target and potential 
      off-target sites in the entire individual genome. 




