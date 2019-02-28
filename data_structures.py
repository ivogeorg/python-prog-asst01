letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
numbers = [0, 1, 2, 3, 4, 5, 6, 7]
floats = [1.2, 3.4, 6.7, 1.01, 4.9, 12.8, 5.45]

strings = [a + str(b) for (a, b) in zip(letters, numbers)]

print(strings)

# strings = []
# for (a, b, c) in zip(letters, numbers, floats):
#     strings.append(a + str(b) + str(c))
#
# print(strings)

more_strings = {a: b for (a, b) in zip(letters, numbers)}

# more_strings = {}
# for a, b in zip(letters, numbers):
#     more_strings[a] = b

print(more_strings)

