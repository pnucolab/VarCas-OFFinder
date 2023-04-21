<!---
  <script>
  import "../app.postcss";
</script>

<slot />
-->
<script>
	
	import Bottom from '$lib/Bottom.svelte';
	import { Navbar, NavBrand, NavHamburger } from 'flowbite-svelte';
	import './styles.css';
</script>



<div class="px-2 sm:px-4">
	<div class="mx-auto flex mb-20 flex-col container">
		<slot />
	</div>
</div>

<Bottom />