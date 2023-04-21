<script>
	import { Spinner } from 'flowbite-svelte';
	import { load } from './fetch';
	import Top from '../lib/Top.svelte';
	import { A } from 'flowbite-svelte';
	import { Heading } from 'flowbite-svelte';
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import {
		Table,
		TableBody,
		TableBodyCell,
		TableBodyRow,
		TableHead,
		TableHeadCell
	} from 'flowbite-svelte';
	export let ticket;
	let last = (a, i) => i == a.length - 1;
	let result = {};
	let loaded = false;
	
	let pathways =[]
	
	
	async function get_result(ticket) {
		const data = await load('result?ticket='+ ticket);
		if (data.success) {
			if (data.status == 0) {
				pathways = [...data.pathway];
			
				
				
			} else if (data.status > 0) {
				setTimeout(() => get_result(ticket), 1000);
			}
		}
		result = data;
	}
	async function get_result_info(ticket) {
		const results = await load('result?ticket=' + ticket);
		return results;
	}
	
	onMount(async () => {
		await get_result(ticket);
		loaded = true;
	});
	$: {
		
			pathways = result.pathway;
		
	}
</script>

<Top />

{#if loaded}
	<p class="mb-5 text-center font-bold break-all">
		You can access this page again using this link: <A href="">{$page.url}</A>
	</p>
	<Heading class="mb-5" tag="h4">Result Summary</Heading>
	<Table class="border">
		<TableHead>
			<TableHeadCell>Job ID</TableHeadCell>
			<TableHeadCell>output file name</TableHeadCell>
			<TableHeadCell>summary file name</TableHeadCell>
			<TableHeadCell>Status</TableHeadCell>
		</TableHead>
		<TableBody>
			<TableBodyRow>
				<TableBodyCell
					> {result.task_id}
				</TableBodyCell>
				<TableBodyCell
					></TableBodyCell
				>
				<TableBodyCell
					></TableBodyCell
				>
				
				<TableBodyCell>
					{#if result.success}
						{#if result.status == 0} Finished {/if}
						{#if result.status == 1} Running <Spinner size={4} />{/if}
						{#if result.status == 2} Waiting for a slot <Spinner size={4} />{/if}
						{#if result.status == -1} Cancelled {/if}
						{#if result.status == -2} Error {/if}
					{:else}
						No such job ID
					{/if}
				</TableBodyCell>
			</TableBodyRow>
		</TableBody>
	</Table>

	
{:else}
	<div class="w-full text-center">
		<Spinner class="mt-20" />
	</div>
{/if}
