<script>
    import { Heading, P, A } from 'flowbite-svelte';
</script>
<Heading tag="h2" class="mt-5 mb-2">About</Heading>



<Heading tag="h4" class="mt-10 mb-2">Cas-OFFinder</Heading>
<P class="mb-3">In the CRISPR-Cas systems, the guide RNA molecule has the potential to cause 
    the Cas complex to target unintended genomic locations, which are referred to as potential off-target sites. 
    This can lead to incorrect cleavage events. The effectiveness of the CRISPR-Cas system's targeting is directly 
    influenced by the specific sequence composition of the guide RNA (gRNA) and the presence of PAM in the target DNA sequence.
    To address this issue, researchers must be able to search for potential off-target sites in the genome.  Considering the 
    presence of numerous DNA sequences in the genome that closely resemble the target location, 
    the risk of unintended DNA modifications is significantly heightened. Before initiating any genome editing experiment, 
    it is crucial to predict and assess potential off-target sites accurately. </P>
<p class="mb-3" > When predicting off-target sites in silico,the process involves aligning the guide RNA (gRNA) with the reference 
    genome and leveraging sequence homology to accurately 
    identify potential off-target sites. During this process, using reference genomes can have drawbacks because these genomes 
    are usually based on a small number of individuals and may not capture the full genetic diversity within a species. 
    Here we introduce an upgrade of Cas-OFFinder, a computational tool for identifying potential off-target sites based 
    on not only considering a reference genome but also individual genetic variants.Just as the same as Cas-OFFinder, 
    it is not limited by the number of mismatches and allows variations in PAM sequences recognized by Cas9.</p>

<Heading tag="h4" class="mt-10 mb-2">Cas-OFFinder Webtool</Heading>
<P class="mb-3">Cas-OFFinder web tool is designed to assist scientisists and researchers to identify potential off-target sites in the 
    entire individual genome.This website has been renovated, transitioning from the old interface to a new one built with cutting-edge 
    technologies such as SvelteKit, FastAPI, Celery, duckdb,  and Redis to significantly enhance the user experience. </P>
    
   