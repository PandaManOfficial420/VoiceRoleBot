import discord

# ==========================
# CONFIG
# ==========================
TOKEN = "MTUyODI1NDQ3MTcxOTc0NzU4NA.GT8_4T._VK8LfKjijHMBFy6ZoQmPj1M7LPeJc5a_Jt0hs"  # Replace with your NEW bot token
ROLE_ID = 1528254838553706616

# ==========================
# BOT SETUP
# ==========================
intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.voice_states = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.event
async def on_voice_state_update(member, before, after):
    # User joined a voice channel
    if before.channel is None and after.channel is not None:
        role = member.guild.get_role(ROLE_ID)

        if role is None:
            print("Role not found.")
            return

        if role not in member.roles:
            try:
                await member.add_roles(role)
                print(f"Gave role to {member}")
            except discord.Forbidden:
                print("Missing permission to manage roles.")
            except Exception as e:
                print(f"Error: {e}")


client.run(TOKEN)
