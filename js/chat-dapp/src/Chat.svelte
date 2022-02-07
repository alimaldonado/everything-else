<script>
    import Login from "./Login.svelte";
    import ChatMessage from "./ChatMessage.svelte";
    import { username, user } from "./user";
    import { onMount } from "svelte";

    import GUN from "gun";
    const db = GUN();
    const SEA = GUN.SEA;

    let newMessage;
    let messages = [];

    onMount(() => {
        db.get("chat")
            .map()
            .once(async (data, id) => {
                if (data) {
                    const key = "#foo";
                    var message = {
                        who: await db.user(data).get("alias"),
                        what: (await SEA.decrypt(data.what, key)) + "",
                        when: GUN.state.is(data, "what"),
                    };

                    if (message.what) {
                        messages = [...messages.slice(-100), message];
                    }
                }
            });
    });

    async function sendMessage() {
        const secret = await SEA.encrypt(newMessage, "#foo");
        const message = user.get("all").set({
            what: secret,
        });
        const index = new Date().toISOString();

        db.get("chat").get(index).put(message);
    }
</script>

<div class="container">
    {#if $username}
        <main>
            {#each messages as message (message.when)}
                <ChatMessage {message} sender={$username} />
            {/each}
        </main>
        <form on:submit|preventDefault={sendMessage} />
    {:else}
        <main>
            <Login />
        </main>
    {/if}
</div>
