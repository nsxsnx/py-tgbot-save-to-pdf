#!/usr/bin/python3
from SETTINGS import *
import telebot, requests, os, subprocess
from time import strftime

def write_log(message):
    with open(LOG_FILE,"a+") as log:
        log.write(strftime('%Y%m%d_%H%M%S') + ' ' + message + '\n')

def die(message):
    print(message)
    write_log(message)
    exit(1)

def check_document_type(message):
    if not message.document is None:
        return message.document.mime_type in SUPPORTED_MIMES

# Entry point
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, GREETINGS)

@bot.message_handler(func=check_document_type, content_types=['document'])
def convert_file(message):
    file_info = bot.get_file(message.document.file_id)
    response = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TELEGRAM_TOKEN, file_info.file_path))
    if not response: 
        write_log('HTTP error has occurred.')
        return
    ifile = os.path.join(WORK_DIR, message.document.file_name)
    with open(ifile, 'wb') as f: f.write(response.content)
    sub = subprocess.Popen(LIBRE_CMD + [ifile], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = sub.communicate()
    if stdout is not None: write_log(stdout.decode("utf-8"))
    if stderr is not None: write_log(stderr.decode("utf-8"))
    pre, ext = os.path.splitext(ifile)
    ofile = pre + '.pdf'
    with open(ofile, 'rb') as f: bot.send_document(message.chat.id, f, message.message_id)

bot.polling()

