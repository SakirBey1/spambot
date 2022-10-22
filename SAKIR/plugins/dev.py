from .. import worker
from telethon import events, Button

@worker.on(events.NewMessage(incoming=True, pattern="/dev"))
async def repo(event):
    await event.reply("ɪɴғᴏ ᴀʙᴏᴜᴛ ᴅᴇᴠᴇʟᴏᴘᴇʀ",
                    buttons=[
                        [Button.url("SakirBey 🇮🇳", url="https://xnkit.github.io/k")]
                    ])
