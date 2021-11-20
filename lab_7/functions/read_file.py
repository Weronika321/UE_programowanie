# simport csv


def read_file(filename: str):  # -> csv.reader:
    file = open(filename, "r", newline="\n", encoding="utf-8")
    return file
