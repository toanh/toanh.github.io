class Vector(object):
    def __init__(self, *args):
        """ Create a vector, example: v = Vector(1,2) """
        if len(args) == 0:
            self.values = (0, 0)
        else:
            self.values = args

    def cross(self, other):
        if len(self.values) == 3 and len(other.values) == 3:
            ax, ay, az = self.values
            bx, by, bz = other.values
            return Vector(ay*bz - az*by, az*bx - ax*bz, ax*by - ay*bx)
        else:
            return None
            

    def norm(self):
        """ Returns the norm (length, magnitude) of the vector """
        return math.sqrt(sum(comp ** 2 for comp in self))

    def argument(self):
        """ Returns the argument of the vector, the angle clockwise from +y."""
        arg_in_rad = math.acos(Vector(0, 1) * self / self.norm())
        arg_in_deg = math.degrees(arg_in_rad)
        if self.values[0] < 0:
            return 360 - arg_in_deg
        else:
            return arg_in_deg

    def normalize(self):
        """ Returns a normalized unit vector """
        norm = self.norm()
        normed = tuple(comp / norm for comp in self)
        return Vector(*normed)

    def rotate(self, *args):
        """ Rotate this vector. If passed a number, assumes this is a
            2D vector and rotates by the passed value in degrees.  Otherwise,
            assumes the passed value is a list acting as a matrix which rotates the vector.
        """
        if len(args) == 1 and type(args[0]) == type(1) or type(args[0]) == type(1.):
            # So, if rotate is passed an int or a float...
            if len(self) != 2:
                raise ValueError("Rotation axis not defined for greater than 2D vector")
            return self._rotate2D(*args)
        elif len(args) == 1:
            matrix = args[0]
            if not all(len(row) == len(v) for row in matrix) or not len(matrix) == len(self):
                raise ValueError("Rotation matrix must be square and same dimensions as vector")
            return self.matrix_mult(matrix)

    def _rotate2D(self, theta):
        """ Rotate this vector by theta in degrees.

            Returns a new vector.
        """
        theta = math.radians(theta)
        # Just applying the 2D rotation matrix
        dc, ds = math.cos(theta), math.sin(theta)
        x, y = self.values
        x, y = dc * x - ds * y, ds * x + dc * y
        return Vector(x, y)

    def matrix_mult(self, matrix):
        """ Multiply this vector by a matrix.  Assuming matrix is a list of lists.

            Example:
            mat = [[1,2,3],[-1,0,1],[3,4,5]]
            Vector(1,2,3).matrix_mult(mat) ->  (14, 2, 26)

        """
        if not all(len(row) == len(self) for row in matrix):
            raise ValueError('Matrix must match vector dimensions')

            # Grab a row from the matrix, make it a Vector, take the dot product,
        # and store it as the first component
        product = tuple(Vector(*row) * self for row in matrix)

        return Vector(*product)

    def inner(self, other):
        """ Returns the dot product (inner product) of self and other vector
        """
        return sum(a * b for a, b in zip(self, other))

    def __mul__(self, other):
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        if type(other) == type(self):
            return self.inner(other)
        elif type(other) == type(Matrix(1,1)):
            return other * self        
        elif type(other) == type(1) or type(other) == type(1.0):
            product = tuple(a * other for a in self)
            return Vector(*product)

    def __rmul__(self, other):
        """ Called if 4*self for instance """
        return self.__mul__(other)

    def __div__(self, other):
        if type(other) == type(1) or type(other) == type(1.0):
            divided = tuple(a / other for a in self)
            return Vector(*divided)

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        added = tuple(a + b for a, b in zip(self, other))
        return Vector(*added)

    def __sub__(self, other):
        """ Returns the vector difference of self and other """
        subbed = tuple(a - b for a, b in zip(self, other))
        return Vector(*subbed)

    def __iter__(self):
        return self.values.__iter__()

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __repr__(self):
        return str(self.values)


####################### Matrix Class ##################################
class Matrix(object):

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.zeros()

    def ones(self):
        self.values = [[1 for j in range(self.n)] for i in range(self.m)]

    def zeros(self):
        self.values = [[0 for j in range(self.n)] for i in range(self.m)]

    def identity(self):
        if self.m == self.n:
            self.values = [[1 if j == i else 0 for j in range(self.n)] for i in range(self.m)]
        
    def __len__(self):
        return self.m * self.n       
        
    def __mul__(self, other):
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        if type(other) == type(self):
            result = None
            if self.n == other.m:
                result = Matrix(self.m, other.n)
                for m in range(self.m):
                    for n in range(other.n):                        
                        result[m][n] = sum(a * b for a, b in zip(self.values[m], [i[n] for i in other.values]))
            return result
        elif type(other) == type(Vector(0,0,0,0)):
            r = [0,0,0,0]
            for n in range(len(r)):
                r[n] = sum(a * b for a,b in zip(other.values, [c[n] for c in self.values]))
            
            return Vector(r[0], r[1], r[2], r[3])                     
        elif type(other) == type(1) or type(other) == type(1.0):
            product = tuple(a * other for a in self)
            return Vector(*product)
                   

    def __rmul__(self, other):
        """ Called if 4*self for instance """
        return self.__mul__(other)        

    def norm(self):
        """ Returns the norm (length, magnitude) of the vector """
        return math.sqrt(sum(comp ** 2 for comp in self))

    def argument(self):
        """ Returns the argument of the vector, the angle clockwise from +y."""
        arg_in_rad = math.acos(Vector(0, 1) * self / self.norm())
        arg_in_deg = math.degrees(arg_in_rad)
        if self.values[0] < 0:
            return 360 - arg_in_deg
        else:
            return arg_in_deg

    def normalize(self):
        """ Returns a normalized unit vector """
        norm = self.norm()
        normed = tuple(comp / norm for comp in self)
        return Vector(*normed)

    def rotate(self, *args):
        """ Rotate this vector. If passed a number, assumes this is a
            2D vector and rotates by the passed value in degrees.  Otherwise,
            assumes the passed value is a list acting as a matrix which rotates the vector.
        """
        if len(args) == 1 and type(args[0]) == type(1) or type(args[0]) == type(1.):
            # So, if rotate is passed an int or a float...
            if len(self) != 2:
                raise ValueError("Rotation axis not defined for greater than 2D vector")
            return self._rotate2D(*args)
        elif len(args) == 1:
            matrix = args[0]
            if not all(len(row) == len(v) for row in matrix) or not len(matrix) == len(self):
                raise ValueError("Rotation matrix must be square and same dimensions as vector")
            return self.matrix_mult(matrix)

    def _rotate2D(self, theta):
        """ Rotate this vector by theta in degrees.

            Returns a new vector.
        """
        theta = math.radians(theta)
        # Just applying the 2D rotation matrix
        dc, ds = math.cos(theta), math.sin(theta)
        x, y = self.values
        x, y = dc * x - ds * y, ds * x + dc * y
        return Vector(x, y)

    def inverse(self):
        if self.m == 4 and self.n == 4:
            m = [j for i in self.values for j in i]
            inv = 16*[0]
            
            inv[0] = m[5]  * m[10] * m[15] - \
                     m[5]  * m[11] * m[14] - \
                     m[9]  * m[6]  * m[15] + \
                     m[9]  * m[7]  * m[14] + \
                     m[13] * m[6]  * m[11] - \
                     m[13] * m[7]  * m[10]

            inv[4] = -m[4]  * m[10] * m[15] + \
                      m[4]  * m[11] * m[14] + \
                      m[8]  * m[6]  * m[15] - \
                      m[8]  * m[7]  * m[14] - \
                      m[12] * m[6]  * m[11] + \
                      m[12] * m[7]  * m[10]

            inv[8] = m[4]  * m[9] * m[15] - \
                     m[4]  * m[11] * m[13]- \
                     m[8]  * m[5] * m[15] + \
                     m[8]  * m[7] * m[13] + \
                     m[12] * m[5] * m[11] - \
                     m[12] * m[7] * m[9]

            inv[12] = -m[4]  * m[9] * m[14] + \
                       m[4]  * m[10] * m[13]+ \
                       m[8]  * m[5] * m[14] - \
                       m[8]  * m[6] * m[13] - \
                       m[12] * m[5] * m[10] + \
                       m[12] * m[6] * m[9]

            inv[1] = -m[1]  * m[10] * m[15] +\
                      m[1]  * m[11] * m[14] +\
                      m[9]  * m[2] * m[15] - \
                      m[9]  * m[3] * m[14] - \
                      m[13] * m[2] * m[11] + \
                      m[13] * m[3] * m[10]

            inv[5] = m[0]  * m[10] * m[15] - \
                     m[0]  * m[11] * m[14] - \
                     m[8]  * m[2] * m[15] + \
                     m[8]  * m[3] * m[14] + \
                     m[12] * m[2] * m[11] - \
                     m[12] * m[3] * m[10]

            inv[9] = -m[0]  * m[9] * m[15] + \
                      m[0]  * m[11] * m[13] +\
                      m[8]  * m[1] * m[15] - \
                      m[8]  * m[3] * m[13] - \
                      m[12] * m[1] * m[11] + \
                      m[12] * m[3] * m[9]

            inv[13] = m[0]  * m[9] * m[14] - \
                      m[0]  * m[10] * m[13] -\
                      m[8]  * m[1] * m[14] + \
                      m[8]  * m[2] * m[13] + \
                      m[12] * m[1] * m[10] - \
                      m[12] * m[2] * m[9]

            inv[2] = m[1]  * m[6] * m[15] - \
                     m[1]  * m[7] * m[14] - \
                     m[5]  * m[2] * m[15] + \
                     m[5]  * m[3] * m[14] + \
                     m[13] * m[2] * m[7] - \
                     m[13] * m[3] * m[6]

            inv[6] = -m[0]  * m[6] * m[15] + \
                      m[0]  * m[7] * m[14] + \
                      m[4]  * m[2] * m[15] - \
                      m[4]  * m[3] * m[14] - \
                      m[12] * m[2] * m[7] + \
                      m[12] * m[3] * m[6]

            inv[10] = m[0]  * m[5] * m[15] - \
                      m[0]  * m[7] * m[13] - \
                      m[4]  * m[1] * m[15] + \
                      m[4]  * m[3] * m[13] + \
                      m[12] * m[1] * m[7] - \
                      m[12] * m[3] * m[5]

            inv[14] = -m[0]  * m[5] * m[14] + \
                       m[0]  * m[6] * m[13] + \
                       m[4]  * m[1] * m[14] - \
                       m[4]  * m[2] * m[13] - \
                       m[12] * m[1] * m[6] + \
                       m[12] * m[2] * m[5]

            inv[3] = -m[1] * m[6] * m[11] + \
                      m[1] * m[7] * m[10] + \
                      m[5] * m[2] * m[11] - \
                      m[5] * m[3] * m[10] - \
                      m[9] * m[2] * m[7] + \
                      m[9] * m[3] * m[6]

            inv[7] = m[0] * m[6] * m[11] - \
                     m[0] * m[7] * m[10] - \
                     m[4] * m[2] * m[11] + \
                     m[4] * m[3] * m[10] + \
                     m[8] * m[2] * m[7] - \
                     m[8] * m[3] * m[6]

            inv[11] = -m[0] * m[5] * m[11] + \
                       m[0] * m[7] * m[9] + \
                       m[4] * m[1] * m[11] - \
                       m[4] * m[3] * m[9] - \
                       m[8] * m[1] * m[7] + \
                       m[8] * m[3] * m[5]

            inv[15] = m[0] * m[5] * m[10] - \
                      m[0] * m[6] * m[9] - \
                      m[4] * m[1] * m[10] + \
                      m[4] * m[2] * m[9] + \
                      m[8] * m[1] * m[6] - \
                      m[8] * m[2] * m[5]

            det = m[0] * inv[0] + m[1] * inv[4] + m[2] * inv[8] + m[3] * inv[12]

            if det == 0:
                return False

            det = 1.0 / det

            inv = [det * i for i in inv]

            self.values = [[m[0], m[1], m[2], m[3]],
                           [m[4], m[5], m[6], m[7]],
                           [m[8], m[9], m[10], m[11]],
                           [m[12], m[13], m[14], m[15]]]
            
            return True   
        else:
            return False

    def matrix_mult(self, matrix):
        """ Multiply this vector by a matrix.  Assuming matrix is a list of lists.

            Example:
            mat = [[1,2,3],[-1,0,1],[3,4,5]]
            Vector(1,2,3).matrix_mult(mat) ->  (14, 2, 26)

        """
        if not all(len(row) == len(self) for row in matrix):
            raise ValueError('Matrix must match vector dimensions')

            # Grab a row from the matrix, make it a Vector, take the dot product,
        # and store it as the first component
        product = tuple(Vector(*row) * self for row in matrix)

        return Vector(*product)

    def inner(self, other):
        """ Returns the dot product (inner product) of self and other vector
        """
        return sum(a * b for a, b in zip(self, other))

    def __div__(self, other):
        if type(other) == type(1) or type(other) == type(1.0):
            divided = tuple(a / other for a in self)
            return Vector(*divided)

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        added = tuple(a + b for a, b in zip(self, other))
        return Vector(*added)

    def __sub__(self, other):
        """ Returns the vector difference of self and other """
        subbed = tuple(a - b for a, b in zip(self, other))
        return Vector(*subbed)

    def __iter__(self):
        return self.values.__iter__()

    def __getitem__(self, key):
        return self.values[key]

    def __repr__(self):
        return str(self.values)

##################################################################


import math
import colorsys

angle = 0
camera = Vector(0, 0, -10, 1)

shape = [#####
         Vector(2, 1, 0, 1), Vector(1, -1, -1, 1), Vector(3, -1, -1, 1),
         Vector(2, 1, 0, 1), Vector(3, -1, -1, 1), Vector(3, -1, 1, 1),
         Vector(2, 1, 0, 1), Vector(3, -1, 1, 1), Vector(1, -1, 1, 1),
         Vector(2, 1, 0, 1), Vector(1, -1, -1, 1), Vector(1, -1, 1, 1),
         #####]

f = 1
n = -1
t = 1
b = -1
r = 1
l = -1

perspective_transform = Matrix(4, 4)
perspective_transform.values =[[2*n/(r-l),      0,              0,              0],
                               [0,              2*n/(t-b),      0,              0],
                               [(r+l)/(r-l),    (t+b)/(t-b),    -(f+n)/(f-n),   -1],
                               [0,              0,              -2*f*n/(f-n),   0]]

vr = 500
vl = 0
vt = 400
vb = 0
viewport_transfrom = Matrix(4, 4)
'''
viewport_transfrom.values =    [[(vr - vl)/ 2,  0,              0,              (vr + vl)/ 2],
                               [0,              (vt - vb)/ 2,   0,              (vt + vb)/ 2],
                               [0,              0,              1.0/2,          1.0/2],
                               [0,              0,              0,              1]]
'''
viewport_transfrom.values =    [[(vr - vl)/ 2,  0,              0,              (vr + vl)/ 2],
                               [0,              (vt - vb)/ 2,   0,              (vt + vb)/ 2],
                               [0,              0,              1.0/2,          1.0/2],
                               [0,              0,              0,              1]]
def drawLine(x1, y1, x2, y2):
    graphics.drawLine(x1 + graphics.width/2, y1 + graphics.height/2, x2 + graphics.width/2, y2 + graphics.height/2, 1, 1, 1)


def drawTriangleList(triList):
    for i in range(0, len(triList), 3):
        drawLine(triList[i][0], triList[i][1], triList[i + 1][0], triList[i+ 1][1])
        drawLine(triList[i + 1][0], triList[i + 1][1], triList[i + 2][0], triList[i+ 2][1])
        drawLine(triList[i + 2][0], triList[i + 2][1], triList[i][0], triList[i][1])

rightV = Vector(1, 0, 0)
heading = Vector(0, 0, 1)


def viewTransform(triList3D, angle, cameraPos):
    global heading, rightV
    ux = 0
    uy = 1
    uz = 0
    t = angle
    transform = Matrix(4,4)
    transform.identity()
    
    #world_transform_matrix
    rotation = Matrix(4, 4)
    rotation.values = [ [math.cos(t)+ux*ux*(1-math.cos(t)),     ux*uy*(1-math.cos(t))-uz*math.sin(t),   ux*uz*(1-math.cos(t))+uy*math.sin(t),   0],
                        [uy*ux*(1-math.cos(t))+uz*math.sin(t),  math.cos(t)+uy*uy*(1-math.cos(t)),     uy*uz*(1-math.cos(t))-ux*math.sin(t),   0],
                        [uz*ux*(1-math.cos(t))-uy*math.sin(t),  uz*uy*(1-math.cos(t))+ux*math.sin(t),  math.cos(t) + uz*uz*(1-math.cos(t)),    0],
                        [0,                                     0,                                      0,                                      1]]
    
    #rotation.inverse()

    dx = cameraPos[0]
    dy = cameraPos[1]
    dz = cameraPos[2]
    
    translation = Matrix(4, 4)
    translation.values = [ [1,  0,  0,  0],
                           [0,  1,  0,  0],
                           [0,  0,  1,  0],
                           [-dx, -dy, -dz, 1]]
    
    viewTransform = translation * rotation

    heading = Vector(*[i[2] for i in rotation.values])
    rightV = Vector(*[i[0] for i in rotation.values])

    
    viewTransform.inverse()
    #viewTransform = viewTransform * perspective_transform

    transformedList = []
    for vertex in triList3D:
        newTri = Vector(vertex[0], vertex[1], vertex[2], 1)
        newTri = newTri * viewTransform

        transformedList.append([newTri[0], newTri[1], newTri[2], newTri[3]])        
    return transformedList    
    
def perspectiveTransform(triList3D):
    triList2D = []
    n = 0
    # frustum cull
    while n < len(triList3D):
        vertex = triList3D[n]
        if vertex[2] < 0:
            # skip the triangle that this vertex is in
            if n % 3 == 0:
                n += 3
                if n >= len(triList3D):
                    break
                else:
                    continue
            elif n % 3 == 1:
                if len(triList2D) >= 1:
                    del triList2D[-1]
                n += 2
                if n >= len(triList3D):
                    break
                else:
                    continue
            elif n % 3 == 2:
                if len(triList2D) >= 1:
                    del triList2D[-1]
                if len(triList2D) >= 1:
                    del triList2D[-1]

                n += 1
                if n >= len(triList3D):
                    break                  
                else:
                    continue

        newTri = Vector(vertex[0], vertex[1], vertex[2], vertex[3])
        newTri = newTri * perspective_transform

        # perspective divide
        newTri = [newTri[0]/newTri[3], newTri[1]/newTri[3], newTri[2]/newTri[3], newTri[3]]

        # clip space cull
        if newTri[2] < -1 or newTri[2] > 1 or newTri[0] < -1 or newTri[0] > 1 \
            or newTri[1] > 1 or newTri[1] < -1:
            # skip the triangle that this vertex is in
            if n % 3 == 0:
                n += 3
                if n >= len(triList3D):
                    break
            elif n % 3 == 1:
                if len(triList2D) >= 1:
                    del triList2D[-1]
                n += 2
                if n >= len(triList3D):
                    break
            elif n % 3 == 2:
                if len(triList2D) >= 1:
                    del triList2D[-1]
                if len(triList2D) >= 1:
                    del triList2D[-1]

                n += 1
                if n >= len(triList3D):
                    break                  
        else:
        
            triList2D.append([newTri[0], newTri[1], newTri[2]])
            n += 1    
        #triList2D.append([newTri[0], newTri[1], newTri[2]])
    return triList2D

def viewportTransform(triList2D, width, height):
    transformedList = []
    for vertex in triList2D:

        newTri = Vector(vertex[0], vertex[1], vertex[2], 1)
        newTri = newTri * viewport_transfrom #* newTri
        transformedList.append([newTri[0], newTri[1]])
        
    return transformedList        


while True:   
    
    if graphics.isKeyPressed(KEY_W):
        camera = camera + 0.1 * heading
    
    if graphics.isKeyPressed(KEY_S):
        camera = camera - 0.1 * heading

    if graphics.isKeyPressed(KEY_A):
        angle += 0.1
        
    if graphics.isKeyPressed(KEY_D):
        angle -= 0.1
    
    graphics.clear(0, 0, 0)
    triList = viewTransform(shape, angle, camera)
    
    triList = perspectiveTransform(triList)
    triList = viewportTransform(triList, 500, 500)
    
    drawTriangleList(triList)


