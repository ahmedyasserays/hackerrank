def count_substring(string, sub_string):
    counter = 0 # initial value
    # this range is to avoid index error
    for i in range(len(string) - len(sub_string) +1): 
        # to select the target sub 
        if string[i:i+len(sub_string)] == sub_string: 
            counter+=1 # counting 
    return counter
