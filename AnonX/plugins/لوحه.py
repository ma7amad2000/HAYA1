from pyrogram import * 
from pyrogram.types import * 
import time
import requests
import asyncio
from config import OWNER_ID,  BOT_TOKEN
from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from AnonX import app

bot_id = (BOT_TOKEN) 

owner = (OWNER_ID)

try:
	open(f"Users{bot_id}.json","r")
except FileNotFoundError:
	open(f"Users{bot_id}.json","w")
try:
	open(f"sudo{bot_id}.json","r")
except FileNotFoundError:
	open(f"sudo{bot_id}.json","w")
try:
	open(f"maindevs{bot_id}.json","r")
except FileNotFoundError:
	open(f"maindevs{bot_id}.json","w")
try:
	open(f"maindevsVII{bot_id}.json","r")
except FileNotFoundError:
	open(f"maindevsVII{bot_id}.json","w")
try:
	open(f"groups{bot_id}.json","r")
except FileNotFoundError:
	open(f"groups{bot_id}.json","w")
try:
	open(f"band{bot_id}.json","r")
except FileNotFoundError:
	open(f"band{bot_id}.json","w")
try:
	open(f"links{bot_id}.json","r")
except FileNotFoundError:
	open(f"links{bot_id}.json","w")
try:
	open(f"channel{bot_id}.json","r")
except FileNotFoundError:
	open(f"channel{bot_id}.json","w")
try:
	open(f"devchannel{bot_id}.json","r")
except FileNotFoundError:
	open(f"devchannel{bot_id}.json","w")
try:
	open(f"devuser{bot_id}.json","r")
except FileNotFoundError:
	open(f"devuser{bot_id}.json","w")
try:
	open(f'owner{bot_id}.json','r')
except FileNotFoundError:
	f = open(f'owner{bot_id}.json','w')
	f.write(str(owner))
	




OwnerM = ReplyKeyboardMarkup([
[("رفع مالك"),("تنزيل مالك"),("المالكين"),("حذف المالكين")],
[("الغاء")], 
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات"),("نسخه الكل")],
[("عرض المجموعات"),("عدد المجموعات"),("نسخه المجموعات"),("روابط المجموعات")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("نسخه الاعضاء"),("نسخه المحظورين"),("نسخه المطورين")],

[("-")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("تنزيل مطور اساسي"),("تنزيل مطور"),("الغاء حظر عضو")],
[("عرض المطورين الاساسيين"),("عرض المطورين"),("عرض المحظورين")],
[("حذف الاساسيين"),("حذف المطورين"),("حذف المحظورين")],
[("الغاء")],

[("◍ قسم الاشتراك ◍"),("◍ قسم معرف المطور ◍"),("◍ قسم المطور ◍")],
[("عرض قناة الاشتراك"),("عرض معرف المطور"),("عرض قناة المطور")],
[("اضف قناة اشتراك اجباري"),("اضافه معرف المطور"),("اضافه قناه المطور")],
[("حذف قناه الاشتراك"),("حذف معرف المطور"),("حذف قناه المطور")],
[("الغاء")], 
[("•---- حذف الكيبورد -----•")]
])

mainSudoVIIM = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات")],
[("عرض المجموعات"),("عدد المجموعات"),("نسخه المجموعات"),("نسخه للكل")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("نسخه الاعضاء"),("نسخه المحظورين"),("نسخه المطورين")],

[("-")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("تنزيل مطور اساسي"),("تنزيل مطور"),("الغاء حظر عضو")],
[("عرض المطورين الاساسيين"),("عرض المطورين"),("عرض المحظورين")],
[("حذف الاساسيين"),("حذف المطورين"),("حذف المحظورين")],
[("الغاء")],

[("◍ قسم الاشتراك ◍"),("◍"),("◍ قسم المطور ◍")],
[("عرض قناة الاشتراك"),("-"),("عرض قناة المطور")],
[("اضف قناة اشتراك اجباري"),("-"),("اضافه قناه المطور")],
[("حذف قناه الاشتراك"),("-"),("حذف قناه المطور")],
[("الغاء")], 
[("•---- حذف الكيبورد -----•")]
])


main_dev_key = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات")],
[("عرض المجموعات"),("عدد المجموعات"),("نسخه المجموعات"),("نسخه للكل")],
[("عرض الاساسيين"),("عرض الاعضاء"),("عرض المحظورين"),("عرض المطورين")], 
[("عدد الاساسيين"),("عدد الاعضاء"),("عدد المحظورين"),("عدد المطورين")], 
[("نسخه الاساسيين"),("نسخه الاعضاء"),("نسخه المحظورين"),("نسخه المطورين")],

[("-")], 

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 


[("◍ قسم الاساسيين"),("◍ قسم المطورين"),("◍ قسم الحظر ◍")],
[("رفع مطور اساسي"),("رفع مطور"),("حظر عضو")],
[("تنزيل مطور اساسي"),("تنزيل مطور"),("الغاء حظر عضو")],
[("عرض المطورين الاساسيين"),("عرض المطورين"),("عرض المحظورين")],
[("الغاء")],

[("•---- حذف الكيبورد -----•")]
])

sudo_keyboard = ReplyKeyboardMarkup([
[("•---- حذف الكيبورد -----•")],
[("◍ قسم الاحصائيات ◍")],
[("الاحصائيات"),("نسخه")],
[("عرض المجموعات"),("نسخه للجروبات"),("عدد الجروبات")],
[("عرض روابط المجموعات"),("نسخه للمحظورين")],
[("عرض الاعضاء"),("عرض المطورين")], 
[("عدد الاعضاء"),("عدد المطورين")], 
[("نسخه الاعضاء"),("نسخه المطورين")],

[("◍ قسم الاذاعه ◍")],
[("توجيه للكل"),("-"),("اذاعه للكل")],
[("-"),("-"),("-")],
[("اذاعه الاعضاء"),("اذاعه المجموعات"),("اذاعه المحظورين")],
[("توجيه الاعضاء"),("توجيه المجموعات"),("توجيه محظورين")],
[("الغاء")], 

[("◍ قسم الحظر ◍")],
[("حظر عضو "),("الغاء حظر عضو"),("عرض المحظورين")],
[("•---- حذف الكيبورد -----•")]
])




def is_user(id):
	result = False
	file = open(f"Users{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result

def is_dev(id):
	result = False
	file = open(f"sudo{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result
	
def del_all_sudo():
	open(f"sudo{bot_id}.json","w")

def del_all_main():
	open(f"maindevs{bot_id}.json","w")

def del_all_mainVII():
	open(f"maindevsVII{bot_id}.json","w") 
	
def del_all_ban():
	open(f"band{bot_id}.json","w")

def is_main_dev(id):
	result = False
	file = open(f"maindevs{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result
	
def is_main_devVII(id):
	result = False
	file = open(f"maindevsVII{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result
	
def is_band(id):
	result = False
	file = open(f"band{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return  result
	
def is_group(id):
	result = False
	file = open(f"groups{bot_id}.json","r")
	for line in file:
		if line.strip()==id:
			result = True
	file.close()
	return result

def add_user(id):
	file = open(f"Users{bot_id}.json","a")
	file.write("{}\n".format(id))

def show_channel() -> str:
	with open(f"channel{bot_id}.json","r") as file:
		return file.readline()

def add_channel(chat_id):
	with open(f"channel{bot_id}.json","w") as file:
		file.write(chat_id)

def del_channel():
	open(f"channel{bot_id}.json","w")

def get_bot_owner() -> int:
	with open("owner{bot_id}.json","r") as file:
		return file.readline()
		
def set_bot_owner(user_id:int):
	with open(f"owner{bot_id}.json","w") as file:
		file.write(str(user_id))

def show_devchannel() -> str:
	with open(f"devchannel{bot_id}.json","r") as file:
		return file.readline()

def add_devchannel(chat_id):
	with open(f"devchannel{bot_id}.json","w") as file:
		file.write(chat_id)

def del_devchannel():
	open(f"devchannel{bot_id}.json","w")


def show_devuser() -> str:
	with open(f"devuser{bot_id}.json","r") as file:
		return file.readline()

def add_devuser(chat_id):
	with open(f"devuser{bot_id}.json","w") as file:
		file.write(chat_id)

def del_devuser():
	open(f"devuser{bot_id}.json","w")



sudo_message = f"**💌╖اهلا بيك حبيبي آلمـطـور\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس @{show_devchannel()}**"


start_buttons = InlineKeyboardMarkup([[
InlineKeyboardButton("ch",url=f"https://t.me/{show_devchannel()}")
]])


New_Member = """**
دخل عضو جديد للبوت 🪄🪄

᥀︙حسابة : {} 
᥀︙ايديه : `{}`

Time : {} .

**"""
	
dev_ch_bu = InlineKeyboardMarkup([[
InlineKeyboardButton("Dev",user_id=owner),
InlineKeyboardButton("Ch",url=f"https://t.me/{show_devchannel()}")
]])



@app.on_message(command("start"))
async def app_start(c:Client,m:Message):
	do = requests.get(f"https://api.telegram.org/bot{bot_id}/getChatMember?chat_id=@{show_channel()}&user_id={m.from_user.id}").text
	user = m.from_user.id
	mm = m.from_user.mention
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	Sudo = open(f"sudo{bot_id}.json","r").read()
	banD = open(f"band{bot_id}.json","r").read()
	
	
	
	
	if str(user) in banD:
		return await m.reply(f"**◍ عذرا {mm} انت محظور من استخدام البوت \n√**",reply_markup=dev_ch_bu)
		
	if user == owner:
		return await m.reply(f"💌╖اهلا بيك حبيبي آلمـطـور الاساسي\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس @{show_devchannel()}",reply_markup=OwnerM)
	
	if str(user) in mainSudoVII:
		return await m.reply(f"💌╖اهلا بيك حبيبي آلمـطـور الاساسي\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس @{show_devchannel()}",reply_markup=mainSudoVIIM)
	
	if str(user) in mainSudo:
		return await m.reply(f"💌╖اهلا بيك حبيبي آلمـطـور الاساسي\n⚙️╢ تقدر تتحكم باوامر البوت عن طريق\n🔍╢ الكيبور اللي ظهرتلك تحت ↘️\n🔰╜ للدخول لقناة السورس @{show_devchannel()}",reply_markup=main_dev_key)
	
	if str(user) in Sudo:
		return await m.reply(sudo_message,reply_markup=sudo_keyboard)
	
	if is_user(id=user) and not is_band(user):
		return await m.reply(start_text,reply_markup=start_buttons)
		
	if (not is_user(id=str(user))):
		add_user(id=user)
		cc = time.strftime("%H : %M : %S")
		try:
			await app.send_message(owner,New_Member.format(mm,user,cc),
			reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("دخول لحسابه",
			user_id=int(user))]]))
	
	
@app.on_message(command(["الاحصائيات"]))
async def __count(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if  str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		users = len(open(f"Users{bot_id}.json","r").readlines())
		groups = len(open(f"groups{bot_id}.json","r").readlines())
		sudos = len(open(f"sudo{bot_id}.json","r").readlines())
		main = len(open(f"maindevs{bot_id}.json","r").readlines())
		bans = len(open(f"band{bot_id}.json","r").readlines())
		
		msg = f"""
		**◍ Bot Status : **
			
		├ users : {users} 
		├ sudos : {sudos} 
		├ groups : {groups} 
		├ main sudos : {main} 
		├ band  {bans} 
		
		√ """
		return await m.reply(msg,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("close",callback_data="close")]]))
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
	
@app.on_callback_query(command("close"))
async def close__(_,query:CallbackQuery):
	user = query.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		await query.message.delete()
		
	else:
		await query.answer("❎ فقط المطورين من لديهم الحق في القيام بهذا .")

@app.on_message(command(["•---- حذف الكيبورد -----•"]))
async def del_keyboard(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		return await m.reply("**◍ تم حذف الكيبورد بنجاح  /start\n√**",reply_markup=ReplyKeyboardRemove())
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(command(["^نسخه الكل$"]))
async def __get_copy(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		users = open(f"Users{bot_id}.json","rb")
		groups = open(f"groups{bot_id}.json","rb")
		band = open(f"band{bot_id}.json","rb")
		sudos = open(f"sudo{bot_id}.json","rb")
		main = open(f"maindevs{bot_id}.json","rb")
		
		uc = len(open(f"Users{bot_id}.json","r").readlines())
		gc = len(open(f"groups{bot_id}.json","r").readlines())
		bc = len(open(f"band{bot_id}.json","r").readlines())
		sc = len(open(f"sudo{bot_id}.json","r").readlines())
		mc = len(open(f"maindevs{bot_id}.json","r").readlines())
		
		cc = await m.reply("**◍ جاري جلب النسخه الاحتياطية \n√**")
		time.sleep(3)
		await cc.delete()
		try:
			await m.reply_document(document=users,caption=f"**Bot users : {uc} √**")
		except:
			await m.reply("**◍ لم يقم اي عضو بالدخول الي بوتك √**")
		try:
			await m.reply_document(document=groups,caption=f"**Bot groups : {gc} √**")
		except:
			await m.reply("**◍ لم يتم تفعيل اي مجموعات في بوتك √**")
		try:
			await m.reply_document(document=band,caption=f"**Band users : {bc} √**")
		except:
			await m.reply("**◍ لا يوجد اعضاء محظورين في البوت √**")
		try:
			await m.reply_document(document=sudos,caption=f"**Sudo users : {sc} √**")
		except:
			await m.reply("**◍ لا يوجد مطورين في البوت √**")
		try:
			await m.reply_document(document=main,caption=f"**Main devs : {mc} √**")
		except:
			await m.reply("**◍ لا يوجد مطورين اساسيين في البوت √**")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
	


@app.on_message(command(["^عرض المجموعات$"]))
async def show_groups(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		groups = open(f"groups{bot_id}.json")
		x = 1
		text = "**Bot groups **:\n\n"
		for gr in groups:
			text += f"{x} - {gr} \n"
			x+=1
		i =await m.reply("**◍ جاري عرض الجروبات √**")
		time.sleep(.5)
		leng = len(open(f"groups{bot_id}.json","r").readlines())
		if leng == 0:
			return await i.edit("**◍ لا توجد مجموعات تم تفعيلها في البوت √**")
		return await i.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

#--------------------------Group---------------------------

@app.on_message(command(["^نسخه المجموعات$"]))
async def __gcopy(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		gr = open(f"groups{bot_id}.json","rb")
		gc = len(open(f"groups{bot_id}.json","r").readlines())
		i = await m.reply("**◍ جاري جلب نسخه للمجموعات √**")
		time.sleep(1.5)
		try:
			await i.delete()
			await m.reply_document(document=gr,caption=f"**Bot groups {gc}**")
		except:
			await i.delete()
			await m.reply("**◍ لا توجد مجموعات تم تفعيلها في البوت √**")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
		
@app.on_message(command(["^عدد المجموعات$"]))
async def get_groups_count(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		leng = len(open(f"groups{bot_id}.json","r").readlines())
		if leng == 0:
			return await m.reply("**◍ لا توجد مجموعات تم تفعيلها في البوت √**")
		return await m.reply(f"**◍ تم تفعيل {leng} مجموعة في بوتك \n√**")
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(command(["^روابط المجموعات$"]))
async def show_links(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		x = 1
		text = "**Groups links **:\n\n"
		lenl = len(open(f"links{bot_id}.json","r").readlines())
		sl = open(f"links{bot_id}.json","r")
		for link in sl:
			text += f"{x} - {link}"
			x += 1
		l = await m.reply("**◍ جاري عرض الروابط √**")
		time.sleep(.5)
		if lenl == 0:
			return await l.edit("**◍ لا توجد مجموعات تم تفعيلها في البوت √**")
		return await l.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

#-----------------------BanUser---------------------------	
@app.on_message(command(["^نسخه المحظورين$"]))
async def get_copy___band(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		file = open(f"band{bot_id}.json","rb")
		lenb = len(open(f"band{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري جلب نسخه للمحظورين √**")
		time.sleep(2)
		if lenb == 0:
			return await l.edit("**◍ لم يتم حظر اي عضو من استخدام البوت √**")
		await l.delete()
		await m.reply_document(document=file,caption=f"**Band users {lenb} √")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")


@app.on_message(command("^عدد المحظورين$"))
async def countofuserBan(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		l = await m.reply("**◍ جاري حساب عدد الاعضاء √**")
		lens = len(open(f"band{bot_id}.json","r").readlines())
		time.sleep(.5)
		if lens == 0:
			return await l.edit("**◍ لم يدخل اي عضو للبوت حتي الآن √**")
		return await l.edit(f"**◍ عدد اعضاء بوتك {lens} √**")
	return await m.reply("**◍ انت لست مطور في البوت \n√**")


#----------------SpecialVIIUser-------------------------

@app.on_message(command(["عرض المطورين الاساسيين", "عرض الاساسيين"]) )
async def ShowMain(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in mainSudoVII or int(user) == owner:
		file = open(f"maindevs{bot_id}.json","r")
		lens = len(open(f"maindevs{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري عرض المطورين الاساسيين √**")
		x = 1
		text = "**Bot Main Users **:\n\n"
		for su in file:
			text += f"{x} - {su}"
			x += 1
		time.sleep(1)
		if lens == 0:
			return await l.edit("**◍ لم يتم رفع مطورين اساسيين في البوت √**")
		return await l.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
	

@app.on_message(command(["^نسخه الاساسيين$"]))
async def get_MainSudo(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in mainSudoVII or int(user) == owner:
		file = open(f"maindevs{bot_id}.json","rb")
		lenb = len(open(f"maindevs{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري جلب نسخه للمطورين الاساسيين√**")
		time.sleep(2)
		if lenb == 0:
			return await l.edit("**◍ لم تقم برفع اي مطور اساسي في البوت√**")
		await l.delete()
		await m.reply_document(document=file,caption=f"**Sudo Main Users {lenb} √")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")
	
@app.on_message(command(["^عدد الاساسيين$"]))
async def countofDev(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in mainSudoVII or int(user) == owner:
		l = await m.reply("**◍ جاري حساب عدد اساسيين البوت√**")
		lens = len(open(f"maindevsVII{bot_id}.json","r").readlines())
		time.sleep(.5)
		if lens == 0:
			return await l.edit("**◍ لم تقم برفع اي مطورين اساسيين في البوت √**")
		return await l.edit(f"**◍ تم رفع {lens} مطور اساسي في البوت √**")
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

#----------------------SpecialUser-----------------------

@app.on_message(command(["^عرض المطورين$"]))
async def __show_sudos(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		file = open(f"sudo{bot_id}.json","r")
		lens = len(open(f"sudo{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري عرض المطورين √**")
		x = 1
		text = "**Bot sudo Users **:\n\n"
		for su in file:
			text += f"{x} - {su}"
			x += 1
		time.sleep(1)
		if lens == 0:
			return await l.edit("**◍ لم يتم رفع مطورين في البوت √**")
		return await l.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(command(["^عدد المطورين$"]))
async def countofsudos(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		l = await m.reply("**◍ جاري حساب عدد مطورين البوت √**")
		lens = len(open(f"sudo{bot_id}.json","r").readlines())
		time.sleep(.5)
		if lens == 0:
			return await l.edit("**◍ لم تقم برفع اي مطورين في البوت √**")
		return await l.edit(f"**◍ تم رفع {lens} مطور في البوت √**")
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(command(["^نسخه المطورين$"]))
async def get_copy_Sudo(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		file = open(f"sudo{bot_id}.json","rb")
		lenb = len(open(f"sudo{bot_id}.json","r").readlines())
		l = await m.reply("**◍ جاري جلب نسخه للمطورين√**")
		time.sleep(2)
		if lenb == 0:
			return await l.edit("**◍ لم تقم برفع اي مطور في البوت √**")
		await l.delete()
		await m.reply_document(document=file,caption=f"**Sudo users {lenb} √")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")	
	
#-------------------NormalUser-------------------------

@app.on_message(command(["^عرض الاعضاء$"]))
async def show_users(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		users = open(f"Users{bot_id}.json","r")
		x = 1
		text = "**Bot Users **: \n\n"
		for us in users:
			text += f"{x} - {us} \n"
			x+=1
		i = await m.reply("**◍ جارى عرض الاعضاء √**")
		time.sleep(.5)
		lenm = len(open(f"Users{bot_id}.json","r").readlines())
		if lenm == 0:
			return await i.edit("**◍ لم يقم اي عضو بالدخول للبوت √**")
		return await i.edit(text=text)
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(command("^نسخه الاعضاء$"))
async def __get_users_copy(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		l = await m.reply("**◍ جاري سحب نسخه للاعضاء √**")
		time.sleep(2)
		lenu = len(open(f"Users{bot_id}.json","r").readlines())
		users = open(f"Users{bot_id}.json","rb")
		if lenu == 0:
			return await l.edit("**◍ لم يقم اي عضو بالدخول الي البوت √**")
		await l.delete()
		await m.reply_document(document=users,caption=f"**Bot users {lenu} √**")
		return
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

@app.on_message(command(["^عدد الاعضاء$"]))
async def countofusers(c:Client,m:Message):
	user = m.from_user.id
	mainSudo = open(f"maindevs{bot_id}.json","r").read()
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	
	if str(user) in mainSudo or str(user) in sudo or str(user) in mainSudoVII or int(user) == owner:
		l = await m.reply("**◍ جاري حساب عدد الاعضاء √**")
		lens = len(open(f"Users{bot_id}.json","r").readlines())
		time.sleep(.5)
		if lens == 0:
			return await l.edit("**◍ لم يدخل اي عضو للبوت حتي الآن √**")
		return await l.edit(f"**◍ عدد اعضاء بوتك {lens} √**")
	return await m.reply("**◍ انت لست مطور في البوت \n√**")

#--------♡-------------Subscribe------------♡----------

@app.on_message(command(["اضف قناة اشتراك اجباري"]))
async def AddKey(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
		ask = await m.chat.ask('**معرف القناه بدون @**')
		if ask.text == "الغاء":
			await ask.request.delete()
			await ask.delete()
			await m.reply(f"**تم الالغاء**")
			return
		if '@' in ask.text:
			return await m.reply('**المعرف بدون @**')
		if "ا" in ask.text:
			return await m.reply('لم يتم** التعرف**')
		add_channel(chat_id=ask.text)
		await m.reply('**تم وضع {} قناة اشتراك √**'.format(ask.text))
		return
		
@app.on_message(command(["عرض قناة الاشتراك"]))
async def ShowKey(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
	    return await m.reply(f"**@{show_channel()} قناه الاشتراك**")
	

@app.on_message(command(["حذف قناه الاشتراك"]))
async def DellKey(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	sudo = open(f"sudo{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
	    		del_channel()
	    		await m.reply(f"تم حذفها")
	
#--------------------------------------------------------------
#-----------------------DevChannel---------------------
@app.on_message(command(["اضافه قناه المطور"]))
async def AddChannel(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
		ask = await m.chat.ask('**معرف قناه المطور بدون @**')
		if ask.text == "الغاء":
			await ask.request.delete()
			await ask.delete()
			await m.reply(f"**تم الالغاء**")
			return
		if '@' in ask.text:
			return await m.reply('**المعرف بدون @**')
		if 'اضافه'in ask.text:
			return await m.reply('**لم يتم التعرف**')
		add_devchannel(chat_id=ask.text)
		await m.reply('**تم وضع قناه المطور @{} √**'.format(ask.text))
		return
		
@app.on_message(command(["عرض قناة المطور"]))
async def ShowDevKey(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
	    return await m.reply(f"**@{show_devchannel()} قناه المطور**")
	

@app.on_message(command(["حذف قناه المطور"]))
async def DellDevKey(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
	    		del_devchannel()
	    		await m.reply('**حذفت القناه بنجاح**')

	    		

#--------------------------------------------------------------
#-----------------------DevUser-------------------------
@app.on_message(command(["اضافه معرف المطور"]))
async def AddDevUser(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
		ask = await m.chat.ask('**معرف المطور بدون @**')
		if ask.text == "الغاء":
			await ask.request.delete()
			await ask.delete()
			await m.reply(f"**تم الالغاء**")
			return
		if '@' in ask.text:
			return await m.reply('**المعرف بدون @**')
		if 'اضافه'in ask.text:
			return await m.reply('**لم يتم التعرف**')
		add_devuser(chat_id=ask.text)
		await m.reply('**تم وضع معرف المطور @{} √**'.format(ask.text))
		return
		
@app.on_message(command(["عرض معرف المطور"]))
async def ShowDevUser(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
	    return await m.reply(f"**@{show_devuser()} معرف المطور**")
	

@app.on_message(command(["حذف معرف المطور"]))
async def DellDevUser(c:Client,m:Message):
	user = m.from_user.id
	mainSudoVII = open(f"maindevsVII{bot_id}.json","r").read()
	if str(user) in mainSudoVII or int(user) == owner:
	    		del_devuser()
	    		await m.reply('**حذف المعرف بنجاح**')
	    		
# #-------------------------------------------------------------
# #---------------------AddOwner------------------------

