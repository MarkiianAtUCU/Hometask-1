def read_file(path):
    """
    (str) -> list
    Return list of lines from file that start with key symbols
    'BOOK:', 'NOVL:', 'ADPT:'
    """
    starts = ["NOVL:", "BOOK:", "ADPT"]
    res = []
    with open(path, "r", encoding="utf-8", errors='ignore') as file:
        for i in file:
            for start in starts:
                if i.startswith(start):
                    res.append(i.strip())
    return res


def author_dict(lines_list):
    """
    (str) -> (dict)
    Return dict from list of line, with author name as key and number
    references as value
    """
    res = {}
    for line in lines_list:
        line = line.split(".")[0][6:]
        res[line] = res.get(line, 0) + 1
    return res


def author_set(n, dict_author):
    """
    (int, dict) -> set
    Return set of n authors with highest references
    """
    return set(sorted(list(dict_author.items()), key=lambda i: i[1])[-n:])


def write_author(author_set):
    """
    (set) -> None
    Write authors and number of references to file
    """
    with open("n4_result.txt", "w") as file:
        for i in author_set:
            file.write(i[0] + " " + str(i[1]) + "\n")


def find_literature(n):
    """
    (set) -> None
    """
    lines_list = read_file("literature.list")
    dict_author = author_dict(lines_list)
    authors_set = author_set(n, dict_author)
    write_author(authors_set)


find_literature(int(input('Enter a number: ',)))
