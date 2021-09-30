def foo(character, filepath="fruits.txt"):
    file = open("fruits.txt")
    content = file.read()
    return content.count(character)
print(file=(foo("mango")))