============
Requirements
============

Supported File Format
---------------------

Allelic-Cas-OFFinder tool supports the following file formats for processing and analysis.

- .vcf: Variant Call Format files, used for storing genomic variants
- .vcf.gz: Compressed VCF files, either .gz or bgzip VCF files.

Ensure your input file is in one of these formats for compatibility with the tool.


Required Tools for CLI and Local Deployment
-------------------------------------------
  
For users who prefer to work via the command-line interface or deploy Allelic-Cas-OFFinder locally, the following tools are required:

- bcftools: a utility for manipulating and filtering VCF files.

  - install bcftools via conda:
   


    .. code-block:: bash
    
    conda install -c bioconda bcftools
