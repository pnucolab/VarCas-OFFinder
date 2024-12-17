# Variant Aware Cas-OFFinder pipeline
**The new Cas-OFFinder pipeline**

Cas-OFFinder is a highly efficient and adaptable program built upon OpenCL that identifies potential off-target sites of CRISPR/Cas-derived RNA-guided endonucleases (RGENs).
Cas-OFFinder is not limited by the number of mismatches and accommodates variations in the protospacer-adjacent motif (PAM) sequences recognized by Cas9, which is the crucial protein component in RNA-guided endonucleases (RGENs).
An OpenCL device is essential for optimal functionality.
This newly designed pipeline incorporates Single Nucleotide Polymorphisms (SNPs) into the search criteria for both on-target and potential off-target sites. This tool addresses specific challenges encountered when relying solely on reference genomes for predicting on-target potential off-target sites. Reference genomes are typically generated from the genetic material of a limited number of individuals, resulting in a representation that often falls short of capturing the complete genetic diversity within a species. Our platform empowers users to identify potential off-target sites by incorporating a reference genome and individual genetic variants. 
This tool is available in both web and command-line interfaces. The Cas-OFFinder web tool is user-friendly, and the entire website has undergone a renovation, transitioning from the previous interface at CRISPR RGEN Tools (rgenome.net) to a new one based on cutting-edge web technologies such as SvelteKit, FastAPI, Celery, duckdb, and Redis to enhance the user experience.

**Usage**
1. Download requirements.txt and vcf-cas-offinder.py and Install all dependencies listed in the requirements.txt file using the command:
   ```
   pip install —no-cache-dir -r requirements.txt
   ```
