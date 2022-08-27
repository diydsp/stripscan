
import math

## scan position
# orientation
cx=0
cy=0
ang=0
dx=0
dy=0

scale = 1

## dynamics
lineVel=1
angVel=0

# sequencer


# repeat field
fwid=16
fhei=16

# super field
sfwid=100
sfhei=100

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
    dx=0
    dy=0

def angDecompose( ang ):
    dx = math.cos( ang )
    dy = math.sin( ang )
    return (dx,dy)

def angSet( angIn ):
    angIn = ang
    dx,dy = angDecompose( ang )
    
def step():
    cx += dx
    cy += dy


def dump():
    print( f'ang:{ang},dx,dy:{dx}{dy}' )
    print( f'cx,cy,{cx},{cy}')
    