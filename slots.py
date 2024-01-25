import sys

# #slots doesnt allow extra attribute more than something already defined inside the class if it catches an extra attribute throws an error
# class Author:
#     __slots__=("name","age")
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# me = Author('Yang Zhou', 30)
# me.job = 'Software Engineer'
# print(me.job)

class Author:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class AuthorWithSlots:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age


# Creating instances
me = Author('Yang', 30)
me_with_slots = AuthorWithSlots('Yang', 30)

# Comparing memory usage
memory_without_slots = sys.getsizeof(me) + sys.getsizeof(me.__dict__)
memory_with_slots = sys.getsizeof(me_with_slots)  # __slots__ classes don't have __dict__

print(memory_without_slots, memory_with_slots)
print(me.__dict__)
print(me_with_slots)
