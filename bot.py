import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
def rozroznij(nazwa: str):
    if nazwa in ("butelka", "pudelka sniadaniowe", "klawiatura", "slomka", "pilka", "plastikowy wieszak"):
        rodzaj = "plastik"
    elif nazwa in ("puszka", "kola zebate", "sztuczce"):
        rodzaj = "metal"
    elif nazwa in ("karton", "zeszyt"):
        rodzaj = "papier"
    elif nazwa in ("sloik", "szyba", "butelka szklana"):
        rodzaj = "szklo"
    else:
        rodzaj = "nieznany"

    komunikat = decyduj(rodzaj, nazwa)
    return komunikat

def decyduj(smiec: str, nazwa: str):
    if smiec == "plastik":
        return(f"{nazwa} sie rozklada od 100 do nawet 1000 lat")
    elif smiec == "metal":
        return(f"{nazwa} sie rozklada od kilkunastu lat do nawet 200-300 lat")
    elif smiec == "papier":
        return(f"{nazwa} sie rozklada od kilku tygodni do 6 miesiecy")
    elif smiec == "szklo":
        return(f"{nazwa} sie rozklada od 2 tysiecy lat do 4 tysiecy")
    else:
        return(f"nie rozpoznaje przedmiotu: {nazwa}")

@bot.command()
async def recykling(ctx, *args):

    lista_smieci = list(args)

    for smiec in lista_smieci:
        rozklad = rozroznij(smiec)
        await ctx.send(rozklad)

    


bot.run("token")
