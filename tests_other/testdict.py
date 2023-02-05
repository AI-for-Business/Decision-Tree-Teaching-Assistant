dict1 = {
    "t1": "e1",
    "t2": "e2",
    "t3": "e3"
 }

dict2 = {
    "t4": "e4",
    "t5": "e5",
    "t6": "e6"
}

test_string1 = "t2"
test_string2 = "t4"

if test_string1 in dict1:
    print(dict2.get(test_string2))

a = "t7"
b = "e7"

dict2[a] = b

print(dict2.get(a))
print(len(dict2))
