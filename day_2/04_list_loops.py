flowers = ["💐", "🌷", "🌼", "🌷", "🌺"]

# Task 1.1 - Print all the flower using for loop
# Hint - range, len

# Expected output
# Flower 1 - 💐
# Flower 2 - 🌷
# Flower 3 - 🌼
# Flower 4 - 🌷
# Flower 5 - 🌺
flowers = ["💐", "🌷", "🌼", "🌷", "🌺"]


for i in range(len(flowers)):
    print(f"Flower {i + 1} - {flowers[i]}")






# Task 1.2: Double all the numbers
marks = [80, 90, 100, 60, 85]

# Output
# print(marks) -> [160, 180, 200, 120, 170]


# Task 1.2: Double all the numbers
marks = [80, 90, 100, 60, 85]
#first way
#when you want only value
#Doubling the numbers using list comprehension
doubled_marks = [mark * 2 for mark in marks]
print(doubled_marks)




marks = [80, 90, 100, 60, 85]

#second way
# when you want index value
for i in range(len(marks)):
    marks[i] = marks[i] * 2
print(marks) 





# Task 1.3: Double the power
powers = [2000, 3000, 4000, 1500]
doubled_powers= [power * 2 for power in powers]
print(doubled_powers)


# Output
# doubled_powers -> [4000, 6000, 8000, 3000]
# powers -> [2000, 3000, 4000, 1500]


# ## Task 1.4
# Find longer names (>= 6 letter)

characters = ["Hello kitty", "Goku", "Pikachu", "Luffy", "Yuji Itadori", "Levi"]

# ### Expected Output
# ['Hello kitty', 'Pikachu', 'Yuji Itadori']
greater_characters = [character for character in characters if len(character) > 6 ]
print(greater_characters)