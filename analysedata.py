import statistics as stats
import matplotlib.pyplot as plt

# File which was used to analyze data and make plots for figures

def mean(scores):
    return stats.mean(scores)

def win_rate(scores):
    return scores.count(200) / len(scores) * 100

def min_score(scores):
    return min(scores)

def max_score(scores):
    return max(scores)

def calculate_stats(x, scores):
    statistics = {}
    for i in range(len(x)):
        exp_scores = scores[i]
        statistics[x[i]] = {
            'mean': mean(exp_scores),
            'win_rate': win_rate(exp_scores),
            'min_score': min_score(exp_scores),
            'max_score': max_score(exp_scores),
        }
    return statistics

x = list(range(1, 16))

# all simulation scores

exp1_scores = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 2, 0, 0, 0, 1, 1, 1, 0, 0, 2],
    [5, 12, 4, 9, 9, 11, 11, 6, 7, 8, 5, 6, 8, 2, 2, 19, 14, 2, 6, 5],
    [20, 29, 21, 33, 9, 23, 21, 34, 13, 27, 36, 21, 37, 8, 32, 29, 39, 28, 30, 1],
    [42, 101, 50, 56, 56, 80, 23, 46, 5, 66, 45, 64, 30, 48, 19, 41, 67, 49, 37, 67],
    [138, 69, 68, 34, 148, 68, 31, 95, 101, 71, 108, 97, 141, 126, 79, 200, 101, 126, 47, 142],
    [88, 200, 165, 107, 200, 62, 111, 200, 200, 200, 200, 200, 115, 165, 164, 151, 130, 188, 182, 200],
    [200, 200, 200, 200, 148, 200, 200, 200, 167, 200, 200, 200, 164, 200, 194, 102, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 97, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200],
    [200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200]
]


exp2_scores = [
    90, 106, 70, 69, 92, 55, 108, 79, 43, 132, 34, 69, 56, 45, 77, 35, 100, 69, 90, 82
]


exp3_scores = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 3, 3, 2, 3, 3, 2, 1, 1, 1, 2, 5, 3, 1, 2, 1, 2, 2, 1],
    [7, 3, 7, 3, 0, 6, 1, 4, 5, 3, 4, 1, 2, 4, 1, 8, 7, 4, 3, 5],
    [12, 11, 8, 7, 12, 16, 14, 17, 12, 10, 11, 3, 4, 9, 11, 7, 7, 9, 12, 0],
    [15, 19, 4, 6, 11, 7, 14, 7, 5, 8, 14, 19, 5, 1, 19, 22, 7, 15, 16, 6],
    [22, 11, 24, 16, 20, 14, 22, 22, 5, 14, 24, 15, 4, 22, 12, 30, 5, 6, 20, 15],
    [34, 31, 39, 23, 17, 25, 35, 16, 27, 23, 24, 19, 34, 7, 18, 17, 29, 24, 25, 20],
    [15, 13, 29, 13, 31, 18, 22, 22, 26, 5, 19, 29, 48, 44, 24, 22, 39, 18, 22, 6],
    [13, 13, 25, 24, 26, 39, 28, 49, 23, 19, 27, 19, 27, 15, 20, 51, 35, 27, 25, 35],
    [35, 37, 41, 29, 32, 30, 50, 34, 55, 19, 26, 32, 33, 34, 43, 18, 24, 24, 26, 39],
    [53, 16, 54, 17, 38, 29, 53, 5, 12, 46, 42, 51, 41, 22, 33, 35, 7, 54, 34, 32],
    [17, 57, 48, 33, 37, 25, 33, 41, 63, 19, 43, 37, 52, 30, 56, 31, 28, 31, 40, 27],
    [45, 30, 37, 53, 19, 77, 55, 39, 45, 38, 69, 40, 22, 27, 39, 41, 26, 29, 55, 52],
    [68, 29, 42, 91, 75, 36, 31, 74, 76, 34, 55, 41, 39, 69, 36, 57, 55, 42, 37, 24]
]


exp4_scores = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [4, 8, 3, 7, 7, 2, 0, 2, 3, 3, 3, 1, 1, 1, 3, 4, 0, 3, 3, 1],
    [9, 19, 16, 4, 15, 12, 8, 7, 10, 10, 5, 7, 3, 1, 9, 10, 3, 9, 12, 19],
    [4, 2, 7, 3, 19, 20, 7, 10, 24, 11, 25, 21, 9, 5, 19, 16, 4, 9, 16, 17],
    [27, 26, 33, 25, 1, 11, 16, 7, 12, 20, 23, 23, 34, 14, 35, 12, 26, 26, 18, 21],
    [32, 30, 12, 46, 32, 44, 29, 42, 18, 46, 32, 20, 41, 13, 14, 37, 23, 26, 15, 47],
    [36, 28, 46, 32, 28, 12, 69, 31, 17, 31, 22, 25, 33, 40, 20, 71, 4, 31, 5, 54],
    [12, 41, 49, 23, 32, 40, 58, 52, 36, 17, 28, 39, 4, 50, 23, 40, 27, 36, 67, 56],
    [46, 44, 66, 55, 13, 49, 66, 38, 44, 49, 55, 33, 57, 26, 26, 47, 62, 32, 32, 49],
    [24, 44, 8, 34, 15, 80, 33, 36, 48, 59, 35, 56, 63, 69, 86, 21, 55, 51, 28, 32],
    [49, 64, 40, 81, 48, 116, 46, 42, 40, 69, 78, 67, 17, 14, 104, 29, 4, 23, 76, 38],
    [58, 69, 98, 48, 30, 76, 61, 74, 94, 58, 21, 35, 31, 43, 66, 109, 89, 76, 70, 44],
    [128, 43, 94, 115, 50, 163, 94, 142, 116, 104, 30, 79, 58, 37, 107, 86, 87, 159, 65, 79],
    [99, 88, 48, 78, 116, 117, 138, 131, 99, 134, 142, 59, 26, 100, 90, 90, 9, 130, 125, 83]
]


exp1_stats = calculate_stats(x, exp1_scores)
exp3_stats = calculate_stats(x, exp3_scores)
exp4_stats = calculate_stats(x, exp4_scores)

exp2_mean = mean(exp2_scores)
exp2_wr = win_rate(exp2_scores)
exp2_min = min_score(exp2_scores)
exp2_max = max_score(exp2_scores)


x = list(range(1, 16))
exp1_means = [exp1_stats[i]['mean'] for i in x]
exp3_means = [exp3_stats[i]['mean'] for i in x]
exp4_means = [exp4_stats[i]['mean'] for i in x]

exp1_wrs = [exp1_stats[i]['win_rate'] for i in x]
exp3_wrs = [exp3_stats[i]['win_rate'] for i in x]
exp4_wrs = [exp4_stats[i]['win_rate'] for i in x]

exp1_min = [exp1_stats[i]['min_score'] for i in x]
exp3_min = [exp3_stats[i]['min_score'] for i in x]
exp4_min = [exp4_stats[i]['min_score'] for i in x]

exp1_max = [exp1_stats[i]['max_score'] for i in x]
exp3_max = [exp3_stats[i]['max_score'] for i in x]
exp4_max = [exp4_stats[i]['max_score'] for i in x]


"""
# plot for experiment 1

plt.plot(x, exp1_means, label="Exp 1: Average score", linewidth=3, color = 'red')
plt.plot(x, exp1_min, label="Exp 1: Lowest score", color = 'blue')
plt.plot(x, exp1_max, label="Exp 1: Highest score", color = 'green')

plt.xlabel("Number of colors k")
plt.ylabel("Alice's score")
plt.xticks(range(1, 16))
plt.axvline(x=4.5, ymin=0, ymax=200 , linestyle=(0, (1, 5)), dash_capstyle='round', dash_joinstyle='round', color='#808080')
plt.axvline(x=7.5, ymin=0, ymax=200 , linestyle=(0, (1, 5)), dash_capstyle='round', dash_joinstyle='round', color='#808080')

plt.legend()
plt.show()

plt.plot(x, exp1_means, label="Exp 1: Average score", linewidth=3, color = 'red')
plt.plot(x, exp1_min, label="Exp 1: Lowest score", color = 'blue')
plt.plot(x, exp1_max, label="Exp 1: Highest score", color = 'green')

plt.xlabel("Number of colors k")
plt.ylabel("Alice's score")
plt.xticks(range(1, 16))
#plt.axvline(x=4.5, ymin=0, ymax=200 , linestyle=(0, (1, 5)), dash_capstyle='round', dash_joinstyle='round', color='#808080')
#plt.axvline(x=7.5, ymin=0, ymax=200 , linestyle=(0, (1, 5)), dash_capstyle='round', dash_joinstyle='round', color='#808080')

plt.legend()
plt.show()
"""

"""
# plot for experiment 3

plt.plot(x, exp3_means, label="Exp 3: Average score", linewidth=3, color = 'red')
plt.plot(x, exp3_min, label="Exp 3: Lowest score", color = 'blue')
plt.plot(x, exp3_max, label="Exp 3: Highest score", color = 'green')

plt.xlabel("Number of colors k")
plt.ylabel("Alice's score")
plt.xticks(range(1, 16))
plt.yticks(range(0,225,25))

plt.legend()
plt.show()


# plot for experiment 4

plt.plot(x, exp4_means, label="Exp 4: Average score", linewidth=3, color = 'red')
plt.plot(x, exp4_min, label="Exp 4: Lowest score", color = 'blue')
plt.plot(x, exp4_max, label="Exp 4: Highest score", color = 'green')

plt.xlabel("Number of colors k")
plt.ylabel("Alice's score")
plt.xticks(range(1, 16))
plt.yticks(range(0,225,25))


plt.legend()
plt.show()

# plot comparing average scores of all experiments feat. Bob

colors = list(range(1, 16))
plt.plot(colors, exp3_means, label="Exp 3", linewidth=2, color='purple')
plt.plot(colors, exp4_means, label="Exp 4", linewidth=2, color='orange')

plt.xlabel("Number of colors")
plt.ylabel("Average score")
plt.xticks(range(1, 16))
plt.yticks(range(0,225,25))
#plt.axhline(y=exp2_mean, linestyle='dotted', color='black', label="Exp 2")

plt.legend()
plt.show()

colors = list(range(1, 16))
plt.plot(colors, exp3_means, label="Exp 3", linewidth=2, color='purple')
plt.plot(colors, exp4_means, label="Exp 4", linewidth=2, color='orange')

plt.xlabel("Number of colors")
plt.ylabel("Average score")
plt.xticks(range(1, 16))
plt.yticks(range(0,225,25))
plt.axhline(y=exp2_mean, linestyle='dotted', color='black', label="Exp 2")

plt.legend()
plt.show()
"""

"""
# plot comparing average scores of all 4 experiments

colors = list(range(1, 16))
#plt.plot(colors, exp1_means, label="Exp 1", linewidth=2, color='cyan')
plt.plot(colors, exp3_means, label="Exp 3", linewidth=2, color='purple')
plt.plot(colors, exp4_means, label="Exp 4", linewidth=2, color='orange')

plt.xlabel("Number of colors")
plt.ylabel("Average score")
plt.xticks(range(1, 16))
plt.axhline(y=exp2_mean, linestyle='dotted', color='black', label="Exp 2")
plt.axhline(y=200, linestyle='dotted', color='red', label="standard Tetris")


plt.legend()
plt.show()
"""

