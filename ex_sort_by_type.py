from collections import defaultdict
my_list = [0, "a", "b", "c", "d", "e", 'f', 12, 24, "G^^G"]

data = defaultdict(list)

for x in my_list:
    data[type(x)].append(x)

print(data[str])
print(data[int])