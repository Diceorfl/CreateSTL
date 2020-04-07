from STLTriangle import STLTriangle
from pathlib import Path

def check_argc(size):
  if size != 3:
    print("Example: CreateSTL.py input.txt output.STL")
    return False
  return True

def check_input_file_name(filename):
  if not Path(filename).is_file():
    print("File doesn`t exist")
    return False
  return True

#Если длина меньше 2 или != длине первой строки(задает размер для всех строк),
# то не получится создать пары треугольников
#If length < 2 or != lenght of first string then this is the wrong size for
#creating triangles
def Sizecontrol(index,size,lengthcontrol):
  if lengthcontrol == 0: lengthcontrol = size
  if size < 2 or size != lengthcontrol:
    print("Line number ",index," is the wrong size!")
    return False
  return True

def ReadFile(filename,Zco):
  if not check_input_file_name(filename):
    return False
  try:
    input = open(filename,"r")
  except IOError:
    print("File not available")
    return False
  print("Get information from " + filename)
  lengthcontrol = 0
  for index,line in enumerate(input,1):
    if len(line) == 0: continue
    Z = list(map(int,line.split("\t")))
    if not Sizecontrol(index,len(Z),lengthcontrol): return False
    Zco.append(Z)
  input.close()
  return True

#Высчитывает коэффициенты для нормирования по X
#Calculates coefficients for normalization by X
def CalculateCoeff(Zco):
  Xcoef = 1.0
  Ycoef = len(Zco[0])/len(Zco)
  Zmax = max(Zco[0])
  Zmin = min(Zco[0])
  for i in range(1,len(Zco)):
    imax = max(Zco[i])
    imin = min(Zco[i])
    if Zmax < imax: Zmax = imax
    if Zmin > imin: Zmin = imin
  Zcoef = len(Zco[0])/(Zmax - Zmin)
  return(Xcoef,Ycoef,Zcoef)

#Создает треугольники между i и i+1 строкой
#Creates triangles between i and i + 1 line
def CreateTriangles(Zco,Triangles):
  for i in range(0,len(Zco)-1):
    for j in range(0,len(Zco[0])-1):
      ABC1 = STLTriangle((j,i,Zco[i][j]),(j+1,i,Zco[i][j+1]),(j,i+1,Zco[i+1][j]))
      ABC2 = STLTriangle((j,i+1,Zco[i+1][j]),(j+1,i+1,Zco[i+1][j+1]),(j+1,i+1,Zco[i][j+1]))
      Triangles.append(ABC1)
      Triangles.append(ABC2)

#Создает треугольник в формате STL
#Creates a triangle in STL format
def CreateOutput(Triangles,Coefficient,Outputstr):
  Outputstr.append("solid STL_OBJECT" + "\n")
  for Triangle in Triangles:
    Outputstr.append("   facet normal " + str(Triangle.getNormal(0)) + " " + str(Triangle.getNormal(1)) + " " + str(Triangle.getNormal(2)) + "\n" +
    "      outer loop" + '\n' +
    "         vertex " + str(Triangle.getX(0)*Coefficient[0]) + " " + str(Triangle.getY(0)*Coefficient[1]) + " " + str(Triangle.getZ(0)*Coefficient[2]) + "\n" +
    "         vertex " + str(Triangle.getX(1)*Coefficient[0]) + " " + str(Triangle.getY(1)*Coefficient[1]) + " " + str(Triangle.getZ(1)*Coefficient[2]) + "\n" +
    "         vertex " + str(Triangle.getX(2)*Coefficient[0]) + " " + str(Triangle.getY(2)*Coefficient[1]) + " " + str(Triangle.getZ(2)*Coefficient[2]) + "\n" +
    "      endloop" + '\n' +
    "   endfacet" + '\n')
  Outputstr.append("endsolid")

def CreateSTL(filename,Outputstr):
  output = open(filename,"w")
  for line in Outputstr:
    output.write(line)
  output.close()

if __name__ == "__main__":main()
