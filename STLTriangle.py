class STLTriangle:

    def __init__(self,A0,A1,A2):
        #A0,A1,A2 = [x,y,z]
        self._A = (A0,A1,A2) #([x0,y0,z0],[x1,y1,z1],[x2,y2,z2])
        point1 = (A1[0] - A0[0],A1[1] - A0[1],A1[2] - A0[2]) #A1 - A0
        point2 = (A2[0] - A0[0],A2[1] - A0[1],A2[2] - A0[2]) #A2 - A0
        #Векторное произведение
        #Cross Product
        X = point1[1]*point2[2] - point2[1]*point1[2]
        Y = -1.0*(point2[2]*point1[0] - point2[0]*point1[2])
        Z = point2[1]*point1[0] - point2[0]*point1[1]
        self._Normal = (X,Y,Z)

    def getX(self,i):
        if i not in range(0,3):return None
        return self._A[i][0]

    def getY(self,i):
        if i not in range(0,3):return None
        return self._A[i][1]

    def getZ(self,i):
        if i not in range(0,3):return None
        return self._A[i][2]

    def getNormal(self,i):
        if i not in range(0,3):return None
        return self._Normal[i]

if __name__ == "__main__":main()
