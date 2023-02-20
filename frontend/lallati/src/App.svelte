<script>
	import NavBar from "./components/NavBar.svelte";
	import Home from "./components/Home.svelte";
  	import Caftan from "./components/Caftan.svelte";
	import Accessories from "./components/Accessories.svelte";
	import Bag from "./components/Bag.svelte";
	import Order from "./components/Order.svelte";
  import Account from "./components/Account.svelte";

	let activePage = 'home';

	const changePage = (e) => {
		activePage = e.detail
	}
</script>

<main>
	
	<NavBar on:changePage = {changePage} {activePage}/>
	{#if activePage === 'home'}
		<Home on:caftanPage = {changePage} {activePage}/>
	{:else if activePage === 'caftan'}
		<Caftan {activePage}/>
	{:else if activePage === 'accessories'}
		<Accessories {activePage}/>
	{:else if activePage === 'bag'}
		<Bag on:order={changePage} {activePage}/>
	{:else if activePage === 'order'}
		<Order />
	{:else if activePage === 'account'}
		<Account />
	{/if}
</main>