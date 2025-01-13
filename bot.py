from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging

# 設置日誌
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 機器人啟動指令
def start(update: Update, context: CallbackContext):
    update.message.reply_text("歡迎使用播報機器人！請在群組中使用我吧！")

# 關鍵詞觸發功能
def handle_message(update: Update, context: CallbackContext):
    text = update.message.text.lower()
    if "關鍵字" in text:
        update.message.reply_text("這是觸發關鍵字的回應！")
    elif "規則" in text:
        update.message.reply_text("群規：保持友善，禁止廣告！")

# 主程式
def main():
    TOKEN = "你的機器人Token"  # 替換為你的機器人Token
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    # 添加處理指令
    dp.add_handler(CommandHandler("start", start))
    # 添加文字消息的處理
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # 啟動機器人
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
