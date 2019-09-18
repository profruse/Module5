"""docstring stuff
"""


def averages():
    scores = []
    message = "Please enter a score, a negative number to stop "
    score = float(input(message))
    while score >= 0:
        scores.append(score)
        score = float(input(message))
    if len(scores) == 0:
        raise ZeroDivisionError
    return sum(scores) / len(scores)


def averages_2():
    scores = []
    score = 0
    message = "Please enter a score, a negative number to stop " # sentinnel value/flag
    while score >= 0:
        score = float(input(message))
        if score < 0:
            break
        scores.append(score)
    return sum(scores) / len(scores)


if __name__ == '__main__':
    # try:
    #     print(averages())
    # except ZeroDivisionError:
    #     print("Divide by Zero!")
    # print(averages_2())

    # while True:
    #     print("this goes on forever!!!")

    # # common mistake not update the looping variable
    # x = 20
    # while x > 10:
    #     print (x)
    # print("Done!")

    # common mistake never enter loop CHECK <, <=, >, >=
    x = 20
    while x < 10:
        print(x)
        x -= 2;
    x = 20
    while x > 10:
        print(x)
        x -= 2;
        if x == 14:
            continue
        print("NEXT")
    print("Done!")
