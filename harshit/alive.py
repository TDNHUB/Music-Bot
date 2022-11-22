# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Copyright (C) 2021 By @Itz_VeNom_xD
# Copyright (C) 2021 By @Dr_Asad_Ali
# Copyright (C) 2021 By @HarshitSharma361

import asyncio
from time import time
from datetime import datetime
from rocks.helpers.filters import command
from rocks.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4c7025b0b94c0d2b5f94a.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 ʜᴇʟʟᴏ, ɪ ᴀᴍ ᴛᴅɴ ᴍᴜsɪᴄ
ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ᴄʀᴇᴀᴛᴏʀ : [ᴀᴀᴅɪᴛʏᴀ](https://t.me/Itzaadityaxd)
┣★ ᴄʜᴀᴛᴛɪɴɢ : [ғᴍᴄ](https://t.me/FRIENDS_MASTI_CLUB_FMC)
┣★ sᴜᴘᴘᴏʀᴛ : [ᴛᴅɴ](https://t.me/TDN_CHAT)
┣★ ᴏᴡɴᴇʀ › : [ᴀᴀᴅɪᴛʏᴀ](https://t.me/saikostar_xd)
┗━━━━━━━━━━━━━━━━━┛

💞 ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀɴʏ ǫᴜᴇsᴛɪᴏɴs ᴛʜᴇɴ
ᴅᴍ ᴛᴏ ᴍʏ [ʟᴇɢᴇɴᴅ ᴏᴡɴᴇʀ](https://t.me/saikostar_xd) ...
━━━━━━━━━━━━━━━━━━━━━━━━**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ ᴀᴅᴅ ᴛᴅɴ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ❱ ➕",
                        url=f"https://t.me/Asad_Music_Bot?startgroup=true",
                    )
                ]
            ]
        ),
    )


@Client.on_message(
    commandpro(["/start", "/alive", "ᴛᴅɴ"]) & filters.group & ~filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/b92ed11ca9259ec96aaee.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴊᴏɪɴ ʜᴇʀᴇ ᴀɴᴅ sᴜᴘᴘᴏʀᴛ 💞",
                        url=f"https://t.me/FRIENDS_MASTI_CLUB_FMC",
                    )
                ]
            ]
        ),
    )


@Client.on_message(
    commandpro(["repo", "#repo", "@repo", "/repo", "source"])
    & filters.group
    & ~filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/64191119f900180fab849.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💥 ᴄʟɪᴄᴋ ᴍᴇ ᴛᴏ ɢᴇᴛ ʀᴇᴘᴏ 💞", url=f"https://t.me/saikostar_xd"
                    )
                ]
            ]
        ),
    )
