<script>
    import { onMount } from 'svelte';
    import { cart } from '../stores'

    let caftans = [];
    export let activePage;

    onMount(async () => {
        const res = await fetch('http://127.0.0.1:8000/caftans/');
        caftans = await res.json();
    })

    const addToBag = async (id) => 
		 {
            const res = await fetch(`http://127.0.0.1:8000/carts/${$cart}/items/`, {
            method: 'POST', 
            headers: {
                    'Accept': 'application/json',
                   'Content-Type': 'application/json'
                   },
            body: JSON.stringify({
                product_id: id,
                quantity: 1
            }) 
        })
        const data = await res.json()
    }
</script>


<div class="caftans">
{#each caftans as caftan (caftan.id)}
    <div class="dress">
        <img src={caftan.image} alt="">
        <div class="dress-info">
            <p>{caftan.name}</p>
            <p>${caftan.price}</p>
        </div>
        <button on:click={()=> addToBag(caftan.id)} class="add_to_cart">Add to cart</button>
    </div>
{/each}
</div>


<style>
    .caftans {
        display:flex;
        justify-content: center;
        flex-wrap: wrap;
    }

    .dress {
        margin: 50px;
        padding: 15px;
        
    }

    .dress img {
        width: 250px;
        height: 300px;
    }

    .dress-info {
        display: flex;
        justify-content: center;
        color: white;
        padding-bottom: 25px;
    }


    .caftans p {
        margin: 20px;
    }

    .add_to_cart {
        color: black;
        font-size: 10px;
        width: 100px;
        margin: 0px auto; 
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .add_to_cart:hover {
        cursor: pointer;
      
    }

    

</style>