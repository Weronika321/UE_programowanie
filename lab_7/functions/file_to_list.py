from io import TextIOWrapper
from classes.Movie import Movie


def file_to_list(file_reader: TextIOWrapper) -> list:
    result = []
    for row in file_reader.readlines():
        row_list = list(row.split(","))
        result.append(Movie(row_list[0], row_list[1], row_list[2]))

    return result
