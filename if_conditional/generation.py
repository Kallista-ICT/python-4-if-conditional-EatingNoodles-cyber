birth_year = int(input("please enter your birth year(e.g, 1990): "))

if birth_year < 1928:
    generation = "Silent Generation"
elif birth_year < 1946:
    generation = "Baby Boomer"
elif birth_year < 1965:
    generation = "Generation X"
elif birth_year < 1981:
    generation = "Millennials"
elif birth_year < 2013:
    generation = "Generation Z"
else: 
    generation = "Generation Alpha"

print(f"you belong to: {generation}")