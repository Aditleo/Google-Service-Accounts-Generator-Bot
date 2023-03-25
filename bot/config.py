import os
class config:
    BOT_TOKEN = os.environ.get('6282209685:AAHJIE9PLLfOVWPqSyc5ua35gLl6lWR6Ey4')
    APP_ID = os.environ.get('16621564')
    API_HASH = os.environ.get('8b0bf7e5014d7a6862de76cf59e424b4')
    DATABASE_URL = os.environ.get('postgresql://postgres:nUqt9ocNWwUDftKhDLEC@containers-us-west-103.railway.app:6690/railway')    
    SUDO_USERS = os.environ.get('1814487265')
    SUPPORT_CHAT_LINK = "t.me/moedyiu"
    DOWNLOAD_DIRECTORY = "./downloads/"
    


class BotCommands:
  Authorize = ['auth', 'start']
  Revoke = ['revoke']
  EmptyTrash = ['emptyTrash']
  Proj = ['projects']
  Cproj = ['newproject']
  Delsas = ['delsas']
  Sas = ['sas']
class Messages:
    
    DOWNLOAD_TG_FILE  = "🔒 **DOWNLOADING CREDENIAL FILE.**"

    DOWNLOADED_SUCCESSFULLY = "🔒 **SUCCESSFULLY DOWNLOADED CREDENIAL FILE.**\n__Send /auth to authenticate.__"

    NOT_AUTH = f"🔑 **No credentials found. Please enable the Drive API in:\nhttps://developers.google.com/drive/api/v3/quickstart/python\nand upload the json file as credentials.json**\n__Send /{BotCommands.Authorize[0]} to authenticate.__"
    
    ALREADY_AUTH = "🔒 **Already authorized your Google Drive Account.**\n__Use /revoke to revoke the current account.__\n__Send me a direct link or File to Upload on Google Drive__"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Authorized Google Drive account Successfully.**'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n__The code you have sent is invalid or already used before. Generate new one by the Authorization URL__'
    
    AUTH_TEXT = "⛓️ **To Authorize your Google Drive account visit this [URL]({}) and send the generated code here.**\n__Visit the URL > Allow permissions > you will get a code > copy it > Send it here__"
    
    REVOKED = f"🔓 **Revoked current logged account successfully.**\n__Use /{BotCommands.Authorize[0]} to authenticate again and use this bot.__"
    
