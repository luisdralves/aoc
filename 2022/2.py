
opponent_shapes = {
    "A": "rock",
    "B": "paper",
    "C": "scissor"
}

my_shapes = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissor"
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
        my_shape = my_shapes[me]
        my_index = sequence.index(my_shape)
        opponent_index = sequence.index(opponent_shape)
        score_this_round = 0
        if my_shape == opponent_shape:
            score_this_round = my_index+4
        elif (my_index-opponent_index)%3==1:
            score_this_round = my_index+7
        else:
            score_this_round = my_index+1
        score+=score_this_round

print(score)
