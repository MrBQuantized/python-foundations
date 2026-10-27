# Basics

# Content

- [What is logging](#what-is-logging)
- [Security Levels](#security-levels)
- [Precedence](#precedence)
- [Custom Logger](#custom-logger)
- [log() method](#log-method)
- [FileHandler](#filehandler--redirecting-logs-to-a-file)
- [Formatting Logger](#formatting-logger)

## What is Logging?
Logging is the process of recording events or processes that take place when running your code. These could be errors, warnings, information, or critical security vulnerabilities. You want to know what is going on in your code so that you can prevent running into issues. Logging helps you track processes in your application.

## Security Levels
There are 5 security levels involved in logging. These are as shown below:
- **DEBUG**: Helps developers to debug, troubleshoot, test, or play around. It doesn't have anything that interests the end-user.
- **INFO**: These are informational messages that do not necessarily require any attention. Some examples are:

    - '_You have 5 new emails_',
    - '_File deleted_'.

- **WARNING**: This is a '_heads-up_' about an imminent issue (e.g. errors, crash), but nothing bad has happened yet.
- **ERROR**: A crash, runtime error, or exception.
- **CRITICAL**: This is when a crucial/essential component of a system has an issue. Example: server being down.

## Precedence
- The root logger's default level is **WARNING**, so INFO and DEBUG messages don't get printed unless you configure the level. It's not that INFO has a special rule — it's simply below the default threshold.
- The CRITICAL level has the highest severity and takes the highest precedence.

In order to make the INFO level be displayed, we make some configurations:

```python
logging.basicConfig(level=logging.INFO) # Enables the INFO level to be printed out

logging.info("You have got 20 mails in your inbox!")
logging.warning("Battery is Low!")
logging.error("404. Page not found")
logging.critical("All components failed!")
```

## Custom Logger
You can initialize a custom logger using the `getLogger()` method:

```python
logger = logging.getLogger("OnohLabs Logger")
logger.info("Logger created!")
logger.warning("Your OpenAI token would soon expire")
logger.critical("Your Payoneer account has been permanently disabled")
```

## log() method
This method is an alternative that enables us to specify the security level and the message.

```python
logger.log(logging.ERROR, "An Error occurred!")
```

## FileHandler — Redirecting Logs to a File
As an administrator, you wouldn't want to view a screen of logs all the time. Instead, you want to view these logs in a file. This is done by using the `FileHandler()` method.

We configure the logger to be at the DEBUG level since we want to log debug messages.

```python
import logging
from pathlib import Path

DIR = Path(__file__).resolve().parents[0]
log_file = DIR / "mylog.log"

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("OnohLabs Logger")

handler = logging.FileHandler(log_file)
logger.setLevel(logging.INFO)

logger.addHandler(handler)

logger.debug("This is a debug message.")  # Not added to the log file (logger level is INFO)
logger.info("This is an important information!")  # Displays in the terminal and the file
```

**Note on the two `setLevel` calls:** In the code above, `logger.setLevel(logging.INFO)` sets the logger to INFO, so `logger.debug(...)` will NOT be written to the file. This is because Python logging uses a two-stage filtering mechanism: **first** the logger checks whether the message level is >= the logger's level; if it passes, **then** each handler checks its own level. Since the logger is at INFO, the DEBUG message is discarded at the logger level and never reaches the FileHandler.

If you want DEBUG messages in the file, you have two options:

```python
# Option 1: keep the logger at DEBUG
logger.setLevel(logging.DEBUG)      # logger passes everything through
handler.setLevel(logging.DEBUG)     # handler writes everything to the file

# Option 2: leave the handler at its default level (NOTSET, which processes everything)
logger.setLevel(logging.DEBUG)      # only this line is needed
```

Setting only the handler to DEBUG while the logger stays at INFO will **not** work, because the message is already blocked at the logger level.

## Formatting Logger
Logs can be formatted. For instance, we can format the logger to display the logging level, timestamp, and message.

```python
formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("Logger created!")
logger.info("This is an important information!")
```

So, the output is:

```log
This is an important information!
INFO - 2026-10-27 12:25:09,191: Logger created!
INFO - 2026-10-27 12:25:09,191: This is an important information!
```

**Note:** The first line `This is an important information!` appears unformatted because it was logged by the previous handler *before* the formatter was attached. Only the two lines after the formatter was set show the level, timestamp, and message.

