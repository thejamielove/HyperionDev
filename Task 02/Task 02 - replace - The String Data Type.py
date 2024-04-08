# variable "lazy_dog" is declared and is stored as a string: "The!quick!brown!fox!jumps!over!the!lazy!dog!."
lazy_dog = "The!quick!brown!fox!jumps!over!the!lazy!dog!."

# String is put through the replace function twice:
# 1st - finding "!" and replacing with a blank space " "
# 2nd - finding the " ." at the end of the sentence and replacing with "."  - to get rid of the space
# This is stored in the variable "lazy_dog_replace"
lazy_dog_replace = lazy_dog.replace("!"," ").replace(" .",".")

# "lazy_dog_replace" variable, is now printed to the user
# This is then re-printed in all upper case (.upper function)
# Lastly, this is then reprinted in all upper case, but in reverse order (backwards) using slice [begin:end:step]
print(lazy_dog_replace)
print(lazy_dog_replace.upper())
print(lazy_dog_replace.upper()[::-1])