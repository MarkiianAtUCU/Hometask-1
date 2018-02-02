def perfect_split(msg):
    """
    (str) -> list of string

    Function splits line of text into list and splits sublists of that list

    >>> perfect_split("abc def,klm opq,rst,xyz")
    [['abc'], ['def', 'klm'], ['opq', 'rst', 'xyz']]
    """
    result = []
    splitted = msg.split()
    for element in splitted:
        if element == r"\N":
            result.append([])
        else:
            result.append((element.split(",")))
    return result


def read_file(path):
    """
    (str) -> set

    Return set of lines from file
    """
    result = set()
    with open(path, "r") as file:
        file.readline()
        for item in file:
            result.add(item)
    return result


def directors_dict(lines_set, flag):
    """
    (set) -> dict

    Return dict from set of lines with film id as key
    abd list is directors or writers as value
    """
    result = {}
    if flag == "directors":
        position = 1
    elif flag == "writers":
        position = 2
    for element in lines_set:
        splitted = perfect_split(element)

        result[splitted[0][0]] = splitted[position]
    return result


def directors_max(dict_persons):
    """
    (dict) -> list
    Return list of films with highest number of person
    """
    result = []
    maximum = 0
    for key, value in dict_persons.items():
        if len(value) > maximum:
            maximum = len(value)
            result = []
            result.append([key, value])
        elif len(value) == maximum:
            result.append([key, value])
    return result


def write_films_id(films_id):
    """
    (list) -> None

    Write films id and person id to file
    """
    with open("n6_result.txt", "w") as file:
        for element in films_id:
            file.write("Film id: " + str(element[0]) + "\n")
            file.write("Director's/writer's id:\n")
            for director in element[1]:
                file.write(str(director) + "\n")
            file.write("\n")


def find_directors_id(flag='directors'):
    """
    (str) -> None
    """
    file = read_file("data1.tsv")
    role_dictionary = directors_dict(file, flag)
    maximum_list = directors_max(role_dictionary)
    write_films_id(maximum_list)
    print("Done!")

try:
    find_directors_id(input("Input version (writers/directors): "))
except:
    print("Wrong input!")
