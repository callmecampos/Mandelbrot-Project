#!/usr/bin/python

from mayavi import mlab
import numpy as np

# Calculate the Julia set on a grid
x, y = np.ogrid[-1.5:0.5:500j, -1:1:500j]
z = x + 1j * y

julia = np.zeros(z.shape)

for i in range(50):
    z = z ** 2 - 0.70176 - 0.3842j
    julia += 1 / float(2 + i) * (z * np.conj(z) > 4)

# Display it
mlab.figure(size=(400, 300))
mlab.surf(julia, colormap='gist_earth', warp_scale='auto', vmax=1.5)

# A view into the "Canyon"
mlab.view(65, 27, 322, [30., -13.7,  136])
mlab.show()
