# variable "hero" is declared and is stored as a string: "$$$Superman$$$"
hero = "$$$Superman$$$"

# string is then striped of all characters defined "$" using the strip function
# This is stored in the variable "hero_strip"
# this is then printed and displayed to the user
hero_strip = hero.strip("$")
print(hero_strip)