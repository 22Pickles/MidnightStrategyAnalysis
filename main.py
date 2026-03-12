import random
import matplotlib.pyplot as plt
import numpy as np

def main():
    possible_scores = [0,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    o = [[],[],[],[],[]]
    trials = 100000
    tests = 5
    for i in range(trials-1):
        o[0].append(game(str1))
        o[1].append(game(str2))
        o[2].append(game(str3))
        o[3].append(game(str4))
        o[4].append(game(str5))

    c = possible_scores
    d = [[o[a].count(i)/trials for i in possible_scores] for a in range(tests)]
    mean = [np.mean(o[a]) for a in range(tests)]
    median = [np.median(o[a]) for a in range(tests)]
    
    fig, axes = plt.subplots(tests,1)

    [axes[a].bar(c, d[a]) for a in range(tests)]

    [axes[a].axvline(mean[a]) for a in range(tests)]

    plt.tight_layout()

    plt.savefig('Tests')
    plt.close()

def game(strategy):
    game_running = True
    dice = 6
    b = []
    while game_running:
        a = roll(dice)
        #print(f"Roll: {a}\nPocket: {b}\nScore: {score(b)}\n")
        n = strategy(a,b)
        #print(n)
        for i in [int(x) for x in n]:
            a.remove(i)
            b.append(i)
        dice = len(a)
        #print("--------")
        if dice == 0:
            #print(f"Game Over\nPocket: {b}\nScore: {score(b)}")
            game_running = False
            return score(b)

def roll(number_of_dice):
    return [round(random.randint(1,6)) for i in range(number_of_dice)]

def score(pocket):
    if (1 in pocket) and (4 in pocket):
        r = [1, 4]
        o = []
        for i in range(len(pocket)):
            if pocket[i] in r:
                r.remove(pocket[i])
            else:
                o.append(pocket[i])
        return sum(o)
    else:
        return 0

def str1(roll, pocket):
    #take 1 and 4 if not in pocket
    #take 6 and 5 if option
    #take highest if forced
    s = []
    if 1 not in pocket:
        for i in range(len(roll)):
            if roll[i] == 1:
                s.append(roll[i])
                break
    if 4 not in pocket:
        for i in range(len(roll)):
            if roll[i] == 4:
                s.append(roll[i])
                break

    for i in range(len(roll)):
        if roll[i] == 6:
            s.append(roll[i])
    if len(s) == 0:
        s.append(max(roll))
    return s

def str2(roll, pocket):
    s = []
    if 1 not in pocket:
        for i in range(len(roll)):
            if roll[i] == 1:
                s.append(roll[i])
                break
    if 4 not in pocket:
        for i in range(len(roll)):
            if roll[i] == 4:
                s.append(roll[i])
                break
    if len(s) == 0:
        s.append(max(roll))
    return s


def str3(roll, pocket):
    s = []
    if 1 not in pocket:
        for i in range(len(roll)):
            if roll[i] == 1:
                s.append(roll[i])
                break
    if 4 not in pocket:
        for i in range(len(roll)):
            if roll[i] == 4:
                s.append(roll[i])
                break
    for i in range(len(roll)):
        if roll[i] == 6:
            if len(roll) - len(s) < 4 and ((1 not in pocket) or (4 not in pocket)):
                break
            else:
                s.append(roll[i])
    if len(s) == 0:
        s.append(max(roll))
    return s

def str4(roll, pocket):
    s = []
    if 1 not in pocket:
        for i in range(len(roll)):
            if roll[i] == 1:
                s.append(roll[i])
                break
    if 4 not in pocket:
        for i in range(len(roll)):
            if roll[i] == 4:
                s.append(roll[i])
                break
    for i in range(len(roll)):
        if roll[i] == 6:
            if len(roll) - len(s) < 5 and ((1 not in pocket) or (4 not in pocket)):
                break
            else:
                s.append(roll[i])
    if len(s) == 0:
        s.append(max(roll))
    return s

def str5(roll, pocket):
    s = []
    if 1 not in pocket:
        for i in range(len(roll)):
            if roll[i] == 1:
                s.append(roll[i])
                break
    if 4 not in pocket:
        for i in range(len(roll)):
            if roll[i] == 4:
                s.append(roll[i])
                break
    for i in range(len(roll)):
        if roll[i] == 6:
            if len(roll) - len(s) < 6 and ((1 not in pocket) or (4 not in pocket)):
                break
            else:
                s.append(roll[i])
    if len(s) == 0:
        s.append(max(roll))
    return s


if __name__ == "__main__":
    main()