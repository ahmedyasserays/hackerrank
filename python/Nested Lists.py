names_grades = [] # first we initial an empty list
# getting the first input which is the number of students to loop over
for _ in range(int(input())):   
    name = input()  # inputting the name
    score = float(input()) # inputting the score
    # appending the current score to the empty list
    names_grades.append([name, score]) 

# first we sort the list to be able to compare 
# the scores easily
names_grades.sort(key=lambda x: x[1]) 
lowest = names_grades[0][1] # also you could use min()
second_lowest = 9999  # some useless number to compare with
for i in names_grades:
    if i[1] == lowest:
        continue
    else:
        second_lowest = i[1]  # getting the second lowest score
        break

# then we filter only the students with the required score
selected = list(filter(lambda x : x[1]==second_lowest, names_grades))
# last step is to sort the students base on names
selected.sort(key=lambda x:x[0])
for i in selected:
    print(i[0])


# better solution 
names_grades = []
    
for _ in range(int(input())):
    name = input()
    score = float(input())
    names_grades.append([name, score])

lowest = 99999999 # setting some non sence values
second_lowest = 99999999
for student in names_grades: # looping over the list
    if student[1] < lowest: # comparing each score with the previous lowest
        second_lowest = lowest
        lowest = student[1]
    elif student[1] != lowest and student[1] < second_lowest:
        second_lowest = student[1]
selected = list(filter(lambda x : x[1]==second_lowest, names_grades))
selected.sort(key=lambda x:x[0])
for i in selected:
    print(i[0])
