""" Some simple authentication examples """

import os
from dotenv import load_dotenv

from wrike.api import Wrike

load_dotenv()

PERM_ACCESS_TOKEN = os.getenv("PERM_ACCESS_TOKEN")

wrike = Wrike(api_key=PERM_ACCESS_TOKEN)

me = wrike.get_me()

print(me.me, me.first_name, me.last_name)
