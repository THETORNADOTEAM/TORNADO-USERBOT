"""
credits to @mrconfused and @sandy1709
"""
# Kang with credits. Using in tornadobot...
#    Copyright (C) 2020  sandeep.n(π.$)
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import base64
import os

from telegraph import exceptions, upload_file
from telethon.tl.functions.messages import ImportChatInviteRequest as Get

from userbot import CMD_HELP
from userbot.helpers.functions import (
    convert_toimage,
    deEmojify,
    phcomment,
    threats,
    trap,
    trash,
)
from tornadobot.utils import admin_cmd, edit_or_reply, sudo_cmd
from userbot.cmdhelp import CmdHelp
from . import *


@bot.on(admin_cmd(pattern="threats(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="threats(?: |$)(.*)", allow_sudo=True))
async def tornadobot(tornadomemes):
    replied = await tornadomemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(
            tornadomemes, "`Media file not supported. Reply to a supported media`"
        )
        return
    if replied.media:
        tornadomemmes = await edit_or_reply(tornadomemes, "`Detecting Threats.........`")
    else:
        await edit_or_reply(
            tornadomemes, "`Media file not supported. Reply to a suported media`"
        )
        return
    try:
        tornado = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        tornado = Get(tornado)
        await tornadomemes.client(tornado)
    except BaseException:
        pass
    download_location = await tornadomemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await tornadomemmes.edit(
                "`The replied file is not supported. It should be less than 5mb -_-`"
            )
            os.remove(download_location)
            return
        await tornadomemmes.edit("`Detected Threats....`")
    else:
        await tornadomemmes.edit("`the replied file is not supported`")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await tornadomemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    tornado = f"https://telegra.ph{response[0]}"
    tornado = await threats(tornado)
    await tornadomemmes.delete()
    await tornadomemes.client.send_file(tornadomemes.chat_id, tornado, reply_to=replied)


@bot.on(admin_cmd(pattern="trash(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="trash(?: |$)(.*)", allow_sudo=True))
async def tornadobot(tornadomemes):
    replied = await tornadomemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(
            tornadomemes, "`Media file not supported. Reply to a suported media`"
        )
        return
    if replied.media:
        tornadomemmes = await edit_or_reply(tornadomemes, "`Detecting Trash....`")
    else:
        await edit_or_reply(
            tornadomemes, "`Media file not supported. Reply to a suported media`"
        )
        return
    try:
        tornado = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        tornado = Get(tornado)
        await tornadomemes.client(tornado)
    except BaseException:
        pass
    download_location = await tornadomemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await tornadomemmes.edit(
                "`The replied file is not suported. Its size should be less than 5mb-_-`"
            )
            os.remove(download_location)
            return
        await tornadomemmes.edit("`Detected Trash.....`")
    else:
        await tornadomemmes.edit("Media file not supported. Reply to a suported media")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await tornadomemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    tornado = f"https://telegra.ph{response[0]}"
    tornado = await trash(tornado)
    await tornadomemmes.delete()
    await tornadomemes.client.send_file(tornadomemes.chat_id, tornado, reply_to=replied)


@bot.on(admin_cmd(pattern="trap(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="trap(?: |$)(.*)", allow_sudo=True))
async def tornadobot(tornadomemes):
    input_str = tornadomemes.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if "-" in input_str:
        text1, text2 = input_str.split("-")
    else:
        await edit_or_reply(
            tornadomemes,
            "**Command :** Reply to image or sticker with `.trap (name of the person to trap)-(trapper name)`",
        )
        return
    replied = await tornadomemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(
            tornadomemes, "Media file not supported. Reply to a suported media"
        )
        return
    if replied.media:
        tornadomemmes = await edit_or_reply(tornadomemes, "`Trapping.....`")
    else:
        await edit_or_reply(
            tornadomemes, "Media file not supported. Reply to a suported media"
        )
        return
    try:
        tornado = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        tornado = Get(tornado)
        await tornadomemes.client(tornado)
    except BaseException:
        pass
    download_location = await tornadomemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await tornadomemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await tornadomemmes.edit("`Trapped...`")
    else:
        await tornadomemmes.edit("Media file not supported. Reply to a suported media")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await tornadomemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    tornado = f"https://telegra.ph{response[0]}"
    tornado = await trap(text1, text2, tornado)
    await tornadomemmes.delete()
    await tornadomemes.client.send_file(tornadomemes.chat_id, tornado, reply_to=replied)


@bot.on(admin_cmd(pattern="phc(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="phc(?: |$)(.*)", allow_sudo=True))
async def tornadobot(tornadomemes):
    input_str = tornadomemes.pattern_match.group(1)
    input_str = deEmojify(input_str)
    if "-" in input_str:
        username, text = input_str.split("-")
    else:
        await edit_or_reply(
            tornadomemes,
            "**Command :** reply to image or sticker with `.phc (username)-(text in comment)`",
        )
        return
    replied = await tornadomemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(
            tornadomemes, "Media file not supported. Reply to a suported media"
        )
        return
    if replied.media:
        tornadomemmes = await edit_or_reply(tornadomemes, "`Making A Comment`.")
    else:
        await edit_or_reply(
            tornadomemes, "Media file not supported. Reply to a suported media"
        )
        return
    try:
        tornado = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        tornado = Get(tornado)
        await tornadomemes.client(tornado)
    except BaseException:
        pass
    download_location = await tornadomemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await tornadomemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await tornadomemmes.edit("Commented....")
    else:
        await tornadomemmes.edit("Media file not supported. Reply to a suported media")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await tornadomemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    tornado = f"https://telegra.ph{response[0]}"
    tornado = await phcomment(tornado, text, username)
    await tornadomemmes.delete()
    await tornadomemes.client.send_file(tornadomemes.chat_id, tornado, reply_to=replied)


CmdHelp("prank").add_command(
  "phc", "<reply to img> <name> - <comment>", "Changes the given pic to dp and shows a comment in phub with the given name", "<reply to img/stcr> .phc NAME - tornadoO PHUB"
).add_command(
  "trap", "<reply to img/stcr> <victim name> - <trapper name>", "Changes the given pic to another pic which shows that pic content is trapped in trap card", "<reply to img/stcr> .trap Loda - Lassan"
).add_command(
  "trash", "<reply to image/sticker>", "Changes the given pic to another pic which shows that pic content is as equal as to trash(waste)"
).add_command(
  "threats", "<reply to image/sticker>", "Changes the given pic to another pic which shows that pic content is threat to society as that of nuclear bomb"
).add_command(
  "prank", None, "If this module doesn't work then contact admins in @TornadoBot_Chit_Chat"
).add()
