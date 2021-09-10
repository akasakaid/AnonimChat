from requests import get,post
import json
import re

token = json.loads(open("config.json").read())["token"]
ownerid = json.loads(open("config.json").read())["owner_id"]
api = f"https://api.telegram.org/bot{token}"
n = 0

inChat = []
enterChat = []

def kirim_pesan(userid,text,msgid=None):
	if msgid:
		req = post(f"{api}/sendmessage",json={"chat_id":userid,"parse_mode":"html","text":text,"reply_to_message_id":msgid})
	else:
		req = post(f"{api}/sendmessage",json={"chat_id":userid,"parse_mode":"html","text":text})

def kirim_stiker(userid,file_id,msgid=None,caption=None):
	if msgid and caption:
		req = post(f"{api}/sendAnimation",json={"chat_id":userid,"parse_mode":"html","animation":file_id,"reply_to_message_id":msgid,"caption":caption})
	elif msgid:
		req = post(f"{api}/sendAnimation",json={"chat_id":userid,"parse_mode":"html","animation":file_id,"reply_to_message_id":msgid})
	elif caption:
		req = post(f"{api}/sendAnimation",json={"chat_id":userid,"parse_mode":"html","animation":file_id,"caption":caption})
	else:
		req = post(f"{api}/sendAnimation",json={"chat_id":userid,"parse_mode":"html","animation":file_id})

def kirim_foto(userid,file_id,msgid=None,caption=None):
	if msgid and caption:
		req = post(f"{api}/sendphoto",json={"chat_id":userid,"parse_mode":"html","photo":file_id,"reply_to_message_id":msgid,"caption":caption})
	elif msgid:
		req = post(f"{api}/sendphoto",json={"chat_id":userid,"parse_mode":"html","photo":file_id,"reply_to_message_id":msgid})
	elif caption:
		req = post(f"{api}/sendphoto",json={"chat_id":userid,"parse_mode":"html","photo":file_id,"caption":caption})
	else:
		req = post(f"{api}/sendphoto",json={"chat_id":userid,"parse_mode":"html","photo":file_id})

def kirim_video(userid,file_id,msgid=None,caption=None):
	if msgid and caption:
		req = post(f"{api}/sendvideo",json={"chat_id":userid,"parse_mode":"html","video":file_id,"reply_to_message_id":msgid,"caption":caption})
	elif msgid:
		req = post(f"{api}/sendvideo",json={"chat_id":userid,"parse_mode":"html","video":file_id,"reply_to_message_id":msgid})
	elif caption:
		req = post(f"{api}/sendvideo",json={"chat_id":userid,"parse_mode":"html","video":file_id,"caption":caption})
	else:
		req = post(f"{api}/sendvideo",json={"chat_id":userid,"parse_mode":"html","video":file_id})
	print(req.json())

def kirim_voice(userid,file_id,msgid=None,caption=None):
	if msgid and caption:
		req = post(f"{api}/sendvoice",json={"chat_id":userid,"parse_mode":"html","voice":file_id,"reply_to_message_id":msgid,"caption":caption})
	elif msgid:
		req = post(f"{api}/sendvoice",json={"chat_id":userid,"parse_mode":"html","voice":file_id,"reply_to_message_id":msgid})
	elif caption:
		req = post(f"{api}/sendvoice",json={"chat_id":userid,"parse_mode":"html","voice":file_id,"caption":caption})
	else:
		req = post(f"{api}/sendvoice",json={"chat_id":userid,"parse_mode":"html","voice":file_id})

def kirim_audio(userid,file_id,msgid=None,caption=None):
	if msgid and caption:
		req = post(f"{api}/sendaudio",json={"chat_id":userid,"parse_mode":"html","audio":file_id,"reply_to_message_id":msgid,"caption":caption})
	elif msgid:
		req = post(f"{api}/sendaudio",json={"chat_id":userid,"parse_mode":"html","audio":file_id,"reply_to_message_id":msgid})
	elif caption:
		req = post(f"{api}/sendaudio",json={"chat_id":userid,"parse_mode":"html","audio":file_id,"caption":caption})
	else:
		req = post(f"{api}/sendaudio",json={"chat_id":userid,"parse_mode":"html","audio":file_id})

def kirim_document(userid,file_id,msgid=None,caption=None):
	if msgid and caption:
		req = post(f"{api}/senddocument",json={"chat_id":userid,"parse_mode":"html","document":file_id,"reply_to_message_id":msgid,"caption":caption})
	elif msgid:
		req = post(f"{api}/senddocument",json={"chat_id":userid,"parse_mode":"html","document":file_id,"reply_to_message_id":msgid})
	elif caption:
		req = post(f"{api}/senddocument",json={"chat_id":userid,"parse_mode":"html","document":file_id,"caption":caption})
	else:
		req = post(f"{api}/senddocument",json={"chat_id":userid,"parse_mode":"html","document":file_id})

def get_friends_id(userid):
	for id in inChat:
		if userid in id:
			if id.index(userid) == 0:
				return id[1]
			else:
				return id[0]

def get_index_id(userid):
	for id in inChat:
		if userid in id:
			return id
	return []

def dalam_chat(userid):
	for id in inChat:
		if userid in id:
			return True
		else:
			return False

def main(update):
	userid = update["message"]["from"]["id"]
	first_name = update["message"]["from"]["first_name"]
	last_name = update["message"]["from"]["last_name"]
	tipe = update["message"]["chat"]["type"]
	message_id = update["message"]["message_id"]
	try:
		pesan = update["message"]["text"]
	except KeyError:
		pesan = ""
	if "username" in update["message"]["from"]:
		username = update["message"]["from"]["username"]
	else:
		username = ""
	print(f"{userid} {first_name} - {pesan}")
	if pesan.startswith("/start"):
		kirim_pesan(userid,"<i>Welcome to anonim chat bot\n\nsend /search to find a friend</i>",message_id)
	elif pesan.startswith("/search") and userid in get_index_id(userid):
		kirim_pesan(userid,"<i>you in chat now !</i>")
		return
	elif pesan.startswith("/search") and userid not in enterChat:
		enterChat.append(userid)
		kirim_pesan(userid=userid,text="<i>looking a friend </i>")
	elif pesan == "/search" and userid in enterChat:
		kirim_pesan(userid,"<i>you are in the queue, wait until you get a friend !</i>")
	elif userid not in get_index_id(userid):
		kirim_pesan(userid,"<i>you not in chat, type /search to search friend</i>")
	if len(enterChat) == 2:
		data = [enterChat[0],enterChat[1]]
		inChat.append(data)
		[kirim_pesan(tid,"<i>friend found ❤️\ntype /stop to stop the conversation</i>") for tid in enterChat]
		enterChat.clear()
		return
	if "sticker" in str(update) and dalam_chat(userid):
		file_id = update["message"]["sticker"]["file_id"]
		fid = get_friends_id(userid)
		if "reply_to_message" in str(update) and "caption" in str(update["message"]["sticker"]):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			caption = update["message"]["caption"]
			kirim_stiker(fid,file_id,reply_msgid,caption=caption)
		elif "reply_to_message" in str(update):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			kirim_stiker(userid=fid,file_id=file_id,msgid=reply_msgid)
		elif "caption" in str(update["message"]["sticker"]):
			caption = update["message"]["caption"]
			kirim_stiker(userid=fid,file_id=file_id,caption=caption)
		else:
			kirim_stiker(userid=fid,file_id=file_id)
	elif "voice" in str(update) and dalam_chat(userid):
		file_id = update["message"]["voice"]["file_id"]
		fid = get_friends_id(userid)
		if "reply_to_message" in str(update) and "caption" in str(update["message"]):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			caption = update["message"]["caption"]
			kirim_voice(fid,file_id,reply_msgid,caption=caption)
		elif "reply_to_message" in str(update):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			kirim_voice(userid=fid,file_id=file_id,msgid=reply_msgid)
		elif "caption" in str(update["message"]):
			caption = update["message"]["caption"]
			kirim_voice(userid=fid,file_id=file_id,caption=caption)
		else:
			kirim_voice(userid=fid,file_id=file_id)
	elif "document" in str(update) and dalam_chat(userid):
		file_id = update["message"]["document"]["file_id"]
		fid = get_friends_id(userid)
		if "reply_to_message" in str(update) and "caption" in str(update["message"]):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			caption = update["message"]["caption"]
			kirim_document(fid,file_id,reply_msgid,caption)
		elif "reply_to_message" in str(update):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			kirim_document(fid,file_id,reply_msgid)
		elif "caption" in str(update["message"]):
			caption = update["message"]["caption"]
			kirim_document(fid,file_id,caption=caption)
		else:
			kirim_document(fid,file_id)
	elif "photo" in str(update) and dalam_chat(userid):
		file_id = update["message"]["photo"][0]["file_id"]
		fid = get_friends_id(userid)
		if "reply_to_message" in str(update) and "caption" in str(update["message"]):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			caption = update["message"]["caption"]
			kirim_foto(fid,file_id,reply_msgid,caption=caption)
		elif "reply_to_message" in str(update):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			kirim_foto(userid=fid,file_id=file_id,msgid=reply_msgid)
		elif "caption" in str(update["message"]):
			caption = update["message"]["caption"]
			kirim_foto(userid=fid,file_id=file_id,caption=caption)
		else:
			kirim_foto(userid=fid,file_id=file_id)
	elif "video" in str(update) and dalam_chat(userid):
		file_id = update["message"]["video"]["file_id"]
		fid = get_friends_id(userid)
		if "reply_to_message" in str(update) and "video" in str(update["message"]):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			caption = update["message"]["caption"]
			kirim_video(userid=fid,file_id=file_id,msgid=reply_msgid,caption=caption)
		elif "reply_to_message" in str(update):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			kirim_video(userid=fid,file_id=file_id,msgid=reply_msgid)
		elif "caption" in str(update["message"]):
			caption = update["message"]["caption"]
			kirim_video(userid=fid,file_id=file_id,caption=caption)
		else:
			kirim_video(userid=fid,file_id=userid)
	elif "audio" in str(update) and dalam_chat(userid):
		file_id = update["message"]["audio"]["file_id"]
		fid = get_friends_id(userid)
		if "reply_to_message" in str(update) and "video" in str(update["message"]):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			caption = update["message"]["caption"]
			kirim_video(userid=fid,file_id=file_id,msgid=reply_msgid,caption=caption)
		elif "reply_to_message" in str(update):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			kirim_video(userid=fid,file_id=file_id,msgid=reply_msgid)
		elif "caption" in str(update["message"]):
			caption = update["message"]["caption"]
			kirim_video(userid=fid,file_id=file_id,caption=caption)
		else:
			kirim_video(userid=fid,file_id=userid)
	elif pesan == "/stop" and dalam_chat(userid):
		cid = get_index_id(userid)
		fid = get_friends_id(userid)
		kirim_pesan(fid,"<i>you friend has stop chat !</i>")
		kirim_pesan(userid,"<i>you has stoped chat</i>")
		inChat.remove(cid)
	else:
		fid = get_friends_id(userid)
		if "reply_to_message" in str(update):
			reply_msgid = update["message"]["reply_to_message"]["message_id"] - 1
			kirim_pesan(userid=fid,text=pesan,msgid=reply_msgid)
		else:
			kirim_pesan(userid=fid,text=pesan)