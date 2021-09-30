def code_maker(phrase):
    interrogatives = ("how","why","who")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("say something: ")
    if user_input == "\end":
        break
    else:
        results.append(code_maker(user_input))
print(" ".join(results))
