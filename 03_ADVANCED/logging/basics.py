import logging

logging.basicConfig(level=logging.DEBUG)

# logging.info("You have got 20 mails in your inbox!")
# logging.warning("Battery is Low!")
# logging.critical("All components failed!")

logger = logging.getLogger("OnohLabs Logger")
# logger.info(" Logger created!")
# logger.warning(" Your OpenAI token would soon expire")
# logger.critical(" Your payoneer account has been permanently disabled")

# logger.info("You have got 20 mails in your inbox!")
# logger.warning("Battery is Low!")
# logger.error("404. Page not found")
# logger.critical("All components failed!")

# logger.log(logging.ERROR, "An Error occured!")
