# Write code below 💖

class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

Madrid = City('Madrid', 'Spain', 3223000, ['Palacio Real de Madrid', 'Gran Vía'])
Avila = City('Avila', 'Spain', 55000, ['Muralla de Avila', 'Catedral'])

print(vars(Madrid))
print(vars(Avila))