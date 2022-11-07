import numpy as np

if __name__ == '__main__':
    page_ref_string = np.array([7, 2, 5, 7, 0, 6, 7, 2, 1, 2, 4, 3])
    size_of_working_set = 4
    initial_value_of_frames = np.array([-1, -1, -1, -1])
    total_page_hit = 0
    total_page_fault = 0
    cpu_cycle_counter = 0
    i = 0
    while cpu_cycle_counter < len(page_ref_string):
        frame_counter = 0
        while frame_counter < size_of_working_set:

            # 1st set of if else is checking page hits are there or not
            if page_ref_string[cpu_cycle_counter] == initial_value_of_frames[frame_counter]:
                total_page_hit = total_page_hit + 1
                break
            else:
                frame_counter = frame_counter + 1
             # 2nd set of if else is checking page fault are there or not
            if frame_counter == size_of_working_set:
                total_page_fault = total_page_fault + 1
                initial_value_of_frames[i] = page_ref_string[cpu_cycle_counter]
                i = i + 1

            if i == 4:
                i = 0
        print(initial_value_of_frames)
        cpu_cycle_counter = cpu_cycle_counter + 1
    print("Page  Hits:", total_page_hit)
    print("Page Fault:", total_page_fault )




