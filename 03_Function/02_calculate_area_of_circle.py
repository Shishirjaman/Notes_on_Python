
def calculate_area(rad):
    radius = float(rad)
    area = 3.1416 * radius * radius
    
    return area


# Specify x To close the program
if __name__ == "__main__":
    print("Specify x To close the program!!")
    
    while True:
        rad = input("Enter Radius of the Circle: ")
        if rad == "x":
            print("Code Terminated!!!")
            break
        else:
            area = calculate_area(rad)
            print("Thre area of the circle is "+str(area))