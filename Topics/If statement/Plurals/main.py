number = int(input())
word = input()

# write a condition for plurals
if number != 1:
    if word[:-1] == "s":
        word = word + "'"
    else:
        word += "s"


print(number, word)
