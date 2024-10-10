<script>
  export let data = "Mismatches=0; Mismatches=1;";
  
  // Split the data into individual entries
  const entries = data.split(';').filter(entry => entry.trim());
  
  // Extract the values for "Bulge Size" and "Mismatches" for each entry
  const values = entries.map(entry => ({
    
    mismatches: entry.includes('Mismatches') ? entry.split('=')[1] : 'N/A'
  }));
</script>

<table>
  <thead>
    <tr>
      
      <th>Mismatches</th>
    </tr>
  </thead>
  <tbody>
    {#each values as value}
      <tr>
        
        <td>{value.mismatches}</td>
      </tr>
    {/each}
  </tbody>
</table>
  
  
  
  
  
  
  