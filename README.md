# USB-Detector
This application when ran will detect if a USB is injected into your computer and will send a notification to your linked device preferably a mobile device. The notification system is done via Telegram bots which will be explained further.

## What do i need to start this program?
You will need to install to install the pywin32 and requests libraries. You will also need to download Telegram on your mobile device and set up a Telegram bot which will be explained below.

To install pywin32 and requests libraries open up python in command prompt and enter these commands:
```
pip install requests
```
```
pip install pywin32
```
Once that is done, now you have to set up your Telegram bot:
- Download Telegram on your mobile device and create an account if you haven't
- Open Telegram and search for @BotFather and start a chat with BotFather
- Use the command '/newbot' to create a new bot
- Follow the prompts to choose a name and username for your bot. The username must be unique and must end with the word "bot" (e.g., MyNotificationBot)
- After that BotFather will provide you with your bot token which you should keep safely

You will also need your chat ID which can be done by starting a chat with @userinfobot. Enter the command '/start' to get your chat ID.

## How do i start this program?
To start the program copy and paste the code to your prefered programming software and replace the text in the TELEGRAM_BOT_TOKEN and CHAT_ID variables with your actual bot token and chat ID.
