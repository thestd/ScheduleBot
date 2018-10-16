# ========== BOT SETTINGS ==========
BOT_TOKEN = "<bot_token>"

DEFAULT_ENCODING_FOR_REQUEST = "windows-1251"

DATE_FORMAT = "%d.%m.%Y"

# -------LOGGING-------
LOGGING_ENABLE = True
LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# -------DATABASE-------
DB_NAME = '<database_name>'
DB_USER = '<database_user>'
DB_USER_PASSWORD = '<database_password>'

# -------WEBHOOK SETTINGS-------
WEBHOOK_ENABLE = False
SERVER_IP = '<server_ip>'
LISTEN_IP = '0.0.0.0'
SERVER_PORT = '<port>'
SERVER_KEY = 'private.key'
SERVER_CERT = 'cert.pem'
WEBHOOK_URL = f'https://{SERVER_IP}:{SERVER_PORT}/{BOT_TOKEN}'


# ========== SITE PARSER SETTINGS ==========
SCHEDULE_HOST = "<SCHEDULE_HOST>"
SCHEDULE_URL = f"{SCHEDULE_HOST}/cgi-bin/timetable.cgi"
GET_SCHEDULE_URL = "?n=700"
GROUP_EXISTS = "?n=701&lev=142&faculty=0&query="
TEACHER_EXISTS = "?n=701&lev=141&faculty=0&query="

# ========== SITE PARSER SETTINGS ==========
ADMIN_PANEL_ENABLE = False
ID_ADMINS = []
