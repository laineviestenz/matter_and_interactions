"""model the orbital rotation of the earth around the sun"""
"""tangential velocity of earth = 29800 m/s"""

import numpy as np

#mass of earth
mass_earth  = 6 * 10 ** 24
#mass of sun
mass_sun = 2 * 10 ** 30
#Gravitational constant
g = 6.7 * 10 ** 8
#initial velocity
velocity = np.array([0,29800,0])
#orbital radius
radius_orbit = 1.5 * 10 ** 11
#delta t
dt = 3600
#initial position
r = np.array([1.5 * 10 ** 11, 0, 0])

r_unit = r/np.linalg.norm(r)

#initial momentum
momentum = velocity * mass_earth

###############################################################################
#end variable setup, begin calculations and updates
###############################################################################

#find force on rotating object
force_centripetal = (g * mass_earth * mass_sun)/((radius_orbit) ** 2) * #unit vector sun to earth

#update momentum
momentum += force_centripetal * dt

=

