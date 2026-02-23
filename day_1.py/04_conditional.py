# stock1 = "vanilla"
# stock2 = "green tea"
# stock3 = "lemon"
# stock4 = "chocolate"


# Task 1.2
# Clue - String methods
# Handle the extra space & letter case
# Case1:
# Please enter your fav 🍧?:      vaNillA
# Yes, we have vanilla in stock

# Case 2:
# Please enter your fav 🍧?:   pisTa
# Sorry, we ran out of pista


# Task 1.1
# Compare Two People’s Heights (Taller / Same Height)
# Hint - input
# Better - abs()
# Expected Output -
# Case 1:
# Please tell me the captain name?: Luffy
# Please tell me the vice captain name?: Zoro
# Please tell me the height of Luffy?: 173
# Please tell me the height of Zoro?: 163
# Luffy is taller than Zoro by 10cm

# Case 2:
# Please tell me the captain name?: Luffy
# Please tell me the vice captain name?: Zoro
# Please tell me the height of Luffy?: 173
# Please tell me the height of Zoro?: 185
# Zoro is taller than Luffy by 12cm


# Case 3
# Please tell me the captain name?: Luffy
# Please tell me the vice captain name?: Zoro
# Please tell me the height of Luffy?: 173
# Please tell me the height of Zoro?: 173
# Luffy and Zoro are of same height


captain_name = input("Enter the Captain Name:")
vice_captain_name = input("Enter the Vice Captain Name:")
captain_height = int(input(f"Enter the {captain_name} height:"))
vice_captain_height = int(input(f"Enter the {vice_captain_name}:"))

if captain_height > vice_captain_height:
    height_diff = captain_height - vice_captain_height
    print(f"{captain_name} is taller than {vice_captain_name} by {height_diff}cm")

elif captain_height < vice_captain_height:
    height_diff = vice_captain_height - captain_height
    print(f"{vice_captain_name} is taller than {captain_name} by {height_diff}cm")

else:
    print(f"{captain_name} and {vice_captain_name} are of same height")



