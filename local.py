import time
import resource

def process_data():
    local_data = [i for i in range(10**6)]

    start_time = time.time()
    start_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    
    # Access the local variable passed to the function
    total_sum = sum(local_data)
    
    end_time = time.time()
    end_mem = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

    print(f"Total sum using local variable: {total_sum}")
    print(f"Execution time: {end_time - start_time} seconds")
    print(f"Memory usage: {end_mem - start_mem} KB")


# Call the main function
process_data()