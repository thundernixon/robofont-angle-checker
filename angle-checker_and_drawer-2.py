from AppKit import *
from vanilla import *

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
        self.w.rangeToCheck = SliderEditIntStepper((160, y, -10, 22), 8, callback=self.changedCallback, minValue=0, maxValue=45)
        
        self.w.open()
        self.w.bind("close", self.windowCloseCallback)
        addObserver(self, "myDrawCallback", "draw")
        addObserver(self, "myDrawCallback", "drawInactive")
        addObserver(self, "myDrawCallback", "spaceCenterDraw")
        
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
        self.g.update()

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
                    # tolerance = 1
                    tolerance = self.w.tolerance.get()
                    # rangeToCheck = 8
                    rangeToCheck = self.w.rangeToCheck.get()
                    # desAngle = 16
                    desAngle = self.w.desiredAngle.get()
                    diff = abs(desAngle - lineAngleAdjusted)
                    if diff < tolerance:
                        print diff, "fine"
                        self.goodAngles.append((x1, y1, x2, y2))
                        # self.draw((0,0,1))
                    elif diff < rangeToCheck:
                        print seg.points, diff, "not fine"
                        self.badAngles.append((x1, y1, x2, y2))
                        # self.draw((1,0,0))
                    else:
                        pass
                prevPoint = seg.points[-1]
            print "\n"
            # print self.badAngles
            
    def myDrawCallback(self, notification):
        glyph = notification["glyph"]
        # # scale = notification["scale"]
        # color = self.w.color.get()
        # width = self.w.width.get()
        
        fill(1, 0, 0, 0.5)
        # for c in glyph:
        #     for p in c.points:
        #         oval(p.x, p.y, 10, 10)
                
        for angle in self.badAngles:
            
            stroke(1,0,0,.5)
            strokeWidth(6)
            # line(41, 442, 30, 403)
            # print self.badAngles[angle]
            # print angle[0], angle[1],angle[2],angle[3]
            line(angle[0], angle[1],angle[2],angle[3])
        for angle in self.goodAngles:
            
            stroke(0,1,.5,.5)
            strokeWidth(4)
            # line(41, 442, 30, 403)
            # print self.badAngles[angle]
            # print angle[0], angle[1],angle[2],angle[3]
            line(angle[0], angle[1],angle[2],angle[3])
            
        # if 0:
        #     lineCap = self._lineCapStylesMap[self.w.lineCap.getTitle()]
        #     lineJoin = self._lineJoinStylesMap[self.w.lineJoin.getTitle()]
        
        #     #path = glyph.naked().getRepresentation("defconAppKit.NSBezierPath")       
        #     pen = CocoaPen(glyph.getParent())
        #     glyph.draw(pen)
        #     path = pen.path
        
        #     path.setLineWidth_(width)
        #     path.setLineCapStyle_(lineCap)
        #     path.setLineJoinStyle_(lineJoin)
        
        #     color.set()
        #     path.stroke()   


AngleChecker().checkAngles()
