def minion_game(string):
    vowels = 'AEIOU'
    Stuart_score = Kevin_score = 0
    length = len(string)
    for i, letter in enumerate(string):
        print(i, letter)
        if letter in vowels:
            Kevin_score += length - i
        else:
            Stuart_score += length - i
    if Stuart_score > Kevin_score:
        print(f'Stuart {Stuart_score}')
    elif Stuart_score < Kevin_score:
        print(f'Kevin {Kevin_score}')
    else:
        print("Draw")


print(minion_game("banana"))
