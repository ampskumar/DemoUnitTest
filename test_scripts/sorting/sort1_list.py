a = [4, 2, 7, 1]
for i in range(0, len(a)-1):
    if a[i] > a[i+1]:
        temp = a[i]
        a[i] = a[i+1]
        a[i+1] = temp
print(a)  # [2, 4, 1, 7] it sorts only in first iteration

print("--------solution for above-------")
new_list = []
while a:
    min_val = a[0]
    for i in a:
        if i < min_val:
            min_val= i
            print("inside min", min_val)
    new_list.append(min_val)
    print("outside min", min_val)
    a.remove(min_val)
print(new_list) # [1, 2, 4, 7]
