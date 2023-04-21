<script>
   import { Input, Label, Heading, Select } from 'flowbite-svelte';
   import { Textarea} from 'flowbite-svelte'
  import Pam_type from './Pam_type.svelte'
   import Genome_type from './Genome_type.svelte'

	export let job_title;
	export let email;
    export let mismatches;
	export let dna_bulge;
	export let rna_bulge;
	export let query_seq;
	export let Target_Genome;
	export let Pam;
	let Pams=[
		    {value:"SpCas9 from streptococcus pyogenes: 5'-NGG-3'", name:"SpCas9 from streptococcus pyogenes: 5'-NGG-3'"},
			{value:"SpCas9 from Streptococcus pyogenes: 5'-NRG-3' (R = A or G)", name:"SpCas9 from Streptococcus pyogenes: 5'-NRG-3' (R = A or G)"},
			{value:"StCas9 from Streptococcus thermophilus: 5'-NNAGAAW-3' (W = A or T)", name:"StCas9 from Streptococcus thermophilus: 5'-NNAGAAW-3' (W = A or T)"},
			{value:"NmCas9 from Neisseria meningitidis: 5'-NNNNGMTT-3' (M = A or C)", name:"NmCas9 from Neisseria meningitidis: 5'-NNNNGMTT-3' (M = A or C)"},
			{value:"SaCas9 from Staphylococcus aureus: 5'-NNGRRT-'3 (R=A or G)", name:"SaCas9 from Staphylococcus aureus: 5'-NNGRRT-'3 (R=A or G)"},
			{value:"CjCas9 from Campylobacter jejuni: 5'-NNNVRYAC-3' (V = G or C or A, R = A or G, Y = C or T)",name:"CjCas9 from Campylobacter jejuni: 5'-NNNVRYAC-3' (V = G or C or A, R = A or G, Y = C or T)"},
			{value:"AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTN-3'",name:"AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTN-3'"},
			{value:"AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTV-3' (V = G or C or A)",name:"AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTV-3' (V = G or C or A)"},
			{value:"SpCas9 from Streptococcus pasteurianus: 5'-NNGTGA-3'",name:"SpCas9 from Streptococcus pasteurianus: 5'-NNGTGA-3'"},
			{value:"FnCpf1 from Francisella: 5'-TTN-3'",name:"FnCpf1 from Francisella: 5'-TTN-3'"},
			{value:"SaCas9 from Staphylococcus aureus: 5'-NNNRRT-'3 (R=A or G)",name:"SaCas9 from Staphylococcus aureus: 5'-NNNRRT-'3 (R=A or G)"},
			{value:"FnCpf1 from Francisella: 5'-KYTV-3'",name:"FnCpf1 from Francisella: 5'-KYTV-3'"},
			{value:"VRER SpCas9 from Streptococcus pyogenes: 5'-NGCG-3'",name:"VRER SpCas9 from Streptococcus pyogenes: 5'-NGCG-3'"},
			{value:"VQR SpCas9 from Streptococcus pyogenes: 5'-NGA-3'",name:"VQR SpCas9 from Streptococcus pyogenes: 5'-NGA-3'"},
			{value:"XCas9 3.7 (TLIKDIV SpCas9) from Streptococcus pyogenes: 5'-NGT-3'",name:"XCas9 3.7 (TLIKDIV SpCas9) from Streptococcus pyogenes: 5'-NGT-3'"},
			{value:"XCas9 3.7 (TLIKDIV SpCas9) from Streptococcus pyogenes: 5'-NG-3'",name:"XCas9 3.7 (TLIKDIV SpCas9) from Streptococcus pyogenes: 5'-NG-3'"},
			{value:"BhCas12b from Bacillus hisashii: 5'-TTN-3'",name:"BhCas12b from Bacillus hisashii: 5'-TTN-3'"},
			{value:"BhCas12b v4 from Bacillus hisashii: 5'-ATTN-3'",name:"BhCas12b v4 from Bacillus hisashii: 5'-ATTN-3'"},
			{value:"BhCas12b v4 from Bacillus hisashii: 5'-DTTN-3'",name:"BhCas12b v4 from Bacillus hisashii: 5'-DTTN-3'"},
			{value:"Spy-macCas9 from Streptococcus pyogenes and Streptococcus macacae: 5'-NAAN-3'",name:"Spy-macCas9 from Streptococcus pyogenes and Streptococcus macacae: 5'-NAAN-3'"},
			{value:"Nme2Cas9 from Neisseria meningitidis: 5'-NNNNCC-3'",name:"Nme2Cas9 from Neisseria meningitidis: 5'-NNNNCC-3'"},
			{value:"RR AsCpf1 from Acidaminococcus: 5'-TYCV-3'",name:"RR AsCpf1 from Acidaminococcus: 5'-TYCV-3'"},
			{value:"RVR AsCpf1 from Acidaminococcus: 5'-TATV-3'",name:"RVR AsCpf1 from Acidaminococcus: 5'-TATV-3'"},
			{value:"CcCas9 from Clostridium cellulolyticum: 5'-NNNNGNA-3'",name:"CcCas9 from Clostridium cellulolyticum: 5'-NNNNGNA-3'"},
			{value:"MAD7 nuclease: 5'-YTTV-3'",name:"MAD7 nuclease: 5'-YTTV-3'"},
			{value:"Complementary SpCas9 from Streptococcus pyogenes: 5'-NCC-3'",name:"Complementary SpCas9 from Streptococcus pyogenes: 5'-NCC-3'"},
			{value:"ThermoCas9 from Geobacillus thermodenitrificans T1: 5'-NNNNCNR-3'",name:"ThermoCas9 from Geobacillus thermodenitrificans T1: 5'-NNNNCNR-3'"},
			{value:"ThermoCas9 from Geobacillus thermodenitrificans T1: 5'-NNNNCNAA-3'",name:"ThermoCas9 from Geobacillus thermodenitrificans T1: 5'-NNNNCNAA-3'"},
			{value:"SpRY Cas9 from Streptococcus pyogenes: 5'-NNN-3'",name:"SpRY Cas9 from Streptococcus pyogenes: 5'-NNN-3'"},
			{value:"SpRY Cas9 from Streptococcus pyogenes: 5'-NRN-3'",name:"SpRY Cas9 from Streptococcus pyogenes: 5'-NRN-3'"},
			{value:"SpCas9 Variant from Streptococcus pyogenes: 5'-NGC-3'",name:"SpCas9 Variant from Streptococcus pyogenes: 5'-NGC-3'"},
			{value:"Cas12f1 from Acidibacillus sulfuroxidans: 5'-TTTR-3'",name:"Cas12f1 from Acidibacillus sulfuroxidans: 5'-TTTR-3'"},
			{value:"Cas12f1 from Acidibacillus sulfuroxidans: 5'-NTTR-3'",name:"Cas12f1 from Acidibacillus sulfuroxidans: 5'-NTTR-3'"},
			{value:"DpbCasX (Cas12e) from Deltaproteobacteria: 5'-TTCN-3'",name:"DpbCasX (Cas12e) from Deltaproteobacteria: 5'-TTCN-3'"},
			{value:"SpCas9 Variant (TAT.P5-1) from Streptococcus pyogenes: 5'-NRTH-3' (R=G or A, H=A or C orT)",name:"SpCas9 Variant (TAT.P5-1) from Streptococcus pyogenes: 5'-NRTH-3' (R=G or A, H=A or C orT)"},
			{value:"SpCas9 from Staphylococcus Auricularis: 5'-NNGG-3'",name:"SpCas9 from Staphylococcus Auricularis: 5'-NNGG-3'"},
			{value:"St3Cas9 from Streptococcus Thermophilus: 5'-NGGNG-3'",name:"St3Cas9 from Streptococcus Thermophilus: 5'-NGGNG-3'"},
			{value:"Frcas9 from Faecalibaculum rodentium: 5'-NRTA-3' for target (R=A or G)",name:"Frcas9 from Faecalibaculum rodentium: 5’-NRTA-3’ for target (R=A or G)"},
			{value:"Frcas9 from Faecalibaculum rodentium: 5'-NNNA-3'",name:"Frcas9 from Faecalibaculum rodentium: 5'-NNNA-3'"}

	]

	
</script>
<Heading tag="h4" class="mb-4"> </Heading>

	<div class="mb-2" >
		<Label for = "title" class="space-y-2"> 
		<span> Job Title (Optional): </span>
		<Input bind:value={job_title} type="text" size="lg" id="title" placeholder="Job Title" />
		</Label>
	</div>
    
	<div class="mb-2">
		<Label for="email" class= "" >
		<span class="leading-relaxed dark:text-gray-400 mb-2"> E-mail (Optional): </span>
		</Label>
		<Input class="leading-relaxed dark:text-gray-400 mb-2" bind:value={email} type="email" size="lg" id="email" placeholder="your E-mail" />
	</div>
<!---
    <div class="mb-2"> 
	  <Pam_type/>
    </div>
	-->
     <!---
	<div class="mb-2"> 
	  <Genome_type/>
    </div>
    -->
	<div class="mb-2"> 
			<Label for ="Pams">select pam</Label>
			<Select id="Pams" class="mt-2" bind:value={Pam}>
				{#each Pams as {value, name}}
				<option {value}> {name}</option>
				{/each}
			</Select>
			

		</div>
		

		<!---
		<div class="mb-2" >
			<Label for = "Pam" class="space-y-2"> 
			<span> Pam: </span>
			<Input bind:value={Pam} type="text" size="lg" id="Target_genome" placeholder="SpCas9 from Streptococcus pyogenes: 5'-NRG-3' (R = A or G)" />
			</Label>
		</div>
		--->
			<div class="mb-2" >
				<Label for = "Target_Genome" class="space-y-2"> 
				<span> Target_genome: </span>
				<Input bind:value={Target_Genome} type="text" size="lg" id="Target_genome" placeholder="Homo sapiens (GRCh38/hg38) - Human" />
				</Label>
			</div>
	<div>
	 <Label for="query_seq" class="mb-2">Query Sequences without PAM from 5' to 3'</Label>
	 <Textarea id="query_seq" bind:value={query_seq} placeholder="CAGCAACTCCAGGGGGCCGC" rows="6" name="query" required/>
    </div>


<Heading tag="h4" class="mb-4"></Heading>
<div class="px-5">
	
	<div class="mb-6">
		<Label for="mismatches" class="mb-2">Maximum number of mismatches between gRNA and the target genome </Label>
		<Input bind:value={mismatches} type="number" size = "lg" id="mismatches" placeholder="0"
			required
		/>
	</div>
	<div class="mb-6">
		<Label for="dna_bulge" class="mb-2">Maximum DNA_Bulge size</Label>
		<Input bind:value={dna_bulge} type="number" size = "lg" id="dna_bulge" placeholder="0" required/>
	</div>
	<div >
		<Label for="rna_bulge" class="space-y-2 mb-4">Maximum RNA_Bulge size</Label>
		<Input bind:value={rna_bulge} type="number" size="lg" id="rna_bulge" placeholder="0" required/>
	</div>
</div>