# -*-codding: utf-8-*-
from config.settings import BOT_TOKEN, LISTEN_IP, SERVER_PORT, \
    SERVER_KEY, SERVER_CERT, WEBHOOK_URL, WEBHOOK_ENABLE
from src.dispatch import updater


def run():
    if WEBHOOK_ENABLE:
        updater.start_webhook(
            listen=LISTEN_IP,
            port=SERVER_PORT,
            url_path=BOT_TOKEN,
            key=SERVER_KEY,
            cert=SERVER_CERT,
            webhook_url=WEBHOOK_URL
        )
    else:
        updater.start_polling()
    updater.idle()
