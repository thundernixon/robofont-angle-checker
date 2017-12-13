from AppKit import *
from vanilla import *
from defconAppKit.windows.baseWindow import BaseWindowController

from lib.UI.stepper import SliderEditIntStepper

from math import *

from mojo.events import addObserver, removeObserver
from mojo.UI import UpdateCurrentGlyphView, CurrentSpaceCenter
from mojo.drawingTools import *

class AngleChecker():
    

    def __init__(self):    
        
        self.w = FloatingWindow((350, 130), "Angle Checker")
        y = 10
        self.w.desiredAngleText = TextBox((10, y, 140, 22), "Desired Angle:", alignment="right")
        self.w.desiredAngle = SliderEditIntStepper((160, y, -10, 22), 16.5, callback=self.changedCallback, minValue=0, maxValue=180)
        
        y += 30
        self.w.toleranceText = TextBox((10, y, 140, 22), "Tolerance +/-:", alignment="right")
        self.w.tolerance = SliderEditIntStepper((160, y, -10, 22), 1.5, callback=self.changedCallback, minValue=0, maxValue=15)
        
        y += 30
        self.w.rangeToCheckText = TextBox((10, y, 140, 22), "Range to check +/-:", alignment="right")
        self.w.rangeToCheck = SliderEditIntStepper((160, y, -10, 22), 12, callback=self.changedCallback, minValue=0, maxValue=45)
        
        # self.setUpBaseWindowBehavior()
        self.w.open()
        self.w.bind("close", self.windowCloseCallback)
        addObserver(self, "myDrawCallback", "draw")
        addObserver(self, "myDrawCallback", "drawInactive")
        addObserver(self, "myDrawCallback", "spaceCenterDraw")
        UpdateCurrentGlyphView()
        
        self.g = CurrentGlyph()
        self.badAngles = []
        self.goodAngles = []
                
    def changedCallback(self, sender):
        UpdateCurrentGlyphView()
        sc = CurrentSpaceCenter()
        if sc:
            sc.refreshAllExept()
            
    def windowCloseCallback(self, sender):
        removeObserver(self, "draw")
        removeObserver(self, "drawInactive")
        removeObserver(self, "spaceCenterDraw")
        UpdateCurrentGlyphView()
        # super(SimpleWindowObserver, self).windowCloseCallback(sender)
        # self.g.update()

    def checkAngles(self):
        self.badAngles = []
        self.goodAngles = []
        for contour in self.g:
            prevPoint = contour[-1].points[-1]
            for seg in contour:
                if seg.type == "line":
                    currentPoint = seg.points[-1]
                    x1, y1 = prevPoint.x, prevPoint.y
                    x2, y2 = currentPoint.x, currentPoint.y
                    dx, dy = x2 - x1, y2 - y1
            
                    lineAngle = round(degrees(atan2(dy, dx)),2)
            
                    if lineAngle <= 0:
                        lineAngleAdjusted = abs(lineAngle + 90)
                    elif lineAngle > 0:
                        lineAngleAdjusted = abs(lineAngle - 90)
                        
            
                    #### simplify the math with this
                    tolerance = self.w.tolerance.get()
                    rangeToCheck = self.w.rangeToCheck.get()
                    desAngle = self.w.desiredAngle.get()
                    
                    diff = abs(desAngle - lineAngleAdjusted)
                    if diff < tolerance:
                        # print diff, "fine"
                        self.goodAngles.append((x1, y1, x2, y2))

                    elif diff < rangeToCheck:
                        # print seg.points, diff, "not fine"
                        self.badAngles.append((x1, y1, x2, y2))

                    else:
                        pass
                prevPoint = seg.points[-1]
            
            
    def myDrawCallback(self, notification):
        # self.refreshCanvas()
        self.checkAngles()
        glyph = notification["glyph"]
        # # scale = notification["scale"]

        lineCap("round")
                
        for angle in self.badAngles:
            stroke(1,0,0,.5)
            strokeWidth(6)
            line(angle[0], angle[1],angle[2],angle[3])
            
        for angle in self.goodAngles:
            stroke(0,1,.5,.25)
            strokeWidth(4)
            line(angle[0], angle[1],angle[2],angle[3])


# AngleChecker().checkAngles()
AngleChecker()
# AngleChecker().myDrawCallback()