import discord
import time
# import * - kütüphanedeki tüm dosyaları içe aktarmanın hızlı bir yoludur
from bot_mantik import sifre_olusturucu, emoji_olusturucu, parak, yazi_tura, ayni, tahmin


# ayricaliklar (intents) değişkeni botun ayrıcalıklarını depolayacak
intents = discord.Intents.default()
# Mesajları okuma ayrıcalığını etkinleştirelim
intents.message_content = True
# istemci (client) değişkeniyle bir bot oluşturalım ve ayrıcalıkları ona aktaralım
client = discord.Client(intents=intents)


# Bot hazır olduğunda adını yazdıracak!
@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')


# Bot bir mesaj aldığında, aynı kanalda mesaj gönderecek!
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('$ merhaba') or message.content.startswith('$ Merhaba'):
        await message.channel.send('Selam!')

    elif message.content.startswith('$ nasılsın')or message.content.startswith('$ Nasılsın'):
        await message.channel.send('İyiyim! Peki ya sen?')

    elif message.content.startswith('$ bende iyiyim') or message.content.startswith('$ Bende iyiyim'):
        await message.channel.send('Çok mutlu oldum!')

    elif message.content.startswith('$ ben kötüyüm') or message.content.startswith('$ Ben kötüyüm'):
        await message.channel.send('Çok üzüldüm! Hasta isen geçmiş olsun!')

    elif message.content.startswith('$ teşekkürler') or message.content.startswith('$ teşekkürler'):
        await message.channel.send('Rica ederim!')

    elif message.content.startswith('$ teşekkür ederim') or message.content.startswith('$ teşekkür ederim'):
        await message.channel.send('Rica ederim!')

    elif message.content.startswith('$ doğru') or message.content.startswith('$ Doğru'):
        await message.channel.send('Demek tahminim tam tutmuş!')

    elif message.content.startswith('$ Yanlış') or message.content.startswith('$ yanlış'):
        await message.channel.send("Üzgünüm! bir dahakine doğru tahmin edeceğim")

    elif message.content.startswith('$ soru sor') or message.content.startswith('$ Soru sor'):
        await message.channel.send("Tamam! ama soruyu doğru vevaplamadan sana cevap vermeyeceğim!")
        time.sleep(1)
        await message.channel.send("3 × 5 kaç eder?")
    elif message.content.startswith('$ 15'):
        await message.channel.send("Doğru cevap! Tebrikler!, yeni soru: 5 × 5 kaç eder?")
    elif message.content.startswith('$ 25'):
        await message.channel.send("Doğru cevap! Tebrikler!, yeni soru: 1 + 100 kaç eder?")
    elif message.content.startswith('$ 101'):
        await message.channel.send("Doğru cevap! Tebrikler!, yeni soru: 1000 - 1 kaç eder?")
    elif message.content.startswith('$ 999'):
        await message.channel.send("Doğru cevap! Tebrikler!, yeni soru: 2 + 0 kaç eder?")
    elif message.content.startswith('$ 2'):
        await message.channel.send("Yoruldum! Sende hepsini biliyorsun! :D Artık ben soru sormayacağım!")

    elif message.content.startswith('$ emoji') or message.content.startswith('$ Emoji'):
        await message.channel.send(emoji_olusturucu())

    elif message.content.startswith('$ tahmin') or message.content.startswith('$ Tahmin'):
        await message.channel.send("1 ile 10 arasında bir sayı tut!")
        time.sleep(3)
        await message.channel.send("Umarım doğru tahmin ederim!")
        time.sleep(2)
        await message.channel.send("Tahminim:")
        await message.channel.send(tahmin())
        await message.channel.send("Doğru mu yanlış mı?")

    elif message.content.startswith('$ görüşürüz') or message.content.startswith('$ Görüşürüz'):
        await message.channel.send("Görüşürüz!")

    elif message.content.startswith('$ yazı tura') or message.content.startswith('$ Yazı tura'):
        await message.channel.send("Benim tercihim:")
        await message.channel.send(parak())
        time.sleep(1)
        await message.channel.send("o zaman çeviriyorum...")
        time.sleep(1)
        await message.channel.send(yazi_tura())
        time.sleep(1)
        await message.channel.send(ayni())

    elif message.content.startswith('$ şifre') or message.content.startswith('$ Şifre'):
        await message.channel.send("Şifreniz:")
        await message.channel.send(sifre_olusturucu(10))


    elif message.content.startswith('$ bot ne demek') or message.content.startswith('$ Bot ne demek'):
        await message.channel.send('Bot şu demektir: \U0001f600, \U0001f642, \U0001F606, \U0001F923, \U0001F92A, \U0001F92B,\U0001f600, \U0001f642, \U0001F606, \U0001F923, \U0001F92A, \U0001F92B, \U0001f600, \U0001f642, \U0001F606, \U0001F923, \U0001F92A, \U0001F92B, \U0001f600, \U0001f642, Anladığını düşünüyorum hahahahahhahahah!')


client.run("Gizli Token!")