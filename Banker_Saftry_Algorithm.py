
import numpy as np

if __name__ == '__main__':
    number_of_processes = 5
    number_of_resource = 4
    safe_sequence = np.zeros((number_of_processes,), dtype=int)
    print("Safe Sequence initially: ", safe_sequence)

    finish = np.zeros((number_of_processes,), dtype=int)
    print("Finish Array: ", finish)

    allocation = np.array([[4, 0, 0, 1], [1, 1, 0, 0], [1, 2, 5, 4], [0, 6, 3, 3], [0, 2, 1, 2]])

    max_matrix = np.array([[6, 2, 1, 2], [1, 1, 1, 0], [2, 3, 5, 6], [1, 6, 5, 3], [1, 6, 5, 6]])

    available_matrix = np.array([3, 2, 1, 1])

    # Below mentioned code to identify content of need matrix
    need_matrix = max_matrix - allocation
    print("Need Matrix of the Banker Algorithm")
    print(need_matrix)
    print("safe sequence")
    work = available_matrix
    safe_sequence_counter = 0
    process_counter = 0
    while safe_sequence_counter < number_of_processes:
        i = 0
        while i < number_of_processes:
            if finish[i] == 0 and all(np.greater_equal(work, need_matrix[i])):
                work = work + allocation[i]
                finish[i] = 1
                safe_sequence[safe_sequence_counter] = i
                safe_sequence_counter = safe_sequence_counter + 1
                i = i + 1
                print(safe_sequence)
            else:
                i = i + 1
        process_counter = process_counter + 1
        if process_counter > number_of_processes:
            break
    if process_counter > number_of_processes:
        print("deadlock")
    else:
        print("Safe sequence ", safe_sequence)
        print("work sequence ", work)




