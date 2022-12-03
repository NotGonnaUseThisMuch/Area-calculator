def areacalc():
    area = 0
    pi = 3.14
    uinput = input("Enter what shape you would like to find the area of")

    if uinput == "square":
        length= int(input("What is the length of one of the sides?"))
        print(length*length)

    elif uinput == "circle":
        radius = int(input("What is the radius of the circle?"))
        print(pi*radius*radius)
    
    elif uinput == "rectangle":
        length = int(input("Enter one of the sides"))
        length2 = int(input("Enter the other side"))
        print(length*length2)
    
    elif uinput == "triangle":
        base = int(input("Enter the value of the base"))
        height = int(input("Enter the value of the height"))
        print(0.5*base*height)
areacalc()