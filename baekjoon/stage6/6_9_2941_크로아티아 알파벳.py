words = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']


for id, value in enumerate(croatia):
    words = words.replace(value, '*')

print(len(words))