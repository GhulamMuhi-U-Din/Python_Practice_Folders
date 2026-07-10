from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# counter()

fruits = ["apple", "banana", "apple", "orange", "apple"]

count = Counter(fruits)

print(count)

# defaultdict()

student = defaultdict(str)

print(student["name"])

numbers = defaultdict(int)

print(numbers["age"])

# deque()

# add
numbers = deque([1, 2, 3])

numbers.append(4)

numbers.appendleft(0)

print(numbers)

# remove

numbers.pop()

numbers.popleft()

print(numbers)

# namedtuple()

Student = namedtuple("Student", ["name", "age"])

s = Student("Ali", 20)

print(s.name)

print(s.age)

# OrderedDict()

data = OrderedDict()

data["A"] = 1

data["B"] = 2

print(data)