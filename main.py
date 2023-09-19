# Read two phrases from the user
phrase1 = input()
phrase2 = input()

# Check if both phrases match
if phrase1 == phrase2:
    print("Both phrases match")

# Check if phrase1 is found within phrase2
elif phrase1 in phrase2:
    print(f"{phrase1} is found within {phrase2}")

# Check if phrase2 is found within phrase1
elif phrase2 in phrase1:
    print(f"{phrase2} is found within {phrase1}")

# If none of the above conditions are met, there are no matches
else:
    print("No matches")
