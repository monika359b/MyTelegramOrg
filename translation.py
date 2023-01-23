class Translation(object):
    START_TEXT = """
Hi I'm A Simple My.telegram.org Bot. Help You To Get API ID & API HASH Enter Your Telegram Phone Number With Country Code. Click /start to start the bot"""
    AFTER_RECVD_CODE_TEXT = """
Now please send the Telegram code you received from Telegram!

this code is only used for the purpose of getting the APP ID from my.telegram.org
\nIf you don't trust the developer of this bot, please visit telegram trusted web my.telegram.org

Click /start to restart the bot """
    BEFORE_SUCC_LOGIN = "Please wait \n We are Scrapping for you"
    ERRED_PAGE = "Failed To Get Api Id\nPlease get it manually from my.telegram.org login by phone number there > Enter otp received in telegram app> choose Api Development tool > copy app id and ApI hash>done"
    CANCELLED_MESG = "bye! Please /start again to restart the Bot "
    IN_VALID_CODE_PVDED = "The OTP code you entered is WRONG!! Please Enter the OTP Code correctly!!! "
    IN_VALID_PHNO_PVDED = "The cellphone number you entered is WRONG, please enter your Telegram telephone number in the country code format.\nExample: +1628xxxxxxx"
