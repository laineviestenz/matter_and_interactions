"""model the orbital rotation of the earth around the sun"""
"""tangential velocity of earth = 29800 m/s"""

import numpy as np

#mass of earth
mass_earth  = 6 * 10 ** 24
#initial velocity
velocity = np.array([0,29800,0])

#initial momentum
momentum = velocity * mass_earth

print(momentum)