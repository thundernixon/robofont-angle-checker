from fontTools.pens.cocoaPen import CocoaPen
f = CurrentFont()

# g = f.newGlyph("tester") # creates a new glyph

g = CurrentGlyph()

print g.name
print g.width

# pen = g.getPen()
print g.getParent()

path = pen.path


path.setLineWidth_(10)

stroke = (1,0,0)

# color.set()
path.stroke()

pen.moveTo((100,100))
pen.lineTo((100,500))
pen.lineTo((400,500))
pen.closePath()

g.update