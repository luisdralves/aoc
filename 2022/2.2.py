
opponent_shapes = {
    "A": "rock",
    "B": "paper",
    "C": "scissor"
}

sequence = [
    "rock",
    "paper",
    "scissor"
]

score = 0

with open('2.txt', 'r') as file:
    while (line := file.readline().rstrip()):
        opponent, me = line.split(' ')
        opponent_shape = opponent_shapes[opponent]
        opponent_index = sequence.index(opponent_shape)
        my_index = None
        score_this_round = 0
        if me == 'X':
            my_index = (opponent_index-1)%3
            score_this_round = 0
        elif me == 'Y':
            my_index = opponent_index
            score_this_round = 3
        elif me == 'Z':
            my_index = (opponent_index+1)%3
            score_this_round = 6
        score+=score_this_round+my_index+1

print(score)
