const { Client, GatewayIntentBits } = require("discord.js");

const client = new Client({
    intents: [
        GatewayIntentBits.Guilds,
        GatewayIntentBits.GuildVoiceStates,
        GatewayIntentBits.GuildMembers
    ]
});

// Put your Role ID here
const ROLE_ID = "1528254838553706616";

client.once("ready", () => {
    console.log(`Logged in as ${client.user.tag}`);
});

client.on("voiceStateUpdate", async (oldState, newState) => {
    // User joined a voice channel
    if (!oldState.channelId && newState.channelId) {
        const member = newState.member;

        if (!member.roles.cache.has(ROLE_ID)) {
            try {
                await member.roles.add(ROLE_ID);
                console.log(`Gave role to ${member.user.tag}`);
            } catch (err) {
                console.error(err);
            }
        }
    }
});

client.login("MTUyODI1NDQ3MTcxOTc0NzU4NA.GT8_4T._VK8LfKjijHMBFy6ZoQmPj1M7LPeJc5a_Jt0hs");
