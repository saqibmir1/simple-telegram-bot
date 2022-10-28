import Constants as keys
from telegram.ext import *
import Responses as R

print("Bot started...")

def start_command(update, context):
	update.message.reply_text("""
		Hello! I am a simple convo bot
		You can use /help for viewing commands""")

def help_command(update, context):
	update.message.reply_text("""
		Here is a list of commands and texts you can send:
		/start for getting started
		/help for listing all commands and texts you can use

		Things you can try:
		insult me / diss me
		insult my mama / diss my mama / jo mama jokes
		hi
		time
		am i gay
		who are you
		tell me about your penis
	 """)

def handle_message(update, context):
	text=str(update.message.text).lower()
	response=R.sample_responses(text)

	update.message.reply_text(response)

def error(update, context):
	print(f"update {update} caused error {context.error}")

def main():
	updater=Updater(keys.API_KEY, use_context=True)
	dp=updater.dispatcher

	dp.add_handler(CommandHandler("start", start_command))
	dp.add_handler(CommandHandler("help", help_command))

	dp.add_handler(MessageHandler(Filters.text, handle_message))

	dp.add_error_handler(error)

	updater.start_polling()
	updater.idle()

main()