
import math

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from AnonX.utils.formatters import time_to_seconds


## After Edits with Timer Bar

def stream_markup_timer(_, videoid, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
    if 0 < anon <= 10:
        bar = "11”12”13”14”15”16”17”18”19”"
    elif 10 < anon < 20:
        bar = "21”22”23”24”25”26”27”28”29”"
    elif 20 <= anon < 30:
        bar = "31”32”33”34”35”36”37”38”39”"
    elif 30 <= anon < 40:
        bar = "41”42”23”24”25”26”27”28”29”"
    elif 40 <= anon < 50:
        bar = "51”52”53”54”55”56”57”58”59”"
    elif 50 <= anon < 60:
        bar = "61”62”63”64”65”66”67”68”69”"
    elif 60 <= anon < 70:
        bar = "71”72”73”74”75”76”77”78”79”"
    elif 70 <= anon < 80:
        bar = "81”82”83”84”85”86”87”88”89”"
    elif 80 <= anon < 95:
        bar = "91”92”93”94”95”96”97”98”99”"
    else:
        bar = "100”101”102”103”104”105”106”107”108”"
 buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="استئناف",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="ايقاف مؤقت", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="تشغيل", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="تخطي", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ايقاف", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀", url=f"https://t.me/lN_B_Fl"
            )
        ],
        [
            InlineKeyboardButton(
                text="مسح القائمه", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    anon = math.floor(percentage)
        bar = "11”12”13”14”15”16”17”18”19”"
    elif 10 < anon < 20:
        bar = "21”22”23”24”25”26”27”28”29”"
    elif 20 <= anon < 30:
        bar = "31”32”33”34”35”36”37”38”39”"
    elif 30 <= anon < 40:
        bar = "41”42”23”24”25”26”27”28”29”"
    elif 40 <= anon < 50:
        bar = "51”52”53”54”55”56”57”58”59”"
    elif 50 <= anon < 60:
        bar = "61”62”63”64”65”66”67”68”69”"
    elif 60 <= anon < 70:
        bar = "71”72”73”74”75”76”77”78”79”"
    elif 70 <= anon < 80:
        bar = "81”82”83”84”85”86”87”88”89”"
    elif 80 <= anon < 95:
        bar = "91”92”93”94”95”96”97”98”99”"
    else:
        bar = "100”101”102”103”104”105”106”107”108”"

    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text="استئناف",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="ايقاف مؤقت", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="تخطي", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ايقاف", callback_data=f"ADMIN Stop|{chat_id}"

),
        ],
        [
            InlineKeyboardButton(
                text="𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀", url=f"https://t.me/lN_B_Fl"
            )
        ],
        [
            InlineKeyboardButton(
                text="استئناف", callback_data=f"close"
            )
        ],
    ]
    return buttons


def stream_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="استئناف",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="ايقاف مؤقت", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="تشغيل", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="تخطي", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ايقاف", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀", url=f"https://t.me/lN_B_Fl"
            )
        ],
        [
            InlineKeyboardButton(
                text="مسح القائمه", callback_data=f"close"
            )
        ],
    ]
    return buttons


def telegram_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="استئناف",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="ايقاف مؤقت", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="تخطي", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ايقاف", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀", url=f"https://t.me/lN_B_Fl"
            )
        ],
        [
            InlineKeyboardButton(
                text="مسح القائمه", callback_data=f"close"
            )
        ],
    ]
    return buttons


## Search Query Inline


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons

## Live Stream Markup


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSEMENU_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ]
    ]
    return buttons

## wtf

def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],

callback_data=f"AnonPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"{config.SUPPORT_GROUP}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


## Slider Query Markup


def slider_markup(
    _, videoid, user_id, query, query_type, channel, fplay
):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ايقاف   ",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="مسح القائمه",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons

## Extra Shit

close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        text="مسح القائمه", callback_data="close"
                    )
                ]    
            ]
        )


## Queue Markup

def queue_markup(_, videoid, chat_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="استئناف",
                callback_data=f"ADMIN Resume|{chat_id}",
            ),
            InlineKeyboardButton(
                text="ايقاف مؤقت", callback_data=f"ADMIN Pause|{chat_id}"
            ),
            InlineKeyboardButton(
                text="تشغيل", callback_data=f"add_playlist {videoid}"
            ),
            InlineKeyboardButton(
                text="تخطي", callback_data=f"ADMIN Skip|{chat_id}"
            ),
            InlineKeyboardButton(
                text="ايقاف", callback_data=f"ADMIN Stop|{chat_id}"
            ),
        ],
        [
            InlineKeyboardButton(
                text="𝐒𝐎𝐔𝐑𝐂𝐄 𝐇𝐀𝐘𝐀", url=f"https://t.me/lN_B_Fl"
            )
        ],
        [
            InlineKeyboardButton(
                text="مسح القائمه", callback_data=f"close"
            )
        ],
    ]
    return buttons