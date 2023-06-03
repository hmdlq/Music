from pyrogram.types import InlineKeyboardButton
import config

def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⌞ ⩹━⊷⌯ 𓏺َِ᥉َِ᥆َِꪊَِᖇَِᥴُِ꧖ َِ᥉َِρُِꪖَِᖇَِᥴُِƙَِ⌝", url=f"https://t.me/ZZZ7iZ",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons
