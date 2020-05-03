def midpoint(p1, p2):
    return((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
    
graphics.clear()

points = [[(50, 375), (450, 375), (250, 29)]]

colour = 1.0
for point in points:
    for i in range(3):
        first = point[i]
        second = point[(i+1) % 3]
        graphics.drawLine(first[0], first[1], second[0], second[1], r = 0, g = 1, b = 0)

k = 0

@loop_animation
array = []
if k < 7:
    for point in points:
        l = []
        for i in range(3):
            first = midpoint(point[i-1], point[i])
            second = midpoint(point[i], point[(i+1) % 3])
            graphics.drawLine(first[0], first[1], second[0], second[1], r = 1 - colour, g = colour, b = 1 - colour)
            l += [[first, point[i], second]]
        array += l
        
    points = array
    colour -= 0.1
k = k + 1

