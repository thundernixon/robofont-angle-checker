# from mojo.drawingTools import line, stroke, strokeWidth

from mojo.drawingTools import *
from mojo.UI import UpdateCurrentGlyphView

g = CurrentGlyph()

stroke(1,0,0,1)
strokeWidth(8)
fill(1)

# def draw():
# for contour in g:
#     for contour in g:
#         oval(100, 100,200, 200)
#         UpdateCurrentGlyphView()


# draw()

oval(100, 100,200, 200)
UpdateCurrentGlyphView()
    