def update_file(command, path, words):
    file = open(path)
    oldwords = file.read().split("\n")
    file.close()
    
    file = open(path, "w")
    if command == "add":
        uniquewords = set(words + oldwords)
        sortedwords = list(uniquewords)
        sortedwords.sort()
        file.write("\n".join(sortedwords) + "\n")
    elif command == "delete":
        filteredwords = [word for word in oldwords if not word in words]
        file.write("\n".join(filteredwords) + "\n")
    
    file.close()



file = open("in.txt")
command, path, *words = file.read().split()
file.close()

update_file(command, path, words)
update_file(command, 'words.txt', words)
