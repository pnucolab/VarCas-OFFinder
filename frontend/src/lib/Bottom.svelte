<script>
    import { A, P } from 'flowbite-svelte';
</script>

<footer class="py-10 border-t border-gray-200">
    <div class="px-2 sm:px-4">
        <div class="mx-auto flex flex-col container">
            <div class="flex flex-row gap-14 mb-14 justify-center flex-wrap">
                <div class="flex flex-col">
                </div>
                <div class="flex flex-col">
                    <P class="mb-3"><span class="font-bold text-sm">designed & developed by:</span></P>
                    <A class="flex-grow ml-3" href="https://pnucolab.com" target="_blank"><img class="w-60" src="/pnucolab.png" alt="Computational Omics Laboratory at Pusan National University" /></A>
                </div>
            </div>
            <P class="text-center">© 2024, all rights reserved.</P>
        </div>
    </div>
</footer>