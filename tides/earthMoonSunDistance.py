from __future__ import print_function, division
from visual import *
from visual.graph import *
import wx

L=400
Hgraph=400
####Create a window.
w = window(width=2*L, height=L+window.dheight+window.menuheight+Hgraph,
           menus=True, title='Tide Change Simulation', style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

####Placing display
d=20#margin
Hdisp=200
disp = display(window=w, x=d, y=d, width=L*2-(d*2), height=Hdisp, forward=-vector(0,1,2), background=color.white)
#########gdisplay(window=w, y=disp.height+50, width=2*(L+window.dwidth), height=Hgraph)

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


earth = sphere(material=materials.BlueMarble, radius=earthRad*2)
moon = sphere(color=color.gray(2), material=materials.shiny, radius=moonRad*2)
sun = sphere(pos=vector((sunDis/2),0,0), color=color.yellow, material=materials.emissive, radius=sunRad*2)

####starting position
earth.pos=vector(-(sunDis/2)+earthRad*2,0, 0)
moon.pos=earth.pos+(moonDis, 0, 0)
sun.pos=vector((sunDis/2),0,0)


####Make panel to place buttons and slider:
p = w.panel
wx.StaticText(p,pos=(L-2*d,4), size=(L-2*d,4), label='Moon Distance')
####Functionality of buttons and slider:

def moveMoon(value):
    moon.pos.x += 10000*value

def setMove(evt):
    value = s1.GetValue()
    moveMoon(value) #value is range from 0 - 100


####Place slider:
wx.StaticText(p, pos=(1.0*L,0.65*L), label='Set distance between Moon and Earth')
s1 = wx.Slider(p, pos=(1.0*L,0.7*L), size=(0.9*L,20), minValue=0, maxValue=100)
s1.Bind(wx.EVT_SCROLL, setMove)


