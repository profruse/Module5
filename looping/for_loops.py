""" For loops
"""


# function definitions
def average(scores):
    # method 1
    # return sum(scores) / len(scores)
    # method 2
    total = 0;
    num_scores = 0;
    for score in scores:
        print(score)
        total += score
        num_scores += 1
    return total/num_scores


def average_from_input():
    scores = []
    for x in range(5):
        score = float(input('Please enter score #' + str(x+1) + ' '))
        # scores.append(score)
        scores.insert(x, score)
    return sum(scores) / len(scores)


def average_from_user_input():
    scores = []
    num_scores = int(input('Please enter the number of scores '))
    for x in range(num_scores):
        score = float(input('Please enter score #' + str(x+1) + ' '))
        # scores.append(score)
        scores.insert(x, score)
    return sum(scores) / len(scores)

# main
if __name__ == '__main__':
    # print(" The average of 90, 85, 95, 92, 93, 23, 12 is % 5.2f" % average([90, 85, 95, 92, 93, 23, 12]))
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # movies = ["The Princess Bride", "Young Frankenstein", "Serenity"]
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # for movie in movies:
    #     print(movie)
    # movie = "The Princess Bride"
    # for m in movie:
    #     print(m)
    # print(m)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # for x in movies:
    #     if x.__contains__("The"):
    #         print(x)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # for y in movies:
    #     print(y)
    #     if y.__contains__("Young"):
    #         break
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # for x in range(4):
    #     print(x)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # for x in range(1, 5):
    #     print(x)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # for x in range(5, 101, 5):
    #     print(x)
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # for x in range(100, 0, -5):
    #     print(x)
    # print(average_from_input())
    print(average_from_user_input())
