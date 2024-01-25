import sys
import array
import time
my_tuple = (1, 2, 3, 4, 5)

my_list = [1, 2, 3, 4, 5]


print(sys.getsizeof(my_tuple))
print(sys.getsizeof(my_list)) 



my_list = [i for i in range(1000)]

my_array = array.array('i', [i for i in range(1000)])

print(sys.getsizeof(my_list))  
print(sys.getsizeof(my_array)) 
