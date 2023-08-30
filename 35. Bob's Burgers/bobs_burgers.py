# Write code below 💖
class Restaurant:
  name = ''
  type = ''
  rating = 0.0
  delivery = False

bobs_burgers = Restaurant()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.type = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

la_federala = Restaurant()

la_federala.name = 'la_federala'
la_federala.type = 'Mexican Food'
la_federala.rating = 4.8
la_federala.delivery = True

la_española = Restaurant()

la_española.name = 'la_española'
la_española.type = 'Spanish restaurant'
la_española.rating = 4.9
la_española.delivery = True

print(vars(bobs_burgers))
print(vars(la_federala))
print(vars(la_española))