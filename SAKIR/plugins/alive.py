from telethon import events
import os
from .. import worker
from SAKIR import BOT_USERS, BOT_USER, ALIVE_NAME
import asyncio
currentversion = "ONLY ONE"

ALIVE_NAME = str(ALIVE_NAME) if ALIVE_NAME else "ᴀɴᴋɪᴛ 🇮🇳 [ᴏꜰꜰʟɪɴᴇ]™"
import os
xnkit786 = os.environ.get("PM_IMG", None)
if not xnkit786:
 xnkit786 = "https://telegra.ph/file/f062050393e82f5c3cbd7.jpg"
pm_caption = "• Sakir Sᴘᴀᴍᴍᴇʀ ɪs: Oɴʟɪɴᴇ\n\n"
pm_caption += "• Pʏᴛʜᴏɴ: 3.9.7 \n"
pm_caption += "• Dᴀᴛᴀʙᴀsᴇ Sᴛᴀᴛᴜs:  Fᴜɴᴄᴛɪᴏɴᴀʟ\n"     
pm_caption += "• Cᴜʀʀᴇɴᴛ Bʀᴀɴᴄʜ : `ANKIT`\n"
pm_caption += f"• Wᴏʀᴋᴇʀ Oғ : {ALIVE_NAME} \n"
pm_caption += "• Hᴇʀᴏᴋᴜ Dᴀᴛᴀʙᴀsᴇ : ᴀᴡs-ᴡᴏʀᴋɪɴɢ ᴘʀᴏᴘᴇʀʟʏ\n\n"
pm_caption += "• Cᴏᴘʏʀɪɢʜᴛ ϐγ : ©Sakir ᴋᴜᴍᴀʀ™\n\n"
pm_caption += "• Mᴀᴅᴇ ʙʏ : [Sakir 🇮🇳™](https://xnkit.github.io/k)"


@worker.on(events.NewMessage(incoming=True, pattern="^/alive"))
async def alive(event):
  if not str(event.sender_id) in BOT_USERS:
    return await event.reply("ᴋɪᴅ ʏᴏᴜ ʜᴀᴠᴇ ɴᴏ ᴄᴏɴᴛʀᴏʟ ᴏɴ ᴍᴇ (sᴇᴅ)")
  await worker.send_file(event.chat_id, xnkit786, caption=pm_caption)
