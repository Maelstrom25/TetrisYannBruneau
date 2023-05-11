import statistics as stats
import matplotlib.pyplot as plt

# File which was used to analyze data and make plots for figures

def mean(scores):
    return stats.mean(scores)

def median(scores):
    return stats.median(scores)

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
            'median': median(exp_scores),
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
     200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200
]


exp3_scores = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 1, 1, 2, 1, 1, 1, 1, 1, 2, 0, 0, 1, 0],
    [3, 8, 9, 2, 4, 1, 4, 5, 2, 8, 0, 2, 7, 1, 4, 1, 2, 5, 0, 4],
    [12, 10, 3, 11, 8, 9, 3, 8, 9, 4, 17, 4, 10, 6, 14, 11, 5, 14, 7, 18],
    [2, 7, 12, 26, 8, 13, 25, 7, 12, 10, 16, 17, 21, 12, 7, 21, 14, 12, 42, 13],
    [26, 14, 18, 53, 8, 24, 36, 18, 50, 31, 4, 10, 22, 56, 10, 35, 15, 35, 14, 31],
    [53, 48, 44, 16, 48, 69, 42, 48, 32, 33, 28, 65, 46, 47, 23, 42, 33, 31, 67, 15],
    [75, 61, 66, 47, 31, 37, 55, 71, 39, 79, 125, 98, 69, 44, 53, 89, 53, 48, 46, 90],
    [69, 97, 24, 76, 64, 76, 146, 26, 93, 76, 144, 97, 35, 78, 61, 10, 53, 35, 111, 20],
    [136, 106, 150, 22, 128, 134, 142, 63, 107, 200, 67, 78, 159, 22, 54, 76, 200, 53, 45, 116],
    [93, 152, 80, 22, 41, 55, 81, 77, 98, 152, 45, 123, 36, 199, 33, 142, 66, 40, 127, 70],
    [92, 200, 102, 182, 117, 200, 65, 65, 82, 43, 174, 138, 128, 112, 167, 137, 200, 90, 135, 139],
    [200, 49, 117, 106, 200, 200, 111, 200, 172, 115, 200, 107, 116, 119, 200, 200, 115, 145, 144, 200],
    [34, 200, 200, 199, 200, 96, 200, 33, 180, 200, 200, 200, 105, 200, 156, 200, 200, 200, 142, 86],
    [79, 135, 134, 200, 200, 200, 123, 181, 200, 200, 45, 200, 200, 200, 200, 200, 165, 200, 200, 200]
]


exp4_scores = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 2, 0, 3, 0, 2, 2, 3],
    [6, 2, 3, 3, 7, 3, 0, 3, 6, 4, 6, 5, 12, 2, 12, 7, 2, 2, 9, 4],
    [10, 12, 18, 10, 7, 10, 1, 10, 11, 22, 17, 4, 10, 17, 11, 17, 8, 12, 3, 16],
    [35, 12, 15, 21, 22, 23, 12, 9, 21, 23, 29, 32, 10, 21, 15, 20, 19, 46, 26, 21],
    [10, 15, 30, 20, 20, 23, 55, 48, 47, 45, 24, 70, 50, 99, 45, 24, 49, 24, 18, 39],
    [33, 71, 49, 23, 40, 42, 19, 29, 63, 71, 38, 32, 65, 65, 54, 44, 57, 57, 25, 16],
    [96, 15, 69, 42, 44, 70, 50, 14, 46, 72, 44, 41, 61, 107, 127, 86, 34, 104, 90, 20],
    [143, 110, 98, 45, 53, 167, 75, 200, 50, 39, 50, 125, 71, 55, 72, 29, 94, 120, 18, 75],
    [122, 200, 46, 58, 136, 130, 54, 124, 96, 55, 51, 106, 85, 33, 200, 61, 13, 200, 52, 154],
    [39, 193, 122, 72, 24, 200, 80, 98, 65, 89, 96, 125, 52, 121, 200, 64, 67, 188, 27, 118],
    [181, 118, 53, 195, 119, 174, 138, 18, 137, 38, 200, 200, 107, 67, 200, 47, 200, 89, 34, 200],
    [50, 200, 31, 171, 189, 94, 200, 200, 110, 200, 133, 200, 200, 200, 200, 155, 200, 132, 58, 44],
    [82, 82, 200, 27, 28, 43, 200, 90, 18, 106, 40, 200, 200, 200, 200, 200, 87, 49, 200, 200],
    [200, 161, 200, 121, 200, 66, 200, 200, 27, 200, 193, 60, 77, 200, 200, 65, 72, 200, 200, 200]
]


exp1_stats = calculate_stats(x, exp1_scores)
exp3_stats = calculate_stats(x, exp3_scores)
exp4_stats = calculate_stats(x, exp4_scores)


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

exp1_medians = [exp1_stats[i]['median'] for i in x]
exp3_medians = [exp3_stats[i]['median'] for i in x]
exp4_medians = [exp4_stats[i]['median'] for i in x]



# plot for experiment 2

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



# plot for experiment 3

plt.plot(x, exp4_means, label="Exp 1: Average score", linewidth=3, color = 'red')
plt.plot(x, exp4_min, label="Exp 1: Lowest score", color = 'blue')
plt.plot(x, exp4_max, label="Exp 1: Highest score", color = 'green')

plt.xlabel("Number of colors k")
plt.ylabel("Alice's score")
plt.xticks(range(1, 16))

plt.legend()
plt.show()


# plot for experiment 4

plt.plot(x, exp4_means, label="Exp 4: Average score", linewidth=3, color = 'red')
plt.plot(x, exp4_min, label="Exp 4: Lowest score", color = 'blue')
plt.plot(x, exp4_max, label="Exp 4: Highest score", color = 'green')

plt.xlabel("Number of colors k")
plt.ylabel("Alice's score")
plt.xticks(range(1, 16))

plt.legend()
plt.show()


# plot comparing average scores of all 4 experiments

colors = list(range(1, 16))
plt.plot(colors, exp1_means, label="Exp 1", linewidth=2, color='red')
plt.plot(colors, exp3_means, label="Exp 3", linewidth=2, color='blue')
plt.plot(colors, exp4_means, label="Exp 4", linewidth=2, color='green')

plt.xlabel("Number of colors")
plt.ylabel("Average score")
plt.xticks(range(1, 16))
plt.axhline(y=200, linestyle='dotted', color='black', label="Exp 2") #exp 2, because all results were with score=200

plt.legend()
plt.show()


