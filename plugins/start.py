from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        InlineKeyboardButton('⚡️𝗛𝗲𝗹𝗽⚡️', callback_data='help_btn'),
        InlineKeyboardButton('𝗝𝗼𝗶𝗻 𝗚𝗿𝗼𝘂𝗽 🌷', url='https://t.me/joinchat/bZfGkMGaGwswZjI1')
    ],
        [InlineKeyboardButton(
            "දෝෂයක් රිපෝට් කරන්න 🥺", url="https://t.me/Ravindu_Deshanz")]
    ])
    welcomed = f"හායි <b>{message.from_user.first_name}</b>\n/help කියලා ගහන්න මාව පාවිච්චි කරන හැටි දැනගන්න ❤️😍.මට වඩා ගොඩාක් වැඩකෑලි මගෙ සහෝදරයා ගාව තියේ..එයාට මැසේජ් එකක් දාන්න 🥰❤️. @YtRavinduBot"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
