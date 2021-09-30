def mean(value):
    if type(value)==dict:
        the_mean= sum(value.values())/len(value)
    else:
        the_mean= sum(value)/len(value)

    return the_mean
monday_tempretures=[8, 9, 4]
student_grades={"marry": 9,"sim": 8, "john": 7}

print(mean(student_grades))