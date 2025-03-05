from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "7261746068:AAHVWKWt_OiN7M8YpJx7H0ZE_ODeVgTkh1Q"
# WEBHOOK_URL = "https://sanjudev1.pythonanywhere.com"  

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Hello Welcome to Film Making Department\n"
        "\n"
        "/help  -> Please reach out to my Team for further information\n"
        "\n"     
        "/content -> There are some sample making wondering shoots, have a look at my direction styles\n"
        "\n"
        "/contact -> Feel free to reach out to my team at 9542862232\n"
        "\n"
        "/Chittivideo -> Chitti cover song\n"
        "\n"
        "/Kingfishervideo -> Kingfisher short film\n"
        "\n"
        "/Amruthavideo -> Amrutha cover song\n"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "/start -> Welcome to the Film shoots Channel\n"
        "/help  -> Please reach out to my Team for further information\n"
        "/content -> There are some sample making wondering shoots, have a look at my direction styles\n"
        "/contact -> Feel free to reach out to my team at 9542862232\n"
        "/Chittivideo -> Chitti cover song\n"
        "/Kingfishervideo -> Kingfisher short film\n"
        "/Amruthavideo -> Amrutha cover song\n"
    )

async def content(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Check out our playlists: https://www.youtube.com/@localtouringtalkiesltt4999")

async def Chittivideo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Watch the Chitti cover song: https://www.youtube.com/watch?v=ro77dYAYmGM&list=PLbmtXAms75JBOITg3ZUhmu4_Uw23PYtqg")

async def Kingfishervideo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Watch the Kingfisher short film: https://www.youtube.com/watch?v=6N10zpHvS9I")

async def Amruthavideo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Watch the Amrutha cover song: https://www.youtube.com/watch?v=lIo46bYftZE")

def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("content", content))
    application.add_handler(CommandHandler("Chittivideo", Chittivideo))
    application.add_handler(CommandHandler("Kingfishervideo", Kingfishervideo))
    application.add_handler(CommandHandler("Amruthavideo", Amruthavideo))

    print("Bot is running...")
    application.run_polling()  # Polling works now

if __name__ == "__main__":
    main()
