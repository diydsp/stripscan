

import math

class StripScanner:
    def __init__(self):
    
        ## scan position
        # orientation
        self.cx=0
        self.cy=0
        self.ang=0
        self.dx=0
        self.dy=0
        self.scale = 1

        ## dynamics
        self.lineVel=1
        self.angVel=0

        # sequencer

        # repeat field
        self.fwid=16
        self.fhei=16

        # super field
        self.sfwid=100
        self.sfhei=100

        ## output
        self.numLEDs = 16

    def posRender( self, idx ):
        pass


    def stripRender(self):
        for idx in range( numLEDS ):
            posRender( idx )
        
    def angDecompose( self, ang ):
        self.dx = math.cos( ang )
        self.dy = math.sin( ang )
        return (self.dx,self.dy)

    def angSet( self, ang ):
        self.ang = ang
        self.dx,self.dy = self.angDecompose( ang )
    
    def step( self ):
        self.cx += self.dx
        self.cy += self.dy


    def dump( self ):
        print( f'ang:{self.ang},dx,dy:{self.dx}{self.dy}' )
        print( f'cx,cy,{self.cx},{self.cy}')
    