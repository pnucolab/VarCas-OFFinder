
<script>
	
	import Bottom from '$lib/Bottom.svelte';
	import { Navbar, NavBrand, NavUl, NavLi, } from 'flowbite-svelte';
	import { page } from '$app/stores';
	import './styles.css';
	
</script>
<Navbar let:hidden>
	<div class="flex items-center  gap-1 p-0 m-0   text-black  rounded-lg w-full">
	<NavBrand href="/">
		<span class="self-center whitespace-nowrap text-xl font-semibold dark:text-white p-0 m-0 ">CRISPR Toolkit</span>
	</NavBrand>
	<NavUl class="flex flex-row gap-1 p-0 m-0" {hidden}>

		<NavLi href="/" active={$page.url.pathname === '/'} class="p-0 m-0 text-xl">Cas-OFFinder</NavLi>
		<NavLi href="/about" active={$page.url.pathname === '/about'} class="p-0 m-0 text-xl">About</NavLi>
	</NavUl>
    </div>
</Navbar>

<div class="px- sm:px-4">
	<div class="mx-auto flex mb-20 flex-col container">
		<slot />
	</div>
</div>

<Bottom />