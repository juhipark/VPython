from __future__ import print_function, division
from visual import *
from visual.graph import *
import wx

L=400
Hgraph=400
font1 = wx.Font(18, wx.DECORATIVE, wx.NORMAL, wx.BOLD)
font2 = wx.Font(16, wx.ROMAN, wx.ITALIC, wx.NORMAL) 
####Create a window.
w = window(width=2*L, height=L+window.dheight+window.menuheight+Hgraph,
           menus=True, title='Tide Change Simulation', style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX)

####Placing display
d=20#margin
Hdisp=200
disp = display(window=w, x=d, y=d+7, width=L*2-(d*2), height=Hdisp, forward=-vector(0,1,2),
               background=color.black)

earthMass = 5.97e21#Mass of Earth: 5.97e21t
moonMass = 7.36e19#Mass of Moon: 7.36e19t
sunMass = 2e27#Mass of Sun: 2e27t

"""Adjustment is needed to make each Earth, Moon, Sun to be visible"""
earthRad = 4.37e6#radius of Earth: 6.37e3km
moonRad = 6.74e5#radius of Moon: 1.74e3km
sunRad = 1.99e7#radius of Sun: 6.95e5km

#Distance bewtween:
moonDis = 3.85e5#Earth to Moon: 384835km
sunDis = 1.50e8#Earth to sun: 149785000km e8

disp.range = sunDis/2+earthRad
disp.center = (sunDis/2,0,0)
earth = sphere(material=materials.BlueMarble, radius=earthRad)
moon = sphere(color=color.gray(2), material=materials.shiny, radius=moonRad)
sun = sphere(pos=vector((sunDis/2)+sunRad,0,0), color=color.yellow, material=materials.emissive, radius=sunRad)

####starting position
earth.pos=vector(0,0, 0)
initialPos = earth.pos.x+moonDis+moonRad*2+earthRad*2
moon.pos=(initialPos, 0, 0)
sun.pos=earth.pos+((sunDis),0,0)

####Place another display:
dispOrbit = display(window=w, x=d, y=Hdisp+d*2, width=L-d*2, height=Hdisp+d, forward=-vector(-0.5,1,2),
               background=color.white)
G=6.67e-11
earth2=sphere(pos=vector(-1e11,0,0), radius=2e10, material=materials.earth)
earth2.m=2e30
earth2.p=vector(0,0,-1e4)*earth2.m

moon2=sphere(pos=vector(1.5e11,0,0), radius=1e10, color=(.7,0.7,.7), make_trail=True, interval=10, retain=50)
moon2.m=1e30
moon2.p=-earth2.p
dispOrbit.range=(1e11*2.5,1,1)
    
####Graph display:
#gdisplay(window=w, y )




####Make panel to place buttons and slider:
p = w.panel
displayTitle = wx.StaticText(p, pos=(L-2*d,4), label='Moon Display')
displayTitle.SetFont(font1)
displayTitle.SetBackgroundColour((247, 181, 158))


####Functionality of buttons and slider:

def moveMoon(value):
    d = (sunDis-sunRad*2-earthRad*2 - moonDis)
    moon.pos.x = initialPos + d*(value/100)

def moveOrbit(value):    
    dt=1e5
    while value:
        rate(75)
        r=moon2.pos-earth2.pos
        F= G*earth2.m*earth2.m*norm(r)/mag2(r)
        earth2.p=earth2.p
        moon2.p=moon2.p-F*dt
        earth2.pos=earth2.pos
        moon2.pos=moon2.pos+(moon2.p/moon2.m)*dt
    orbit.Bind(wx.EVT_BUTTON, )
        
def setOrbit(evt):
    value = orbit.GetAuthNeeded()
    moveOrbit(value)
    
def setLow(evt):
    moveMoon(0)#lowest value is 0

def setHigh(evt):
    moveMoon(100)#highest value is 100

def setMove(evt):
    value = s1.GetValue()
    moveMoon(value) #value is range from 0 - 100

###Place butttons:
low = wx.Button(p, label='Low tide', pos=(1.0*L,0.85*L))
low.Bind(wx.EVT_BUTTON, setLow)
high = wx.Button(p, label='High tide', pos=(1.25*L,0.85*L))
high.Bind(wx.EVT_BUTTON, setHigh)
orbit = wx.Button(p, label='Orbit', pos=(1.125*L,0.95*L))
orbit.Bind(wx.EVT_BUTTON, setOrbit)

###Place TextCtrl for userinput:
userText = wx.TextCtrl(p, pos=(1.55*L,0.85*L), value='You can type here:\n', size=(150,80))
userText.SetInsertionPoint(len(userText.GetValue())+1)#cursor position at the end of text
userText.SetFocus()#keypresses go to this TextCtrl without clicking it

####Place slider:
sliderTitle = wx.StaticText(p, pos=(1.0*L,0.65*L), label='Set distance between Moon and Earth')
sliderTitle.SetFont(font1)
sliderTitle.SetForegroundColour((134, 66, 244))
sliderTitle.SetBackgroundColour((244, 226, 65))
describe = wx.StaticText(p, pos=(1.0*L,0.75*L),
              label='Slide left- Closer to Earth, Slide right- Closer to Sun')
describe.SetFont(font2)
s1 = wx.Slider(p, pos=(1.0*L,0.7*L), size=(0.9*L,20), minValue=0, maxValue=100)
s1.Bind(wx.EVT_SCROLL, setMove)

####Graph
gdisp=gdisplay(window=w, y=disp.height+300, width=2*(L+window.dwidth), height=Hdisp*1.4)
funct1 = gcurve(color=color.cyan)
funct2 = gvbars(delta=0.5, color=color.red)

for t in arange(-30,74,1):
    funct1.plot(pos=(t, 5.0+5.0*cos(-0.2*t)*exp(0.015*t)))
    funct2.plot(pos=(t, 2.0+5.0*cos(-0.1*t)*exp(0.015*t)))




