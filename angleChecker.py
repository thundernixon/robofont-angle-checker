# get current glyph
# loop through straight contours
# if a straight contour is between [20] and [22] degrees, highlight in [teal]
# maybe: if a a straight contour is between [18] and [20] degrees OR [22] and [24] degrees, highlight in [red]

# watch for changes to point coordinates, and run the checker again each time
# (possibly, it could limit the checker to that only contours connected to changed point?)


# in the future, maybe this could also run a check through all glyphs in a font, and highlight in red glyphs with potential issues? that may be a separate extension, though...