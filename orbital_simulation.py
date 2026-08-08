"""model the orbital rotation of the earth around the sun"""
"""tangential velocity of earth = 29800 m/s"""

import numpy as np

#mass of earth
mass_earth  = 6e24
#mass of sun
mass_sun = 2e30
#Gravitational constant
g = 6.7e-11
#initial velocity
velocity = np.array([0,29800,0])
#orbital radius
radius_orbit = 1.5e11
#delta t
dt = 36000
#initial position
r = np.array([1.5 * 10 ** 11, 0, 0])

r_unit = r/np.linalg.norm(r)

#initial momentum
momentum = velocity * mass_earth

#initial values
r_list = []
t = 0

###############################################################################
#end variable setup, begin calculations and updates
###############################################################################

while t < 360000:
    #find force on rotating object
    force_gravitational = (g * mass_earth * mass_sun)/((radius_orbit) ** 2) * r_unit

    #update momentum
    momentum += force_gravitational * dt

    velocity = momentum / mass_earth

    r = r +velocity * dt

    r_list.append(np.round(r, decimals=10))

    t += dt

#create graph here after loop done
print(r_list)