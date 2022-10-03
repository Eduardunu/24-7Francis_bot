from click import pass_context
from discord.ext import commands
import datetime
import discord
import time


token = open('token.txt').read()
bot = commands.Bot(command_prefix='!', description='Esto es un bot de ayuda')

@bot.command(aliases=['Buenas', 'Hola', 'Buenas tardes', 'Buenas noches'])
async def hola(ctx ):
  mensaje= await ctx.send('Hola!')
  sms1= await mensaje.edit (content='Espero este pasando un buen día!\n\n El bot funciona con un "!" al principio de cada comando, luego los comandos los puede abrir con "!Comandos"\n')

#error handling
"""@hola.error
async def hola_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('El comando no existe, intente con otro.')
    return"""


@bot.command (pass_context= True, hidden=True)
async def ping(ctx):
    antes= time.monotonic()
    mensaje= await ctx.send('pong!')
    ping1= (time.monotonic() - antes)*1000
    ping2= (str(ping1).split('.'))[0]
    await mensaje.edit (content='pong! (' + ping2 + 'ms) ')


@bot.command(pass_context=True)
async def Comandos(ctx):
  embed= discord.Embed(title="Comandos de ayuda", description="Esto te servira para poder preguntarme un par de dudas frecuentes", color=0xFFFF00)
  embed.set_footer(text='Si necesita ayuda con preguntas más personales, puede agarrar un ticket en el canal de tickets, o puede llamar al '', o envíen un correo al '', incluso pueden úbicarnos en redes sociales como ''. ')
  embed.add_field(name="Preguntas 1", value="""1. Matriculas.
  !matriculas

  2. Grados en la escuela.
  !grados 

  3. Directores.
  !profesores

  """, inline=True)
  embed.add_field(name="Preguntas 2", value="""1. Entrega de notas.
  !entrega_de_notas

  2. Examenes de nuevo ingreso.
  !examenes_nuevo_ingreso

  3. Entrega de viveres.
  !entrega_de_viveres
  
  """, inline=True)
  embed.set_thumbnail(url=f'https://img1.freepng.es/20180705/pgf/kisspng-francis-of-assisi-prayer-of-saint-francis-our-lady-vaco-san-francisco-5b3e93afa1b720.5681711515308276956624.jpg')
  await ctx.send(embed=embed)
#preguntas1

@bot.command (pass_context=True)
async def matriculas (ctx):
  await ctx.send ("Las matriculas son del 12 de noviembre al 22 de noviembre, para nuevo y antiguo ingreso.")

@bot.command (pass_context=True)
async def grados (ctx):
  await ctx.send ("Hay desde primero hasta noveno, incluyendo los años de bachillerato, en total las aulas son 25 y grados 15.")

@bot.command (pass_context=True)
async def profesores (ctx):
  await ctx.send ("""Tenemos los profesores de básica, que serian
  1. Seño juanita
  2. Seño damaris
  3. Profe alberto
  Y los profesores de bachillerato son
  1. Profe Oscar
  2. Profe Daniel
  3. Seño Stephanie.""")

#preguntas2

@bot.command (pass_context=True)
async def entrega_de_notas (ctx):
  await ctx.send ("Las entregas de notas se hacen por lo habitual cada finalizacion de trimestre o periodo, por lo tanto estas serían entregadas cada segunda semana del trimestre o periodo siguiente.")

@bot.command (pass_context=True)
async def examenes_nuevo_ingreso (ctx):
  await ctx.send ("Los examenes de nuevo ingreso serán a partir de noviembre 29, y estos examenes solo se hacen para conocer su nivel de aprendizaje, pero la nota minima en los examenes requerida es 6.0.")

@bot.command (pass_context=True)
async def entrega_de_viveres (ctx):
  await ctx.send ("Las entregas de viveres se estarán dando cada 4 meses, estar pendientes a las indicaciones de los orientadores a los alumnos.")

"""@bot.command (pass_context=True)
async def mensaje(ctx):
  mensaje= ctx.mesagge
  await ctx.send(mensaje.author)
  channel = await mensaje.author.create_dm(ctx)
  await channel.send ('Hola')"""

@bot.event
async def on_ready():
    print('El Bot está listo')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Activo para servirle'))


bot.run(token)