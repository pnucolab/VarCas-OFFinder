
==============
Best Practices
==============

Best Practices for Optimizing Performance with Large VCF Files
--------------------------------------------------------------

When working with large VCF files, it is recommended to follow these best practices to minimize processing time. 

1. Filter Chromosomes for Targeted Processing

For Faster execution time, **filter specific chromosomes** before using the input VCF file once. You can filter 2 or 3 chromosomes once from the available VCF file and upload it separately. 

Example:

Use bcftools to extract data for specific chromosomes:


  :  code-block:: bash
    
    bcftools view -r chr6,chr10 NA12877.vcf.gz -o Filtered_Sample.vcf.gz

