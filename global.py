import time
import resource

# Global variable holding a large list
global_data = [i for i in range(10**6)]

def process_data():
    start_time = time.time()
    start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    
    # Access the global variable within the function
    total_sum = sum(global_data)
    
    end_time = time.time()
    end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    print(f"Total sum using global variable: {total_sum}")
    print(f"Execution time: {end_time - start_time} seconds")
    print(f"Memory usage: {end_mem - start_mem} KB")

# Call the function
process_data()
