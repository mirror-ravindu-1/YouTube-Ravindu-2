from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"හායි...🥰❤️...මට ඕනිම YouTube වීඩියෝ එකක් Download කරන්න පුළුවන් 🥰❤️...YouTube ලිංක් එකක් එවලා පහස අත්විඳින්න 🥲❤️"
    await message.reply_text(helptxt)
