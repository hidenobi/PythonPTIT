# # % operator
# text = "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down." % (3, 'huff', 'puff', 'house')
# print(text)
# # Add parentheses to make the long line work:
# text = (
#     "%d little pigs come out, or I'll %s, and I'll %s, and I'll blow your %s down."
#     % (3, 'huff', 'puff', 'house')
# )
# print(text)
# text = (
#     "%d little pigs come out, "
#     "or I'll %s, and I'll %s, "
#     "and I'll blow your %s down."
#     % (3, 'huff', 'puff', 'house')
# )
# print(text)

# """
# output:
# 3 little pigs come out, or I'll huff, and I'll puff, and I'll blow your house down.

a = [1,2,3]
b = list(map(lambda x:x+10,a))
print(b)