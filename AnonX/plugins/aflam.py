"""
        [InlineKeyboardButton("◁", callback_data="Yrw1 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("➡️ التالي", callback_data="Yrw3 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="moslsl " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀 ⌝⚡", url=f"https://t.me/lN_B_Fl")],
"""

import asyncio

from strings import get_command
from strings.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from AnonX import app



#########################################################################################
#########################################################################################
#########################         # Aflam Arabic #             ##########################
#########################################################################################
#########################################################################################

# Replay Text

@app.on_message(
    command(["افلام"])
    & ~filters.edited
)
async def aflamAR(c: Client, m: Message):
    global mid
    mid = m.message_id
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("افلام 🎬", callback_data="film " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("مسلسلات 📼", callback_data="moslsl " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("مسرحيات 🎭 ", callback_data="msrahia " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.reply_text("◍ اهلا بيك في قائمة الافلام والمسلسلات العربيه\n√", reply_markup=keyboard)


# Replay Edit
@app.on_callback_query(filters.regex("^aflamAR2 (\\d+)$"))
async def aflamAR2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("افلام 🎬", callback_data="film " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("مسلسلات 📼", callback_data="moslsl " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("مسرحيات 🎭 ", callback_data="msrahia " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة الافلام والمسلسلات العربيه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^film (\\d+)$"))
async def film(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("كوميدي 😹", callback_data="comedy " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("اكشن 🔥", callback_data="action " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("دراما 🌚", callback_data="drama " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="aflamAR2 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة الافلام العربيه\n√", reply_markup=keyboard)


#########################################################################################
#########################################################################################
#########################         # Aflam Comedy #             ##########################
#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^comedy (\\d+)$"))
async def comedy(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ وقفة رجاله", callback_data="Xco1 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الخطة العايمة", callback_data="Xco2 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ بنات ثانوي", callback_data="Xco3 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ عفريت ترانزيت", callback_data="Xco4 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ زكي شان", callback_data="Xco5 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ سمير وشهير وبهير", callback_data="Xco6 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ تصبح علي خير", callback_data="Xco7 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ بابا", callback_data="Xco8 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ جدو نحنوح", callback_data="Xco9 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ سمير ابو النيل", callback_data="Xco10 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ كلبي دليلي", callback_data="Xco11 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ بنات العم", callback_data="Xco12 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ علي بابا", callback_data="Xco13 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ فول الصين العظيم", callback_data="Xco14 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ حسن وبقلظ", callback_data="Xco15 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الكويسين", callback_data="Xco16 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ يوم مالوش لازمه", callback_data="Xco17 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ غبي منه فيه", callback_data="Xco18 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ خير وبركه", callback_data="Xco19 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ البدله", callback_data="Xco20 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="film " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بك في قائمة الافلام الكوميدي العربيه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco1 (\\d+)$"))
async def Xco1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco1 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco2 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : وقفة رجالة
    📖 انتاج سنة : 2021
    🌎 الدولة : مصر
    🗄 تصنيف : كوميدي
    📜 قصة الفيلم:
    تدور أحداث العمل في قالب كوميدي حول مجموعة من الأصدقاء الذين يجتمعون بعد سنوات لمساعدة أحدهم في الخروج من ورطة كبيرة، وتتطوّر الأحداث فتقودهم للسفر إلى إحدى المدن الساحلية.
    """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco2 (\\d+)$"))
async def Xco2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco3 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco4 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : الخطة العايمة
        📖 انتاج سنة  : 2020
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        في إطار كوميدي لايت تدور الأحداث حول أحد الأشخاص يتطلع إلى سرقة أحد البنك لوجود أوراق هامة في الخزانة، فيتفق مع (جلال وياسمين) لتولي المهمة، واللذان يختاران اللصان الساذجان (حمزون وعلى الله) لتنفيذ تلك المهمة، ويبدآن في تدريبهما.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco3 (\\d+)$"))
async def Xco3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco5 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco6 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : بنات ثانوي
         انتاج سنة : 2020
        🌎 الدولة : مصر
        🗄 تصنيف : دراما, كوميدي, رومانسي
        📜 قصة الفيلم:
        تدور أحداث الفيلم حول فترة المراهقة، حيث تبحث خمس فتيات في مرحلة المراهقة عن ذواتهن وشخصياتهن، ليقعن في العديد من المتاعب والصعاب خلال مرحلة الدراسة الثانوية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco4 (\\d+)$"))
async def Xco4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco7 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco8 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : عفريت ترانزيت
        📖 انتاج سنة : 2020
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        يتناول العمل قصة بائع مخدرات يتعرض للعديد من المشاكل واتهامه في جريمة قتل، الأمر الذي يدفعه لمحاولة البحث عن براءته والسير في طريق التوبة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco5 (\\d+)$"))
async def Xco5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco9 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco10 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : زكي شان
        📖 انتاج سنة  : 2005
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        زكي شاب كثير المشاكل سواء مع أفراد أسرته أو في عمله، يعلم أن رب عمل والده يرغب في تعيين بودي جارد كي يحرس ابنه وابنته، ويقرر التقدم للوظيفة رغم عدم ملائمته جسديًا للوظيفة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco6 (\\d+)$"))
async def Xco6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco11 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco12 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : سمير وشهير وبهير
        📖 انتاج سنة  : 2010
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي, رومانسي
        📜 قصة الفيلم:
        ثلاثة أخوة لنفس الأب؛ ولكن لأمهات مختلفة هم  (سمير)، ويعمل دوبلير فى السينما، و (شهير) يحب الموسيقي ومعروف بعلاقاته النسائية المتعددة، (بهير) وهو ابن لأسرة أرستقراطية. نتيجة سوء تعامل مع إحدى آلآت الزمن يسافروا عبر الزمن إلى اليوم الذي قابل فيه والدهم الأمهات الثلاثة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco7 (\\d+)$"))
async def Xco7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco13 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco14 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : تصبح علي خير
        📖 انتاج سنة  : 2017
        🌎 الدولة : مصر
        🗄 تصنيف : دراما , كوميدي , رومانسي
        📜 قصة الفيلم:
        في إطار كوميدي رومانسي تشويقي، تدور قصة الفيلم في إطار مُختلف عن مهندس ناجح وثري يدعى (حسام الخديوي)، ولكنه يعاني في اﻵونة اﻷخيرة من مشاكل في حياته الطبيعية فيلجأ إلي حياة بديلة من خلال جهاز جديد يُدخله في عالم الأحلام.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco8 (\\d+)$"))
async def Xco8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco15 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco16 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : بابا
        📖 انتاج سنة  : 2012
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي , رومانسي
        📜 قصة الفيلم:
        تدور أحداث الفيلم في إطار رومانسي كوميدي حيث الطبيب حازم (أحمد السقا) طبيب أمراض النساء الذي تتعلق بحبه مهندسة الديكور فريدة (درة) وعقب زواجهما يفاجأ حازم بعدم قدرته على الإنجاب فيضطر للجوء إلى عملية الحقن المهجري، فترى هل سيتمكن من تحقيق رغبتهما؟
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco9 (\\d+)$"))
async def Xco9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco17 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco18 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : جدو نحنوح
        📖 انتاج سنة  : 2018
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        مجموعة من الشباب يتوفى جدهم، وعند توزيع الميراث يكتشفون أن جدهم لم يترك أموالًا لهم، بينما ترك وصية يُطالبهم فيها بالبحث عن كنز مدفون، وبالبحث عن مكان الكنز يتضح أنه داخل مستشفى المجانين. فيخططون لدخول مستشفى المجانين سعيًا لإيجاد هذا الكنز، وهناك تحدث لهم الكثير من المفارقات الكوميدية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco10 (\\d+)$"))
async def Xco10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco19 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco20 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : سمير ابو النيل
        📖 انتاج سنة : 2013
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        في إطار كوميدي تدور أحداث الفيلم حول الشاب البخيل سمير أبو النيل (أحمد مكي) الذي يقطن بحي شعبي، ونتيجة لبخله الشديد تقع له العديد من المفارقات والمشاكل مع أهل منطقته، ويزيد من كرههم له لسوء معاملته لهم، وبين ليلة وضحاها يمرض ابن عمه حسين أبو النيل (حسين اﻹمام) ويقرر أن يترك ثروته لسمير الذي يستغل ذلك ويقوم بإنشاء قناة فضائية يناقش فيها أحواله وعلاقاته بأصدقائه وأهل منطقته.. تتوالى الأحداث في سياق كوميدي بعد إنشاء حزب سياسي يدعو له المواطنين.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco11 (\\d+)$"))
async def Xco11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco21 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco22 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : كلبي دليلي
        📖 انتاج سنة : 2013
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        تدور قصة الفيلم حول ضابط الشرطة مغاوري (سامح حسين)، الذي يعيش في صعيد مصر، ثم يُنقل فجأة إلى مارينا بالساحل الشمالي، وما عليه هناك إلا إثبات ذاته كضابط يحتذى به أمام الضباط وإشادة رئيسه بأدائه، إلى جانب ذلك يجد (مغاوري) نفسه واقعًا في حب فتاة تختلف عنه تمامًا في كل شيء.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco12 (\\d+)$"))
async def Xco12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco23 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco24 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : بنات العم
        📖 انتاج سنة : 2012
        🌎 الدولة : مصر
        🗄 تصنيف : دراما, كوميدي
        📜 قصة الفيلم:
        ثلاث فتيات تربطهن علاقة عمومة يعشن مع جدتهن، يتطلعن إلى بيع القصر الذي يعشن به، فيتوجهن إلى (عزيز الهانش) ليشتري القصر، فتحاول الجدة منعهن وتحذرهن من لعنة حدثت لأجدادهن، إلا أن الفتيات لا ينصتن لها، فأصابتهن اللعنة ويتحولن إلى رجال، وطوال الأحداث تسعى الفتيات لإعادة القصر، ومحاولة فك اللعنة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco13 (\\d+)$"))
async def Xco13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco25 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco26 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : علي بابا
        📖 انتاج سنة : 2018
        🌎 الدولة : مصر
        🗄 تصنيف : دراما، كوميدي
        📜 قصة الفيلم:
        تدور أحداث الفيلم في إطار كوميدي حول شخص انتهازي يُدعى (علي)، يسعى إلى تحقيق مصالحه الشخصية حتى ولو كانت على حساب الآخرين، وإذا به يفاجئ بوجود ابنة له (أيتن عامر) في سن العشرينات، وتبدأ من هنا المفارقات الكوميدية التي يقع فيها.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco14 (\\d+)$"))
async def Xco14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco27 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco28 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : فول الصين العظيم
        📖 انتاج سنة : 2004
        🌎 الدولة : مصر
        🗄 تصنيف :  كوميدي، اكشن
        📜 قصة الفيلم:
        يدور الفيلم في إطار كوميدي حول شاب مصري يدعى (محي الشرقاوي)، يشكل كل من جده (جابر الشرقاوي) وأعمامه عصابة للتهريب، ولأنه جبان لا يستطيع مسايرتهم والعمل معهم، يذهب لوالدته وزوجها والذي يرسله للصين ليمثل مصر في مسابقة للطبخ، ليقع في العديد من المشكلات.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco15 (\\d+)$"))
async def Xco15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco29 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco30 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : حسن وبقلظ
        📖 انتاج سنة : 2016
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي , رومانسي , دراما
        📜 قصة الفيلم:
        تدور أحداث الفيلم حول شقيقين ملتصقين ببعضهما البعض (علي ربيع) و(كريم فهمي)، تقع معهما العديد من المواقف الكوميدية، يتورط معهما ابن خالتهما (محمد أسامة) وفي مشاكلهما.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco16 (\\d+)$"))
async def Xco16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco31 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco32 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : الكويسين
        📖 انتاج سنة : 2018
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        مفتاح وشقيقته غزال ثنائي متخصص في النصب، يكتشف مفتاح وجود جوهرة ثمينة تدعى القرموط القرمزي في منزل عائلة الكويسين، فيقرر اختراق صفوف هذه العائلة من خلال انتحال شخصية ابنهم مظهر المفقود منذ سنوات طويلة، لكن هذه المهمة تواجه الكثير من الصعوبات رغم نجاحها في البداية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco17 (\\d+)$"))
async def Xco17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco33 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco34 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : يوم مالوش لازمة
        📖 انتاج سنة : 2015
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        ?? قصة الفيلم:
        اليوم هو يوم زفاف يحيى ومها ,و منذ الصباح الباكر يستعد العروسان لاستقبال هذا اليوم، لكن بمجرد أن يبدأ هذا اليوم حتى يقع العروسان طوال اليوم وفي حفل الزفاف نفسه في سلسلة طويلة لا تنتهي من المفارقات والمواقف الصعبة، وما يزيد الطين بلة هو مطاردة الفتاة المهووسة بوسي ليحيى طوال اليوم، وإصرارها الشديد أن تكون هي زوجته بدلًا من مها.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco18 (\\d+)$"))
async def Xco18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco35 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco36 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : غبي منه فيه
        📖 انتاج سنة : 2004
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي
        📜 قصة الفيلم:
        يشعر سلطان باليأس من تحقيق حلمه بالزواج من حبيبته سامية التي أعطى له والدها مهلة شهر واحد كي يعد خلاله بيت الزوجية، فتعرف سامية على زوج خالتها ضبش، والذي يشركه في سرقاته لمساعدته، لكنه يوقعه في المتاعب بسبب غبائه الشديد.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco19 (\\d+)$"))
async def Xco19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco37 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco38 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : خير وبركة
        📖 انتاج سنة : 2017
        🌎 الدولة : مصر
        🗄 تصنيف : كوميديا
        📜 قصة الفيلم:
        تدور أحداث الفيلم في إطار كوميدي يتناول قصة شقيقين يحاولان البحث عن فرصة عمل، وخلال رحلة البحث يواجهان العديد من المواقف الكوميدية عندما يعملان في مهن لا يعرفان عنها شيئًا.

        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xco20 (\\d+)$"))
async def Xco20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXco39 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXco40 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="comedy " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : البدلة
        📖 انتاج سنة : 2018
        🌎 الدولة : مصر
        🗄 تصنيف : كوميدي , رومانسي
        📜 قصة الفيلم:
        تدور القصة حول حمادة، ووليد اللذين ولدا في نفس اليوم فاشلين في الحياة، يقرران الذهاب إلى حفلة تنكرية، ويتنكران في زي رجال الشرطة لمقابلة زملائهم القدامى، الأمر الذي يجعل الجميع يعتقد بأنهما شرطيين حقيقيين، وتقع لهما العديد من الأحداث والمشاكل.

        """, reply_markup=keyboard)


#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^XXco1 (\\d+)$"))
async def XXco1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/121", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco2 (\\d+)$"))
async def XXco2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/122", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco3 (\\d+)$"))
async def XXco3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/123", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco4 (\\d+)$"))
async def XXco4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/124", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco5 (\\d+)$"))
async def XXco5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/125", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco6 (\\d+)$"))
async def XXco6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/126", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco7 (\\d+)$"))
async def XXco7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/127", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco8 (\\d+)$"))
async def XXco8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/128", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco9 (\\d+)$"))
async def XXco9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/129", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco10 (\\d+)$"))
async def XXco10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/130", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco11 (\\d+)$"))
async def XXco11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/131", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco12 (\\d+)$"))
async def XXco12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/132", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco13 (\\d+)$"))
async def XXco13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/133", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco14 (\\d+)$"))
async def XXco14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/134", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco15 (\\d+)$"))
async def XXco15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/135", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco16 (\\d+)$"))
async def XXco16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/136", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco17 (\\d+)$"))
async def XXco17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/137", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco18 (\\d+)$"))
async def XXco18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/139", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco19 (\\d+)$"))
async def XXco19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/140", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco20 (\\d+)$"))
async def XXco20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/141", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco21 (\\d+)$"))
async def XXco21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/142", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco22 (\\d+)$"))
async def XXco22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/143", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco23 (\\d+)$"))
async def XXco23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/144", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco24 (\\d+)$"))
async def XXco24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/145", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco25 (\\d+)$"))
async def XXco25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/146", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco26 (\\d+)$"))
async def XXco26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/147", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco27 (\\d+)$"))
async def XXco27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/148", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco28 (\\d+)$"))
async def XXco28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/149", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco29 (\\d+)$"))
async def XXco29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/150", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco30 (\\d+)$"))
async def XXco30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/151", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco31 (\\d+)$"))
async def XXco31(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/152", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco32 (\\d+)$"))
async def XXco32(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/153", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco33 (\\d+)$"))
async def XXco33(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/154", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco34 (\\d+)$"))
async def XXco34(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/155", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco35 (\\d+)$"))
async def XXco35(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/156", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco36 (\\d+)$"))
async def XXco36(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/157", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco37 (\\d+)$"))
async def XXco37(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/158", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco38 (\\d+)$"))
async def XXco38(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/159", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco39 (\\d+)$"))
async def XXco39(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/160", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXco40 (\\d+)$"))
async def XXco40(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/161", reply_to_message_id=mid)


#########################################################################################
#########################################################################################
#########################         # Aflam Action #             ##########################
#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^action (\\d+)$"))
async def action(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("حملة فرعون", callback_data="Xact1 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("بني ادم", callback_data="Xact2 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("الخليه", callback_data="Xact3 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("حرب كرموز", callback_data="Xact4 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("من ضهر راجل", callback_data="Xact5 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("زنزانة سبعة", callback_data="Xact6 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("خارج عن القانون", callback_data="Xact7 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("ولاد العم", callback_data="Xact8 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("وش سجون", callback_data="Xact9 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="aflamAR2 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("اهلا بك في قائمة الافلام الاكشن العربيه", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact1 (\\d+)$"))
async def Xact1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact1 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact2 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="action " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : حملة فرعون
📖 انتاج سنة : 2019
🌎 الدولة : مصر
🗄 تصنيف : اكشن , اثارة , تشويق
📜 قصة الفيلم:
تدور أحداث الفيلم في إطار تشويقي مثير حول الشاب يحيى الشهير بفرعون والذي يدير أكبر شبكة اغتيالات منظمة في مصر، ويضطر إلى التوجه إلى سوريا لتحرير أبنه المخطوف .
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact2 (\\d+)$"))
async def Xact2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact3 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact4 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="action " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : بني ادم
📖 انتاج سنة : 2018
🌎 الدولة : مصر
🗄 تصنيف : اكشن , اثارة , تشويق
📜 قصة الفيلم:
تدور الأحداث في إطار بوليسي تشويقي مثير حول رجل الأعمال (آدم) الذي يتهم بأعمال إجرامية، في الوقت الذي تلجأ إليه الشرطة في مهمة خطيرة، فهل الأحداث ستتطور وتجعله متورط، أم هناك جانب غامض غير معروف عنه؟.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact3 (\\d+)$"))
async def Xact3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact5 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact6 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="action " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""فيلم #الخلية | دراما , اكشن | 2017
عندما يذهب صديقه ضحية عملية إرهابية، يقسم سيف، وهو ضابط عمليات خاصة، على الثأر لصديقه، ويطلب مساعدة الضابط صابر في سبيل تحقيق ذلك.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact4 (\\d+)$"))
async def Xact4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact7 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact8 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="action " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : حرب كرموز
📖 انتاج سنة : 2018
🌎 الدولة : مصر
🗄 تصنيف : اكشن , اثارة , تشويق
📜 قصة الفيلم:
تتعرض فتاة للاعتداء على يد جنود إنجليز فيثأر لها ثلاثة شبان مصريين ويقومون باحتجاز أحد الجنود في مركز شرطة كرموز، الأمر الذي ستترتب عليه عواقب وخيمة.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact5 (\\d+)$"))
async def Xact5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact9 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact10 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="action " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : من ضهر راجل
📖 انتاج سنة : 2015
🌎 الدولة : مصر
🗄 تصنيف : دراما، رومانسي، اكشن
📜 قصة الفيلم:
رحيم أدهم ملاكم شاب ويعيش في حارة شعبية مع والده المسن إمام المسجد، ويحب مي وينوي الزواج منها، وفور علم حِنش بما يدور بين رحيم ومي من لقاءات عن طريق طه الذي ينافس رحيم على حب مي، تتحول حياة رحيم ووالده إلى جحيم مقيم على الأرض، خاصة مع انكشاف أسرار من الماضي.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact6 (\\d+)$"))
async def Xact6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact11 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact12 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="action " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : زنزانة سبعة
📖 انتاج سنة : 2020
🌎 الدولة : مصر
🗄 تصنيف : دراما , اكشن , تشويق , اثارة
📜 قصة الفيلم:
تدور حول شاب يدعى "حربي الكومي"، يدخل السجن بعد اتهامه في إحدى القضايا, داخل السجن يلتقي "حربي" بـ"منصور العايق" ، ويحدث بينهما خلافات كثيرة في بداية الأحداث، وبعد ذلك تنشأ بينهما علاقة صداقة قوية.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact7 (\\d+)$"))
async def Xact7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact13 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact14 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="action " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : خارج عن القانون
📖 انتاج سنة : 2007
🌎 الدولة : مصر
🗄 تصنيف : دراما, اكشن, اثارة وتشويق
📜 قصة الفيلم:
تدور أحداث الفيلم حول شخصية عمر (كريم عبدالعزيز). تبدأ مأساة عمر منذ أن كان طفلًا صغيرًا حيث شهد علي تبادلٍ لإطلاق النار بين والده (محمود الجندي) وقوات الشرطة ،وبالرغم من أن والده استسلم وترك سلاحه لكن يتم قنصه. ومن هنا يصبح ما تبقى من عائلته مهددًا بالهلاك ولا يجد أمامه خيارٌ غير أن يرمي نفسه في أحضان أحد حيتان تجارة المخدرات (حسن حسني) ليأخذه تحت جناحه وينشأ عمر ليجد نفسه وقد أصبح تاجرًا للمخدرات. 
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact8 (\\d+)$"))
async def Xact8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact15 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact16 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="action " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : ولاد العم
📖 انتاج سنة : 2009
🌎 الدولة : مصر
🗄 تصنيف : دراما, اكشن, اثارة وتشويق
📜 قصة الفيلم:
ضابط بالموساد مسئول عن تكوين شبكة جاسوسية لتنفيذ اغتيالات في مصر، يتزوج بفتاة مصرية دون أن يخبرها بحقيقته، ثم يهرب بها رغمًا عنها إلى إسرائيل ضاغطًا عليها بحرمانها من أولادها. فترسل المخابرات المصرية ضابطًا لكشف نوعية المعلومات التي حصل عليها وإعادة الزوجة المخدوعة للقاهرة بصحبة طفليها.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xact9 (\\d+)$"))
async def Xact9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXact17 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXact18 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="action " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : وش سجون
📖 انتاج سنة : 2014
🌎 الدولة : مصر
🗄 تصنيف : اثارة وتشويق, اكشن
📜 قصة الفيلم:
تدور الأحداث في إطار درامي شيق حول ثلاث شباب، يتقابلون داخل سجن واحد، ولكل منهم حكاية عن سبب دخوله للسجن، أولهم شاب  يُحكم عليه بالإعدام في قضية اغتصابه لفتاة من العمارة التي كان يعمل بها كبواب، والثاني جابر المتزوج من عزة والذي يدخل السجن بسببها مرتين، والثالث وليد رجل الأعمال المتزوج من نور التي تورطه في قضية شيكات بعد أن تعلم بخيانته لها وزواجه من واحدة أخرى فتحاول الانتقام منه. يتناول الفيلم تفاصيل الحياة داخل السجن، والعلاقات اﻹنسانية بين السجناء.
        """, reply_markup=keyboard)


#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^XXact1 (\\d+)$"))
async def XXact1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/162", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact2 (\\d+)$"))
async def XXact2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/163", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact3 (\\d+)$"))
async def XXact3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/164", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact4 (\\d+)$"))
async def XXact4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/165", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact5 (\\d+)$"))
async def XXact5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/166", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact6 (\\d+)$"))
async def XXact6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/167", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact7 (\\d+)$"))
async def XXact7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/168", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact8 (\\d+)$"))
async def XXact8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/169", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact9 (\\d+)$"))
async def XXact9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/170", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact10 (\\d+)$"))
async def XXact10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/171", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact11 (\\d+)$"))
async def XXact11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/172", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact12 (\\d+)$"))
async def XXact12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/173", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact13 (\\d+)$"))
async def XXact13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/174", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact14 (\\d+)$"))
async def XXact14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/175", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact15 (\\d+)$"))
async def XXact15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/176", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact16 (\\d+)$"))
async def XXact16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/177", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact17 (\\d+)$"))
async def XXact17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/178", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXact18 (\\d+)$"))
async def XXact18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/179", reply_to_message_id=mid)


#########################################################################################
#########################################################################################
#########################         # Aflam Drama #             ###########################
#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^drama (\\d+)$"))
async def drama(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ هذه ليلتي", callback_data="Xdra1 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ ورقة جمعية", callback_data="Xdra2 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ حظر تجوال", callback_data="Xdra3 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ القط", callback_data="Xdra4 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ خان تيولا", callback_data="Xdra5 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="aflamAR2 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("اهلا بك في قائمة الافلام الدراما العربيه", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xdra1 (\\d+)$"))
async def Xdra1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXdra1 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXdra2 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="drama " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : هذه ليلتي
📖 انتاج سنة : 2019
🌎 الدولة : مصر
🗄 تصنيف : دراما
📜 قصة الفيلم:
تقرر (عزة) الاستمتاع بيومها، والذهاب رفقة ابنها المصاب بمتلازمة داون في مغامرة، وحينما تتجه من عشوائيات القاهرة إلى الأحياء الفخمة من أجل تناول المثلجات، تقابل العديد من المضايقات والعقبات في طريقها.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xdra2 (\\d+)$"))
async def Xdra2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXdra3 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXdra4 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="drama " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : ورقة جمعية
📖 انتاج سنة : 2020
🌎 الدولة : مصر
🗄 تصنيف : دراما
📜 قصة الفيلم:
تتناول أحداث الفيلم في قالب درامي قصة امرأة يُطلق عليها أم عبدالله، حيث تسعى لرعاية شقيقتها وعائلتها في حارة بسيطة من خلال إدارة محل كوافير خاص بها.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xdra3 (\\d+)$"))
async def Xdra3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXdra5 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXdra6 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="drama " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : حظر تجول
📖 انتاج سنة : 2021
🌎 الدولة : مصر
🗄 تصنيف : دراما
📜 قصة الفيلم:
تدور الأحداث في خريف عام 2013 بعد قرار حظر التجوال بمصر، حيث تخرج فاتن من السجن بعد قضائها عشرين عامًا بسبب ارتكابها جريمةّ مريعة، وتجبر فاتن على قضاء ليلتها عند ابنتها ليلى والتي تعرضها لمحاكمة ثانية بحثاً عن اجابات لأسئلة مسكوت عنها. لتمر الليلة في محاولة كل منهما لتقبل الأخرى.
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xdra4 (\\d+)$"))
async def Xdra4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXdra7 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXdra8 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="drama " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : القط
📖 انتاج سنة : 2014
🌎 الدولة : مصر
🗄 تصنيف : دراما
📜 قصة الفيلم:
يتناهى إلى سمع القط (عمرو واكد) خبر اختطاف مجموعة من الأطفال في المنطقة التي يعيش بها ، بغرض الحصول على أعضائهم الحيوية وبيعها في السوق السوداء ، وعلى إثر ذلك يقوم (القط) بقتل أحد رجال المعلم فتحي (صلاح الحنفي) ، وتخليص الفتاة التي بقت على قيد الحياة ، وبعدها ينخرط في رحلة طويلة محمومة مع غجري (عمرو فاروق) ؛ لملاحقة المعلم (فتحي) بتشجيع من أحد الرجال النافذين (فاروق الفيشاوي) .
        """, reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xdra5 (\\d+)$"))
async def Xdra5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton("⌯ جوده متوسطه", callback_data="XXdra9 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ جوده عاليه", callback_data="XXdra10 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("◁", callback_data="drama " + (https://t.me/lV_P_Nl))],
    ])
    await m.message.edit_text("""🎥 اسم الفيلم : خان تيولا
📖 انتاج سنة : 2020
🌎 الدولة : مصر
🗄 تصنيف : دراما, اثارة وتشويق، غموض
📜 قصة الفيلم:
تدور أحداث الفيلم في حقبة الأربعنيات خلال الحرب العالمية الثانية داخل أحد الفنادق بمدينة العالمين، الذي يملكه الفنان محمود البزاوي والذي يعيش مع أسرته المكونة من  زوجته والتي تجسد دورها الفنانة وفاء عامر ونجله الذي يقوم بدوره الفنان علي الشجيري ونجلته التي تجسدها الفنانة الشابة زهرة الحاروفي، ويصل إليهم في أحد الليالي نزيل جديد والذي يجسد دوره الفنان نضال الشافعي، ليتفاجئ بالكثير من الأشياء الغامضة داخل هذا الفندق تقلب أحداث العمل.
        """, reply_markup=keyboard)


#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^XXdra1 (\\d+)$"))
async def XXdra1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/180", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra2 (\\d+)$"))
async def XXdra2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/181", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra3 (\\d+)$"))
async def XXdra3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/182", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra4 (\\d+)$"))
async def XXdra4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/183", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra5 (\\d+)$"))
async def XXdra5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/184", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra6 (\\d+)$"))
async def XXdra6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/185", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra7 (\\d+)$"))
async def XXdra7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/186", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra8 (\\d+)$"))
async def XXdra8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/187", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra9 (\\d+)$"))
async def XXdra9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/188", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^XXdra10 (\\d+)$"))
async def XXdra10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/189", reply_to_message_id=mid)


#########################################################################################
#########################################################################################
#########################         # END Aflam AR #             ##########################
#########################################################################################
#########################################################################################


#########################################################################################
#########################################################################################
#########################         # Start Moslsl AR #          ##########################
#########################################################################################
#########################################################################################


@app.on_callback_query(filters.regex("^moslsl (\\d+)$"))
async def moslsl(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("حشمت في البيت الأبيض 📼", callback_data="Xmos1 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("لعبة النسيان 📼", callback_data="Xmos2 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("ب 100 وش 📼", callback_data="Xmos3 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("آدم 📼", callback_data="Xmos4 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("توبه 📼", callback_data="toba " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("ابو العروسة 📼", callback_data="Xmos5 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="aflamAR2 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة المسلسلات العربيه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmos1 (\\d+)$"))
async def Xmos1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmos214 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmos215 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmos216 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmos217 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmos218 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmos219 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmos220 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmos221 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmos222 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmos223 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmos224 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmos225 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmos226 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="moslsl " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مسلسل 📼 حشمت في البيت الأبيض\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmos2 (\\d+)$"))
async def Xmos2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmos229 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmos230 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmos231 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmos232 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmos233 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmos234 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmos235 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmos236 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmos237 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmos238 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmos239 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmos240 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmos241 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmos242 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmos243 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmos244 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmos245 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="Zmos246 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="Zmos247 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="Zmos248 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="Zmos249 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="Zmos250 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 23", callback_data="Zmos251 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 24", callback_data="Zmos252 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 25", callback_data="Zmos253 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 26", callback_data="Zmos254 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 27", callback_data="Zmos255 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 28", callback_data="Zmos256 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 29", callback_data="Zmos257 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 30", callback_data="Zmos258 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="moslsl " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مسلسل 📼 2- لعبة النسيان\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmos3 (\\d+)$"))
async def Xmos3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmos261 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmos262 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmos263 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmos264 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmos265 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmos266 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmos267 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmos268 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmos269 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmos270 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmos271 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmos272 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmos273 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmos274 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmos275 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmos276 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmos277 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="Zmos278 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="Zmos279 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="Zmos280 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="Zmos281 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="Zmos282 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 23", callback_data="Zmos283 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 24", callback_data="Zmos284 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 25", callback_data="Zmos285 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 26", callback_data="Zmos286 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 27", callback_data="Zmos287 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 28", callback_data="Zmos288 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 29", callback_data="Zmos289 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 30", callback_data="Zmos290 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="moslsl " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مسلسل 📼 3- ب 100 وش\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmos4 (\\d+)$"))
async def Xmos4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmos293 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmos294 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmos295 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmos296 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmos297 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmos298 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmos299 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmos300 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmos301 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmos302 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmos303 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmos304 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmos305 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmos306 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmos307 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmos308 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmos309 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="Zmos310 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="Zmos311 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="Zmos312 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="Zmos313 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="Zmos314 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 23", callback_data="Zmos315 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 24", callback_data="Zmos316 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 25", callback_data="Zmos317 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 26", callback_data="Zmos318 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 27", callback_data="Zmos319 " + (https://t.me/lV_P_Nl))], 
        [InlineKeyboardButton("⌯ الحلقة 28", callback_data="Zmos320 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 29", callback_data="Zmos321 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 30", callback_data="Zmos322 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="moslsl " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مسلسل 📼 4- آدم\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmos5 (\\d+)$"))
async def Xmos5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmos325 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmos326 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmos327 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmos328 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmos329 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmos330 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmos331 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmos332 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmos333 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmos334 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmos335 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmos336 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmos337 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmos338 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmos339 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmos340 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmos341 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="Zmos342 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="Zmos343 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="Zmos344 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="Zmos345 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="Zmos346 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 23", callback_data="Zmos347 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 24", callback_data="Zmos348 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 25", callback_data="Zmos349 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 26", callback_data="Zmos350 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 27", callback_data="Zmos351 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 28", callback_data="Zmos352 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 29", callback_data="Zmos353 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 30", callback_data="Zmos354 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 31", callback_data="Zmos355 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 32", callback_data="Zmos356 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 33", callback_data="Zmos357 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 34", callback_data="Zmos358 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 35", callback_data="Zmos359 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 36", callback_data="Zmos360 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 37", callback_data="Zmos361 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 38", callback_data="Zmos362 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 39", callback_data="Zmos363 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 40", callback_data="Zmos364 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 41", callback_data="Zmos365 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 42", callback_data="Zmos366 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 43", callback_data="Zmos367 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 44", callback_data="Zmos368 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 45", callback_data="Zmos369 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 46", callback_data="Zmos370 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 47", callback_data="Zmos371 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 48", callback_data="Zmos372 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 49", callback_data="Zmos373 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 50", callback_data="Zmos374 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 51", callback_data="Zmos375 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 52", callback_data="Zmos376 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 53", callback_data="Zmos377 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 54", callback_data="Zmos378 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 55", callback_data="Zmos379 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 56", callback_data="Zmos380 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 57", callback_data="Zmos381 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 58", callback_data="Zmos382 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 59", callback_data="Zmos383 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 60", callback_data="Zmos384 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="moslsl " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مسلسل 📼 6-ابو العروسة\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^toba (\\d+)$"))
async def toba(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="toba1 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="toba2 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="toba3 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="toba4 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="toba5 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="toba6 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="toba7" + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="toba8 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="toba9 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="toba10 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="toba11 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="toba12 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="toba13 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="toba14 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="toba15 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="toba16 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="toba17 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="toba18 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="toba19 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="toba20 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="toba21 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="toba22 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 23", callback_data="toba23 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 24", callback_data="toba24 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 25", callback_data="toba25 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 26", callback_data="toba26 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 27", callback_data="toba27 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 28", callback_data="toba28 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 29", callback_data="toba29 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 30", callback_data="toba30 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="moslsl " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في مسلسل 📼 5-توبه\n√", reply_markup=keyboard)
    

## link moslsl
@app.on_callback_query(filters.regex("^Zmos214 (\\d+)$"))
async def Zmos214(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/190", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos215 (\\d+)$"))
async def Zmos215(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/191", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos216 (\\d+)$"))
async def Zmos216(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/192", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos217 (\\d+)$"))
async def Zmos217(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/193", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos218 (\\d+)$"))
async def Zmos218(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/194", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos219 (\\d+)$"))
async def Zmos219(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/195", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos220 (\\d+)$"))
async def Zmos220(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/196", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos221 (\\d+)$"))
async def Zmos221(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/197", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos222 (\\d+)$"))
async def Zmos222(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/198", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos223 (\\d+)$"))
async def Zmos223(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/200", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos224 (\\d+)$"))
async def Zmos224(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/201", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos225 (\\d+)$"))
async def Zmos225(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/202", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos226 (\\d+)$"))
async def Zmos226(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/203", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos228 (\\d+)$"))
async def Zmos228(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/205", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos229 (\\d+)$"))
async def Zmos229(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/205", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos230 (\\d+)$"))
async def Zmos230(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/206", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos231 (\\d+)$"))
async def Zmos231(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/207", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos232 (\\d+)$"))
async def Zmos232(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/208", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos233 (\\d+)$"))
async def Zmos233(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/209", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos234 (\\d+)$"))
async def Zmos234(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/210", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos235 (\\d+)$"))
async def Zmos235(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/211", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos236 (\\d+)$"))
async def Zmos236(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/212", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos237 (\\d+)$"))
async def Zmos237(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/213", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos238 (\\d+)$"))
async def Zmos238(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/214", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos239 (\\d+)$"))
async def Zmos239(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/215", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos240 (\\d+)$"))
async def Zmos240(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/216", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos241 (\\d+)$"))
async def Zmos241(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/217", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos242 (\\d+)$"))
async def Zmos242(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/218", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos243 (\\d+)$"))
async def Zmos243(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/219", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos244 (\\d+)$"))
async def Zmos244(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/220", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos245 (\\d+)$"))
async def Zmos245(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/221", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos246 (\\d+)$"))
async def Zmos246(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/222", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos247 (\\d+)$"))
async def Zmos247(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/223", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos248 (\\d+)$"))
async def Zmos248(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/224", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos249 (\\d+)$"))
async def Zmos249(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/225", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos250 (\\d+)$"))
async def Zmos250(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/226", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos251 (\\d+)$"))
async def Zmos251(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/227", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos252 (\\d+)$"))
async def Zmos252(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/228", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos253 (\\d+)$"))
async def Zmos253(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/229", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos254 (\\d+)$"))
async def Zmos254(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/230", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos255 (\\d+)$"))
async def Zmos255(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/231", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos256 (\\d+)$"))
async def Zmos256(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/232", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos257 (\\d+)$"))
async def Zmos257(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/233", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos258 (\\d+)$"))
async def Zmos258(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/Musicah4/234", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos261 (\\d+)$"))
async def Zmos261(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/261", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos262 (\\d+)$"))
async def Zmos262(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/262", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos263 (\\d+)$"))
async def Zmos263(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/263", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos264 (\\d+)$"))
async def Zmos264(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/264", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos265 (\\d+)$"))
async def Zmos265(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/265", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos266 (\\d+)$"))
async def Zmos266(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/266", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos267 (\\d+)$"))
async def Zmos267(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/267", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos268 (\\d+)$"))
async def Zmos268(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/268", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos269 (\\d+)$"))
async def Zmos269(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/269", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos270 (\\d+)$"))
async def Zmos270(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/270", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos271 (\\d+)$"))
async def Zmos271(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/271", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos272 (\\d+)$"))
async def Zmos272(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/272", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos273 (\\d+)$"))
async def Zmos273(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/273", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos274 (\\d+)$"))
async def Zmos274(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/274", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos275 (\\d+)$"))
async def Zmos275(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/275", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos276 (\\d+)$"))
async def Zmos276(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/276", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos277 (\\d+)$"))
async def Zmos277(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/277", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos278 (\\d+)$"))
async def Zmos278(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/278", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos279 (\\d+)$"))
async def Zmos279(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/279", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos280 (\\d+)$"))
async def Zmos280(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/280", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos281 (\\d+)$"))
async def Zmos281(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/281", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos282 (\\d+)$"))
async def Zmos282(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/282", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos283 (\\d+)$"))
async def Zmos283(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/283", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos284 (\\d+)$"))
async def Zmos284(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/284", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos285 (\\d+)$"))
async def Zmos285(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/285", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos286 (\\d+)$"))
async def Zmos286(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/286", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos287 (\\d+)$"))
async def Zmos287(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/287", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos288 (\\d+)$"))
async def Zmos288(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/288", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos289 (\\d+)$"))
async def Zmos289(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/289", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos290 (\\d+)$"))
async def Zmos290(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/290", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos293 (\\d+)$"))
async def Zmos293(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/293", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos294 (\\d+)$"))
async def Zmos294(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/294", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos295 (\\d+)$"))
async def Zmos295(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/295", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos296 (\\d+)$"))
async def Zmos296(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/296", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos297 (\\d+)$"))
async def Zmos297(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/297", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos298 (\\d+)$"))
async def Zmos298(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/298", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos299 (\\d+)$"))
async def Zmos299(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/299", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos300 (\\d+)$"))
async def Zmos300(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/300", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos301 (\\d+)$"))
async def Zmos301(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/301", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos302 (\\d+)$"))
async def Zmos302(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/302", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos303 (\\d+)$"))
async def Zmos303(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/303", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos304 (\\d+)$"))
async def Zmos304(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/304", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos305 (\\d+)$"))
async def Zmos305(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/305", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos306 (\\d+)$"))
async def Zmos306(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/306", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos307 (\\d+)$"))
async def Zmos307(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/307", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos308 (\\d+)$"))
async def Zmos308(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/308", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos309 (\\d+)$"))
async def Zmos309(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/309", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos310 (\\d+)$"))
async def Zmos310(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/310", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos311 (\\d+)$"))
async def Zmos311(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/311", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos312 (\\d+)$"))
async def Zmos312(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/312", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos313 (\\d+)$"))
async def Zmos313(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/313", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos314 (\\d+)$"))
async def Zmos314(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/314", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos315 (\\d+)$"))
async def Zmos315(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/315", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos316 (\\d+)$"))
async def Zmos316(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/316", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos317 (\\d+)$"))
async def Zmos317(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/317", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos318 (\\d+)$"))
async def Zmos318(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/318", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos319 (\\d+)$"))
async def Zmos319(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/319", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos320 (\\d+)$"))
async def Zmos320(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/320", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos321 (\\d+)$"))
async def Zmos321(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/321", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos322 (\\d+)$"))
async def Zmos322(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/322", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos325 (\\d+)$"))
async def Zmos325(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/325", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos326 (\\d+)$"))
async def Zmos326(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/326", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos327 (\\d+)$"))
async def Zmos327(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/327", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos328 (\\d+)$"))
async def Zmos328(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/328", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos329 (\\d+)$"))
async def Zmos329(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/329", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos330 (\\d+)$"))
async def Zmos330(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/330", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos331 (\\d+)$"))
async def Zmos331(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/331", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos332 (\\d+)$"))
async def Zmos332(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/332", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos333 (\\d+)$"))
async def Zmos333(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/333", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos334 (\\d+)$"))
async def Zmos334(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/334", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos335 (\\d+)$"))
async def Zmos335(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/335", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos336 (\\d+)$"))
async def Zmos336(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/336", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos337 (\\d+)$"))
async def Zmos337(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/337", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos338 (\\d+)$"))
async def Zmos338(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/338", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos339 (\\d+)$"))
async def Zmos339(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/339", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos340 (\\d+)$"))
async def Zmos340(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/340", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos341 (\\d+)$"))
async def Zmos341(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/341", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos342 (\\d+)$"))
async def Zmos342(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/342", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos343 (\\d+)$"))
async def Zmos343(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/343", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos344 (\\d+)$"))
async def Zmos344(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/344", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos345 (\\d+)$"))
async def Zmos345(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/345", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos346 (\\d+)$"))
async def Zmos346(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/346", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos347 (\\d+)$"))
async def Zmos347(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/347", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos348 (\\d+)$"))
async def Zmos348(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/348", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos349 (\\d+)$"))
async def Zmos349(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/349", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos350 (\\d+)$"))
async def Zmos350(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/350", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos351 (\\d+)$"))
async def Zmos351(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/351", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos352 (\\d+)$"))
async def Zmos352(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/352", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos353 (\\d+)$"))
async def Zmos353(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/353", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos354 (\\d+)$"))
async def Zmos354(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/354", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos355 (\\d+)$"))
async def Zmos355(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/355", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos356 (\\d+)$"))
async def Zmos356(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/356", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos357 (\\d+)$"))
async def Zmos357(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/357", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos358 (\\d+)$"))
async def Zmos358(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/358", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos359 (\\d+)$"))
async def Zmos359(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/359", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos360 (\\d+)$"))
async def Zmos360(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/360", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos361 (\\d+)$"))
async def Zmos361(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/361", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos362 (\\d+)$"))
async def Zmos362(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/362", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos363 (\\d+)$"))
async def Zmos363(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/363", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos364 (\\d+)$"))
async def Zmos364(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/364", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos365 (\\d+)$"))
async def Zmos365(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/365", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos366 (\\d+)$"))
async def Zmos366(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/366", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos367 (\\d+)$"))
async def Zmos367(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/367", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos368 (\\d+)$"))
async def Zmos368(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/368", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos369 (\\d+)$"))
async def Zmos369(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/369", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos370 (\\d+)$"))
async def Zmos370(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/370", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos371 (\\d+)$"))
async def Zmos371(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/371", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos372 (\\d+)$"))
async def Zmos372(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/372", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos373 (\\d+)$"))
async def Zmos373(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/373", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos374 (\\d+)$"))
async def Zmos374(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/374", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos375 (\\d+)$"))
async def Zmos375(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/375", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos376 (\\d+)$"))
async def Zmos376(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/376", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos377 (\\d+)$"))
async def Zmos377(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/377", reply_to_message_id=mid)

    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/381", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos382 (\\d+)$"))
async def Zmos382(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/382", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos383 (\\d+)$"))
async def Zmos383(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/383", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmos384 (\\d+)$"))
async def Zmos384(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/384", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^toba1 (\\d+)$"))
async def toba1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/7", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba2 (\\d+)$"))
async def toba2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/8", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba3 (\\d+)$"))
async def toba3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/9", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba4 (\\d+)$"))
async def toba4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/10", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba5 (\\d+)$"))
async def toba5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/11", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba6 (\\d+)$"))
async def toba6(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/12", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba7 (\\d+)$"))
async def toba7(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/13", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba8 (\\d+)$"))
async def toba8(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/14", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba9 (\\d+)$"))
async def toba9(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/15", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba10 (\\d+)$"))
async def toba10(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/16", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba11 (\\d+)$"))
async def toba11(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/17", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba12 (\\d+)$"))
async def toba12(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/18", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba13 (\\d+)$"))
async def toba13(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/19", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba14 (\\d+)$"))
async def toba14(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/20", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba15 (\\d+)$"))
async def toba15(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/21", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba16 (\\d+)$"))
async def toba16(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/22", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba17 (\\d+)$"))
async def toba17(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/23", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba18 (\\d+)$"))
async def toba18(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/24", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba19 (\\d+)$"))
async def toba19(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/25", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba20 (\\d+)$"))
async def toba20(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/26", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba21 (\\d+)$"))
async def toba21(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/27", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba22 (\\d+)$"))
async def toba22(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/28", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba23 (\\d+)$"))
async def toba23(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/29", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba24 (\\d+)$"))
async def toba24(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/30", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba25 (\\d+)$"))
async def toba25(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/31", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba26 (\\d+)$"))
async def toba26(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/32", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba27 (\\d+)$"))
async def toba27(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/33", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba28 (\\d+)$"))
async def toba28(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/34", reply_to_message_id=mid)
   
  
 
@app.on_callback_query(filters.regex("^toba29 (\\d+)$"))
async def toba29(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/35", reply_to_message_id=mid)
   
  
@app.on_callback_query(filters.regex("^toba30 (\\d+)$"))
async def toba30(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/FFMMTTFF/36", reply_to_message_id=mid)
   
   
#########################################################################################
#########################################################################################
#########################         # END Moslsl AR #            ##########################
#########################################################################################
#########################################################################################


#########################################################################################
#########################################################################################
#########################         # Start msrahia AR #        ##########################
#########################################################################################
#########################################################################################


#########################################################################################
#########################################################################################
#########################         # Msrh Masr #               ##########################
#########################################################################################
#########################################################################################

@app.on_callback_query(filters.regex("^msrahia (\\d+)$"))
async def msrahia(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("🎭 1- مسرح مصر", callback_data="Xms1 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="aflamAR2 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة المسرحيات العربيه\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xms1 (\\d+)$"))
async def Xms1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("الجزء الأول 🎭", callback_data="Xmsrh1 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("الجزء الثاني 🎭", callback_data="Xmsrh2 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("الجزء الثالث 🎭", callback_data="Xmsrh3 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("الجزء الرابع 🎭", callback_data="Xmsrh4 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("الجزء الخامس 🎭", callback_data="Xmsrh5 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="msrahia " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمة اجزاء مسرح مصر\n√", reply_markup=keyboard)


@app.on_callback_query(filters.regex("^Xmsrh1 (\\d+)$"))
async def Xmsrh1(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmsrh388 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmsrh389 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmsrh390 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmsrh391 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmsrh392 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmsrh393 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmsrh394 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmsrh395 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmsrh396 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmsrh397 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmsrh398 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmsrh399 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmsrh400 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmsrh401 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmsrh402 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmsrh403 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmsrh404 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="Xms1 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمه 🔘 | روايات والقصص |\n√", reply_markup=keyboard)
    return


@app.on_callback_query(filters.regex("^Xmsrh2 (\\d+)$"))
async def Xmsrh2(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmsrh406 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmsrh407 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmsrh408 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmsrh409 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmsrh410 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmsrh411 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmsrh412 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmsrh413 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmsrh414 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmsrh415 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmsrh416 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmsrh417 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmsrh418 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmsrh419 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="Xms1 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمه 🔘 | روايات والقصص |\n√", reply_markup=keyboard)
    return


@app.on_callback_query(filters.regex("^Xmsrh3 (\\d+)$"))
async def Xmsrh3(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmsrh421 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmsrh422 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmsrh423 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmsrh424 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmsrh425 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmsrh426 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmsrh427 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmsrh428 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmsrh429 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmsrh430 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmsrh431 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmsrh432 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmsrh433 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmsrh434 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmsrh435 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmsrh436 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmsrh437 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="Zmsrh438 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="Zmsrh439 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="Zmsrh440 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="Zmsrh441 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="Zmsrh442 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="Xms1 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمه 🔘 | روايات والقصص |\n√", reply_markup=keyboard)
    return


@app.on_callback_query(filters.regex("^Xmsrh4 (\\d+)$"))
async def Xmsrh4(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmsrh444 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmsrh445 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmsrh446 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmsrh447 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmsrh448 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmsrh449 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmsrh450 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmsrh451 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmsrh452 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmsrh453 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmsrh454 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmsrh455 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmsrh456 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="Xms1 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمه 🔘 | روايات والقصص |\n√", reply_markup=keyboard)
    return


@app.on_callback_query(filters.regex("^Xmsrh5 (\\d+)$"))
async def Xmsrh5(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    keyboard = InlineKeyboardMarkup(inline_keyboard=[

        [InlineKeyboardButton("⌯ الحلقة 1", callback_data="Zmsrh467 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 2", callback_data="Zmsrh468 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 3", callback_data="Zmsrh469 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 4", callback_data="Zmsrh470 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 5", callback_data="Zmsrh471 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 6", callback_data="Zmsrh472 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 7", callback_data="Zmsrh473 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 8", callback_data="Zmsrh474 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 9", callback_data="Zmsrh475 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 10", callback_data="Zmsrh476 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 11", callback_data="Zmsrh477 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 12", callback_data="Zmsrh478 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 13", callback_data="Zmsrh479 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 14", callback_data="Zmsrh480 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 15", callback_data="Zmsrh481 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 16", callback_data="Zmsrh482 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 17", callback_data="Zmsrh483 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 18", callback_data="Zmsrh484 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 19", callback_data="Zmsrh485 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 20", callback_data="Zmsrh486 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌯ الحلقة 21", callback_data="Zmsrh487 " + (https://t.me/lV_P_Nl))] +
        [InlineKeyboardButton("⌯ الحلقة 22", callback_data="Zmsrh488 " + (https://t.me/lV_P_Nl))],

        [InlineKeyboardButton("𝐖𝐇𝐈𝐒𝐊𝐄𝐘", callback_data="Xms1 " + (https://t.me/lV_P_Nl))],
        [InlineKeyboardButton("⌞ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀⌝⚡", url=f"https://t.me/lN_B_Fl")],

    ])
    await m.message.edit_text("◍ اهلا بيك في قائمه 🔘 | روايات والقصص |\n√", reply_markup=keyboard)
    return


# link msrh
@app.on_callback_query(filters.regex("^Zmsrh388 (\\d+)$"))
async def Zmsrh388(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/388", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh389 (\\d+)$"))
async def Zmsrh389(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/389", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh390 (\\d+)$"))
async def Zmsrh390(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/390", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh391 (\\d+)$"))
async def Zmsrh391(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/391", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh392 (\\d+)$"))
async def Zmsrh392(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/392", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh393 (\\d+)$"))
async def Zmsrh393(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/393", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh394 (\\d+)$"))
async def Zmsrh394(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/394", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh395 (\\d+)$"))
async def Zmsrh395(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/395", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh396 (\\d+)$"))
async def Zmsrh396(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/396", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh397 (\\d+)$"))
async def Zmsrh397(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/397", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh398 (\\d+)$"))
async def Zmsrh398(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/398", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh399 (\\d+)$"))
async def Zmsrh399(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/399", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh400 (\\d+)$"))
async def Zmsrh400(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/400", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh401 (\\d+)$"))
async def Zmsrh401(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/401", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh402 (\\d+)$"))
async def Zmsrh402(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/402", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh403 (\\d+)$"))
async def Zmsrh403(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/403", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh404 (\\d+)$"))
async def Zmsrh404(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/404", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh406 (\\d+)$"))
async def Zmsrh406(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/406", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh407 (\\d+)$"))
async def Zmsrh407(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/407", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh408 (\\d+)$"))
async def Zmsrh408(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/408", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh409 (\\d+)$"))
async def Zmsrh409(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/409", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh410 (\\d+)$"))
async def Zmsrh410(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/410", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh411 (\\d+)$"))
async def Zmsrh411(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/411", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh412 (\\d+)$"))
async def Zmsrh412(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/412", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh413 (\\d+)$"))
async def Zmsrh413(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/413", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh414 (\\d+)$"))
async def Zmsrh414(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/414", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh415 (\\d+)$"))
async def Zmsrh415(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/415", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh416 (\\d+)$"))
async def Zmsrh416(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/416", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh417 (\\d+)$"))
async def Zmsrh417(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/417", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh418 (\\d+)$"))
async def Zmsrh418(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/418", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh419 (\\d+)$"))
async def Zmsrh419(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/419", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh421 (\\d+)$"))
async def Zmsrh421(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/421", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh422 (\\d+)$"))
async def Zmsrh422(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/422", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh423 (\\d+)$"))
async def Zmsrh423(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/423", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh424 (\\d+)$"))
async def Zmsrh424(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/424", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh425 (\\d+)$"))
async def Zmsrh425(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/425", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh426 (\\d+)$"))
async def Zmsrh426(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/426", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh427 (\\d+)$"))
async def Zmsrh427(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/427", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh428 (\\d+)$"))
async def Zmsrh428(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/428", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh429 (\\d+)$"))
async def Zmsrh429(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/429", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh430 (\\d+)$"))
async def Zmsrh430(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/430", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh431 (\\d+)$"))
async def Zmsrh431(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/431", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh432 (\\d+)$"))
async def Zmsrh432(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/432", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh433 (\\d+)$"))
async def Zmsrh433(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/433", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh434 (\\d+)$"))
async def Zmsrh434(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/434", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh435 (\\d+)$"))
async def Zmsrh435(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/435", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh436 (\\d+)$"))
async def Zmsrh436(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/436", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh437 (\\d+)$"))
async def Zmsrh437(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/437", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh438 (\\d+)$"))
async def Zmsrh438(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/438", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh439 (\\d+)$"))
async def Zmsrh439(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/439", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh440 (\\d+)$"))
async def Zmsrh440(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/440", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh441 (\\d+)$"))
async def Zmsrh441(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/441", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh442 (\\d+)$"))
async def Zmsrh442(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/442", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh444 (\\d+)$"))
async def Zmsrh444(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/444", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh445 (\\d+)$"))
async def Zmsrh445(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/445", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh446 (\\d+)$"))
async def Zmsrh446(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/446", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh447 (\\d+)$"))
async def Zmsrh447(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/447", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh448 (\\d+)$"))
async def Zmsrh448(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/448", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh449 (\\d+)$"))
async def Zmsrh449(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/449", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh450 (\\d+)$"))
async def Zmsrh450(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/450", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh451 (\\d+)$"))
async def Zmsrh451(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/451", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh452 (\\d+)$"))
async def Zmsrh452(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/452", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh453 (\\d+)$"))
async def Zmsrh453(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/453", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh454 (\\d+)$"))
async def Zmsrh454(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/454", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh455 (\\d+)$"))
async def Zmsrh455(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/455", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh456 (\\d+)$"))
async def Zmsrh456(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/456", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh467 (\\d+)$"))
async def Zmsrh467(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/467", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh468 (\\d+)$"))
async def Zmsrh468(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/468", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh469 (\\d+)$"))
async def Zmsrh469(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/469", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh470 (\\d+)$"))
async def Zmsrh470(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/470", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh471 (\\d+)$"))
async def Zmsrh471(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/471", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh472 (\\d+)$"))
async def Zmsrh472(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/472", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh473 (\\d+)$"))
async def Zmsrh473(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/473", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh474 (\\d+)$"))
async def Zmsrh474(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/474", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh475 (\\d+)$"))
async def Zmsrh475(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/475", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh476 (\\d+)$"))
async def Zmsrh476(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/476", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh477 (\\d+)$"))
async def Zmsrh477(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/477", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh478 (\\d+)$"))
async def Zmsrh478(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/478", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh479 (\\d+)$"))
async def Zmsrh479(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/479", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh480 (\\d+)$"))
async def Zmsrh480(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/480", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh481 (\\d+)$"))
async def Zmsrh481(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/481", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh482 (\\d+)$"))
async def Zmsrh482(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/482", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh483 (\\d+)$"))
async def Zmsrh483(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/483", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh484 (\\d+)$"))
async def Zmsrh484(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/484", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh485 (\\d+)$"))
async def Zmsrh485(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/485", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh486 (\\d+)$"))
async def Zmsrh486(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/486", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh487 (\\d+)$"))
async def Zmsrh487(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/487", reply_to_message_id=mid)


@app.on_callback_query(filters.regex("^Zmsrh488 (\\d+)$"))
async def Zmsrh488(c: Client, m: CallbackQuery):
    a = m.data.split(" ")
    if m.from_user.id != int(a[1]):
        await c.answer_callback_query(m.id, text="صاحب الامر هو فقط من يستطيع الضغط على الزر 🖤🙂", show_alert=True)
        return
    await m.message.delete()
    await m.message.reply_audio("https://t.me/UMoslsl/488", reply_to_message_id=mid)

#########################################################################################
#########################################################################################
#########################         # END masrahia AR #          ##########################
#########################################################################################
#########################################################################################
