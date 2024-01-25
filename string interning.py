# Example without String Interning
import time


string3 = "Hi"
string4 = "Hi"

if string3 == string4:
    start_time=time.time()
    print("Strings are identical")
    end_time=time.time()
    print(end_time-start_time)
else:
    print("Strings are different")



string1 = "hello"
string2 = "hello"
if string1 is string2:
    start_time=time.time()
    print("Strings are identical")
    end_time=time.time()
    print(end_time-start_time)
else:
    print("Strings are different")


