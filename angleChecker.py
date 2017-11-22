# from mojo.events import addObserver, removeObserver
# from mojo.drawingTools import *

# # get current glyph
# # loop through straight contours
# # maybe you need to define that a contour is straight based on lineTo?
# # maybe you need to compute the angle of contours?
# # if a straight contour is between [20] and [22] degrees, highlight in [teal]
# # maybe: if a a straight contour is between [18] and [20] degrees OR [22] and [24] degrees, highlight in [red]

# class angleCheck(object):
    
#     tolerance = 3    # how many degrees off can an angle be?
    
#     def setup(self):
#         self.markColor = (    255/255.0,    0/255.0,    0/255.0,     0.8)
#         self.okColor = (      0/255.0,      0/255.0,    255/255.0,   0.8)
        
#     def __init__(self):
#         addObserver(self, "checkAngles", "draw")
#         addObserver(self, "draw", "draw")
#         addObserver(self, "draw", "drawInactive")
#         addObserver(self, "draw", "spaceCenterDraw")
        
#     def windowCloseCallback(self, sender):
#         super(StrokeObserer, self).windowCloseCallback(sender)
#         removeObserver(self, "draw")
#         removeObserver(self, "drawInactive")
#         removeObserver(self, "spaceCenterDraw")
        
#     def checkAngles(self):
#         g = CurrentGlyph()
#         f = CurrentFont()
#         if f is None:
#             return
#         if not g: 
#             return
            
#         for c in g.contours:
#             print c
    
#     def draw(self, notification):
#         glyph = notification["glyph"]
        
        

# # watch for changes to point coordinates, and run the checker again each time
# # (possibly, it could limit the checker to that only contours connected to changed point?)


# # in the future, maybe this could also run a check through all glyphs in a font, and highlight in red glyphs with potential issues? that may be a separate extension, though...

# angleCheck()