import discord
from discord.ext import commands
import random
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command(name="evde_yap")
async def evde_yap(ctx):
    ideas = [
        "Eski botundan saksı yapabilirsiniz.",
        "Plastik kapaklardan küçük süs eşyaları yapabilirsiniz.",
        "Karton koliler kullanarak saklama kutusu yapabilirsiniz.",
        "Plastik kaşık ve çatallardan dekoratif çerçeveler oluşturabilirsiniz."
    ]
    await ctx.send(f"İşte bir evde yap fikri: {random.choice(ideas)}")
@bot.command(name="YOK_OLMA_SURELERI")
async def YOK_OLMA_SURELERI(ctx):
    ideas = [
        "Strafor 5000 yıl - 2 Milyon yıl.",
        "Cam Şişe 4000 yıl.",
        "Plastik 1000 yıl.",
        "Kağıt gazete 3 ay.",
        "Poliüretan (Sentetik fiberler, yapıştırıcılar, halıların alt kısmı ve sert plastik contalar) 1000 yıl.",
        "Telefon Kartı 1000 yıl.",
        "Su Boruları 1000 yıl.",
        "Bebek Bezi 550 yıl.",
        "Plastik Tabak 500 yıl.",
        "Pet Şişe 400 yıl.",
        "Deterjan 400 yıl.",
        "Pil 300 yıl.",
        "Alüminyum 100 yıl.",
        "Tahta Parçaları 15 yıl.",
        "Kutu Kola 10 yıl.",
        "Çiklet 5 yıl - 25 yıl."
    ]
    await ctx.send(f"İşte bir el işi fikri: {random.choice(ideas)}")
    

bot.run("token")
