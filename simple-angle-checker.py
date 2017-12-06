from math import *

g = CurrentGlyph()

for contour in g:
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
            elif diff < rangeToCheck:
                print seg.points, diff, "not fine"
            else:
                pass
        prevPoint = seg.points[-1]
    print "\n"