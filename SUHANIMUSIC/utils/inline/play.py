import math

from pyrogram.types import InlineKeyboardButton

from SUHANIMUSIC.utils.formatters import time_to_seconds


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
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    umm = math.floor(percentage)
    if 0 < umm <= 8:
        bar = "ᴘ————————————"
    elif 8 < umm < 16:
        bar = "ᴘʀ———————————"
    elif 16 <= umm < 24:
        bar = "ᴘʀᴀ——————————"
    elif 24 <= umm < 32:
        bar = "ᴘʀᴀᴛ—————————"
    elif 32 <= umm < 40:
        bar = "ᴘʀᴀᴛᴀ————————"
    elif 40 <= umm < 48:
        bar = "ᴘʀᴀᴛᴀᴘ———————"
    elif 48 <= umm < 56:
        bar = "ᴘʀᴀᴛᴀᴘ♡゙——————"
    elif 56 <= umm < 64:
        bar = "ᴘʀᴀᴛᴀᴘ♡゙s—————"
    elif 64 <= umm < 72:
        bar = "ᴘʀᴀᴛᴀᴘ♡゙sᴜ————"
    elif 72 <= umm < 80:
        bar = "ᴘʀᴀᴛᴀᴘ♡゙sᴜʜ———"
    elif 80 <= umm < 85:
        bar = "ᴘʀᴀᴛᴀᴘ♡゙sᴜʜᴀ——"
    elif 85 <= umm < 95:    
        bar = "ᴘʀᴀᴛᴀᴘ♡゙sᴜʜᴀɴ—"
        else:
        bar = "ᴘʀᴀᴛᴀᴘ♡゙sᴜʜᴀɴɪ"
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
