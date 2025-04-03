import math

try:
    user_shapes = input("Enter the 3D shape you want to calculate the volume for (Cube, Sphere, Cone, Tetrahedron, Triangular Pyramid, Triangular Prism, Cuboid, Cylinder, Octahedron, Rectangular Pyramid, Ellipsoid, Dodecahedron, Icosahedron, Frustum of a Cone, Frustum of a Pyramid, Pyramid)? ").strip().lower()
except ValueError:
    print("Invalid input. Please enter a valid shape name.")
    exit()

try:
    if user_shapes == "cube":
        side = float(input("Enter the length of a side: "))
        volume = side ** 3
        print(f"The volume of the cube is {volume}")
    elif user_shapes == "sphere":
        radius = float(input("Enter the radius: "))
        volume = (4/3) * math.pi * radius ** 3
        print(f"The volume of the sphere is {volume}")
    elif user_shapes == "cone":
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        volume = (1/3) * math.pi * radius ** 2 * height
        print(f"The volume of the cone is {volume}")
    elif user_shapes == "tetrahedron":
        side = float(input("Enter the length of a side: "))
        volume = (side ** 3) / (6 * math.sqrt(2))
        print(f"The volume of the tetrahedron is {volume}")
    elif user_shapes == "triangular pyramid":
        base_area = float(input("Enter the area of the base: "))
        height = float(input("Enter the height: "))
        volume = (1/3) * base_area * height
        print(f"The volume of the triangular pyramid is {volume}")
    elif user_shapes == "triangular prism":
        base_area = float(input("Enter the area of the base: "))
        height = float(input("Enter the height: "))
        volume = base_area * height
        print(f"The volume of the triangular prism is {volume}")
    elif user_shapes == "cuboid":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        height = float(input("Enter the height: "))
        volume = length * width * height
        print(f"The volume of the cuboid is {volume}")
    elif user_shapes == "cylinder":
        radius = float(input("Enter the radius: "))
        height = float(input("Enter the height: "))
        volume = math.pi * radius ** 2 * height
        print(f"The volume of the cylinder is {volume}")
    elif user_shapes == "octahedron":
        side = float(input("Enter the length of a side: "))
        volume = (1/3) * math.sqrt(2) * side ** 3
        print(f"The volume of the octahedron is {volume}")
    elif user_shapes == "rectangular pyramid":
        base_area = float(input("Enter the area of the base: "))
        height = float(input("Enter the height: "))
        volume = (1/3) * base_area * height
        print(f"The volume of the rectangular pyramid is {volume}")
    elif user_shapes == "ellipsoid":
        a = float(input("Enter the semi-major axis (a): "))
        b = float(input("Enter the semi-minor axis (b): "))
        c = float(input("Enter the semi-minor axis (c): "))
        volume = (4/3) * math.pi * a * b * c
        print(f"The volume of the ellipsoid is {volume}")
    elif user_shapes == "dodecahedron":
        side = float(input("Enter the length of a side: "))
        volume = ((15 + 7 * math.sqrt(5)) / 4) * side ** 3
        print(f"The volume of the dodecahedron is {volume}")
    elif user_shapes == "icosahedron":
        side = float(input("Enter the length of a side: "))
        volume = (5 * (3 + math.sqrt(5)) / 12) * side ** 3
        print(f"The volume of the icosahedron is {volume}")
    elif user_shapes == "frustum of a cone":
        radius1 = float(input("Enter the radius of the bottom base: "))
        radius2 = float(input("Enter the radius of the top base: "))
        height = float(input("Enter the height: "))
        volume = (1/3) * math.pi * height * (radius1 ** 2 + radius1 * radius2 + radius2 ** 2)
        print(f"The volume of the frustum of the cone is {volume}")
    elif user_shapes == "frustum of a pyramid":
        base_area1 = float(input("Enter the area of the bottom base: "))
        base_area2 = float(input("Enter the area of the top base: "))
        height = float(input("Enter the height: "))
        volume = (1/3) * height * (base_area1 + base_area2 + math.sqrt(base_area1 * base_area2))
        print(f"The volume of the frustum of the pyramid is {volume}")
    elif user_shapes == "pyramid":
        base_area = float(input("Enter the area of the base: "))
        height = float(input("Enter the height: "))
        volume = (1/3) * base_area * height
        print(f"The volume of the pyramid is {volume}")
    else:
        print("Shape not recognized.")
except ValueError:
    print("Invalid input. Please enter valid dimensions.")