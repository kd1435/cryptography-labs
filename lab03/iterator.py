# From limited time spent on "researching":
# Appending to a list you are iterating over probably isn't a good idea
# Good food for thought/depth though

text = list("abc")
textIter = iter(text)
for i in range(10):
    try:
        print(next(textIter))
        text.append("d")
    except StopIteration:
        print("StopIteration exception raised and caught")
        break