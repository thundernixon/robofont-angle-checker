from AppKit import *
from vanilla import *

from lib.UI.stepper import SliderEditIntStepper

from math import *
from mojo.UI import UpdateCurrentGlyphView, CurrentSpaceCenter
from mojo.drawingTools import *

class AngleChecker():
    

    def __init__(self):    
        
        self.w = FloatingWindow((250, 130), "Angle Checker")
        y = 10
        self.w.desiredAngleText = TextBox((10, y, 88, 22), "Desired Angle:", alignment="right")
        self.w.desiredAngle = SliderEditIntStepper((100, y, -10, 22), 16.5, callback=self.changedCallback, minValue=0, maxValue=180)
        
        self.w.open()
        
        self.g = CurrentGlyph()
        
    def changedCallback(self, sender):
        UpdateCurrentGlyphView()
        sc = CurrentSpaceCenter()
        if sc:
            sc.refreshAllExept()

    def checkAngles(self):
        for contour in self.g:
            prevPoint = contour[-1].points[-1]
            for seg in contour:
                if seg.type == "line":
                    currentPoint = seg.points[-1]
                    x1, y1 = prevPoint.x, prevPoint.y
                    x2, y2 = currentPoint.x, currentPoint.y
                    dx, dy = x2 - x1, y2 - y1
            
                    # lineAngle = abs(degrees(atan2(dy, dx)) + 90)
            
                    lineAngle = round(degrees(atan2(dy, dx)),2)
                    # # if lineAngle < 0:
                    # #     lineAngle += 90
            
                    if lineAngle <= 0:
                        lineAngleAdjusted = abs(lineAngle + 90)
                    elif lineAngle > 0:
                        lineAngleAdjusted = abs(lineAngle - 90)
            
                    print x1, ",", y1, "|", x2, ",", y2, "|", "line angle:", lineAngle, "| line angle adj:", lineAngleAdjusted
                        
                    # if lineAngle < -15 and lineAngle > -18:
                    #     currentPoint.selected = True
            
                    #### simplify the math with this
                    tolerance = 1
                    rangeToCheck = 8
                    desAngle = 16
                    diff = abs(desAngle - lineAngleAdjusted)
                    if diff < tolerance:
                        print diff, "fine"
                        # self.draw((0,0,1))
                    elif diff < rangeToCheck:
                        print seg.points, diff, "not fine"
                        # self.draw((1,0,0))
                    else:
                        pass
                prevPoint = seg.points[-1]
            print "\n"
    

AngleChecker().checkAngles()
