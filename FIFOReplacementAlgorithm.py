import numpy as np
if __name__ == '__main__':
    page_ref_string = np.array([7, 2, 5, 7, 0, 6, 7, 2, 1, 2, 4, 3])
    working_set = 4              # Number of frames
    initial_value_of_frames = np.array([-1, -1, -1, -1])     # using -1 refers to empty array
    total_page_hit = 0
    total_page_fault = 0
    frame_counter = 0
    cpu_cycle_counter = 0   # To check the page's cpu cycle position.
    i = 0       # Counter to put a value in the frame set.
    while cpu_cycle_counter < len(page_ref_string):
        frame_counter = 0
        while frame_counter < working_set:
            # To check the page hit
            if page_ref_string[cpu_cycle_counter] == initial_value_of_frames[frame_counter]:
                total_page_hit = total_page_hit + 1
                break
            else:
                frame_counter = frame_counter + 1
            # To check the page fault
            if frame_counter == working_set:
                total_page_fault = total_page_fault + 1
                initial_value_of_frames[i] = page_ref_string[cpu_cycle_counter]
                i = i + 1

            if i > 3:
                i = 0
        cpu_cycle_counter = cpu_cycle_counter + 1

        print("The initial value of frames: ")
        print(initial_value_of_frames)
    print("Total hits:", total_page_hit)
    print("total fault:", total_page_fault)




