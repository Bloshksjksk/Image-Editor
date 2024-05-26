# By @TroJanzHEX
from pyrogram import Client
from datetime import datetime
import os

if bool(os.environ.get("WEBHOOK", False)):
    from config import Config
else:
    from config import Config  # pylint:disable=import-error


if __name__ == "__main__":
    plugins = dict(root="plugins")

    app = Client(
        "TroJanz",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300,
    )
with app:
    app_username = app.get_me().username  # Better call it global once due to telegram flood id
    Current_date = datetime. now(). date() 
    print("Bot started!",Current_date)
    app.send_message(int(945284066),"Bot started!")
    app.send_message(int(945284066), Current_date)
app.run()
