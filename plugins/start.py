from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("𝗝𝗼𝗶𝗻 𝗚𝗿𝗼𝘂𝗽 🌷", url="https://t.me/joinchat/bZfGkMGaGwswZjI1"),
        InlineKeyboardButton("𝗖𝗼𝗻𝘁𝗮𝗰𝘁 𝗠𝗲 🥰🌷", url="https://t.me/Ravindu_Deshanz")]
    ])
    welcomed = f"𝗛𝗶...🖤🍂<b>{message.from_user.first_name}</b>\n\n𝗦𝗲𝗻𝗱 𝗔𝗻𝘆 𝗬𝗼𝘂𝗧𝘂𝗯𝗲 𝗟𝗶𝗻𝗸 𝘁𝗼 𝗺𝗲 𝗮𝗻𝗱 𝗦𝗲𝗲 𝘁𝗵𝗲 𝗠𝗮𝗴𝗶𝗰 🖤\n\n𝗦𝗲𝗹𝗲𝗰𝘁 𝗧𝗵𝗲 𝗤𝘂𝗮𝗹𝗶𝘁𝘆 𝗮𝗻𝗱 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗶𝘁 🖤\n\n𝗣𝗿𝗼𝗷𝗲𝗰𝘁 𝗯𝘆 <b>@Ravindu_Deshanz</b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
