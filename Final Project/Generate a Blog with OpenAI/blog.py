#the super inteligent Blog 📔

import openai
#from dotenv import dotenv_values

#config = dotenv_values('.env')
#openai.api_key = config['API_KEY']

openai.api_key = 'Your key'

def generate_blog(paragraph_topic):
  response = openai.Completion.create(
    model = 'text-davinci-002',
    prompt = 'Escribe un párrafo sobre el siguiente tema. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )

  retrieve_blog = response.choices[0].text

  return retrieve_blog

keep_writing = True

while keep_writing:
  answer = input('¿Escribir otro párrafo? Y para continuar, N para finalizar.')
  if (answer == 'Y'):
    paragraph_topic = input('¿De qué debería hablar este párrafo?')
    print(generate_blog(paragraph_topic))
  else:
    keep_writing = False

#print(generate_blog('Why NYC is better than your city.'))y'''
