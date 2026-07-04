#==============================
# logging levels
#==============================

# | Level      | Purpose                         |
# | ---------- | ------------------------------- |
# | `DEBUG`    | Detailed debugging information  |
# | `INFO`     | General program information     |
# | `WARNING`  | Something unexpected happened   |
# | `ERROR`    | An error occurred               |
# | `CRITICAL` | Serious error, program may stop |


import logging

logging.debug("Debug Message")
logging.info("Information")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical Error")
print("==========================================")

# by default python does not show loggin.debug and logging.info

# to show everything

logging.basicConfig(level=logging.DEBUG)

logging.debug("Debug")
logging.info("Info")
logging.warning("Warning")
logging.error("Error")
logging.critical("Critical")
print("==========================================")

# to store log in a file

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("Program Started")
logging.warning("Low Disk Space")
logging.error("Database Error")
print("==========================================")