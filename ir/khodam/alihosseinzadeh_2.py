li = [2, 5, 10, 12, 26, 26, 50, 60, 100]
insertable_num = 13
index = 0

for num in li:
    if num < insertable_num:
        index = index + 1
        continue

li.insert(index - 1, insertable_num)
print(li)
