i=int(input("Select the 3D mesh by giving the values of the serial numbers\n1.Cube\n2.Cuboid\n3.Cylinder"))
if i ==1:
    print("The default unit will be taken as centimeter (cm)")
    u=int(input("Enter the side"))
    def cube (a):
        
        TSA=a*a
        TSA=TSA*6
        vol=a*a*a
        print("The volume of the cube = {volume}cm^3\nThe TSA of the cube{Total}cm^2".format(volume=vol, Total=TSA))
    cube(u)
if i == 2:
     print("The default unit will be taken as centimeter (cm)")
     l=int(input("Enter the lenght of the cuboid "))
     b=int(input("Enter the breadth of the cuboid"))
     h=int(input("Enter the height of the cuboid"))
     def cuboid(a,b,c):
        v=a*b*c
        Tsa=2*(a*b + b*c + c*a)
        print("The volume of the cuboid = {volume}cm^3\nThe TSA of the cube = {Total}cm^2.".format(volume=v, Total=Tsa))
     cuboid(l,b,h)
if i == 3:
     print("The default unit will be taken as centimeter (cm)")
     r = int(input("Enter the radius of the cylinder"))
     h = int(input("Enter the height of the cylinder"))
     def cylinder (a,b):
         vol_1 = 3.14*a*a
         vol_2 = vol_1*b
         TSA_1 = a+b
         TSA_2 = TSA_1 *2*3.14*a

         print("The volume of the cylinder = {volume}cm^3\n The TSA of the cylinder = {Total}cm^2".format(volume=vol_2, Total= TSA_2))
     cylinder(r,h)



