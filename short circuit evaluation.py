#traditional approach 
import time
def validate_input(name, age):
    # Check if the name is not empty and age is greater than 18
    if name != '' and age > 18 and 1:
        return True
    else:
        return False

# Example usage:
start_time= time.time()
result = validate_input("John", 25)
end_time= time.time()
print(end_time-start_time)
print(result)  # Output: True

#short circuit validation approach 
def validate_input(name, age):
    # Check if the name is not empty and age is greater than 18
       return name != '' and age > 18 and 1

# Example usage:
start_time= time.time()
result = validate_input("Michael", 25)
end_time= time.time()
print(end_time-start_time)
print(result)