import math


def input_inf():
    '''
    Input information about amount of chocolates, radius of box
    and the accuracy of the calculations
    '''
    # check the input
    try:
        # create variables and ask user to input required information
        n = int(input("Input amount of chocolates: "))
        r = int(input("Input radius of box: "))
        tch = float(input("Input the accuracy of the calculations: "))
        if n < 0 or r < 0:
            print("Wrong input")
            return 0
        l, s1, s2 = [], [], []
        for i in range(n):
            a1, a2, a3 = map(int, input("Input info: ").split())
            l.append(a1)
            s1.append(a2)
            s2.append(a3)
        return n, r, tch, l, s1, s2
    except:
        print("Wrong input")


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
    with open("result.txt", "w") as file:
        for i in lst:
            file.write(str(i + "\n"))


def check(r, tch, l, s1, s2):
    '''
    Check whether the band matches all the requirements
    '''
    print(type(s1))
    if cycle_len(r) - l * 1.17 <= tch and s1 - cycle_area(r) <= tch \
            and s2 - cycle_area(r) <= tch:
        return True
    else:
        return False


def main_program():
    n, r, tch, l, s1, s2 = input_inf()
    print(s1)
    print(s2)
    res = []
    for i in range(n):
        if check(r, tch, l[i], s1[i], s2[i]):
            res.append((l[i], s1[i], s2[i]))
    # print and write in file the result
    print (res)
    write_file(res)


main_program()
