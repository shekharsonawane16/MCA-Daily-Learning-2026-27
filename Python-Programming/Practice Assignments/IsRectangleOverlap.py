def isRectangleOverlap(r1x1, r1y1, r1x2, r1y2,
                       r2x1, r2y1, r2x2, r2y2):
    return (r1x1 < r2x2 and r1x2 > r2x1 and
            r1y1 < r2y2 and r1y2 > r2y1)

print(isRectangleOverlap(0, 0, 2, 2, 1, 1, 3, 3))  # Example usage: checks if the rectangles overlap