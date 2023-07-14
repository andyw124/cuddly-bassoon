def triangle(height,width,size):
    for i in range(height):
        for q in range(height-i,0,-1):
            for z in range(width*size):
                print(" ",end="")
        for j in range(i):
            print("*",end=" ")
            for z in range(width*size):
                print(" ",end="")
        print()

triangle(12,1,3)