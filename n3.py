def read_file(path):
    """
    (str) -> (list)
    Return list of lines from file (path to file)
    """
    res = []
    with open(path, "r") as file:
        for i in range(14):
            file.readline()
        for i in file:
            res.append(i.strip())
    return res


def country_dict(lines_list, year):
    """
    (list) -> (dict)
    Return dict from list of lines with country as key and name as value
    """
    res = {}
    n = 0
    for line in lines_list:
        if "(" + str(year) in line:
            n += 1
            country = line.split("\t")[-1]
            if country in res:
                res[country].append(line.split("\t")[0])
            else:
                res[country] = [line.split("\t")[0]]
    return res


def country_num(dict_country):
    """
    (dict)->(list)
    Return sorted list of tuple with country and number of films
    """
    res = []
    for i in dict_country:
        res.append((i, len(dict_country[i])))
    return sorted(res, key=lambda name: name[1], reverse=True)


def write_films(film_list):
    """
    (list) -> None
    Write country and number of films to file
    """
    with open("n3_result.txt", "w") as file:
        for i in film_list:
            file.write(str(i))
            file.write("\n")


def films_year(year):
    """
    (int -> None)
    Program read from file country and amount of films that were or will be
    released in a certain year. Function return sorted list countries with
    the bigest amount of films in recession. Results are written to the file.
    """
    cont = read_file("countries.list")
    cont = country_dict(cont, year)
    cont = country_num(cont)
    write_films(cont)


films_year(int(input("Enter a year's number: ")))
