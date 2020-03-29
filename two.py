import math

def partition(s):
    middle = math.floor(len(s) / 2)
    return s[:middle] + '-' + s[middle:len(s)]

print(partition('Reymann'))
print(partition('sixsix'))
