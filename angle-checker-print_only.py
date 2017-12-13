from math import *
# from fontTools.pens.cocoaPen import CocoaPen
from mojo.UI import UpdateCurrentGlyphView

class AngleChecker():
    

    def __init__(self):    
        self.g = CurrentGlyph()

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
    
    # def draw(self, color):
    #     # glyph = notification["glyph"]
    #     # scale = notification["scale"]
    #     width = 10
    #     lineCap = "round"
    #     lineJoin = "round"
        
    #     #path = glyph.naked().getRepresentation("defconAppKit.NSBezierPath")       
    #     pen = CocoaPen(self.g.getParent())
    #     self.g.draw(pen)
    #     path = pen.path
        
    #     path.setLineWidth_(width)
    #     path.setLineCapStyle_(lineCap)
    #     path.setLineJoinStyle_(lineJoin)
        
    #     color.set()
    #     path.stroke()
AngleChecker().checkAngles()
# AngleChecker().draw()