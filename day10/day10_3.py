#3-Print a list after removing specified elements

col = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
col = [x for (i,x) in enumerate(col) if i not in (0,4,5)]
print(col)
