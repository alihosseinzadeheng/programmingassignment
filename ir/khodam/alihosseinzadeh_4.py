li = [3, 5, 9, 12, 65, 55, 88, 99, 2, 4]
edited_li = li

print("\tDefined list:")
print(li)

def extract_small_number(lis):
    for num in lis:
        small = num
    for num1 in lis:
        if num1 <= small:
            small = num1
    return small

def extract_big_number(lis):
    for num in lis:
        big = num
    for num1 in lis:
        if num1 >= big:
            big = num1
    return big

# Extracted first small number (smallest)
first_small_number = extract_small_number(li)

# Remove first small number from main list
edited_li.remove(first_small_number)
# Extracted first small number
second_small_number = extract_small_number(edited_li)
# Refresh edited list
edited_li = li

# Extracted first big number (biggest)
first_big_number = extract_big_number(li)

# Remove first big number from main list
edited_li.remove(first_big_number)
# Extracted first big number
second_big_number = extract_big_number(edited_li)
# Refresh edited list (not necessary!)
edited_li = li

# Extract desired list
extracted_list = [first_small_number, second_small_number, second_big_number, first_big_number]

print("\n\tTwo small and two big ones  in a list:")
print(extracted_list)

