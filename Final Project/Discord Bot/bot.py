import discord
import requests
import json
import random

# Función para obtener memes
def get_meme():
  response = requests.get('https://meme-api.com/gimme')
  json_data = json.loads(response.text)
  return json_data['url']

# Función para obtener un acertijo aleatorio
def get_random_riddle():
    riddles = [
        "Si me tumbas, soy todo. Si me cortas por la cintura, me quedo en nada. ¿Qué soy?",
        "¿Cuántos ladrillos se necesitan para completar un edificio hecho de ladrillos",
        "Una mujer tuvo dos hijos que nacieron a la misma hora del mismo día del mismo año, pero no son gemelos. ¿Cómo es posible?",
        "Un hombre empuja su coche. Se detiene al llegar a un hotel y de pronto sabe que está arruinado. ¿Qué ha pasado?",
        "Estás en un laberinto completamente a oscuras y tienes una vela, una antorcha, un puñado de paja y una sola cerilla. ¿Qué enciendes primero?",
        "¿Qué es lo que no está ni dentro ni fuera de la casa, pero que es necesario para cualquier hogar?",
        "El hombre que lo vendió no lo quería. El hombre que lo compró no lo necesitaba. El hombre que lo usó no lo conocía.",
        "20+20+20=60. ¿Cómo puedes hacer 60 nuevamente usando el mismo número 3 veces?",
        "Tom mide 1,80, es ayudante en una carnicería y lleva zapatos de la talla 45. ¿Qué pesa?",
        "El señor y la señora García–Palomeque tienen seis hijas y cada hija tiene un hermano. ¿Cuántas personas hay en la familia García–Palomeque.",

        # Agrega más acertijos aquí
    ]
    return random.choice(riddles)

# Función para obtener una cita inspiradora o frase célebre aleatoria
def get_random_quote():
    quotes = [
        "No hay hombre tan cobarde a quien el amor no haga valiente y transforme en héroe. Platón.",
        "Hay alguien tan inteligente que aprende de la experiencia de los demás. Voltaire.",
        "Vivir sin filosofar es, propiamente, tener los ojos cerrados, sin tratar de abrirlos jamás. René Descartes.",
        "Lo menos frecuente en este mundo es vivir. La mayoría de la gente existe, eso es todo. Oscar Wilde.",
        "La felicidad de tu vida depende de la calidad de tus pensamientos. Marco Aurelio. ",
        "La vida no se trata de encontrarte a ti mismo, sino de crearte a ti mismo. Bernard Shaw.",
        "Pensar es fácil, actuar es difícil, y poner los pensamientos de uno mismo en acción es lo más difícil del mundo. Goethe. ",
        "No lastimes a los demás con lo que te causa dolor a ti mismo. Buda.",
        "El hombre que mueve montañas empieza apartando piedras pequeñas. Confucio.",
        "Educa a los niños y no será necesario castigar a los hombres. Pitágoras de Samos. ",
        "¿Quieres ser rico? Pues no te afanes en aumentar tus bienes sino en disminuir tu codicia. Epicuro.",


        # Agrega más citas aquí
    ]
    return random.choice(quotes)

def get_bot_info():
    bot_name = 'MEME BOte'
    bot_version = '1.0'
    bot_description = 'Pasemos un rato divertido.'
    return f'Bot Name: {bot_name}\nVersion: {bot_version}\nDescription: {bot_description}'

class MyClient(discord.Client):

  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))
  async def on_message(self, message):
    if message.author == self.user:
        return

    if message.content.startswith('$meme'):
        await message.channel.send(get_meme())
    if message.content.startswith('$hello'):
        await message.channel.send('Hola. Aqui MemeBot.')
    if message.content.startswith('$server_info'):
        server = message.guild
        await message.channel.send(f'Server Name: {server.name}')
        await message.channel.send(f'Server Region: {server.region}')
        await message.channel.send(f'Server ID: {server.id}')
        await message.channel.send(f'Server Members: {server.member_count}')
    if message.content.startswith('$botinfo'):
        bot_info = get_bot_info()
        await message.channel.send(bot_info)
    if message.content.startswith('$riddle'):
        riddle = get_random_riddle()
        await message.channel.send(f'Adivina adivinanza: {riddle}')

    if message.content.startswith('$quote'):
        quote = get_random_quote()
        await message.channel.send(f'Presta atencion: {quote}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(your token) # Replace with your own token.
