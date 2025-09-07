import itertools

text = [
    "1 ŠANTVAYAIOPAASAKDŲ",
    "2 LIIĄŠŠAŠNIIGASSAEK",
    "3 IIEEŠTTSSIRDRUTITS",
    "4 KUĄIYUNIVJARŽIKIEI",
    "5 ĖVRMKKTIYOSĖIAAPBŠ"
]

for perm in itertools.permutations(text):
    for line in perm:
        print(line)
    print()
