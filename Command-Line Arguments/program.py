import sys

print(sys.argv)

# another example

print("Program Name :", sys.argv[0])
print("Name         :", sys.argv[1])
print("Age          :", sys.argv[2])
print("City         :", sys.argv[3])

# for how many arguments

print(len(sys.argv))

# everything in sys.argv is string , so to convert it into integer

a = int(sys.argv[1])
b = int(sys.argv[2])

print(a + b)