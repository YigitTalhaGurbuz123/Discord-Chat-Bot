# bot_logic in original

import random


def sifre_olusturucu(sifre_uzunlugu):
    ogeler = "+-/*!&$#?=@<>"
    sifre = ""

    for i in range(sifre_uzunlugu):
        sifre += random.choice(ogeler)

    return sifre


def emoji_olusturucu():
    emoji = ["\U0001f600", "\U0001f642", "\U0001F606", "\U0001F923"]
    return random.choice(emoji)


def yazi_tura():
    para = random.randint(0, 1)
    if para == 0:
        return "YAZI"
    else:
        return "TURA"
        
def parak():
    secim = random.randint(0, 1)
    if secim == 0:
        return "YAZI"
    else:
        return "TURA"

def ayni():
    if parak() == yazi_tura():
        return "Ben kazandım!"
    else:
        return "Sen kazandın!"
    
def tahmin():
    tahminim = random.randint(0,10)
    return tahminim

