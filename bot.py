import discord
import responses  # Assuming 'responses' is a separate module that handles user responses

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"{client.user} is now running")

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # Ignore messages sent by the bot itself

    user_message = message.content  # Get the content of the user's message
    is_private = isinstance(message.channel, discord.DMChannel)  # Check if the message is sent in a private channel

    response = responses.handle_response(user_message)

    try:
        if is_private:
            await message.author.send(response)
        else:
            await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = "MTE2NzcxNTI0OTYwMDg2NDI3Ng.G7Wi_x.gmL5WreupHI6YCsBqsfTepoVCJJ5E15RJuzfNI"  # Replace with your bot token
    client.run(TOKEN)

if __name__ == '__main__':
    run_discord_bot()
