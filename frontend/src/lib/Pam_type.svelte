<script> 
   import { Heading} from 'flowbite-svelte'
	 let Pams=[
			{value: "SpCas9 from Streptococcus pyogenes: 5'-NGG-3'", name:"SpCas9 from Streptococcus pyogenes: 5'-NGG-3'"},
			{value: "SpCas9 from Streptococcus pyogenes: 5'-NRG-3' (R = A or G)", name:"SpCas9 from Streptococcus pyogenes: 5'-NRG-3' (R = A or G)"},
			{value:"StCas9 from Streptococcus thermophilus: 5'-NNAGAAW-3' (W = A or T)", name:"StCas9 from Streptococcus thermophilus: 5'-NNAGAAW-3' (W = A or T)"},
			{value:"NmCas9 from Neisseria meningitidis: 5'-NNNNGMTT-3' (M = A or C)", name:"NmCas9 from Neisseria meningitidis: 5'-NNNNGMTT-3' (M = A or C)"},
			{value:"SaCas9 from Staphylococcus aureus: 5'-NNGRRT-'3 (R=A or G)", name:"SaCas9 from Staphylococcus aureus: 5'-NNGRRT-'3 (R=A or G)"},
			{value:"CjCas9 from Campylobacter jejuni: 5'-NNNVRYAC-3' (V = G or C or A, R = A or G, Y = C or T)",name:"CjCas9 from Campylobacter jejuni: 5'-NNNVRYAC-3' (V = G or C or A, R = A or G, Y = C or T)"},
			{value:"CjCas9 from Campylobacter jejuni: 5'-NNNNRYAC-3' (R=A or G, Y= C or T)",name:"CjCas9 from Campylobacter jejuni: 5'-NNNNRYAC-3' (R=A or G, Y= C or T)"},
			{value:"AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTN-3'",name:"AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTN-3'"},
			{value:"AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTV-3' (V = G or C or A)",name:"AsCpf1 from Acidaminococcus or LbCpf1 from Lachnospiraceae: 5'-TTTV-3' (V = G or C or A)"},
			{value:"SpCas9 from Streptococcus pasteurianus: 5'-NNGTGA-3'",name:"SpCas9 from Streptococcus pasteurianus: 5'-NNGTGA-3'"},
			{value:"FnCpf1 from Francisella: 5'-TTN-3'",name:"FnCpf1 from Francisella: 5'-TTN-3'"},
			{value:"SaCas9 from Staphylococcus aureus: 5'-NNNRRT-'3 (R=A or G)",name:"SaCas9 from Staphylococcus aureus: 5'-NNNRRT-'3 (R=A or G)"},
			{value:"FnCpf1 from Francisella: 5'-KYTV-3'",name:"FnCpf1 from Francisella: 5'-KYTV-3'"},
			{value:"VRER SpCas9 from Streptococcus pyogenes: 5'-NGCG-3'",name:"VRER SpCas9 from Streptococcus pyogenes: 5'-NGCG-3'"},
			{value:"VQR SpCas9 from Streptococcus pyogenes: 5'-NGA-3",name:"VQR SpCas9 from Streptococcus pyogenes: 5'-NGA-3'"},
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
			{value:"NGC",name:"SpCas9 Variant from Streptococcus pyogenes: 5'-NGC-3'"},
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
<!--- class="  leading-relaxed  mb-2" class="space-y-2"--->
<!---
<div class="mb-2">
    <Label for="pam"  size="lg" >Select RGENs Type 
        <Select   size="lg" id="pam" items={Pam} class=" cursor-pointer flex-shrink-0 z-10 inline-flex py-2.5 px-4 items-center text-md font-medium text-left text-gray-500 bg-gray-100 border border-gray-300 rounded-l-lg hover:bg-gray-200 focus:ring-4 focus:outline-none focus:ring-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 dark:focus:ring-gray-700 dark:text-white dark:border-gray-600" bind:value={selected} />
      </Label>
</div>
-->
<!---
{#if selected}
  <p>You selected: {selected}</p>
  {:else}
  <p class='text-bold'>Please select PAM type</p>
{/if}
-->


	



<Heading tag="h4" class="mb-6"></Heading>