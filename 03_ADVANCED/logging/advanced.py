import logging
from pathlib import Path

DIR = Path(__file__).resolve().parents[0]
log_file = DIR / "mylog.log"


logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("OnohLabs Logger")

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler(log_file)
logger.setLevel(
    logging.INFO
)  # This only allows the info logs to be sent to the log file.

# Formatting
formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug("This is a debug message.")
logger.info("Logger created!")
logger.info("This is an important information!")
# logger.warning(" Your OpenAI token would soon expire")
# logger.critical(" Your payoneer account has been permanently disabled")
