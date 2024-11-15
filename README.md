# Cas-vcf
This is the repo for the Cas-OFFinder update to handle vcf file.

**Introduction**

Genome editing nucleases can precisely cleave the DNA at a specific target site within the genome. 
The accuracy in identifying the exact target sequence plays a crucial role in determining the success of genetic manipulation. 
CRISPR genome editing has demonstrated its potential to treat genetic diseases such as sickle cell anemia, cystic fibrosis, 
and muscular dystrophy by targeting and correcting the genetic abnormalities responsible for these conditions. However, 
one challenge regarding CRISPR genome editing is its off-target effect. Using reference genomes alone to predict potential 
off-target sites can have drawbacks. These genomes are usually based on a small number of individuals and may not 
capture the full genetic diversity within a species. In this study, we report an upgrade of Cas-OFFinder, a computational tool 
for identifying potential off-target sites based on not only considering a reference genome but also individual genetic variants.

**Requirment**
- OpenCL device
- Phased Single sample VCF file generated by different variant calling pipelines
  
**Usage **
1. Upload phased single sample vcf file only
2. Select PAM type from the available options
3. Select the target genome you are interested in to investigate the available on-target and  potential off-target sites
4. Enter the target sequence without PAM from 5' to 3'
5. Enter the maximum mismatches you want to allow for the investigation
   
 **Testing**
 - download the vcf file from https://s3.eu-central-1.amazonaws.com/platinum-genomes/2017-1.0/hg38/small_variants/NA12877/NA12877.vcf.gz or
   https://s3.eu-central-1.amazonaws.com/platinum-genomes/2017-1.0/hg38/small_variants/NA12878/NA12878.vcf.gz. for the human genome.
   the system has a default value (Target Genome = Homo sapiens (GRCH38/hg38)-Human, PAM type = SpCas9 from streptococcus pyogenes: 5'-NGG-3, 
    target sequnce = CAGCAACTCCAGGGGGCCGC and Mismatch = 0)
- The default value can be used or enter your preference for each input.
  
   
  
