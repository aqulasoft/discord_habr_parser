import discord

from bot.command import Command
from bot.get_article_command import ArticleCommand
from bot.ping_command import PingCommand

prefix = '#'


class HabrParserClient(discord.Client):

    def __init__(self):
        super().__init__()
        self.commands = {}

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message: discord.Message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        text = message.content

        if not text.startswith(prefix):
            return

        text = text[len(prefix):]  # "article"

        cmd = text.split()[0]

        if cmd not in self.commands:
            return

        await self.commands[cmd].execute(message)

    def register_command(self, command: Command):
        self.commands[command.get_name()] = command


client = HabrParserClient()

client.register_command(ArticleCommand())
client.register_command(PingCommand())

client.run('ODE3NDYyNjIwOTgxOTUyNTky.YEJ3ZA.Koi0UcX0byO2Vi3RId0TUy2M9Lw')
