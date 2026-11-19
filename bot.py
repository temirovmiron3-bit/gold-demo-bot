
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder, CommandHandler, ContextTypes
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom! AKE Gold Demo Bot ishga tushdi.\n\n"
        "/analysis — tahlil haqida\n"
        "/help — yordam"
    )

async def analysis(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hozir bozor ma'lumotlari ulanmagan.\n"
        "Bu bot hali BUY yoki SELL signali bermaydi."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Bot demo va o'quv maqsadida ishlaydi."
    )

token = os.getenv("BOT_TOKEN")
if not token:
    raise RuntimeError("BOT_TOKEN sozlanmagan")

app = ApplicationBuilder().token(token).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("analysis", analysis))
app.add_handler(CommandHandler("help", help_command))
app.run_polling()

