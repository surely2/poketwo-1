from discord.ext import commands

from . import mongo


class MustHaveStarted(commands.CheckFailure):
    pass


def is_admin():
    return commands.check_any(
        commands.is_owner(), commands.has_permissions(administrator=True)
    )


def has_started():
    async def predicate(ctx: commands.Context):
        member = await mongo.Member.find_one({"id": ctx.author.id})

        return member is not None

    return commands.check(predicate)
