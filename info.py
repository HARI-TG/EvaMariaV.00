import re, os
from os import environ, getenv
from Script import script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '10261086'))
API_HASH = environ.get('API_HASH', '9195dc0591fbdb22b5711bcd1f437dab')
BOT_TOKEN = environ.get('BOT_TOKEN', "6802235059:AAGyFlSQRUvl_gOFFbAaaQvaLFsGFzKSK_E")

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled((environ.get('USE_CAPTION_FILTER', 'True')), True)

PICS = (environ.get('PICS', 'https://graph.org/file/64aa65f5019f44220a058.jpg https://graph.org/file/79b31ed618ab163aa681c.jpg https://graph.org/file/11149e001a1abffab1934.jpg https://graph.org/file/b4ac27df8e8e443fa219d.jpg https://graph.org/file/d77eb9050db8e7700fff7.jpg https://graph.org/file/40b89081a5ee2e1a84251.jpg https://graph.org/file/ae85884397284e2aae446.jpg https://graph.org/file/0097bc77bbc24592bebd6.jpg https://graph.org/file/32a28148dc4552f934ce7.jpg https://graph.org/file/2cc0e4b229e8805abd6ae.jpg https://graph.org/file/845ffca9eae27536e7825.jpg https://graph.org/file/e224691a8c3a5146c5cc7.jpg https://graph.org/file/1d19d59c74a6d2fd69a33.jpg https://graph.org/file/e015100b5c27cf9224037.jpg https://graph.org/file/d09a6c86ca0e8ac360785.jpg https://graph.org/file/860e261d8c4ce72ae9386.jpg https://graph.org/file/49b2af84e44b08f945c06.jpg https://graph.org/file/7bb41739746bf0a4bee34.jpg')).split()
MELCOWE_IMG = environ.get("MELCOWE_IMG", "https://telegra.ph//file/5db753d2897e5fc9ce954.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/438e4abd5a2cf97fcfd8f.jpg")
SETTINGS_PICS = (environ.get('SETTINGS_PICS', 'https://graph.org/file/73e4acd0a9f4425fd34be.jpg')).split()
RULES_PICS = (environ.get('RULES_PICS', 'https://graph.org/file/4752441b16362f2df8e27.jpg https://graph.org/file/e5445f406f428b47556fc.jpg')).split()
SUPPORT_PICS = (environ.get('SUPPORT_PICS', 'https://graph.org/file/30fc6ea74df988db9b417.jpg')).split()

# Admins, Channels & Users

# Admins, Channels & Users
OWNER_ID = int(getenv("OWNER_ID", 1426588906))
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1426588906').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001878854070').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID')
reqst_channel = environ.get('REQST_CHANNEL_ID')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = is_enabled((environ.get("NO_RESULTS_MSG", 'False')), False)
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in environ.get('PREMIUM_USER', '').split()]

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://tedtingxbot:tedtingxbot@cluster0.urwgprn.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "tedtingxbot")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# FSUB
auth_channel = environ.get('AUTH_CHANNEL', '-1001881205059')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else REQ_CHANNEL
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = environ.get("REQ_CHANNEL", '')
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else AUTH_CHANNEL
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

# Others
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'onepagelink.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '59d8f4b692be27f966418748423e52cf7b440dff')
IS_SHORTLINK = is_enabled((environ.get('IS_SHORTLINK', 'True')), False)
TUTORIAL = environ.get('TUTORIAL', 'https://t.me/Team_HMT/8')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+GOFte-Rz2tcxODg1')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/+mCMdCb_ymAowZmNl')
MSG_ALRT = environ.get('MSG_ALRT', 'Wʜᴀᴛ Aʀᴇ Yᴏᴜ Lᴏᴏᴋɪɴɢ Aᴛ ?')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', "-1001606248152"))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'DQ_The_File_Donor_Support')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), False)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
