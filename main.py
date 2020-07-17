import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyrogram import Client

select = " "

docs = """Generate your Telegram String Session
T -->> Telethon [https://docs.telethon.dev]
p -->> Pyrogram [https://docs.pyrogram.org]
"""

tutor = """
~ go-to my.telegram.org
~ Login using your Telegram account
~ Click on API Development Tools
~ Create a new application, by entering the required details
~ Check your Telegram saved messages section to copy the STRING_SESSION
"""


print(docs)

while select != ("p", "t"):
    time.sleep(0.5)
    select = input("Enter your required client < p / t > : ")
    if select == "t":
        print("""\nTelethon selected\nRunning script...""")
        time.sleep(1)
        print(tutor)
        API_KEY = int(input("Enter API_KEY here: "))
        API_HASH = input("Enter API_HASH here: ")

        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            session_string = client.session.save()
            saved_messages_template = """Support: @userbotindo
            
        <code>STRING_SESSION</code>: <code>{}</code>

        ⚠️ <i>Please be carefull to pass this value to third parties</i>""".format(session_string)
            client.send_message("me", saved_messages_template, parse_mode="html")
            print("Your STRING_SESSION value have been sent to your Telegram Saved Messages")
        break

    if select == "p":
        print("""\nPyrogram selected.\nRunning script...""")
        time.sleep(1)
        print(tutor)
        with Client(
        "UserBot", 
        api_id=int(input("Enter API ID: ")),
        api_hash=input("Enter API HASH: ")) as pyrogram:
            print("Generating String session")
            saved_messages_template = """Support: @userbotindo

        <code>STRING_SESSION</code>: <code>{}</code>

        ⚠️ <i>Please be carefull to pass this value to third parties</i>""".format(pyrogram.export_session_string())
            pyrogram.send_message("me", saved_messages_template, parse_mode="html")
            print("Your STRING_SESSION value have been sent to your Telegram Saved Messages")
        break