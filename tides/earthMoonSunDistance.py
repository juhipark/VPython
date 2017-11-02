from __future__ import print_function, division
from visual import *

#Mass of Earth: 5.97e21t
#Mass of Moon: 7.36e19t
#Mass of Sun: 2e27t
earthMass = 5.97e21
moonMass = 7.36e19
sunMass = 2e27

#Mean radius of Earth: 6.37e3km
#Mean radius of Moon: 1.74e3km
#Mean radius of Sun: 6.95e5km
"""Earth and Moon will be too small to see, adjustment is needed to enlarge moon and sun"""
earthRad = 9.37e5
moonRad = 5.74e5
sunRad = 7.00e6

#Distance bewtween:
"""Too far apart, adjustment is needed"""
#Earth to Moon: 384835km
moonDis = 3.85e5+earthRad*2+moonRad*2
#Earth to sun: 149785000km e8
sunDis = 1.50e8

#setting display scene
scene.title = "The Earth's tides"
scene.caption = "The Earth's tides"

scene.visible = False # show nothing yet
scene.visible = True  # show everything
scene.width = 950
scene.height = 350
scene.background = color.white
#scene.range = (sunDis/2,1,1)

earth = sphere(material=materials.BlueMarble, radius=earthRad*2)
moon = sphere(color=color.gray(2), material=materials.shiny, radius=moonRad*2)
sun = sphere(pos=vector((sunDis/2),0,0), color=color.yellow, material=materials.emissive, radius=sunRad*2)

#starting position
earth.pos=vector(-(sunDis/2)+earthRad*2,0, 0)
moon.pos=earth.pos+(moonDis, 0, 0)
sun.pos=vector((sunDis/2),0,0)
