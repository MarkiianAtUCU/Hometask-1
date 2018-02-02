import math


def input_inf():
    '''
    Input information about amount of chocolates, radius of box
    and the accuracy of the calculations
    '''
    # create variables and ask user to input required information
    n = int(input("Input amount of chocolates: "))
    r = int(input("Input radius of box: "))
    e = float(input("Input the accuracy of the calculations: "))
    if n < 0 or r < 0:
        print("Wrong input")
        return 0
    l, s1, s2 = [], [], []
    for i in range(n):
        a1, a2, a3 = map(int, input("Enter Triples of value:\n\
Length of rope, Area of first chocolate bar, \
Area of second chocolate bar (1 2 3): ").split())
        l.append(a1)
        s1.append(a2)
        s2.append(a3)
    return n, r, e, l, s1, s2


def cycle_len(r):
    '''
    Count a length of a cycle
    '''
    return 2 * math.pi * r


def cycle_area(r):
    '''
    Count an area of a cycle
    '''
    return math.pi * r * r


def write_file(lst):
    '''
    Write the result to file
    '''
    with open("n2_result.txt", "w") as file:
        for i in lst:
            file.write(str(i) + "\n")


def check(r, e, l, s1, s2):
    '''
    Check whether the band maees all the requirements
    '''
    if cycle_len(r) - l * 1.17 <= e and s1 - cycle_area(r) <= e \
            and s2 - cycle_area(r) <= e:
        return True
    else:
        return False


def main_program():
    """
    This function takes info about amount of chocolates, radius of box
    and the accuracy of the calculations and return the length of the ropes
    that can strap the box. Results are written to the file.
    """
    try:
        n, r, e, l, s1, s2 = input_inf()
        res = []
        for i in range(n):
            if check(r, e, l[i], s1[i], s2[i]):
                res.append((l[i], s1[i], s2[i]))
        # print and write in file the result
        write_file(res)
    except:
        print("Wrong input!")


main_program()
