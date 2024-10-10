<script>
   import { Input, Label, Heading, Select, Fileupload } from 'flowbite-svelte';
   import { Textarea} from 'flowbite-svelte'
   import Pam_type from './Pam_type.svelte'
   import Genome_type from './Genome_type.svelte'
   import { onMount } from 'svelte'
	
	export let email;
    export let mismatches;
	export let Pam;
	
	export let query_seq;
	export let Target_Genome;
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
	let Target_Genomes=[
				{value:"Homo sapiens (GRCh38/hg38) - Human", name:"Homo sapiens (GRCh38/hg38) - Human"},
				{value:"Homo sapiens (hg19) - Human", name:"Homo sapiens (hg19) - Human"},
				{value: "Pepper", name: "Pepper"},
				{value: "Dempsey", name: "Dempsey"},
				{value:"Mus musculus (mm10) - Mouse", name:"Mus musculus (mm10) - Mouse"},
				{value:"Bos taurus (bosTau7) - Cow",name:"Bos taurus (bosTau7) - Cow"},
				{value:"Canis familiaris (canFam3) - Dog", name: "Canis familiaris (canFam3) - Dog"},
				{value:"Rattus norvegicus (rn5) - Rat", name: "Rattus norvegicus (rn5) - Rat"},
				{value:"Sus scrofa (susScr11) - Pig", name: "Sus scrofa (susScr11) - Pig"},
				{value:"Danio rerio (danRer7) - Zebrafish", name: "Danio rerio (danRer7) - Zebrafish"},
				{value:"Macaca mulatta(rheMac3) - Monkey",name: "Macaca mulatta(rheMac3) - Monkey"},
				{value:"Xenopus tropicalis (JGI 4.2/xenTro3) - Western clawed frog", name: "Xenopus tropicalis (JGI 4.2/xenTro3) - Western clawed frog"},
				{value:"Xenopus tropicalis (JGI 7.1) - Western clawed frog", name: "Xenopus tropicalis (JGI 7.1) - Western clawed frog"},
				{value:"Xenopus laevis (JGI 7.1) - African clawed frog",name: "Xenopus laevis (JGI 7.1) - African clawed frog"},
				{value:"Cricetulus griseus (v1.0) - Chinese Hamster", name: "Cricetulus griseus (v1.0) - Chinese Hamster"},
				{value:"Xenopus tropicalis (JGI 8.0) - Western clawed frog", name: "Xenopus tropicalis (JGI 8.0) - Western clawed frog"},
				{value:"Xenopus tropicalis (JGI 9.0) - Western clawed frog", name: "Xenopus tropicalis (JGI 9.0) - Western clawed frog"},
				{value:"Xenopus laevis (JGI 9.1) - African clawed frog", name: "Xenopus laevis (JGI 9.1) - African clawed frog"},
				{value:"Macaca fascicularis (5.0) - Crab-eating macaque", name: "Macaca fascicularis (5.0) - Crab-eating macaque"},
				{value:"Danio rerio (GRCz10) - Zebrafish", name: "Danio rerio (GRCz10) - Zebrafish"},
				{value: "Rattus norvegicus (Rnor 6.0) - Rat", name: "Rattus norvegicus (Rnor 6.0) - Rat"},
				{value:"Equus caballus (EquCab2) - Horse", name: "Equus caballus (EquCab2) - Horse"},
				{value: "Oryctolagus cuniculus (OryCun2) - Rabbit", name: "Oryctolagus cuniculus (OryCun2) - Rabbit"},
				{value: "Mesocricetus auratus (MesAur1.0) - Golden hamster", name: "Mesocricetus auratus (MesAur1.0) - Golden hamster"},
				{value:"Felis catus (6.2) - Cat", name: "Felis catus (6.2) - Cat"},
				{value:"Mochrtus ochrogaster (AHZW01) - Prairie vole", name: "Mochrtus ochrogaster (AHZW01) - Prairie vole"},
				{value:"Bos taurus (bosTau8) - Cow", name: "Bos taurus (bosTau8) - Cow"},
				{value: "Callithrix jacchus (calJac3) -marmoset", name: "Callithrix jacchus (calJac3) -marmoset"},
				{value:"Pimephales promelas (SOAPdenovo v. 2) - fathead minnow", name: "Pimephales promelas (SOAPdenovo v. 2) - fathead minnow"},
				{value: "ovis_aries (Oar_v3.1) - sheep", name: "ovis_aries (Oar_v3.1) - sheep"},
				{value: "Chlorocebus_sabeus (AQIB01) - green monkey", name: "Chlorocebus_sabeus (AQIB01) - green monkey"},
				{value:"Gallus gallus (Galgal4) - Chicken", name: "Gallus gallus (Galgal4) - Chicken"},
				{value:"Oreochromis niloticus (ASM185804v2)",name: "Oreochromis niloticus (ASM185804v2)"},
				{value: "Capra hircus (ARS1) - goat", name: "Capra hircus (ARS1) - goat"},
				{value: "Peromyscus maniculatus (Pman_1.0) - North American deer mouse", name: "Peromyscus maniculatus (Pman_1.0) - North American deer mouse"},
				{value: "Macaca mulatta (Mmul_8.0.1) - Monkey", name: "Macaca mulatta (Mmul_8.0.1) - Monkey"},
				{value: "Cricetulus griseus (CriGri_1.0) - Chinese hamster", name: "Cricetulus griseus (CriGri_1.0) - Chinese hamster"},
				{value: "Cavia porcellus (Cavpor3.0) -guinea pig", name: "Cavia porcellus (Cavpor3.0) -guinea pig"},
				{value:"Danio rerio (GRCz11) - zebrafish", name: "Danio rerio (GRCz11) - zebrafish"},
				{value: "Mus musculus (mm9) - Mouse", name: "Mus musculus (mm9) - Mouse"},
				{value: "Anas platyrhynchos (BGI_duck_1.0) - duck", name: "Anas platyrhynchos (BGI_duck_1.0) - duck"},
				{value: "Gallus gallus (Gallus_gallus-5.0) - Chicken", name: "Gallus gallus (Gallus_gallus-5.0) - Chicken"},
				{value:"Salmo salar (ICSASG_v2) -Atlantic salmon",name: "Salmo salar (ICSASG_v2) -Atlantic salmon"},
				{value: "Cyprinus carpio (common carp genome)", name: "Cyprinus carpio (common carp genome)"},
				{vaule: "Oncorhynchus tshawytscha (Otsh_v1.0) - Chinook salmon", name: "Oncorhynchus tshawytscha (Otsh_v1.0) - Chinook salmon"},
				{value: "Human Mitochondria genome (NC_012920.1)", name: "Human Mitochondria genome (NC_012920.1)"},
				{value:"BalbC/J mouse Mitochondria genome (AJ512208.1)", name: "BalbC/J mouse Mitochondria genome (AJ512208.1)"},
				{value: "Bos taurus (ARS UCD1.2)", name: "Bos taurus (ARS UCD1.2)"},
				{value: "Paralichthys olivaceus (Flounder_ref_guided_V1.0)", name: "Paralichthys olivaceus (Flounder_ref_guided_V1.0)"},
				{value:"Myotis lucifugus (Myoluc2.0)",name: "Myotis lucifugus (Myoluc2.0)"},
				{value:"Rousettus aegyptiacus (Raegyp2.0)",name: "Rousettus aegyptiacus (Raegyp2.0)"},
				{value:"Tree shrew (TS_20 long-read)",name: "Tree shrew (TS_20 long-read)"},
				{value:"Ambystoma mexicanum (ASM291563v2) -axolotl", name: "Ambystoma mexicanum (ASM291563v2) -axolotl"},
				{value:"Gallus gallus (GRCg6a) - chicken", name: "Gallus gallus (GRCg6a) - chicken"},
				{value: "Ictalurus punctatus (IpCoco_1.2)", name: "Ictalurus punctatus (IpCoco_1.2)"},
				{value:"Mustela putorius furo (MusPutFur1.0) - Ferret", name: "Mustela putorius furo (MusPutFur1.0) - Ferret"},
				{value: "Erinaceus_europaeus (GCF_000296755.1)", name: "Erinaceus_europaeus (GCF_000296755.1)"},
				{value:"Macaca mulatta (Mmul_10)",name: "Macaca mulatta (Mmul_10)"},
				{value: "Macaca fascicularis (Macaca_fascicularis_5.0)", name: "Macaca fascicularis (Macaca_fascicularis_5.0)"},
				{value: "Pagrus major (Pmaj_1.0)", name: "Pagrus major (Pmaj_1.0)"},
				{value: "Petromyzon_marinus", name: "Petromyzon_marinus"},
				{value: "Homo sapiens (CHM13 T2T v1.1) - Human",name: "Homo sapiens (CHM13 T2T v1.1) - Human"},
				{value: "Ovis aries (ARS-UI_Ramb_v2.0) - Sheep",name: "Ovis aries (ARS-UI_Ramb_v2.0) - Sheep"},
				{value: "Equus caballus (EquCab3.0) - horse",name: "Equus caballus (EquCab3.0) - horse"},
				{value: "Epinephelus coioides () - Orange-spotted grouper",name: "Epinephelus coioides () - Orange-spotted grouper"},
				{value: "Anabas testudineus (fAnaTes1.2) - Climbing perch",name: "Anabas testudineus (fAnaTes1.2) - Climbing perch"},
				{value: "Bubalus bubalis (NDDB_SH_1)",name: "Bubalus bubalis (NDDB_SH_1)"},
				{value: "Sus scrofa (Large white v1 from ensembl) - pig",name: "Sus scrofa (Large white v1 from ensembl) - pig"},
				{value: "Homo sapiens (T2T_CHM13v2) - Human",name: "Homo sapiens (T2T_CHM13v2) - Human"},
				{value: "Salmo salar (USDA_NASsal_1.1) - Atlantic salmon",name: "Salmo salar (USDA_NASsal_1.1) - Atlantic salmon"},
				{value: "Vulpes lagopus (ASM1834538v1) - Arctic fox",name: "Vulpes lagopus (ASM1834538v1) - Arctic fox"},
				{value: "Takifugu rubripes (fTakRub1.3 from ENA)",name: "Takifugu rubripes (fTakRub1.3 from ENA)"},
				{value: "Macaca nemestrina (Mnem_1.0)",name: "Macaca nemestrina (Mnem_1.0)"},
				{value: "Eptesicus fuscus (EptFus1.0) - Big brown bat", name: "Eptesicus fuscus (EptFus1.0) - Big brown bat"},
				{value: "Oncorhynchus mykiss (USDA_OmykA_1.1) - rainbow trout",name: "Oncorhynchus mykiss (USDA_OmykA_1.1) - rainbow trout"},
				{value: "Pteropus alecto (ASM32557v1) - Black flying fox",name: "Pteropus alecto (ASM32557v1) - Black flying fox"},
				{value: "Macaca fascicularis (6.0) - Crab-eating macaque",name: "Macaca fascicularis (6.0) - Crab-eating macaque"},
				{value: "Dicentrarchus labrax - (European seabass)",name: "Dicentrarchus labrax - (European seabass)"},
				{value: "Equus asinus (ASM1607732v2) - Ass",name: "Equus asinus (ASM1607732v2) - Ass"},
				{value: "GRCm39/mm39- mouse", name: "GRCm39/mm39- mouse"},
				
]
let textareaprops = {
    id: 'Target_sequence',
    name: 'query',
    label: "Query Sequences without PAM from 5' to 3'",
    rows: 10,
    placeholder: 'AAAGGAAACCATTGTGTTAA\nCAGCAACTCCAGGGGGCCGC'
  };

  
  function handlemismatchesInput(event) {
    const inputmismatchValue = event.target.value;

    // Check if the input is negative or fraction number
    if (inputmismatchValue < 0 || inputmismatchValue % 1 !== 0 || inputmismatchValue > 9) {
      alert("not allowed!");
    
      mismatches = 0;
    } else {
      mismatches = inputmismatchValue;
    }
  }

  const uploadEndpoint = "http://localhost:8006/uploadfile/";
 
  let status = ''; 
  async function handleFileUpload(event) {
    const file = event.target.files[0]; // Get the selected file
    const formData = new FormData(); // Create a new FormData object
    formData.append('file', file); 
    status = 'uploading';

    try {
      const response = await fetch(uploadEndpoint, { // Send a POST request to the backend
        method: 'POST',
        body: formData
      });

      if (response.ok) {
		status = 'success';
        console.log('File uploaded successfully!');
       
      } else {
        console.error('Failed to upload file');
        
      }
    } catch (error) {
      console.error('Error uploading file:', error);
     
    }
  }
  
</script>

<Heading tag="h4" class="mb-4"> </Heading>

	
    
	<div class="mb-2">
		<Label for="email" class= "" >
		<span class="leading-relaxed dark:text-gray-400 mb-2"> E-mail (Optional): </span>
		</Label>
		<Input class="leading-relaxed dark:text-gray-400 mb-2" bind:value={email} type="email" size="lg" id="email" placeholder="your E-mail" />
	</div>

	
		<Label class="pb-2">Upload vcf file</Label>
		<Fileupload id="file" on:change={handleFileUpload} required/>
		{#if status === 'uploading'}
		<!-- Display progress bar when uploading -->
		<p style="color: red;">uploading, please wait! </p>
	  {:else if status === 'success'}
		<!-- Display success message when upload is successful -->
		<p style="color: blue;">File uploaded successfully!</p>
	  {/if}

	  <Heading tag="h4" class="mb-4"> </Heading>

	<div class="mb-2"> 
			<Label for ="Pams">Select PAM Type</Label>
			<Select id="Pams" class="mt-2" bind:value={Pam} >
				
				{#each Pams as {value, name}}
				<option {value}> {name}</option>
					    
				{/each}
			</Select>
	
		</div>
		
		
		
			<div class="mb-2" >
				
				<Label for ="Target_Genomes">Select Target Genome</Label>
			<Select id="Target_genomes" class="mt-2" bind:value={Target_Genome}>
				{#each Target_Genomes as {value, name}}
				<option {value}> {name}</option>
				{/each}
			</Select>
			</div>
	<div> 

	</div>

   
	<div>
		<span> Query Sequences without PAM from '5 to 3' </span>
		<Textarea {...textareaprops} bind:value={query_seq} required />
		
	</div>

<Heading tag="h4" class="mb-4"></Heading>
<div class="px-5">
	
	<div class="mb-6">
		<Label for="mismatches" class="mb-2">Maximum number of mismatches between gRNA and the target </Label>
		<Input bind:value={mismatches} type="number" size = "lg" id="mismatches" placeholder="0" on:input={handlemismatchesInput} required/>
	</div>
	
</div>
