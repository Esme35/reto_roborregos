'''
Control:
    robot.move_forward()
    robot.rotate_right()
    robot.rotate_left()
    robot.insertCode(password) -> int

Sensors:
    robot.ultrasonicFront() -> int
    robot.getColor() -> string
    robot.detectSimbolLeft() -> int
    robot.detectSimbolRight() -> int
    robot.detectDoorFront() -> bool
'''

def main():
    
    "los errores son por que no se declaro --> robot=Robot()"
    bin=[]
    r=1
    while r == 1:
        i=1
        while i<=2:
            if i == 1:
                izq= robot.detectSimbolLeft()
                if izq== 0 or izq==1:
                    n=[]
                    n.append(izq)
                    bin[:0]=n
                    i=i+1
                else:
                    i=i+1
            else:
                der= robot.detectSimbolRight()
                if der== 0 or der==1:
                    bin.append(der)
                    i=i+1
                else:
                    i=i+1       

        deci=0
        for i in range(len(bin)):

            bit = bin.pop()

            if bit == '1':
                
                deci += pow(2, i)

        resto= deci/2

        if resto == 0:
            ndec="par"
        else:
            ndec= "impar"

        color= robot.getColor()
        if color== 'yellow':
            if ndec== 'par':
                robot.rotate_right()
                robot.move_forward()
            elif ndec == 'impar':
                robot.rotate_left()
                robot.move_forward()
        elif color == 'green':
            if ndec == 'par':
                robot.rotate_left()
                robot.move_forward()
            elif ndec == 'impar':
                robot.rotate_right()
                
                robot.move_forward()
        elif color== 'white':
            puerta= robot.detectDoorFront()
            if puerta== True:
                robot.insertCode(bin)
                robot.move_forward()
            else:
                robot.move_forward()
        else:
            robot.move_forward()
            r=r+1


'''


    robot.move_forward()
    robot.move_forward()
    robot.move_forward()
    robot.rotate_right()
    robot.move_forward()
    robot.insertCode("011")
    robot.move_forward()
    robot.move_forward()
    robot.rotate_left()
    robot.move_forward()
    robot.insertCode("110")
    robot.move_forward()
    robot.rotate_right()
    robot.move_forward()
    robot.move_forward()
    robot.rotate_left()
    robot.move_forward()
    robot.rotate_left()
    robot.move_forward()
    robot.move_forward()
    robot.move_forward()
    robot.rotate_right()
    #get Huffman root node
    root = robot.getHuffmanTree()
    answer = ""
    #add decode code here
    print("Decoded answer: ", answer)
'''
if __name__ == "__main__":
    
    main()

    