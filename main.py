team_1_score = 0
team_2_score = 0
team_1_last_move = ""
team_2_last_move = ""

first_round = True

def team1strat():
    if first_round:
        return "Silent"
    elif team_2_last_move == "Confess":
        return "Confess"
    else:
        return "Silent"

def team2strat():
    #return "Confess"
    if first_round:
        return "Silent"
    elif team_1_last_move == "Confess":
        return "Confess"
    else:
        return "Silent"

def eval_round():
    global team_1_score
    global team_2_score
    if team_1_last_move == "Confess" and team_2_last_move == "Confess":
        team_1_score += 5
        team_2_score += 5
    elif team_1_last_move == "Confess" and team_2_last_move == "Silent":
        team_1_score += 1
        team_2_score += 8
    elif team_1_last_move == "Silent" and team_2_last_move == "Confess":
        team_1_score += 8
        team_2_score += 1
    else:
        team_1_score += 2
        team_2_score += 2

for i in range(0, 1000):
    next_team1_move = team1strat()
    next_team_2_move = team2strat()
    team_1_last_move = next_team1_move
    team_2_last_move = next_team_2_move
    eval_round()
    first_round = False

print(f"Team 1 score: {team_1_score}")
print(f"Team 2 score: {team_2_score}")