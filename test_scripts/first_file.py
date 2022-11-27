# res = "today is today was"
# my_list = res.split()
#
# count = 0
# new_list = []
# for i in my_list:
#     if i=="today":
#         count+=1
#     if count==2:
#         i="tomorrow"
#     new_list.append(i)
# # print(new_list)


# chck consonants or vowels
# char = input("Enter a string :")
# if char in ("aeiou" or "AEIOU"):
#     print(f"{char} : is consonant")
# else:
#     print(f"{char} : is vowel")



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
