from collections import Counter

order = []
count = Counter()
while(True):
    item = raw_input()
    item.strip()
    if item == "stop":
        break
    count[item] += 1
    if count[item] == 1:
        order.append(item)
for item in order:
    if count[item] == 1:
        print count[item], item
    else:
        print count[item], item+"s"
