<script>
    import { cart, items, cartDetails, user_info } from "../stores"
    import { onMount } from "svelte";
    import { createEventDispatcher } from "svelte";

    import LallatiApi from "../LallatiApi";
    export let activePage

    const dispatch = createEventDispatcher()
    
    onMount(async () => {
        $items = await LallatiApi.getCartItems($cart),
        $cartDetails = await LallatiApi.getCartDetails($cart)
    })


    const increaseItem = async (item) => {
        const quantity = item.quantity + 1
		const id = item.id
        const cartdetail = await fetch(`http://127.0.0.1:8000/carts/${$cart}/items/${id}/`,{
            method: 'PATCH',
            body: JSON.stringify({
                quantity: quantity,
            }),
			headers: {
        		'Content-Type': 'application/json; charset=utf-8'
    		}
        });
        const data = await cartdetail.json()
        $items = await LallatiApi.getCartItems($cart)
        $cartDetails = await LallatiApi.getCartDetails($cart)
    }


	const decreaseItem = async (item) => {
		const quantity = item.quantity - 1
        if(quantity === 0) {
            deleteItem(item)
        }
		const id = item.id
		const cartdetail = await fetch(`http://127.0.0.1:8000/carts/${$cart}/items/${id}/`,{
            method: 'PATCH',
            body: JSON.stringify({
                quantity: quantity,
            }),
			headers: {
        		'Content-Type': 'application/json; charset=utf-8'
    		}
        });
		const data = await cartdetail.json()
        $items = await LallatiApi.getCartItems($cart)
        $cartDetails = await LallatiApi.getCartDetails($cart)
	}

    const deleteItem = async (item) => {
        const id = item.id;
        const res = await fetch(`http://127.0.0.1:8000/carts/${$cart}/items/${id}/`, {
            method: 'DELETE',
        })
        $items = await LallatiApi.getCartItems($cart)
        $cartDetails = await LallatiApi.getCartDetails($cart)
    }


    const makeOrder = async () => {
		const res = await fetch(`http://127.0.0.1:8000/orders/`);
		const data = await res.json()
        clearBag()
        dispatch('order', 'order')
	}

    const clearBag = () => {
        $items.forEach(deleteItem)
    }

    const sendMail = async () => {
        console.log($user_info.email)
        const res = await fetch('http://127.0.0.1:8000/send_email/', {
			method: 'POST',
            body: JSON.stringify({
                // subject: "confirm order",
                // message: "Your order has been confirmed",
                // email_from: "sofia.elmalmi@gmail.com",
                recipient: $user_info.email
            }),
            headers: {
        		'Content-Type': 'application/json; charset=utf-8'
    		}
		})
        const data = await res.json()
        console.log(data)
    }
    console.log($user_info)

</script>


<div class="articles">
    {#if $items.length > 0 }
        {#each $items as item (item.id)}
            <div class='article'>
                <img src="{item.product.image}" alt="">
                <p class="name">{item.product.name}</p>
                <p class="price">{item.product.price}</p>
                <p class="quantity">{item.quantity}</p>
                <button on:click={() => increaseItem(item)} class="increase">+</button>
                <button on:click={() => decreaseItem(item)} class="decrease">-</button>
                <button on:click={() => deleteItem(item)} class="delete">x</button>
            </div>
            {/each}
            <div class="totale">
                <p>Total price: {$cartDetails.total_price}</p>
            </div>
            
            <div class="order">
                <button 
                        on:click={makeOrder}
                        on:click={sendMail}
                > Make Order</button>
            </div>
    {:else}
            <p class="empty">Your bag is empty</p>
    {/if}
</div>


<style>
    .articles {
        width: 50%;
        margin: 20px;
        padding: 30px;      
    }

    .article {
        background-color: rgb(61, 59, 59);
        margin: 20px;
    }

    .name, .price, .quantity {
        display: inline-block;
        color: white;
        padding-left: 15px;
        padding-right: 15px;

    }

    img{
        width: 15%;
        height: auto;
    }

    .totale {
        color: bisque;
        display: flex;
        justify-content: center;
        font-size: 17px;
    }

    .delete {
        background-color: red;
    }

    .order {
        display: flex;
        justify-content: center;
    }

    .empty {
        color: white;
        font-size: 20px;
    }
</style>