from collections import defaultdict


#recursively print keys in embedded dict



print("----------till here noted......")


ls = [
    {"india": 40, "code": "1001"}, {"pakistan": 20, "code": "1001"},
    {"china": 40, "code": "1001"},
    {"india": 56, "code": "1002"},
    {"pakistan": 14, "code": "1002"},
    {"china": 30, "code": "1002"}
    ]

codes = set([each_dict["code"] for each_dict in ls])
print(codes)

d = defaultdict(dict)
for i in codes:
    d["code"] = i


# print(d)

print("------2--------")


animaldict = {
    "name": "Dog",
    "age": 5,
    "Weight": 4,
    "Country": "US",
    "City": "California"
}

res = {key: animaldict[key] for key in animaldict.keys() - ["name", 'age']}
# print(res)

print("------------dict sort-------------")
dictlang = {'c#': 6, 'GO': 89, 'Python': 4, 'Rust': 10}
for k in sorted(dictlang):
    print(dictlang[k])

print("----How to change the name of key in dictionary.---------")
animaldict = {
    "name": "Dog",
    "age": 5,
    "Weight": 4,
    "Country": "US",
    "City": "California"

}

# animaldict['Animalname'] = animaldict.pop('name')
animaldict.pop('name')
print(animaldict)

print("-------------------")

Fruit = {'Apple': 100, 'banana': 5}
Subject = {'Math': 100, 'English': 98}
animal = {'name': 'Rabbit', 'age': 1}

# nn = {dict for dict in [Fruit, Subject, animal]}
# for i in nn:
#     # pass
#     print(i)

print("--to check number of keys have same value.--")
empdict = {'Racx': 12000, 'Max': 80000, 'Stack': 80000, 'John': 80000}
valuetofind = 80000
count = sum(val == valuetofind for val in empdict.values())
# >>> r= (True,True,False)
# >>> sum(i for i in r)
# 2
print("number of keys have same value : ", count)

print("----------if value is not None-------------")
mutidict = {'lang': 'C#', 'Fruit': 'Apple', 'Subj': None, 'Animal': None}
OutDict = {key: value for (key, value) in mutidict.items() if value is not None}
print(OutDict)

print("19---------remove space in keys-------")
myDict = {'Fr   uit': ['Apple', 'Banana', 'Orange'], 'Sub   ject': ['Phy', 'Math', 'English']}
# myDict = {i.translate({32: None}): j for i, j in myDict.items()} or
myDict = {i.replace(" ", ""): j for i, j in myDict.items()}
print("dict after remove space = ", myDict)


print("..................merge dicts..............")
ls = [
    {"india": 40, "code": "1001"},
    {"pakistan": 20, "code": "1001"},
    {"china": 40, "code": "1001"},
    {"india": 56, "code": "1002"},
    {"pakistan": 14, "code": "1002"},
    {"china": 30, "code": "1002"}
]

codes = set([dict['code'] for dict in ls])
# new_dict = {for d in ls if d['code'] in codes}
new_list = []
for i in list(codes):
    # uniq_codes = {}
    # uniq_codes['code'] = i
    uniq_codes = {'code': i}
    new_list.append(uniq_codes)
print(new_list)

for i in new_list:
    for j in ls:
        if i['code'] == j['code']:
            i.update(j)
print(new_list)

print("---------soert by value........")

inp_dict = { 'a':3,'ab':2,'abc':1,'abcd':0 }
print("Dictionary: ", inp_dict)
sort_dict= dict(sorted((value, key) for (key,value) in inp_dict.items()))
print("Sorted Dictionary by value: ", sort_dict)


print("---------sort by value 2........")
inp_dict1 = { 'a':3,'ab':2,'abc':1,'abcd':0 }
print("Dictionary: ", inp_dict)
sort_dict= dict(sorted(inp_dict1.items(), key=lambda item: item[1]))
print("Sorted Dictionary by value: ", sort_dict)