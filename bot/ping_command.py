from discord import Message

from bot.command import Command


class PingCommand(Command):

    async def execute(self, msg: Message):
        await msg.channel.send("pong")

    def get_name(self):
        return "ping"
