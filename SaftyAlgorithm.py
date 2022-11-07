import numpy as np                  # Created By Laila Shihada 764700695

if __name__ == '__main__':
    number_of_process = 5
    number_of_resources = 4

    # Create Safe sequence array
    safe_sequence = np.zeros((number_of_process,), dtype=int)
    # print (safe_sequence)

    # Create finish array
    finish = np.zeros((number_of_process,), dtype=int)
    # print(finish)

    # Create the allocation matrix array (two-dimensional)
    allocation = np.array([[0, 0, 1, 2], [1, 0, 0, 0], [1, 3, 5, 4], [0, 6, 3, 2], [0, 0, 1, 4]])
    # Create the max matrix array (two-dimensional)
    max_matrix = np.array([[0, 0, 1, 2], [1, 7, 5, 0], [2, 3, 5, 6], [0, 6, 5, 2], [0, 6, 5, 6]])
    # Create the available array
    available = np.array([1, 5, 2, 0])

    need_matrix = max_matrix - allocation
    print('Need matrix for Banker Algorithm')
    print(need_matrix)

    # Start the banker's algorithm
    work = available
    safe_sequence_counter = 0   # Create a counter for the safe processes' sequence
    process_counter = 0         # Count the number of executed processes.

    while safe_sequence_counter < number_of_process:
        i = 0
        while i < number_of_process:
            if finish[i] == 0 and all(np.greater_equal(work, need_matrix[i])):  # Compare if the work instances > the need instances
                # Process is executing
                work = work + allocation[i]
                finish[i] = 1       # Assign process number to true (executed process)
                safe_sequence[safe_sequence_counter] = i + 1
                safe_sequence_counter = safe_sequence_counter + 1
                i = i + 1
            else:           # The process is not executed --> finish[i] = 0
                i = i + 1
        process_counter = process_counter + 1
        if process_counter >= number_of_process:    # All processes are executed.
            break
    if process_counter > number_of_process:     # If the number of loop cycles > number of processes --> Deadlock.
        print("Deadlock")
    else:               # The algorithm is completed --> print out the results
        print("Safe sequence")
        print(safe_sequence)
        print("work sequence ")
        print(work)









