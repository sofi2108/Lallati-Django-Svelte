<script>
    import { createEventDispatcher } from 'svelte';
    import { onMount } from 'svelte'
    import { cart } from '../stores'

    import LallatiApi from '../LallatiApi'

    export let activePage;


    const dispatch = createEventDispatcher()

    let caftans = [];
    let accessories = []

    onMount(async () => {
        const res = await fetch('http://127.0.0.1:8000/caftans/', 
            {
                method: 'GET'
            })
        const res2 = await fetch('http://127.0.0.1:8000/accessories/')
        caftans = await res.json()
        accessories = await res2.json()
        // check if the card is in local storage 
        $cart = LallatiApi.get()

        if ($cart == undefined){
            const cart = await fetch('http://127.0.0.1:8000/carts/', {
            method: 'POST', 
            headers: {
                   'Content-Type': 'application/json'
                   }
        })
        const cartres = await cart.json()
        LallatiApi.save(cartres['id'])
        }
        $cart = LallatiApi.get()
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

<main>
    <img src="img/girlincaftan.jpeg" alt="">
    <div class="new-collection">
        <p>New Collection</p>
    </div>
    <hr>
    <div class="caftan">
        <h1>Caftan</h1>
        {#each caftans.slice(0, 3) as caftan (caftan.id)}
            <div class="dress">
                <img src={caftan.image} alt="">
                <div class="dress-info">
                    <p>
                        {caftan.name}
                    </p>
                    <p>${caftan.price}</p>
                </div>
                <button on:click={()=>addToBag(caftan.id)} class="add_to_cart">Add to cart</button>
            </div>
        {/each}

        <div class="all-products">
            <a on:click|preventDefault=
                {() => dispatch('caftanPage', 'caftan')} 
                href="">See all Caftan</a>
        </div>
    </div>


    <div class="accessories">
        <h1>Accessories</h1>
        {#each accessories.slice(0, 3) as accessory (accessory.id)}
            <div class="dress">
                <img src="img/girlincaftan.jpeg" alt="">
                <div class="dress-info">
                    <p>{accessory.name}</p>
                    <p>${accessory.price}</p>
                </div>
            </div>
        {/each}
        <div class="all-products">
            <a on:click|preventDefault=
            {() => dispatch('caftanPage', 'accessories')}  
            href="">See all Accessories</a>
        </div>
    </div>
</main>


<style>
    main {
        height: 200vh;
        font-family: Arial, Helvetica, sans-serif;
    }

    img {
		display: block;
		width: 100%;
		height: 60vh;
		margin-top: 0;
		padding-top: 0;
		margin-left: auto;
		margin-right: auto;
        object-fit: cover;
	}

	.new-collection {
		display: flex;
		justify-content: center;
		color: white;
		font-size: 40px;
		text-shadow: 2px 2px #443f3f;
        margin-top: 25px;
	}

	.new-collection p {
		margin-bottom: 6px;
        padding: 0px;
		color: white;

	}

	hr {
		width: 30%;
		border-color: goldenrod;
        margin-bottom: 60px;
	}

    .accessories h1 {
        width: 10%;
        margin-right: auto;
        margin-left: auto;
        font-weight: 100;
    }

    .caftan {
        margin: 5px;
        padding: 2px;
    }

    .caftan h1 {
        display: flex;
        justify-content: center;
        font-weight: 100;
    }

    .dress {
        float: left;
        width: 33.33%;
        height: 40%;
    }

    .dress img {
        width: 250px;
        height: 300px;
    }

    .dress-info {
        display: flex;
        justify-content: center;
        color: white;
        padding-bottom: 0;
    }

    h1 {
        margin-bottom: 15px;
        padding-bottom: 25px;
        color: white;
        font-size: 30px;
    }

    .all-products {
        width: 100%;
        text-align: center;
        
    } 

    .all-products a {
        color: rgb(248, 248, 248);
        padding: 15px;
        border-right: 1Px solid goldenrod;
        border-left: 1Px solid goldenrod;

    }

    .caftan p, .accessories p {
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