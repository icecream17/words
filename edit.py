file = open("in.txt")
command, path, *words = file.read().split()
file.close()

file = open(path)
oldwords = file.read().split("\n")
file.close()

file = open(path, "w")
if command == "add":
    uniquewords = set(words + oldwords)
    sortedwords = list(uniquewords)
    sortedwords.sort()
    filetext = "\n".join(sortedwords)
    file.write(filetext)
elif command == "delete":
    filteredwords = [word for word in oldwords if not word in words]
    file.write("\n".join(filteredwords))

file.close()
