# Admin cam usage tracker
ADMIN_LOG_FILENAME              = "admincam.log"

# Server details
SERVER_DETAILS                  = [
    # HOST          , QPORT, BASE DIRECTORY              , TK CHANNEL WEBHOOK
    ("209.222.98.15", 27165, r"C:\servers\squad_server_1", "PUT WEBHOOK URL HERE"), # public 1 (NYC)
    ("209.222.98.15", 27205, r"C:\servers\squad_server_3", "PUT WEBHOOK URL HERE"), # public 2 (NYC)
    ("104.194.8.111", 27195, r"C:\servers\squad_server_3", "PUT WEBHOOK URL HERE"), # public 3 (LA)
    ("185.38.151.16", 27165, r"C:\servers\squad_server_1", "PUT WEBHOOK URL HERE"), # public 4 (EU)
]


#####################################
# DO NOT EDIT BELOW
#####################################

import pytz
from dataclasses import dataclass

TIMEZONE = pytz.timezone("US/Eastern")
TIMEZONE_NAME = "EST"

@dataclass
class Server():
    host : str
    qport : int
    basedir : str
    webhook_url: int

servers = []
for details in SERVER_DETAILS:
    servers.append(Server(*details))

