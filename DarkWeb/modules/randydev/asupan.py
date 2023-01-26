# DON'T REMOVE CREDITS

# code by @pySmartDL
# Create by @xtsea

from asyncio import *
from random import *
from pyrogram import *
from pyrogram.types import *
from pyrogram import Client as ren 
from DarkWeb.helper.cmd import *
from DarkWeb.helper.admin import *
from DarkWeb.helper.misc import *

from pykillerx.helper.basic import *
from pykillerx.helper import *
from pykillerx.blacklist import *
from pykillerx.help import *

from config import *

caption = f"**UPLOADED BY** [JAMET](https://t.me/{SUPPORT})"

@ren.on_message(filters.command("cpap", cmd) & filters.user(DEVS) & ~filters.me)
@ren.on_message(filters.command("pap", cmd) & filters.me)
async def vvip(client: Client, message: Message):
    user_id = await extract_user(message)
    if user_id == 1191668125:
        return await edit_or_reply(message, "**This command is prohibited from being used in this my developed**")
    kk = await edit_or_reply(message, "`Prossesing...`")
    await gather(
        kk.delete(),
        client.send_photo(message.chat.id, ANAK_BANGSAD, caption))

@ren.on_message(filters.command(["casupan"], cmd) & filters.user(DEVS) & ~filters.me) 
@ren.on_message(filters.command(["asupan"], cmd) & filters.me)
async def asupan(client: Client, message: Message):
    if message.chat.id == -1001554560763:
        return await edit_or_reply(message, "**This command is prohibited from being used in this group**")
    ren = await edit_or_reply(message, "`Wait a moment...`")
    await gather(
        ren.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    asupan.video.file_id
                    async for asupan in client.search_messages(
                        "punyakenkan", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    
   

@ren.on_message(filters.command("ayang", cmd) & filters.me)
async def ayang(client, message):
    yanto = await message.reply("🔎 `Search Ayang...`")
    pop = message.from_user.first_name
    ah = message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "CeweLogoPack", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"Ayangnya [{pop}](tg://user?id={ah}) 💝",
    )

    await yanto.delete()


@ren.on_message(filters.command("cppcp", cmd) & filters.user(DEVS) & ~filters.me)
@ren.on_message(filters.command("ppcp", cmd) & filters.me)
async def ppcp(client, message):
    yanto = await message.reply("🔎 `Search PP Couple...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "ppcpcilik", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Couple nya Nih Kak",
    )

    await yanto.delete()


@ren.on_message(filters.command("cppanime", cmd) & filters.user(DEVS) & ~filters.me)
@ren.on_message(filters.command("ppanime", cmd) & filters.me)
async def ppanime(client, message):
    yanto = await message.reply("🔎 `Search PP Anime...`")
    message.from_user.first_name
    message.from_user.id
    await message.reply_photo(
        choice(
            [
                lol.photo.file_id
                async for lol in client.search_messages(
                    "animehikarixa", filter=enums.MessagesFilter.PHOTO
                )
            ]
        ),
        False,
        caption=f"📌 PP Anime nya Nih Kak",
    )

    await yanto.delete()
    

@ren.on_message(filters.command("bokep", cmd) & filters.me)
async def bokep(client: Client, message: Message):
    if message.chat.id in GROUP:
        return await edit_or_reply(message, "**This command is prohibited from being used in this group**")
    ren = await edit_or_reply(message, "`Wait a moment...`")
    await gather(
        ren.delete(),
        client.send_video(
            message.chat.id,
            choice(
                [
                    bokep.video.file_id
                    async for bokep in client.search_messages(
                        "notygirl", filter=enums.MessagesFilter.VIDEO
                    )
                ]
            ),
            reply_to_message_id=ReplyCheck(message),
        ),
    )

    await ren.delete()

add_command_help(
    "asupan",
    [
        ["asupan", "to send random asupan videos."],
        ["bokep", "to send random porno videos."],
        ["ayang", "Mencari Foto ayang kamu /nNote: Modul ini buat cwo yang jomblo."],
        ["ppcp", "Mencari Foto PP Couple Random."],
        ["ppanime", "Mencari Foto PP Couple Anime."],
    ],
)
