# By @TroJanzHEX


import os


class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6582902727:AAHfJm_jNz1i9CC86f4K82i1mWj1qdfTrJU")

    APP_ID = int(os.environ.get("APP_ID", 4682685))

    API_HASH = os.environ.get("API_HASH", "3eba5d471162181b8a3f7f5c0a23c307")

    # Get this api from https://www.remove.bg/b/background-removal-api
    RemoveBG_API = os.environ.get("RemoveBG_API", "vyXAWzTiUvEkjqrDXC2PFo6H")

    # Enable or disable private bot
    PRIVATE = False
    CHANNELS =int(os.environ.get("CHANNELS",-1001678093514))

    # Add id without @
    # if PRIVATE is True only users that are in this list are allowed to use the bot
    USERNAMES = ["", ]

    # Add your language
    LANG = "en"

    # languages
    # 'af': 'afrikaans',
    # 'sq': 'albanian',
    # 'am': 'amharic',
    # 'ar': 'arabic',
    # 'hy': 'armenian',
    # 'az': 'azerbaijani',
    # 'eu': 'basque',
    # 'be': 'belarusian',
    # 'bn': 'bengali',
    # 'bs': 'bosnian',
    # 'bg': 'bulgarian',
    # 'ca': 'catalan',
    # 'ceb': 'cebuano',
    # 'ny': 'chichewa',
    # 'zh-cn': 'chinese (simplified)',
    # 'zh-tw': 'chinese (traditional)',
    # 'co': 'corsican',
    # 'hr': 'croatian',
    # 'cs': 'czech',
    # 'da': 'danish',
    # 'nl': 'dutch',
    # 'en': 'english',
    # 'eo': 'esperanto',
    # 'et': 'estonian',
    # 'tl': 'filipino',
    # 'fi': 'finnish',
    # 'fr': 'french',
    # 'fy': 'frisian',
    # 'gl': 'galician',
    # 'ka': 'georgian',
    # 'de': 'german',
    # 'el': 'greek',
    # 'gu': 'gujarati',
    # 'ht': 'haitian creole',
    # 'ha': 'hausa',
    # 'haw': 'hawaiian',
    # 'iw': 'hebrew',
    # 'he': 'hebrew',
    # 'hi': 'hindi',
    # 'hmn': 'hmong',
    # 'hu': 'hungarian',
    # 'is': 'icelandic',
    # 'ig': 'igbo',
    # 'id': 'indonesian',
    # 'ga': 'irish',
    # 'it': 'italian',
    # 'ja': 'japanese',
    # 'jw': 'javanese',
    # 'kn': 'kannada',
    # 'kk': 'kazakh',
    # 'km': 'khmer',
    # 'ko': 'korean',
    # 'ku': 'kurdish (kurmanji)',
    # 'ky': 'kyrgyz',
    # 'lo': 'lao',
    # 'la': 'latin',
    # 'lv': 'latvian',
    # 'lt': 'lithuanian',
    # 'lb': 'luxembourgish',
    # 'mk': 'macedonian',
    # 'mg': 'malagasy',
    # 'ms': 'malay',
    # 'ml': 'malayalam',
    # 'mt': 'maltese',
    # 'mi': 'maori',
    # 'mr': 'marathi',
    # 'mn': 'mongolian',
    # 'my': 'myanmar (burmese)',
    # 'ne': 'nepali',
    # 'no': 'norwegian',
    # 'or': 'odia',
    # 'ps': 'pashto',
    # 'fa': 'persian',
    # 'pl': 'polish',
    # 'pt': 'portuguese',
    # 'pa': 'punjabi',
    # 'ro': 'romanian',
    # 'ru': 'russian',
    # 'sm': 'samoan',
    # 'gd': 'scots gaelic',
    # 'sr': 'serbian',
    # 'st': 'sesotho',
    # 'sn': 'shona',
    # 'sd': 'sindhi',
    # 'si': 'sinhala',
    # 'sk': 'slovak',
    # 'sl': 'slovenian',
    # 'so': 'somali',
    # 'es': 'spanish',
    # 'su': 'sundanese',
    # 'sw': 'swahili',
    # 'sv': 'swedish',
    # 'tg': 'tajik',
    # 'ta': 'tamil',
    # 'te': 'telugu',
    # 'th': 'thai',
    # 'tr': 'turkish',
    # 'uk': 'ukrainian',
    # 'ur': 'urdu',
    # 'ug': 'uyghur',
    # 'uz': 'uzbek',
    # 'vi': 'vietnamese',
    # 'cy': 'welsh',
    # 'xh': 'xhosa',
    # 'yi': 'yiddish',
    # 'yo': 'yoruba',
    # 'zu': 'zulu',


