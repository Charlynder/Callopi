<!-- ProductCard.svelte -->

<script lang='ts'>
  export let product;
</script>

<style>
  .card {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 16px;
    margin: 16px;
    max-width: 300px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }

  h2 {
    margin-bottom: 8px;
    color: #333;
  }

  p {
    margin-bottom: 16px;
    color: #666;
  }

  .price {
    font-weight: bold;
    color: #333;
  }
</style>

<div class="card">
  <h2>{product.name}</h2>
  <p>{product.description}</p>
  <p class="price">Price: ${product.price}</p>
</div>
