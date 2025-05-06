import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot.google_ads_client import fetch_ad_data
from bot.report_builder import generate_report

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('👋 Hello! I can fetch Google Ads reports. Use /report to get started.')

# /report command handler
async def report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        data = fetch_ad_data()
        report = generate_report(data)
        await update.message.reply_text(f'📊 Report:\n\n{report}')
    except Exception as e:
        logger.error(e)
        await update.message.reply_text('❌ Failed to generate report.')

def main() -> None:
    from dotenv import load_dotenv
    import os
    load_dotenv()

    token = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("report", report))

    app.run_polling()

if __name__ == '__main__':
    main()
