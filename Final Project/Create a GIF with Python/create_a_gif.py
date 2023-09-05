#gift projec 🖼️

import imageio

filenames = ['cuenca1.jpg', 'cuenca2.jpg']
images = [ ]

for filename in filenames:
  images.append(imageio.v2.imread(filename))

imageio.mimsave('cuenca.gif', images, duration = 100)


