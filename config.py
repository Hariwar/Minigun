#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = os.environ.get("API_ID", "17822592")
API_HASH = os.environ.get("API_HASH", "a20b3dbbe07ed695563b4609a3e62012")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
ADMIN = int(os.environ.get("ADMIN", '578811855'))
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "mtpmasala")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "mtpmasala")
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://idol:hari813143@idol.cukivnu.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Cluster0")
CAPTION = os.environ.get("CAPTION", "")
group = environ.get('GROUP', '-1002147535144')
GROUP = int(group) if group and id_pattern.search(group) else None
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
SUNRISES_PIC= "https://graph.org/file/bd91761f6e938e2e6d23a.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '578811855'))
WEBHOOK = bool(os.environ.get("WEBHOOK", True))
PORT = int(os.environ.get("PORT", "8080"))
LOG_CHANNEL_ID = os.environ.get("LOG_CHANNEL_ID", "-1002236618870")
