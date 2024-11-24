from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from VIPMUSIC import app
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ˹ 𝘼𝙧𝙖𝙙𝙝𝙮𝙖 ✘ 𝐌ᴜꜱɪᴄ ˼
 
 ⚡ • ʙsᴅᴋ ʀᴇᴘᴏ ʟᴇɢᴀ 😏 •
 
 ⚡ • ᴘᴇʜʟᴇ ᴢᴇᴜꜱ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ •
 
 ⚡ • ᴄʜᴜᴘ ᴄʜᴜᴘ ʙᴏᴛ ʟᴇᴋᴇ ɴɪᴋᴀʟ •
 
 ⚡ • ᴀɢʀ ᴄʜᴀʜɪʏᴇ ᴛᴏ ᴢᴇᴜꜱ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟɴᴀ ᴘᴀᴅᴇɢᴀ •
 
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("𝗔𝗗𝗗 𝗠𝗘", url=f"https://t.me/ZEUS_MUSIC_BOT?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝗦𝗨𝗣𝗣𝗢𝗥𝗧", url="https://t.me/ll_BOTCHAMBER_ll"),
          InlineKeyboardButton("𝗢𝗪𝗡𝗘𝗥", url="https://t.me/UNBORNEDVILLIAN"),
          ],
               [
                InlineKeyboardButton("𝗨𝗣𝗗𝗔𝗧𝗘𝗦", url="https://t.me/ll_BOTCHAMBER_ll"),

],
[
              InlineKeyboardButton("𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/ZEUS_MUSIC_ROBOT"),
              InlineKeyboardButton("︎𝗠𝗨𝗦𝗜𝗖", url=f"https://t.me/RADHE_music_RObot"),
              ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await msg.reply_photo(
        photo="https://graph.org/file/b289b9d0ce8b2b0222986-c7f68366c35d6f7f7e.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
