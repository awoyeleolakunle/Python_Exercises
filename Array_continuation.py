arr = ["hi", "hi", "hello"]
for i in range(5):
    arr.append("Hi")
    print(arr)

c14 = arr.copy()
print(c14)
print(c14.count("hi"))

set_val = {1, 1, 2, 3, 4, 5, 6, 6, 7, 4, 8}
count = 0
user_input = [int(input(" enter numbers "))]

for i in range(len(set_val)):
    if user_input == set_val:

        print(user_input)