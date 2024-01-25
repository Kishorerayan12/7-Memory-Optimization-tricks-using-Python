from itertools import islice
import sys

numbers_without_generator= [i for i in range(0,100)]
print(numbers_without_generator)
def number_generator():
    for i in range(100):
        yield i

numbers_with_generator = number_generator()
print(sys.getsizeof(numbers_without_generator))
print(sys.getsizeof(numbers_with_generator))
print(numbers_with_generator)
print(next(numbers_with_generator))
print(next(numbers_with_generator))


for _ in range(5):
    result= next(numbers_with_generator)
    print(result)

subset = list(islice(numbers_with_generator, 3, 7))
print(sys.getsizeof(subset))
print("Subset of values:", subset)

