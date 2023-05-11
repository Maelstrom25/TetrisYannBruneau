import ai
import tetris

# "main" file which run the simulation

# summary of all steps which are happening:

# 1 AI is initialized
dude = ai.AI([0.510066, 0.760666, 0.35663, 0.184483])

# 2 tetris environtment is initialized
test = tetris.Tetris()

# 3 run simulation
# function is explained thoroughly in tetris.py
# 1st parameter is the AI
# 2nd parameter is the amount of colors which want to be used
# 3rd parameter is boolean, True -> the color rule is enforced, False -> the rule is not enfored (regular tetris)
# 4th parameter is boolean, True -> only works if the next parameter duo is also True, it makes it that Bob chooses the colors,
#   False -> Bob chooses tetrominoes, if duo=False, does nothing
# 5th parameter is boolean, True -> Bob plays, False -> Bob doesn't play
test.run(dude, 12, coloring=True, colorexp=False, duo=True)


# next code is in string because it starts a very long simulation (~25-30h)

"""
filename = 'expoutput.txt'
outfile = open(filename, 'w')

x = [i for i in range(1,16)]

outfile.writelines(str(x) + '\n')

outfile.writelines('Experiment 1:' + '\n' + '[')
for i in range(1,16):
    scores = []
    for k in range(10):
        test = tetris.Tetris()
        score = test.run(dude, i, coloring=True, colorexp=False, duo=False)         
        scores.append(score)
outfile.writelines(str(scores) + ',' + '\n')

outfile.writelines('\n' + ']')


outfile.writelines('\n' + 'Experiment 2:' + '\n')
scores = []
for k in range(10):
    test = tetris.Tetris()
    score = test.run(dude, 7, coloring=False, colorexp=False, duo=True)
    scores.append(score)
outfile.writelines(str(scores) + '\n')

outfile.writelines('\n' + 'Experiment 3:' + '\n' + '[')

for i in range(1,16):
    scores = []
    for k in range(10):
        test = tetris.Tetris()
        score = test.run(dude, i, coloring=True, colorexp=False, duo=True)
        scores.append(score)
outfile.writelines(str(scores) + ',' + '\n')

outfile.writelines('\n' + ']')

outfile.writelines('\n' + 'Experiment 4:' + '\n' + '[')

for i in range(1,16):
    scores = []
    for k in range(10):
        test = tetris.Tetris()
        score = test.run(dude, i, coloring=True, colorexp=True, duo=True)
        scores.append(score)    
    outfile.writelines(str(scores) + ',' + '\n')

outfile.writelines('\n' + ']')

outfile.close()
"""
