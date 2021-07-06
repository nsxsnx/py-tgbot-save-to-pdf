# Telegram options:
TELEGRAM_TOKEN = 'TOKEN_HERE'

# Misc:
WORK_DIR = '/u01/PDFBotFiles/'
LOG_FILE = '/u01/PDFSaveBot/pdfbotlog.txt'
GREETINGS = 'Send me a file and I\'ll convert it into .pdf for you.'
SUPPORTED_MIMES = (
        'text/plain',
        #'image/bmp'
        #'image/jpeg'
        #'image/png',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'application/vnd.ms-excel',
        'application/msword',
        'application/vnd.oasis.opendocument.spreadsheet',
        'application/vnd.oasis.opendocument.text',
        )

LIBRE_CMD = ['/usr/bin/libreoffice', '--headless', '--convert-to', 'pdf', '--outdir', WORK_DIR]
