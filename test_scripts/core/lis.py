a = [2, 3, 4]
print(a)
c = a
c.append(5)
print("after appending")
print("printing a")
print(a)  #  [2,3,4,5]

print("------lists to dict----------")
names = ["amp", "pmp", "pnp"]
ages = [30, 26, 78]
false_ages = [4, 5, 6]

name_and_age = {k: str(v)+" "+str(fv) for k, v, fv in zip(names, ages, false_ages)}
# print(name_and_age)
# print(type(zip(names, ages)))
for i in zip(names, ages, false_ages):
    pass
    # print(i,type(i))

print("-----diff len list values to dict----")
print("------lists to dict----------")
names = ["amp", "pmp", "pnp"]
ages = [30, 26]
# false_ages = [4, 5]

name_and_age = {k: str(v) for k, v in zip(names, ages)}
print(name_and_age)
# print(type(zip(names, ages)))
for i in zip(names, ages):
    print(i, type(i))
