import os

API_ID = API_ID = 23455230

API_HASH = os.environ.get("API_HASH", "1740e4541ec18b9cdd3e5ff6f3687d46")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6458458851:AAHtCGYLSKGKnqensjvvkqT8K-ET2YlH9Q4")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6332321765))

LOG = -1002118355958

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6332321765").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


