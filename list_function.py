states_of_india = ["UP", "MP", "JK", "UK"]

print(states_of_india[-4])

states_of_india[1] = "Rajsthan"

print(states_of_india)

# to append something at end of the list, we can use append function

states_of_india.append("Maharashtra") # this will append Maharashtra to end of the list

print(states_of_india)

# with extend function we can extend existing list

states_of_india.extend(["Andhra", "Telangana", "Odisa"])

print(states_of_india)