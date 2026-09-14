"""
The random module is used for generating random data — numbers, names...
"""
import random

# # Any random value
value = random.random()
# print(value)

# # Random floating point values between 1 and 10
float_value = random.uniform(1, 10)
# print(float_value.__round__(2))
# print(round(float_value, 2))

# # Random integers
integer = random.randint(1, 6)
# print(integer)

# # Random choice from a list value
greetings = ["Hello", "Ni hau", "Annyeonghaseyo", "Ohayo Gozaimasu", "Ciao"]

greeting = random.choice(greetings)

# print(greeting + ", Blessing!")

# Multiple random choices from a list
car_brands = ['Bugatti', 'Bentley', 'Rose Royce', 'Toyota']

# or simulating a roulette of different colors
colors = ['Red', 'Black', 'Green']
 
results = random.choices(car_brands, k=10)              # k-value represents the number of times we want to pick a random value

for col in colors:
    print(f"{col.capitalize()} {}")

# An actuall roulette wheel has 18 red and black pockets and 2 Green pockets mkaing it a total of 38.
# We will add  these odds in the random choice  as weights
color_results = random.choices(colors, weights=[18, 18, 2], k=10)  # weights determine the number of chances that a certain value get's picked.          
# from the weights the chances of getting a Green pocket are very slim
# print(color_results)


# randomly shuffling a list of values
deck = list(range(1, 53))
random.shuffle(deck)        # shuffles the list inplace.
# print(deck)

# in order to get 5 random numbers from this deck:
hand = random.sample(deck, k=5)
# print(hand)

# Generating 