# Copyleft (c) 2020 Mr.Miss, All wrongs reserved.
#
# Redistribution and use in source with or
# without modufication, are permitted.


import time
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from pyrogram import Client

select = " "

docs = """Generate your Telegram String Session

P -->> Pyrogram [https://docs.pyrogram.org]
T -->> Telethon [https://docs.telethon.dev]
"""

tutor = """
~ go-to my.telegram.org
~ Login using your Telegram account
~ Click on API Development Tools
~ Create a new application, by entering the required details
~ Check your Telegram saved messages section to copy the STRING_SESSION
"""

template = """
UserBot support: @userbotindo
            
<code>STRING_SESSION</code>: <code>{}</code>

⚠️ <b>Please be carefull to pass this value to third parties</b>"""


print(docs)

while select != ("p", "t"):
    select = input("Enter your required client < p / t > : ").lower()
    if select == "t":
        print("""\nTelethon selected\nRunning script...""")
        time.sleep(1)
        print(tutor)
        API_KEY = int(input("Enter API_KEY here: "))
        API_HASH = input("Enter API_HASH here: ")

        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:
            session_string = client.session.save()
            saved_messages_template = "Telethon session" + template.format(session_string)
            print("\nGenerating String Session...\n")
            client.send_message("me", saved_messages_template, parse_mode="html")
            time.sleep(1)
            print("Your STRING_SESSION value have been sent to your Telegram Saved Messages")
        break

    elif select == "p":
        print("""\nPyrogram selected.\nRunning script...""")
        time.sleep(1)
        print(tutor)
        with Client(
        "UserBot", 
        api_id=int(input("Enter API ID: ")),
        api_hash=input("Enter API HASH: ")) as pyrogram:
            saved_messages_template = "Pyrogram session" + template.format(pyrogram.export_session_string())
            print("\nGenerating String session...\n")           
            pyrogram.send_message("me", saved_messages_template, parse_mode="html")
            time.sleep(1) 
            print("Your STRING_SESSION value have been sent to your Telegram Saved Messages")
        break
    
    else:
        print("\nPlease only select P or T\n")
        time.sleep(1.5)
