from userbot import bot
from sys import argv
import sys
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from userbot.utils import load_module
from userbot import LOAD_PLUG, LOGS, tornadoversion
from pathlib import Path
import asyncio
import telethon.utils

TORNADO_PIC = Config.ALIVE_PIC or "https://telegra.ph/file/21be5b02ff5de6690c046.mp4"

os.system("pip install -U telethon")

async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if Var.TG_BOT_USER_NAME_BF_HER is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=Var.APP_ID,
            api_hash=Var.API_HASH
        ).start(bot_token=Var.TG_BOT_TOKEN_BF_HER)
        print("Initialisation finished with no errors")
        print("Starting TornadoBot")
        bot.loop.run_until_complete(add_bot(Var.TG_BOT_USER_NAME_BF_HER))
        print("TornadoBot Startup Completed")
    else:
        bot.start()


import glob
path = 'userbot/plugins/*.py'
files = glob.glob(path)
for name in files:
    with open(name) as f:
        path1 = Path(f.name)
        shortname = path1.stem
        load_module(shortname.replace(".py", ""))

import userbot._core

print(f"""TORNADOBOT IS ON!!! TORNADOBOT VERSION :- {tornadoversion} YOUR ššøš½ššøš¹šš IS READY TO USE! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES @TornadoBot_Support .""")
async def tornado_is_on():
    try:
        if Config.TORNADOBOT_LOGGER != 0:
            await bot.send_file(
                Config.TORNADOBOT_LOGGER,
                TORNADO_PIC,
                caption=f"ą¼ŹÉÉ¢ÉÕ¼ÉaŹŹ į“Ņ į“į“ŅÉŖį“Źį“į“ą¼\n\n**šš“šššøš¾š½ āŖ {tornadoversion}**\n\nšš²š©š `.ping` or `.alive` š­šØ šš”ššš¤! \n\nš¹š¾šøš½ [TORNADOBOT š²š·š°š](t.me/MAHADEV_TORNADO_USERBOT_SUPPORT) šš¾ ššš“šš & š¹š¾šøš½ [TORNADO ššæš³š°šš“š](t.me/MAHADEV_TORNADO_USERBOT_OFFICIAL) šš¾ šŗš½š¾š šš“š¶šš°š³šøš½š¶ ššæš³š°šš“ š°š½š³ š½š“šš š°š±š¾šš TORNADOš±š¾š",
            )
    except Exception as e:
        LOGS.info(str(e))

bot.loop.create_task(tornado_is_on())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
