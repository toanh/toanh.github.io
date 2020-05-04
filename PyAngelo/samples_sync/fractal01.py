def midpoint(p1, p2):
    return((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

triangles = [[(50, 375), (450, 375), (250, 29)]]

colour = 1.0
depth = 0

graphics.clear()

@loop_animation
next_level = []
if depth < 7:
    for tri in triangles:
        new_tri = []
        for i in range(3):
            first = midpoint(tri[i-1], tri[i])
            second = midpoint(tri[i], tri[(i+1) % 3])
            graphics.drawLine(first[0], first[1], second[0], second[1], r = 1 - colour, g = colour, b = 1 - colour)
            new_tri += [[first, tri[i], second]]
        next_level += new_tri
    triangles = next_level
    colour -= 0.1
depth = depth + 1

