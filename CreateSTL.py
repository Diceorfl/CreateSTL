import sys
import Create

if not Create.check_argc(len(sys.argv)):sys.exit(1)
Zco = []
if not Create.read_file(str(sys.argv[1]),Zco):sys.exit(1)
if len(Zco) < 2:
    print("Not enough data!")
    sys.exit(1)
print("Creating " + str(sys.argv[2]))
print("  1.Creating Triangles")
Triangles = []
Create.create_triangles(Zco,Triangles)
print("  2.Creating Output File")
Outputstr = []
Create.create_output(Triangles,Create.calculate_coeff(Zco),Outputstr)
Create.create_STL(str(sys.argv[2]),Outputstr)
print("Done!")
