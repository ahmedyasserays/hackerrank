n = int(input())
arr = input().split()
my_players = list(map(int, arr))
winner = max(my_players)
while winner in my_players:
    my_players.remove(winner)
print(max(my_players))


# better solution 

arr = input().split()
my_players = list(map(int, arr))
max_score = -999999
runner_up = -999999
for score in my_players:
    if score > max_score:
        runner_up = max_score
        max_score = score
    elif score> runner_up and score != max_score:
        runner_up = score
print(runner_up)
