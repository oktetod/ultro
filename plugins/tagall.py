import asyncio
from . import ultroid_cmd
from telethon import events, TelegramClient
from telethon.errors import UserNotParticipantError
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator



spam_chats = []


@ultroid_cmd(pattern="all ?(.*)")
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("__Perintah ini dapat digunakan dalam grup dan channel!__")

    is_admin = False
    try:
        partici_ = await event.client(GetParticipantRequest(
            event.chat_id,
            event.sender_id
        ))
    except UserNotParticipantError:
        is_admin = False
    else:
        if (
                isinstance(
                    partici_.participant,
                    (
                            ChannelParticipantAdmin,
                            ChannelParticipantCreator
                    )
                )
        ):
            is_admin = True
    if event.pattern_match.group(1) and event.is_reply:
        return await event.reply("__Beri aku satu argumen!__")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "__Saya tidak bisa menyebut anggota untuk pesan lama! (pesan yang dikirim sebelum saya ditambahkan ke grup)__")
    else:
        return await event.reply("__Membalas pesan atau memberi saya beberapa teks untuk menyebutkan orang lain!__")

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ''
    async for usr in event.client.iter_participants(chat_id):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"😎 [{usr.first_name}](tg://user?id={usr.id})\n"
        if usrnum == 10:
            if mode == "text_on_cmd":
                txt = f"{msg}\n\n{usrtxt}"
                await event.client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(1)
            usrnum = 0
            usrtxt = ''
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@ultroid_cmd(pattern="cancel$")
async def cancel_spam(event):
    is_admin = False
    try:
        partici_ = await event.client(GetParticipantRequest(
            event.chat_id,
            event.sender_id
        ))
    except UserNotParticipantError:
        is_admin = False
    else:
        if (
                isinstance(
                    partici_.participant,
                    (
                            ChannelParticipantAdmin,
                            ChannelParticipantCreator
                    )
                )
        ):
            is_admin = True
    if not is_admin:
        return await event.reply("__Hanya admin yang dapat menjalankan perintah ini!__")
    if not event.chat_id in spam_chats:
        return await event.reply("__Tidak ada proses berjalan...__") 
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("__Dihentikan...__")
