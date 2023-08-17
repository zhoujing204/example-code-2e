
# trailing comma will be ignored in a literal
my_list = [1, 2, 3, 4, 5,]
print(my_list)

# how about not a literal? It's still ignored
a, b, c, d = 45, 56, 67, 78,
var_list = [a, b, c, d,]
print(var_list)

import time

# Create a large tuple
large_tuple = tuple(range(100_000_000))

# Create a large list
large_list = list(range(100_000_000))

# Measure the time taken to create a copy using tuple()
start_time_tuple = time.time()
new_tuple = tuple(large_tuple)
end_time_tuple = time.time()

# Measure the time taken to create a copy using list()
start_time_list = time.time()
new_list = list(large_list)
end_time_list = time.time()

# Calculate the time taken for each operation
time_taken_tuple = end_time_tuple - start_time_tuple
time_taken_list = end_time_list - start_time_list

# Compare the time taken
print("Time taken for tuple():", time_taken_tuple)
print("Time taken for list():", time_taken_list)
