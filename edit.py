def create_file(path):
    try:
        open(path, "x").close()
    finally:
        pass

def read_lines(path):
    file = open(path)
    lines = file.read().split("\n")
    file.close()
    return lines

def update_file(command, path, words):
    create_file(path)
    oldwords = set(read_lines(path))
    words = set(words)
    with open(path, "w") as file:
        if command == "add":
            uniquewords = words | oldwords
            sortedwords = sorted(uniquewords)
            file.write("\n".join(sortedwords) + "\n")
        elif command == "delete":
            filteredwords = oldwords - words
            file.write("\n".join(filteredwords) + "\n")


file = open("in.txt")
command, path, *words = file.read().split()
file.close()

update_file(command, path, words)
update_file(command, 'words.txt', words)
