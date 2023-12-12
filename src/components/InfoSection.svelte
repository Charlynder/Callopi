<script lang='ts'>
  export let product: any;

  let isFolded = false;

  function toggleFold() {
    isFolded = !isFolded;
  }
</script>

<style>
  .card {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    margin: 16px;
    max-width: 300px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    position: relative;
    overflow: hidden;
    transition: all 0.3s ease-out;
  }

  .content {
    overflow: hidden;
    transition: max-height 0.3s ease-out;
  }

  h2 {
    margin-bottom: 8px;
    color: #333;
    cursor: pointer;
  }

  p {
    margin-bottom: 8px;
    color: #666;
    transition: opacity 0.3s ease-out;
  }

  .price {
    font-weight: bold;
    color: #333;
  }

  .folded {
    max-height: 70px; /* Adjust as needed */
  }

  .folded .content {
    max-height: 0;
    padding-top: 0;
    padding-bottom: 0;
  }

  .folded p {
    opacity: 0;
  }
</style>

<div class="card" class:folded={isFolded}>
  <h2 on:click={toggleFold}>{product.name}</h2>
  <div class="content" class:folded={isFolded}>
    <p>{product.description}</p>
    <p class="price">Price: ${product.price}</p>
  </div>
</div>
