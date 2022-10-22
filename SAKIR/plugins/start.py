from .. import worker
from telethon import events, Button

@worker.on(events.NewMessage(incoming=True, pattern="/start"))
async def start(event):
    await event.reply("ѕοмє ιиƒο αϐουτ οωиєя.",
                    buttons=[
                        [Button.url("οωиєя", url="https://xnkit.github.io/k")],
                        [Button.inline("Cнєϲκ мє",data="op")]
                    ])

@worker.on(events.callbackquery.CallbackQuery(data="op"))
async def ex(event):
    await event.edit("υѕє τнιѕ ρℓєαѕє /help",
                    buttons=[
                        [Button.url("οωиєя", url="https://xnkit.github.io/k")]
                    ])
