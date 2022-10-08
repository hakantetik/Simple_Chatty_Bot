#  You can experiment here, it won’t be checked

family = {
    "Mary": 49,
    "Andrew": 50,
    "Dora": 21,
    "John": 15,
    "Ann": 75
          }

for i in family.keys():
    if family[i] > 65 or family[i] < 21:
        print(i, True)
    else:
        print(i, False)
