import discord
from discord.ext import commands
from controlador.controlador import ControladorSensores

controlador = ControladorSensores()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def temperatura(ctx):
    resultado = controlador.obtener_temperatura()
    await ctx.send(resultado)

@bot.command()
async def humedad(ctx):
    resultado = controlador.obtener_humedad_suelo()
    await ctx.send(resultado)

@bot.command()
async def movimiento(ctx):
    resultado = controlador.obtener_distancia()
    await ctx.send(resultado)

# --- main.py ---
from bot import discord_bot

if __name__ == "__main__":
    
    TOKEN = "Bot Discord"
    discord_bot.bot.run(TOKEN)
