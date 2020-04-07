import sys
import Create

if not Create.check_argc(len(sys.argv)):sys.exit(1)
Zco = []
if not Create.ReadFile(str(sys.argv[1]),Zco):sys.exit(1)
if len(Zco) < 2:
    print("Not enough data!")
    sys.exit(1)
print("Creating " + str(sys.argv[2]))
print("  1.Creating Triangles")
Triangles = []
Create.CreateTriangles(Zco,Triangles)
print("  2.Creating Output File")
Outputstr = []
Create.CreateOutput(Triangles,Create.CalculateCoeff(Zco),Outputstr)
Create.CreateSTL(str(sys.argv[2]),Outputstr)
print("Done!")
