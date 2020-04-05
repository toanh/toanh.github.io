import math

angle = 0
camera = [0, -0.3, -2]

# setting up the screen
width = 500
height = 400

shape =[
    [0.7, 1, 0], [-1, -0.5, -1], [1, -0.5, -1],
    [0.7, 1, 0], [1, -0.5, -1], [1, -0.5, 1],
    [0.7, 1, 0], [1, -0.5, 1], [-1, -0.5, 1],
    [0.7, 1, 0], [-1, -0.5, -1], [-1, -0.5, 1]]

def drawLine(x1, y1, x2, y2):
  global win
  points = get_line((x1, y1), (x2, y2))
  for p in points:
    win.addch(int(round(p[1])), int(round(p[0])), '.')

def drawTriangleList(triList):
 
    for i in range(0, len(triList), 3):
        graphics.drawLine(triList[i][0], triList[i][1], triList[i + 1][0], triList[i+ 1][1])
        graphics.drawLine(triList[i + 1][0], triList[i + 1][1], triList[i + 2][0], triList[i+ 2][1])
        graphics.drawLine(triList[i + 2][0], triList[i + 2][1], triList[i][0], triList[i][1])

def rotateTransform(triList3D, angle):
    transformedList = []
    for vertex in triList3D:
        x = vertex[0] * math.cos(angle) - vertex[2] * math.sin(angle)
        y = vertex[1]
        z = vertex[0] * math.sin(angle) + vertex[2] * math.cos(angle)       

        newTri = (x, y, z)
        transformedList.append(newTri)
    return transformedList    

def translateTransform(triList3D, cameraPos):
    transformedList = []
    for i in range(len(triList3D)):
        newTri = (triList3D[i][0] - cameraPos[0], triList3D[i][1] - cameraPos[1], triList3D[i][2] - cameraPos[2])
        transformedList.append(newTri)
    return transformedList
    
def perspectiveTransform(triList3D):
    triList2D = [];
    for i in range(0, len(triList3D)):
        newTri = (triList3D[i][0]/triList3D[i][2], triList3D[i][1]/triList3D[i][2])
        triList2D.append(newTri)
    return triList2D

def viewportTransform(triList2D, width, height):
    transformedList = []
    for vertex in triList2D:
        x = int(vertex[0] * width/2 + width/2)
        y = int(vertex[1] * height/2 + height/2)
        newTri = (x, y)
        transformedList.append(newTri)
    return transformedList        

@loop_animation
angle = angle + 0.05   

graphics.clear(0, 0, 0)
triList = rotateTransform(shape, angle)    
triList = translateTransform(triList, camera)

triList = perspectiveTransform(triList)
triList = viewportTransform(triList, width, height)

drawTriangleList(triList)
