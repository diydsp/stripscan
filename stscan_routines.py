

## scan position
# orientation
cx=0
cy=0
ang=0

scale = 1

## dynamics
lineVel=1
angVel=0

## sequencer


## field
fwid=16
fhei=16

## output
numLEDs = 16

def posRender( idx ):
    pass


def stripRender():
    for idx in range( numLEDS ):
        posRender( idx )
        

def init():
    cx=0
    cy=0
    ang=0

def step():
    pass


def blank():
    pass
