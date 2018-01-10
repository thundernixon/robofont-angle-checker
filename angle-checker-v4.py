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
        
        self.w = FloatingWindow((380, 140), "Angle Checker")
        y = 10
        self.w.desiredAngleText = TextBox((10, y, 140, 22), "Desired Angle:", alignment="right")
        self.w.desiredAngle = SliderEditIntStepper((160, y, -10, 22), 15.5, callback=self.changedCallback, minValue=0, maxValue=180)
        
        y += 30
        self.w.toleranceText = TextBox((10, y, 140, 22), "Tolerance +/-:", alignment="right")
        self.w.tolerance = SliderEditIntStepper((160, y, -10, 22), 1, callback=self.changedCallback, minValue=0, maxValue=15)
        
        y += 30
        self.w.rangeToCheckText = TextBox((10, y, 140, 22), "Range to check +/-:", alignment="right")
        self.w.rangeToCheck = SliderEditIntStepper((160, y, -10, 22), 12, callback=self.changedCallback, minValue=0, maxValue=45)
        
        # y += 30
        # self.w.layerNameText = TextBox((10, y, 140, 22), "Current layer name:", alignment="right")
        # self.w.layerName = TextEditor((160, y, -10, 22), "foreground")
        
        # self.setUpBaseWindowBehavior()
        self.g = CurrentGlyph()
        
        self.w.open()
        self.w.bind("close", self.windowCloseCallback)
        addObserver(self, "myDrawCallback", "draw")
        addObserver(self, "myDrawCallback", "drawInactive")
        # self.g.addObserver(self, "myDrawCallback", "Glyph.Changed")

        # addObserver(self, "myDrawCallback", "spaceCenterDraw")
        addObserver(self, "glyphViewChangedCallback", "viewDidChangeGlyph")
        
        self.g.addObserver(self, "glyphDataChangedCallback", "Glyph.Changed")
        
        UpdateCurrentGlyphView()
        
        
        # self.badAngles = []
        # self.goodAngles = []
        
        self.timesFired = 0
                
    def changedCallback(self, sender):
        UpdateCurrentGlyphView()
        sc = CurrentSpaceCenter()
        if sc:
            sc.refreshAllExept()
            
    def windowCloseCallback(self, sender):
        removeObserver(self, "draw")
        removeObserver(self, "drawInactive")
        # self.g.removeObserver(self, "Glyph.Changed")
        # removeObserver(self, "spaceCenterDraw")
        removeObserver(self, "viewDidChangeGlyph")
        UpdateCurrentGlyphView()

    def checkAngles(self):
        self.badAngles = []
        self.goodAngles = []
        # self.layerName = self.w.layerName.get()
        # for contour in self.g.getLayer(self.layerName):
        for contour in self.g:
            # print "\n"
            prevPoint = contour[-1].points[-1]
            for seg in contour:
                if seg.type == "line":
                    currentPoint = seg.points[-1]
                    # print "prevPoint is ", prevPoint, "currentPoint is ", currentPoint
                    x1, y1 = prevPoint.x, prevPoint.y
                    x2, y2 = currentPoint.x, currentPoint.y
                    
                    lineAngleAdjusted = self.getAngleValue(x1, y1, x2, y2)
                    # print lineAngleAdjusted
                    
                    tolerance = self.w.tolerance.get()
                    rangeToCheck = self.w.rangeToCheck.get()
                    desAngle = self.w.desiredAngle.get()
                    
                    diff = abs(desAngle - lineAngleAdjusted)
                    if diff <= tolerance:
                        # print diff, "fine"
                        self.goodAngles.append((x1, y1, x2, y2))

                    elif diff <= rangeToCheck:
                        # print seg.points, diff, "not fine"
                        self.badAngles.append((x1, y1, x2, y2))

                    else:
                        pass
                prevPoint = seg.points[-1]
                
    def getAngleValue(self, x1, y1, x2, y2):
        dx, dy = x2 - x1, y2 - y1
        lineAngle = round(degrees(atan2(dy, dx)),2)
        if lineAngle <= 0:
            lineAngleAdjusted = abs(lineAngle + 90)
        elif lineAngle > 0:
            lineAngleAdjusted = abs(lineAngle - 90)
        # print "lineAngleAdjusted is ", lineAngleAdjusted
        return lineAngleAdjusted
        
    def getAngleDist(self, x1, y1, x2, y2):
        dist = round(sqrt((x2 - x1)**2 + (y2 - y1)**2),2)
        return dist
          
    def writeText(self, x1, y1,x2,y2):
        # stroke(1,0,0,.5)
        strokeWidth(6)
        line(x1, y1,x2,y2)

        lineAngleAdjusted = self.getAngleValue(x1, y1,x2,y2)
        txt = "∡".decode('utf-8') + str(lineAngleAdjusted) + "°".decode('utf-8')
        
        
        
        textX, textY = x1 + 15, y1 + 15
        fontSize(12)
        text(txt, (textX, textY))
        
        
        lineDist = "⤢".decode('utf-8') +  str(self.getAngleDist(x1, y1,x2,y2))
        strokeWidth(0)
        text(lineDist, (textX + 50, textY))
        
    def computeAndDraw(self, info):
        print(info)
        self.g = info["glyph"]
        self.checkAngles()
        
        print self.g
        
        self.timesFired += 1
        
        print self.timesFired

        lineCap("round")
        
        for coordinate in self.badAngles:            
            stroke(1,0,0,.5)
            self.writeText(coordinate[0], coordinate[1],coordinate[2],coordinate[3])
            
        for coordinate in self.goodAngles:
            stroke(0,1,.5,.5)
            self.writeText(coordinate[0], coordinate[1],coordinate[2],coordinate[3])
        
            
    def myDrawCallback(self, info):
        # self.refreshCanvas()
        # self.g.saveGraphicsState()
        
        # UpdateCurrentGlyphView()
        
        print("event")

    def glyphViewChangedCallback(self, info):
        print "glyph changed"
        self.computeAndDraw(info)
        
    def glyphDataChangedCallback(self, info):
        print "glyph data changed"
        print info
        self.computeAndDraw(info)
        


AngleChecker()