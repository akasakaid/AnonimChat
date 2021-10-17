import os
import json
from module import main
from requests import get
from requests.exceptions import *

token = json.loads(open("config.json").read())["token"]
n = 0
#os.system("cls" if os.name == "nt" else "clear")
while True:
	try:
		req = get(f"https://api.telegram.org/bot{token}/getupdates",params={"offset":n}).json()
		if len(req["result"]) == 0:
			continue
		n = req['result'][0]['update_id'] + 1	
		main(req['result'][0])
	except ConnectionError:
		print("no internet !")
	except KeyboardInterrupt:
		exit()