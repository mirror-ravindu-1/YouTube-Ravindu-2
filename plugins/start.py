from pyrogram import Client, Filters, Message, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("šš¼š¶š» ššæš¼šš½ š·", url="https://t.me/joinchat/bZfGkMGaGwswZjI1"),
        InlineKeyboardButton("šš¼š»šš®š°š š š² š„°š·", url="https://t.me/Ravindu_Deshanz")],
        [InlineKeyboardButton("š¢š½š²š» š¬š¼šš§ššÆš² āØš„", url="https://www.youtube.com/")]
    ])
    welcomed = f"šš¶...š¤š <b>{message.from_user.first_name}</b>\n\nš¦š²š»š± šš»š š¬š¼šš§ššÆš² šš¶š»šø šš¼ šŗš² š®š»š± š¦š²š² ššµš² š š®š“š¶š° š¤\n\nš¦š²š¹š²š°š š§šµš² š¤šš®š¹š¶šš š®š»š± šš¼šš»š¹š¼š®š± š¶š š¤\n\nš£šæš²šš <b>/help</b> š³š¼šæ š š¼šæš² š¢š½šš¶š¼š»š š„\n\nš£šæš¼š·š²š°š šÆš <b>@Ravindu_Deshanz</b>"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
