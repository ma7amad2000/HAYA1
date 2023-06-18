import requests 
import teleapp
import json
import urllib
import gtts 
import geocoder
import socket
from teleapp import types
import os
from strings.filters import command
from AnonX import app

def ex_id(id):
     result = False
     file = open("users.txt", 'r')
     for line in file:
           if line.strip()==id:
           	result = True
     file.close()
     return result
     x='ضفني في مجموعتك'
     keyboard =types.InlineKeyboardMarkup(row_width=2)
     button =types.InlineKeyboardButton(x,url='https://t.me/DrakolaVzx_app?startgroup=new')
     button2 =types.InlineKeyboardButton ('الأوامر',callback_data="click1")
     button3=types.InlineKeyboardButton ('حول ',callback_data='click2')
     keyboard.add(button,button2,button3)
     app.send_message(message.chat.id,text='ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ\n🎤╖ أهلآ بك عزيزي أنا بوت دراكولا\n⚙️╢ وظيفتي حماية المجموعات\n✅╢ لتفعيل البوت عليك اتباع مايلي \n🔘╢ أضِف البوت إلى مجموعتك\n⚡️╢ ارفعهُ » مشرف\n⬆️╜ سيتم ترقيتك مالك في البوت\nـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ' ,reply_markup =keyboard )
     
@app.message_handler(command["start"])
def start(message):
	if message.chat.type == "private":
		ch = '@VZX_TEAM'#يوزر قناتك مع @
		sudo_id = sudo#ايديك
		msg = '''🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- مــعرف القـناة : {ch} 

‼️| اشترك ثم ارسل /start'''
		idd = message.from_user.id
		url = f"https://api.telegram.org/app{token}/getchatmember?chat_id={ch}&user_id={idd}"
		req = requests.get(url)
		ID = message.from_user.id
		name = message.chat.first_name
		url = f"https://api.telegram.org/app{token}/getchatmember?chat_id={ch}&user_id={ID}"
		req = requests.get(url).text
		if ID == sudo_id or "member" in req or "creator" in req or "administartor" in req:
		      first = message.from_user.first_name
		      user = message.from_user.username
		      idu = message.from_user.id
		      f = open("users.txt", "a")
		      if (not ex_id(str(idu))):
		      	app.send_message(sudo, text=f"اهلا بك يا عزيزي المطور يوجد عضو جديد دخل للبوت\nاسم الشخص : {first}\nمعرف الشخص : {user}\nايدي الشخص : {idu}")
		      	f.write("{}\n".format(idu))
		      	f.close()		      	
		      x='ضفني في مجموعتك'
		      keyboard =types.InlineKeyboardMarkup(row_width=2)
		      button =types.InlineKeyboardButton(x,url='https://t.me/DrakolaVzx_app?startgroup=new')
		      button2 =types.InlineKeyboardButton ('الأوامر',callback_data="click1")
		      button3=types.InlineKeyboardButton ('حول ',callback_data='click2')
		      keyboard.add(button,button2,button3)
		      app.send_message(message.chat.id,text='ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ\n🎤╖ أهلآ بك عزيزي أنا بوت دراكولا\n⚙️╢ وظيفتي حماية المجموعات\n✅╢ لتفعيل البوت عليك اتباع مايلي \n🔘╢ أضِف البوت إلى مجموعتك\n⚡️╢ ارفعهُ » مشرف\n⬆️╜ سيتم ترقيتك مالك في البوت\nـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ', reply_markup =keyboard )
		      
		else:
		      app.send_message(message.chat.id, """*🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- مــعرف القـناة : {} 

‼️| اشترك ثم ارسل /start*""".format(ch),parse_mode="markdown")

@app.callback_query_handler(func=lambda call: True)
def callback_deta(call):
 if call.message:
  if call.data == ("click1"):
   app.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ\n🎤╖ أهلآ بك عزيزي أنا بوت دراكولا\n⚙️╢ وظيفتي حماية المجموعات\n✅╢ لتفعيل البوت عليك اتباع مايلي \n🔘╢ أضِف البوت إلى مجموعتك\n⚡️╢ ارفعهُ » مشرف\n⬆️╜ سيتم ترقيتك مالك في البوت\nـــــــــــــــــــــــــــــــــــــــــــــــــــــــــ")
  elif call.data ==("click2"):
   app.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text="معرف مالك البوت: @Mr_Aws\nقناه مالك البوت: @VZX_TEAM\nالدعم الفني: @Mr_Aws|@VZX_TEAM")

@app.message_handler(command["locstick"]) 
def lock_sticker(message) :
    try:
    	if app.get_chat_member(message.chat.id,message.from_user.id).status in ['creator','administrator']:
    		d = {}
    		looks = 'look'
    		d["app"] = {"status": looks}
    		s = json.dumps(d)
    		id_chat = message.chat.id
    		with open(f'{id_chat}-stick-look.json', 'w') as f1:
        			app.send_message(message.chat.id, text="تم قفل الملصقات ⛔") 
        			f1.write(s)
        			f1.close()
    	else:
        	app.send_message(message.chat.id, text="انت لا تمتلك صلاحية لتنفيذ هذا الامر")
    except:
    	app.send_message(message.chat.id, text="خطأ")
@app.message_handler(content_types=["sticker"]) 
def sticker(message):
    try:
    	id_chat = message.chat.id
    	with open(f'{id_chat}-stick-look.json', 'r') as f:
    		r = json.loads(f.read())
    	status = r["app"]["status"]
    	if status == "look":
    		app.delete_message(message.chat.id, message.message_id)
    	else:
    		pass
    except:
    		app.send_message(message.chat.id, text="خطأ")
@app.message_handler(command["locdoc"]) 
def lock_doc(message) :
    try:
    	if app.get_chat_member(message.chat.id,message.from_user.id).status in ['creator','administrator']:
    		d = {}
    		looks = 'look'
    		d["app"] = {"status": looks}
    		s = json.dumps(d)
    		id_chat = message.chat.id
    		with open(f'{id_chat}-doc-look.json', 'w') as f1:
    		  	app.send_message(message.chat.id, text="تم قفل الملفات ⛔") 
    		  	f1.write(s)
    		  	f1.close()		  	
    	else:
        	app.send_message(message.chat.id, text="انت لا تمتلك صلاحية لتنفيذ هذا الامر")
    except:
    	app.send_message(message.chat.id, text="خطأ")
@app.message_handler(content_types=["document"]) 
def doc(message):
    try:
    	id_chat = message.chat.id
    	with open(f'{id_chat}-doc-look.json', 'r') as f:
    		r = json.loads(f.read())
    	status = r["app"]["status"]
    	if status == "look":
    		app.delete_message(message.chat.id, message.message_id)
    	else:
    		pass
    except:
    	app.send_message(message.chat.id, text="خطأ")
@app.message_handler(command["locphoto"]) 
def lock_photo(message) :
    try:
    	if app.get_chat_member(message.chat.id,message.from_user.id).status in ['creator','administrator']:
    		d = {}
    		looks = 'look'
    		d["app"] = {"status": looks}
    		s = json.dumps(d)
    		id_chat = message.chat.id
    		with open(f'{id_chat}-photo-look.json', 'w') as f1:
        		app.send_message(message.chat.id, text="تم قفل الصور⛔") 
        		f1.write(s)
        		f1.close()    
    	else:
        	app.send_message(message.chat.id, text="انت لا تمتلك صلاحية لتنفيذ هذا الامر")
    except:
    	app.send_message(message.chat.id, text="خطأ")
@app.message_handler(content_types=["photo"]) 
def photo(message):
    try:
    	id_chat = message.chat.id
    	with open(f'{id_chat}-photo-look.json', 'r') as f:
    		r = json.loads(f.read())
    	status = r["app"]["status"]
    	if status == "look":
    		app.delete_message(message.chat.id, message.message_id)
    	else:
    		pass
    except:
    	app.send_message(message.chat.id, text="خطأ")
@app.message_handler(command["openphoto"]) 
def open_photo(message) :
    try:
    	if app.get_chat_member(message.chat.id,message.from_user.id).status in ['creator','administrator']:
        	d = {}
        	looks = 'open'
        	d["app"] = {"status": looks}
        	s = json.dumps(d)
        	id_chat = message.chat.id
        	with open(f'{id_chat}-photo-open.json', 'w') as f1:
        		app.send_message(message.chat.id, text="تم فتح الصور⛔") 
        		f1.write(s)
        		f1.close()
        		os.remove(f'{id_chat}-photo-look.json')
    	else:
        	app.send_message(message.chat.id, text="انت لا تمتلك صلاحية لتنفيذ هذا الامر")
    except:
    	   app.send_message(message.chat.id, text="خطأ")     

@app.message_handler(content_types=["photo"]) 
def op_photo(message):
    try:
    	id_chat = message.chat.id
    	with open(f'{id_chat}-photo-open.json', 'r') as f:
    		r = json.loads(f.read())
    	status = r["app"]["status"]
    	if status == "open":
    		pass
    	else:
    		pass
    except:
    	app.send_message(message.chat.id, text="خطأ")     
    	
@app.message_handler(command["openstick"])
def open_sticker(message) :
    try:
    	if app.get_chat_member(message.chat.id,message.from_user.id).status in ['creator','administrator']:
        	d = {}
        	looks = 'open'
        	d["app"] = {"status": looks}
        	s = json.dumps(d)
        	id_chat = message.chat.id
        	with open(f'{id_chat}-stick-open.json', 'w') as f1:
        		app.send_message(message.chat.id, text="تم فتح الملصقات⛔") 
        		f1.write(s)
        		f1.close()
        		os.remove(f'{id_chat}-stick-look.json')
    	else:
        	app.send_message(message.chat.id, text="انت لا تمتلك صلاحية لتنفيذ هذا الامر")
    except:
        app.send_message(message.chat.id, text="خطأ")     
        
@app.message_handler(content_types=["sticker"]) 
def op_sticker(message):
    try:
    	id_chat = message.chat.id
    	with open(f'{id_chat}-stick-open.json', 'r') as f:
    		r = json.loads(f.read())
    	status = r["app"]["status"]
    	if status == "open":
    		pass
    	else:
    		pass
    except:
    	app.send_message(message.chat.id, text="خطأ")     
@app.message_handler(command["opendoc"]) 
def open_doc(message) :
    try:
    	if app.get_chat_member(message.chat.id,message.from_user.id).status in ['creator','administrator']:
        	d = {}
        	looks = 'open'
        	d["app"] = {"status": looks}
        	s = json.dumps(d)
        	id_chat = message.chat.id
        	with open(f'{id_chat}-stick-open.json', 'w') as f1:
        		app.send_message(message.chat.id, text="تم فتح الملفات⛔") 
        		f1.write(s)
        		f1.close()
        		os.remove(f'{id_chat}-doc-look.json')
    	else:
        	app.send_message(message.chat.id, text="انت لا تمتلك صلاحية لتنفيذ هذا الامر")
    except:
    	app.send_message(message.chat.id, text="خطأ")     
@app.message_handler(content_types=["document"]) 
def op_photo(message):
    try:
    	id_chat = message.chat.id
    	with open(f'{id_chat}-stick-open.json', 'r') as f:
    		r = json.loads(f.read())
    	status = r["app"]["status"]
    	if status == "open":
    		pass
    	else:
    		pass
    except:
    	app.send_message(message.chat.id, text="خطأ")     
@app.message_handler(command["adming"])
def admin_user(message):
  replytrue = message.reply_to_message
  if app.get_chat_member(message.chat.id,message.from_user.id).status in ['creator','administrator'] and replytrue:
           chat = message.chat.id
           user_from = message.from_user
           ree0 = requests.get(f"https://api.telegram.org/app{token}/promoteChatMember?chat_id={chat}&user_id={message.reply_to_message.from_user.id}&can_change_info=True&can_delete_messages=True&can_invite_users=True&can_restrict_members=True&can_pin_messages=false&can_promote_members=True").json()
           app.reply_to(message,"تم رفع الشخص ادمن في القروب")
  else:
  	app.send_message(message.chat.id, text="انت لا تمتلك الصلاحيات الكافية لرفع الشخص هذا ادمن")
@app.message_handler(command["stopapp"])
def stop_app(message):
	if message.from_user.id == sudo:
	   app.send_message(message.chat.id, text="تم ايقاف البوت يا سيدي")
	   app.stop_app()
@app.message_handler(command["cmds"])
def cmds(message):
	app.send_message(message.chat.id, text="ارسل /id للحصول على الايدي الخاص بك\nارسل /info للحصول على ايدي شخص ما\nارسل /number والكلمة للحصول على عدد احرف الكلمة\nارسل /leaveapp لخروج البوت من المجموعة\nارسل /echo والكلمة لكي يرسل البوت الكلمة\nارسل /ban لحظر شخص في المجموعة\nارسل /count والرقم للعد من رقم الى رقم\nارسل /split لوضع الرابط في النص\nارسل /link للحصول على الرابط الخاص للمجموعة\nارسل /unban لفك الحظر عن شخص في المجموعة\nارسل /myrank للحصول على رتبتك في المجموعة\nارسل /rank للحصول على رتبة شخص في المجموعة\nارسل /delete لحذف رسالة شخص ما\nارسل /tevo والنص واللغة لتحويل النص الى تسجيل\nارسل /locip للحصول على معلومات ip شخص ما\nارسل /ipsite والرابط للحصول على ip الموقع\nارسل /cm للحصول على عدد اعضاء المجموعة\nارسل /adming لرفع شخص ادمن في المجموعة\nارسل /locdoc لقفل الملفات والمستندات\nارسل /locstick لقفل الملصقات\nارسل /locphoto لقفل الصور\nارسل /opendoc لفتح الملفات\nارسل /openphoto لفتح الصور\nارسل /openstick لفتح الملصقات")
@app.message_handler(command["id"])
def id(message):
	try:
		username = message.from_user.username
		id = message.from_user.id
		first_name = message.from_user.first_name
		typ = message.chat.type
		date = message.date
		idph = f"https://t.me/{message.from_user.username}"
		bio = app.get_chat(message.from_user.id).bio
		if app.get_chat_member(message.chat.id,message.from_user.id).status in ['creator']:
			app.send_photo(message.chat.id,idph, "الاسم : {}\nالايدي : {}\nاليوزر : @{}\nنوع الشات : {}\nوقت الرسالة : {}\nالرتبة : المالك\nالبايو : {}".format(first_name,id,username,typ,date,bio))
		if app.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator']:
			app.send_photo(message.chat.id,idph, "الاسم : {}\nالايدي : {}\nاليوزر : @{}\nنوع الشات : {}\nوقت الرسالة : {}\nالرتبة : مشرف\nالبايو : {}".format(first_name,id,username,typ,date,bio))
		if app.get_chat_member(message.chat.id,message.from_user.id).status not in ['administrator','creator']:
			app.send_photo(message.chat.id,idph, "الاسم : {}\nالايدي : {}\nاليوزر : @{}\nنوع الشات : {}\nوقت الرسالة : {}\nالرتبة : عضو\nالبايو : {}".format(first_name,id,username,typ,date,bio))
	except:
		app.send_message(message.chat.id, text="خطأ")
@app.message_handler(command["info"])
def info(message):
	
		username = message.reply_to_message.from_user.username
		id = message.reply_to_message.from_user.id
		first_name = message.reply_to_message.from_user.first_name
		last_name = message.reply_to_message.from_user.last_name
		typ = message.reply_to_message.chat.type
		date = message.reply_to_message.date
		idph = f"https://t.me/{message.reply_to_message.from_user.username}"
		bio = app.get_chat(message.reply_to_message.from_user.username).bio
		if app.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator']:
			app.send_photo(message.chat.id,idph, "الاسم : {}\nالايدي : {}\nاليوزر : @{}\nنوع الشات : {}\nوقت الرسالة : {}\nالرتبة : مشرف\nالبايو : {}".format(first_name,id,username,typ,date,bio))
		if app.get_chat_member(message.chat.id,message.from_user.id).status not in ['administrator','creator']:
			app.send_photo(message.chat.id,idph, "الاسم : {}\nالايدي : {}\nاليوزر : @{}\nنوع الشات : {}\nوقت الرسالة : {}\nالرتبة : عضو\nالبايو : {}".format(first_name,id,username,typ,date,bio))
		if app.get_chat_member(message.chat.id,message.from_user.id).status in ['creator']:
			app.send_photo(message.chat.id,idph, "الاسم : {}\nالايدي : {}\nاليوزر : @{}\nنوع الشات : {}\nوقت الرسالة : {}\nالرتبة : المالك\nالبايو : {}".format(first_name,id,username,typ,date,bio))
	
		app.send_message(message.chat.id, text = "خطأ")
@app.message_handler(command["number"])
def number_message(message):
	try:
		oo = message.text.split()[1]
		fr = len(oo)
		app.send_message(message.chat.id, text = "{}".format(fr))
	except:
		app.send_message(message.chat.id, text = "خطأ")

@app.message_handler(command["leaveapp"])
def leave_app(message):
	try:
		idu = message.reply_to_message.from_user.id
		if app.get_chat_member(message.chat.id,message.from_user.id).status in ['creator','administrator'] or message.from_user.id == sudo:
				app.send_message(message.chat.id,text="وداعًا ...")
				app.leave_chat(message.chat.id)
	except:
		app.send_message(message.chat.id, text = "خطأ")
@app.message_handler(command["echo"])
def echo_message(message):
	try:
		techo = message.text.replace("/echo", "")
		app.send_message(message.chat.id, text = "*{}*".format(techo), parse_mode="markdown")
	except:
		app.send_message(message.chat.id, text = "خطأ")
@app.message_handler(command["ban"])
def kick_member(message):
	try:
		replytrue = message.reply_to_message
		idu = message.from_user.id
		user = message.chat.username
		if app.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator'] and replytrue or (ex_admin(str(idu))) :
			id = message.reply_to_message.from_user.id
			app.kick_chat_member(message.chat.id,id)
			user = message.reply_to_message.from_user.username
			app.send_message(message.chat.id, text="تم حظر الشخص : {}".format(user))
	except:
		app.send_message(message.chat.id, text = "خطأ")
@app.message_handler(command["count"])
def count_number(message):
	try:
		text = message.text.split()[1]
		x = 0
		while x < int(text):
			x=x+1
			app.send_message(message.chat.id, text = "{}".format(x))
	except:
		app.send_message(message.chat.id, text = "خطأ")
	
@app.message_handler(command["split"])
def split_message(message):
	try:
		text = message.text.split()[1]
		text1 = message.text.split()[2]
		app.send_message(message.chat.id, text = "[{}]({})".format(text,text1),parse_mode="markdown",disable_web_page_preview="True")
	except:
		app.send_message(message.chat.id, text = "خطأ")

@app.message_handler(command["link"])
def link_chat(message):
	try:
		link = app.export_chat_invite_link(message.chat.id)
		app.reply_to(message,"**رابط المجموعة : {}**".format(link),parse_mode="markdown")
	except:
	    app.send_message(message.chat.id, text="خطأ")
	   
@app.message_handler(command["unban"])
def unban_user(message):
	try:	
		replytrue = message.reply_to_message
		idu = message.from_user.id
		user = message.chat.username
		if app.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator'] and replytrue or (ex_admin(str(idu))):
			app.unban_chat_member(message.chat.id,message.reply_to_message.from_user.id)
			app.reply_to(message,f"**تم الغاء الحظر عن : @{message.reply_to_message.from_user.username}**",parse_mode="markdown")
			
	except:
		app.send_message(message.chat.id, text="خطأ")
@app.message_handler(command["myrank"])
def my_rank(message):
	try:
		if app.get_chat_member(message.chat.id,message.from_user.id).status not in ['administrator','creator']:
			app.reply_to(message,"**رتبتك هي : عضو**",parse_mode="markdown")
		if app.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator']:
			app.reply_to(message,"**رتبتك هي : مشرف**",parse_mode="markdown")
		if app.get_chat_member(message.chat.id,message.from_user.id).status in ['creator']:
		  	app.reply_to(message,"**رتبتك هي : المالك**",parse_mode="markdown")
	except:
		app.send_message(message.chat.id, text="خطأ")
@app.message_handler(command["rank"])
def rank_user(message):
     try:
     	replytrue = message.reply_to_message
     	if app.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status not in ['administrator','creator'] and replytrue:
     		app.send_message(message.chat.id, text = "**رتبتك هي : عضو**",parse_mode="markdown")
     	if app.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status in ['administrator'] and replytrue:
     		app.reply_to(message,"**رتبتك هي : مشرف**",parse_mode="markdown")
     	if app.get_chat_member(message.chat.id,message.reply_to_message.from_user.id).status in ['creator'] and replytrue:
     		app.reply_to(message,"**رتبتك هي : المالك**",parse_mode="markdown")
     except:
     	app.send_message(message.chat.id, text="خطأ")
     
@app.message_handler(command["mute"])
def mute_user(message):
	try:
		replytrue = message.reply_to_message
		idu = message.from_user.id
		user = message.chat.username
		if app.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator'] and replytrue or (ex_admin(str(idu))):
			app.restrict_chat_member(message.chat.id,message.reply_to_message.from_user.id)
			app.send_message(message.chat.id,f"**تم كتم هذا الشخص : @{message.reply_to_message.from_user.username}**",parse_mode="markdown") 

	except:
		app.send_message(message.chat.id, text="خطأ")

@app.message_handler(command["locip"])
def lociton_ip(message):
	try:
			ip = message.text.split()[1].strip()
			url = "http://ip-api.com/json/{0}"
			resp = requests.get(url.format(ip)).json()
			country = resp["country"]
			countryCode = resp["CountryCode"]
			region = resp["region"]
			regionName = resp["regionName"]
			city = resp["city"]
			zip = resp["zip"]
			lat = resp["lat"]
			lon = resp["lon"]
			timezone = resp["timezone"]
			isp = resp["isp"]
			org = resp["org"]
			ass = resp["as"]
			our_ip = geocoder.ip(ip)
			location = our_ip.latlng
			app.send_message(message.chat.id, text=f"Ip : {ip}\nCountry Code : {countryCode}\nCountry : {country}\nRegion : {region}\nRegion Name : {regionName}\nCity : {city}\nZip : {zip}\nLat : {lat}\nLon : {lon}\nTimezone : {timezone}\nIsp : {isp}\nOrg : {org}\nAs : {ass}\nLocation : {location}")
	except:
		app.send_message(message.chat.id, text="خطأ")	
@app.message_handler(command["delete"])
def delete_msg(message):
	try:
		replytrue = message.reply_to_message
		idu = message.from_user.id
		user = message.chat.username
		if app.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator'] and replytrue or (ex_admin(str(idu))):
			id_msg = message.reply_to_message.id
			msg = message.reply_to_message.text
			username = message.from_user.username
			app.delete_message(message.chat.id, id_msg)
			app.send_message(message.chat.id, text="تم حذف الرسالة بواسطة : @{}".format(username))
		
	except:
		app.send_message(message.chat.id, text="خطأ")
	
@app.message_handler(command["tevo"])
def Text_Voice(message):
	try:
		text = message.text.split()[1]
		lang = message.text.split()[2]
		tts = gtts.gTTS(text, lang=lang)
		tts.save("voice.mp3")
		v = open("voice.mp3",'rb')
		app.send_audio(message.chat.id,v,text)
	except:
			app.send_message(message.chat.id, text="خطأ")
	
@app.message_handler(command["ipsite"])
def ip_site(message):
	try:
		site = message.text.split()[1]
		if "://" in site:
			app.send_message(message.chat.id, text="يرجى حذف http:// او https:// من الرابط")
		else:
			ip = socket.gethostbyname(site)
			app.send_message(message.chat.id, text=f"الايبي : {ip}")
	except:
			app.send_message(message.chat.id, text="خطأ")
			
@app.message_handler(command["cm"])
def c_member(message):
	members = app.get_chat_members_count(message.chat.id)
	app.send_message(message.chat.id, text=f"عدد الاعضاء هو :  : {members}")


def id_ls(id):
    result = False
    file = open("agr/ids.txt", 'r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

def id_ls_pr(id):
    result = False
    file = open("agr/private.txt", 'r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

def id_ls_gr(id):
    result = False
    file = open("agr/groups.txt", 'r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

def id_ls_ca(id):
    result = False
    file = open("agr/channels.txt", 'r')
    for line in file:
        if line.strip()==id:
            result = True
    file.close()
    return result

@app.message_handler(func=lambda message:True)
def d(message):
    if message.text == "الاحصائيات" and message.chat.id == sudo:
        private  = open("users.txt","r",encoding="utf-8").read().splitlines()
        groups = open("agr/groups.txt","r",encoding="utf-8").read().splitlines()
        channels = open("agr/channels.txt","r",encoding="utf-8").read().splitlines()
        of_all = private + groups + channels
        al = f"""
- الاحصائيات :

- المجموعات :{len(groups)} .
- القنوات :{len(channels)} .
- الخاص :{len(private)} .
- الكل :{len(of_all)} .

"""
        app.reply_to(message,al)
    name = message.from_user.first_name
    msg = message.text
    #####
    ####
    if msg ==  "تفعيل" and message.chat.type == "supergroup" or message.chat.type == "group":
        try:
            idu = message.chat.id
            us = str(message.chat.first_name)
            f3 = open("agr/groups.txt", 'a')
            group_name = message.chat.first_name
            group_id = message.chat.id
            group_user = message.chat.username
            if (not id_ls_gr(str(idu))):
                app.send_message(sudo, text=f"اهلا بك يا عزيزي هناك مجموعة جديدة تم تفعيلها\nالاسم : {group_name}\nالايدي : {group_id}\nالمعرف : {group_user}")
                f3.write("{}\n".format(idu))
                f3.close()
                app.reply_to(message,f"- اهلا عزيزي {name} تم تفعيل بوت  بنجاح .")
            else:
                app.reply_to(message,f"- البوت مفعل من قبل ! .")
        except Exception as err:
            app.reply_to(message,f"- حصل خطأ !\nرمز الخطأ :\n{err}")

@app.channel_post_handler(func=lambda m: True)
def f(message):
    msg = message.text
    if msg == "تفعيل":
        try:
            idu = message.chat.id
            us = str(message.chat.first_name)
            f = open("agr/channels.txt", 'a')
            if (not id_ls_ca(str(idu))):
                channel_name = message.chat.first_name
                channel_id = message.chat.id
                channel_user = message.chat.username
            if (not id_ls_gr(str(idu))):
                app.send_message(sudo, text=f"اهلا بك يا عزيزي هناك قناة جديدة تم تفعيلها\nالاسم : {channel_name}\nالايدي : {channel_id}\nالمعرف : {channel_user}")
                f.write(f"{idu}\n")
                f.close()
                app.reply_to(message, f"- اهلا عزيزي  تم تفعيل بوت  بنجاح .")
            else:
                app.reply_to(message, f"- البوت مفعل من قبل ! .")
        except Exception as err:
            app.reply_to(message, f"- حصل خطأ !\nرمز الخطأ :\n{err}")

@app.message_handler(func=lambda m: True)
def stop_messages(message):
	try:
		replytrue = message.reply_to_message
		if app.get_chat_member(message.chat.id,message.from_user.id).status in ['administrator','creator']:
			id_msg = message.id
			msg = message.text
			list = ["كس","شرموط","شرموطه","تمرج","تبياته","كسمك","كسبوك","كسختك", "كسي" ,"زبي","زب" ,"قحبه","اقحب","سكس","sex","نيك", "طيز", "طيزك", "عيري", "عير", "اير", "ايري"]
			if msg in list:
				app.delete_message(message.chat.id, id_msg)
				app.send_message(message.chat.id, text="Done Delete Message\nPlease Don't Send Message Sex")
			list_p = ["مطور","مطوري","قناة","قناتي","مبرمج","مبرمجي","دراكولا بوت","بوت","دراكولا","تفعيل","Activate","/activate","نوفا","شبح الاردن","كوست","جوست"]
	except:
		app.send_message(message.chat.id, text="Error")

app.polling(True)
