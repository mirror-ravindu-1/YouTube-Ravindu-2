from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"<b>මට ඕනිම YouTube Video එකක් Download කරගෙන ඔයාට එවන්න පුළුවන් 🔥</b>\n\n<b>කරන්න තියෙන්නේ YouTube Link එකක් එවීම හෝ @vid කියා Type කර පසුව ඔබට අදාළ වීඩියෝවේ නම Type කර තේරීම පමණි 🍂</b>\n\n<b>Project By @Ravindu_Deshanz</b>"
    await message.reply_text(helptxt)
