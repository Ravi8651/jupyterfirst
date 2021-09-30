def weather_condition(temperature):
    if temperature > 7:
        return "warm"
    else:
        return "cold"

user_input=float(input("enter temperature:"))
print(weather_condition(user_input))
