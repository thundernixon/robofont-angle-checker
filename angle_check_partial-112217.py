# def checkGlyph(g):
#     ...
#     return result

g = CurrentGlyph()

stroke(0)
fill(None)

for contour in g:
    lastPoint = contour[-1].points[-1]
    
    for seg in contour:
        if seg.type == "line":
            currentPoint = seg.points[-1]
            x1 = lastPoint.x
            y1 = lastPoint.y
            x2 = currentPoint.x
            y2 = currentPoint.y
            # print (x1, y1), (x2, y2)
            line((x1, y1), (x2, y2))
            if y2 < 100:
                currentPoint.selected = True
            dy = y2-y1
            dx = x2 - x1
            
            stroke(0)
            
            lineAngle = degrees(atan2(dy, dx))
            lineDist = hypot(dy, dx)
            
            maxLineLengthToCheck = 45
            desiredAngle = 16 # angle you want to check
            
            tolerance = 2 # how much total wiggle room you're okay with in the angle check
            rangeToCheck = 8
            # plusMinus = tolerance/2
            upperLimit = 90 + desiredAngle + tolerance
            lowerLimit = 90 + desiredAngle - tolerance
            
            upperRange = 90 + desiredAngle + rangeToCheck
            lowerRange = 90 + desiredAngle - rangeToCheck
                        
            if lineDist < maxLineLengthToCheck:
                # print "yo"
                # print "lower limit is ", lowerLimit -180, ", " "upper limit is ", upperLimit -180
                # print "angle is ", lineAngle
                
                isInTolerance = abs(lineAngle) < abs(upperLimit) and abs(lineAngle) > abs(lowerLimit) or  abs(lineAngle) < abs(upperLimit-180) and abs(lineAngle) > abs(lowerLimit-180)
                isInRangeToCheck = (abs(lineAngle) < abs(upperRange) and abs(lineAngle) > abs(lowerRange)) or  (abs(lineAngle) < abs(lowerRange-180) and abs(lineAngle) > abs(upperRange-180))
                
                # print abs(lowerRange), ", ", abs(lineAngle), ", ", abs(upperRange), ", angle lower than upper range: ", abs(lineAngle) < abs(upperRange)
                # print abs(upperRange-180), ", ", abs(lineAngle), ", ", abs(lowerRange-180), ", angle lower than upper range: ", abs(lineAngle) < abs(lowerRange-180)
                # print abs(lowerRange), ", ", abs(lineAngle), ", ", abs(upperRange), ", angle higher than lower range: ", abs(lineAngle) > abs(lowerRange)
                # print abs(upperRange-180), ", ", abs(lineAngle), ", ", abs(lowerRange-180), ", angle higher than lower range: ", abs(lineAngle) > abs(upperRange-180)
                
                
                # print lowerRange, ", ", lineAngle, ", ", upperRange
                # print abs(lowerRange - 180), ", ", lineAngle, ", ", abs(upperRange - 180)
                # print isInRangeToCheck
                # print "angle is not in tolerance:", isInTolerance == 0
                # print "angle is in range to check:", isInRangeToCheck
                
                if isInTolerance and isInRangeToCheck:
                    print "angle: ", lineAngle, "; distance: ", lineDist, "; nice", "; points: ",x1,y1, x2, y2
                    stroke(0,1,1)
                elif isInTolerance == 0 and isInRangeToCheck:
                    print lineAngle, "oops", x1,y1, x2, y2
                    stroke(1,0,0)
                else:
                    print "nothing to see here"
                    stroke(0)
                
                print "\n"
        lastPoint = seg.points[-1]


# atan2(dy, dx)
# hypot(dx, dy)