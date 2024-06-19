# You are working in a team of developers.
# Another developer has written the code to import the names in the inputs
# You can run the code to see what this names list looks like.
# Then change the names in the input to see how it imports the names.

# 🚨 Remember to remove the print statement above when you submit.
import random
start = 0
end = len(names) - 1
random_name = names[random.randint(start, end)]
print(f"{random_name} is going to buy the meal today!")