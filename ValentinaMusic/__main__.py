import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ValentinaMusic import LOGGER, app, userbot
from ValentinaMusic.core.call import Valentina
from ValentinaMusic.misc import sudo
from ValentinaMusic.plugins import ALL_MODULES
from ValentinaMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("ValentinaMusic.plugins" + all_module)
    LOGGER("ValentinaMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Valentina.start()
    try:
        await Valentina.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ValentinaMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await valentina.decorators()
    LOGGER("ValentinaMusic").info(
        "Valentina Music Bot Started Successfully"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ValentinaMusic").info("Stopping Valentina Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
