import sys

name = "Steve"

# 2 references, 1 from the name variable and 1 from getrefcount
print(sys.getrefcount(name))