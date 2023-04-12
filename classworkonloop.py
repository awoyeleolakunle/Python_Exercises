a = "hello boss baby"
to_be_found = "b"

for i in range(len(a)):
    if a[i] == to_be_found:
        print(f"{a[i]} was found at the index of {i} ")

print()
    # print(a.split("b"))
for i in range(len(a)):
    if a[i] != to_be_found:
        print(f"{a[i]} was found at the index of {i} ")
# print(f"{a[i]!=to_be_found} was found at the index of {i}")
