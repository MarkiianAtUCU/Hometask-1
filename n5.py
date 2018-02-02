def read_file(path):
    """
    (str) -> (set)
    Return set of lines from file.

    :param path:
    :return:
    """
    result = set()
    with open(path, "r") as file:
        file.readline()
        for item in file:
            result.add(item)
    return result


def votes_dict(set_file, num_v):
    """
    (set, int) -> (dict)
    Return dict from set of lines if number of votes > num_v.

    :param set_file:
    :param num_v:
    :return:
    """
    dct_votes = {}
    for elements in set_file:
        elements = elements.split()
        if int(elements[2]) >= num_v:
            dct_votes[elements[0]] = float(elements[1])
    return dct_votes


def films_id(n, votes_dict):
    """
    (int, dict) -> (set)
    Return set of n films id with highest rating.

    :param n:
    :param votes_dict:
    :return:
    """
    result = set()
    # create a list of films and sort it
    lst_of_film = [(vote, votes_dict[vote]) for vote in votes_dict]
    lst_of_film = sorted(lst_of_film, key=lambda i: i[1], reverse=True)
    # use the lst_of_film for result set
    try:
        for i in range(n):
            result.add(lst_of_film[i][0])
    except:
        print("Not enough films")
    return result


def write_films_id(set_films_id):
    """
    (set) -> None
    Write films_id to file.

    :param set_films_id:
    :return:
    """
    with open("n5_result.txt", "w") as file:
        for films in set_films_id:
            file.write(films + "\n")

def find_films_id(n, num_v):
    """
    (int, int) -> None

    :param n:
    :param num_v:
    :return:
    """
    set_file = read_file("data.tsv")
    dict_votes = votes_dict(set_file, num_v)
    set_films_id = films_id(n, dict_votes)
    write_films_id(set_films_id)
    print("Done!")

try:
    n = int(input("Enter number of films: "))
    votes_number = int(input("Enter minimal number of votes: "))
    find_films_id(n, votes_number)
except:
    print("Wrong input!")
