text =(
["1 ŠANTVAYAIOPAASAKDŲ"],
["2 LIIĄŠŠAŠNIIGASSAEK"],
["3 IIEEŠTTSSIRDRUTITS"],
["4 KUĄIYUNIVJARŽIKIEI"],
["5 ĖVRMKKTIYOSĖIAAPBŠ"])

length = len(text)

print(length)

for index, line in enumerate(text): 
    for i in range(length):
        print(text[i])
        for j in range(index + 1, length - 1):
            print(text[j])
    print('\n')