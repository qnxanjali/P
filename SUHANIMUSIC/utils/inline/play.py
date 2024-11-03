import math

from pyrogram.types import InlineKeyboardButton

from SUHANIMUSIC.utils.formatters import seconds_to_min


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


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = seconds_to_min(played)
    duration_sec = seconds_to_min(dur)
    percentage = (played_sec / duration_sec) * 200
    umm = math.floor(percentage)
    if 0 < umm <= 15:
        bar = "ᴘ——————————————"
    elif 15 < umm < 30:
        bar = "ᴘʀ—————————————"
    elif 30 <= umm < 45:
        bar = "ᴘʀᴀ————————————"
    elif 45 <= umm < 60:
        bar = "ᴘʀᴀᴛ———————————"
    elif 60 <= umm < 75:
        bar = "ᴘʀᴀᴛᴀ——————————"
    elif 75 <= umm < 90:
        bar = "ᴘʀᴀᴛᴀᴘ—————————"
    elif 90 <= umm < 105:
        bar = "ᴘʀᴀᴛᴀᴘ—————————"
    elif 105 <= umm < 120:
        bar = "ᴘʀᴀᴛᴀᴘ—♡———————"
    elif 120 <= umm < 135:
        bar = "ᴘʀᴀᴛᴀᴘ—♡—s—————"
    elif 135 <= umm < 150:
        bar = "ᴘʀᴀᴛᴀᴘ—♡—sᴜ————"
    elif 150 <= umm < 165:
        bar = "ᴘʀᴀᴛᴀᴘ—♡—sᴜʜ———"
    elif 165 <= umm < 180:    
        bar = "ᴘʀᴀᴛᴀᴘ—♡—sᴜʜᴀ——"
    elif 180 <= umm < 195:
        bar = "ᴘʀᴀᴛᴀᴘ—♡—sᴜʜᴀɴ—"
    else:    
        bar = "ᴘʀᴀᴛᴀᴘ—♡—sᴜʜᴀɴɪ"
    
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [   
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="Ⅱ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="♡", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="🛑", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [ InlineKeyboardButton(text="ᴍᴀsᴛɪ ᴋɪ ʙᴀsᴛɪ", url=f"https://t.me/+b1gc4qrvfLZlNGI1")],
    ]
    
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="Ⅱ", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="♡", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="⏭", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="🛑", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
        [ InlineKeyboardButton(text="ᴍᴀsᴛɪ ᴋɪ ʙᴀsᴛɪ", url=f"https://t.me/+b1gc4qrvfLZlNGI1")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"AnonyPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


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
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
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
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
