list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]

sum_list = [x + y for x, y in zip(list_a, list_b)]
print(sum_list)
# for i in range(len(list_b)):
#     sum_list.append(list_a[i] + list_b[i])
# print(sum_list)

# for i, _ in enumerate(list_b):
#     sum_list.append(list_a[i] + list_b[i])
# print(sum_list)
