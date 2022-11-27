brackets = {"(": ")", "{": "}", "[": "]"}
s = "()){}}"
for k, v in brackets.items():
    if (s.count(k)) == (s.count(v)):
        print(f"ley is :{k}, value is {v}")
        print(True)
        print("--------------")
    else:
        print(False)

for k, v in brackets.items():
    print(brackets.items())