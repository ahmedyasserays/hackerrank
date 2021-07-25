def compareTriplets(a, b): 
    score_a = 0 # setting initial score value 
    score_b = 0 
    for i , j in zip(a, b):  # loop over the scores of two questions
        if i > j:  # if the score of the first questoins is higher
            score_a +=1  # then increase it's score
        if i < j: # if the score of the second questoins is higher
            score_b +=1 # then increase it's score
    return [score_a, score_b]