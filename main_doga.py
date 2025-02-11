import discord
import random

# İstekler değişkeni botun yetkilerini saklar
intents = discord.Intents.default()
# Mesaj okuma yetkisini etkinleştirme
intents.message_content = True
# Bir bot oluşturma ve yetkileri aktarma
client = discord.Client(intents=intents)

el_isi_fikirleri= [
    "Plastik şişelerden çiçek saksısı yapabilirsiniz",
    "Plastik bardaklardan avize yapabilirisniz",
    "Pet şişelerden ayakkabı yapımı",
    "Pet şişeleri kullarak hayvanlar içim yem yapımı",
    "Kartonlardan kedilere ev yapımı",
    "Kartonlardan futbol kupası yapımı"
]

geri_donusum_rehberi ={
    "Plastik şişe":"Geri dönüştürülebilir. Plastik atık kutusuna atın.",
    "cam":"Geri dönüştürülebilir. Cam atık kutusuna atın.",
    "karton":"Geri dönüştürülebilir. Karton atık kutusuna atın.",
    "metal":"Geri dönüştürülebilir. Metal atık kutusuna atın.",
    "yag":"Geri dönüştürülebilir. Yağ atık kutusuna atın.",
    "pil":"Geri dönüştürülebilir. Pil atık kutusuna atın."
}

ayrisma_sureleri ={
    "plastik": "450 yıl",
    "cam": " 4000 yıl",
    "karton":"12 yıl"
}

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yapıldı')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Merhaba!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$nasılsın'):
         await message.channel.send("iyiyim")

    elif message.content.startswith("$elisi"):
        fikir= random.choice(el_isi_fikirleri)
        await message.channel.send(f"El İşi Fikri: {fikir}")
    
    elif message.content.startswith("$geri"):
        item = message.content[len("$geri "):].lower()
        if item in geri_donusum_rehberi:
            await message.channel.send(geri_donusum_rehberi[item])
        else:
             await message.channel.send("Anladığımdan emin değilim, rehbere bak lütfen..")

    elif message.content.startswith("$ayrisma"):
        item = message.content[len("$ayrisma "):].lower()
        if item in ayrisma_sureleri:
            await message.channel.send(ayrisma_sureleri[item])
        else:
             await message.channel.send("Yanlış bilgi yazdınız lütfen tekrar deneyiniz..")
    else:
        await message.channel.send("Kelimelere başlamdan once dolar işaretini unutma: Lütfen `$hello`, `$bye`, `$nasılsın`, `$elisi`, `$geri [öğe]`, `$ayrisma [öğe]` gibi komutlar kullanın.")

client.run("token")
