def code_maker(phrase):
    interrogatives = ("how","why","who")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

print(code_maker("how are you"))