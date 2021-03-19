from discord import Message

from bot.command import Command


class ArticleCommand(Command):

    async def execute(self, msg: Message):
        await msg.channel.send(self.get_article())

    def get_name(self):
        return "article"

    def get_article(self):
        return "TITLE + TEXT article"
