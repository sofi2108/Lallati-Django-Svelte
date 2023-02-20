<script>
    import { onMount } from 'svelte';

    let accessories = [];
    export let activePage;

    onMount(async () => {
        const res = await fetch('http://127.0.0.1:8000/accessories/');
        accessories = await res.json();
    })
</script>


<div class="accessories">
{#each accessories as accessory (accessory.id)}
    <div class="accessory">
        <img src={accessory.image} alt="">
        <div class="accessory-info">
            <p>{accessory.name}</p>
            <p>${accessory.price}</p>
        </div>
    </div>
{/each}
</div>


<style>
    .accessories {
        display:flex;
        justify-content: center;
        flex-wrap: wrap;
    }

    .accessory {
        margin: 50px;
        padding: 15px;
    }

    .accessory img {
        width: 250px;
        height: 300px;
    }

    .accessory-info {
        display: flex;
        justify-content: center;
        color: white;
        padding-bottom: 25px;
    }

    .accessories p {
        margin: 20px;
    }

</style>