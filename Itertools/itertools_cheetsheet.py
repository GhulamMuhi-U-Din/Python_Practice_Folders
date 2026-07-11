# Import important itertools tools
from itertools import (
    count,
    cycle,
    repeat,
    permutations,
    combinations,
    product,
    accumulate,
    chain,
)


# Repeat one value
print(list(repeat("Python", 3)))


# Generate all possible orders
print(list(permutations(["A", "B", "C"])))


# Generate groups of 2
print(list(combinations(["A", "B", "C"], 2)))


# Generate all possible pairings
print(list(product(["Red", "Blue"], ["Small", "Large"])))


# Create running totals
print(list(accumulate([10, 20, 30])))


# Join iterables
print(list(chain([1, 2, 3], [4, 5, 6])))

# =====================================
# QUICK REVISION
# =====================================

# count()         → Keep counting

# cycle()         → Repeat sequence

# repeat()        → Repeat one value

# permutations()  → All possible orders

# combinations()  → All possible groups

# product()       → All possible pairings

# accumulate()    → Running total

# chain()         → Join iterables