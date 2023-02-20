<script>
    import LallatiApi from "../LallatiApi";
    import { user_info } from "../stores";

    let username;
    let password;
    let logedIn;
    let message;

    const submit = async (username, password) => {
        const res = await fetch(`http://127.0.0.1:8000/auth/jwt/create`, {
            method:'POST',
            body: JSON.stringify({
                username: username,
                password: password,
            }),
            headers: {
        		'Content-Type': 'application/json; charset=utf-8'
    		}
        })

        const data = await res.json()

        if (data.detail == 'No active account found with the given credentials'){
            message = data.detail
        }

        else {
            localStorage.clear()
        localStorage.setItem("token", JSON.stringify(data))
        const token = JSON.parse(localStorage.getItem('token'));
       
        const res2 = await fetch(`http://127.0.0.1:8000/auth/users/me/`, {
            method: 'GET',
            headers: {
                authorization: "JWT " + token.access
            }
        })
        $user_info = await res2.json()
    
        localStorage.setItem('id', $user_info.id)
        logedIn = true
        }
    }

    const logOut = () => {
        localStorage.clear()
        logedIn = false;
    }

</script>

{#if logedIn==true || localStorage.getItem('token')}
    <div>Loged In</div>
    <button on:click={logOut}>Log Out</button>
{:else}
    <div class="account">
        <form action="">
            <input class="username" type="text" placeholder="Username" bind:value={username}>
            <input class="password" type="text" placeholder="password" bind:value={password}>
            <button on:click|preventDefault={() => submit(username, password)}>Submit</button>
            {#if message}
                <div class="error">
                    {message}
                </div>
            {/if}
     </form>
    </div>
{/if}

<style>
    .account {
        display: flex;
        justify-content: center;
    }

   input {
    display: block;
   }

   .error {
    background-color: white;
    color: red;
   }
</style>