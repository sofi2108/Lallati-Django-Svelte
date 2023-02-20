<script>
	import { createEventDispatcher } from "svelte";
	export let activePage;

	const dispatch = createEventDispatcher()
</script>


<div class="nav-bar">
    <img class="logo" src="img/logo.png" alt="">
    <div class="side-navbar">
        <a on:click|preventDefault={() => dispatch('changePage', 'bag')} href="">Bag</a>
        <a on:click|preventDefault={() => dispatch('changePage', 'account')} href="">My account</a>
    </div>
</div>
<div class="products-navbar">
	<a on:click|preventDefault={() => dispatch('changePage', 'home')} href="">Home</a>
    <a on:click|preventDefault={() => dispatch('changePage', 'caftan')} href="">Caftan</a>
    <a on:click|preventDefault={() => dispatch('changePage', 'accessories')} href="">Accessories</a>
</div>


<style>
    .nav-bar {
		display: flex;
		justify-content: center;
	}

	.logo {
		width: 120px;
		height: auto;
		margin: -15px;
		padding: 0;
	}

	.side-navbar{
		position: absolute;
		right: 90px;
		display: flex;
		justify-content: center;
	}

	.side-navbar a {
		margin: 20px;
		padding: 10px;
		color: white;
		font-size: 14px;
		font-family: Arial, Helvetica, sans-serif;
	}

	a:hover {
		text-decoration: underline;
		text-decoration-color: rgb(243, 206, 95);
		text-decoration-thickness: 1.5px;
		text-underline-offset: 2px;
	}

	.products-navbar {
		display: flex;
		justify-content: center;
		margin-bottom: 0;
		padding-bottom: 0;
	}

	.products-navbar a {
		color: white;
		margin: 30px;
		margin-bottom: 13px;
		padding-bottom: 0;
	}

	.products-navbar a:hover {
		text-underline-offset: 13px;
	}
</style>