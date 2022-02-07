<script>
    import { user } from "./user";
    let username;
    let password;

    function login() {
        user.auth(username, password, (error) => {
            error && alert(error);
        });
    }

    function signup() {
        user.create(username, password, (error) => {
            if (error) {
                alert(error);
            } else {
                login();
            }
        });
    }
</script>

<label for="username">Username</label>
<input
    type="text"
    name="username"
    bind:value={username}
    minlength="3"
    maxlength="16"
/>

<label for="password">Password</label>
<input
    type="text"
    name="password"
    bind:value={password}
    minlength="3"
    maxlength="16"
/>

<button class="login" on:click={login}>Login</button>
<button class="login" on:click={signup}> Sign Up</button>
