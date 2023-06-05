import sys
from time import time
from random import seed
import random
from matplotlib import pyplot as plt


class ScoreNumber(object):  # create an object to save the scores of the players used in the leaderboard dictionary
    def __init__(self, Score):
        self.score = Score

    def __str__(self):
        return self.score

    def __repr__(self):
        return "'" + self.score + "'"


player_data = {  # initiate dictionary containing the names of the players as data and their scores as the key
    ScoreNumber("73"): "Napaladin",
    ScoreNumber("20"): "Cocowboy",
    ScoreNumber("15"): "Oysterminate",
    ScoreNumber("67"): "RadioactiveYak",
    ScoreNumber("65"): "RudeFlamingo",
    ScoreNumber("93"): "RadioactiveRose",
    ScoreNumber("90"): "Rerunner",
    ScoreNumber("85"): "Gerbilbo",
    ScoreNumber("37"): "Lobsteroid",
    ScoreNumber("18"): "GiantChimera",
    ScoreNumber("26"): "DapperFledgling",
    ScoreNumber("83"): "ClassicRoach",
    ScoreNumber("24"): "Patriode",
    ScoreNumber("71"): "BalanceBot",
    ScoreNumber("3"): "NurNNNN",
    ScoreNumber("49"): "SmartGull",
    ScoreNumber("90"): "MeanKoala",
    ScoreNumber("55"): "Cloverlord",
    ScoreNumber("90"): "Warthawk",
    ScoreNumber("52"): "StrongFlike"}


def bubbleSorting(array):
    operations_bubble = 0

    sorting = False  # will be false until the array is fully organised, so the loop can start

    while sorting is False:
        sorting = True

        for x in range(len(array)):
            if (x + 1) == len(array):
                break

            operations_bubble += 1  # counter for the operations it goes through

            if array[x] > array[x + 1]:  # if the index which the loop is on now is bigger then the one after then:

                array.insert(x, array[x + 1])  # insert the smaller number at the index of the larger number
                array.pop(x + 2)  # then get rid of the duplicate of the larger number made
                sorting = False  # set this to false to show that a change is made therefore the array is not sorted yet

    return operations_bubble


def leaderboard(Numbers):  # takes in the array which has now been sorted
    prev = 0

    for x in Numbers:  # for each number in the array
        if prev == x:  # check if its equal to previous so no duplicate numbers get printed
            pass
        else:
            for player_score in player_data.keys():
                if str(x) == str(
                        player_score):  # check if the current value being tested is equal to any of the keys in dictionary
                    print("Player " + player_data[player_score] + " has a score of " + str(
                        player_score))  # print the full data

        prev = x  # make the current value of the array being tested equal to the var


def randomNumber():  # generating an array of different sizes with random numbers to test different complexities of sorting
    global operationM
    Random_numbers = []  # begin a new array

    Random_numbers.clear()   # clear the array ready to be used
    for x in range(100): # for loop which will run 100 times
        Random_numbers.append(random.randint(0, 100))  # add a random number
    operationsB1 = bubbleSorting(Random_numbers)  # 0.0024046000000019774      9207 ops
    print("\nthis took only (bubble) " + str(operationsB1) + " operations\n\n\n")

    Random_numbers.clear()
    for x in range(100):
        Random_numbers.append(random.randint(0, 100))
    operationM = 0
    mergeSorting(Random_numbers)  # 0.00027810000000005886        99 ops
    operationsM1 = operationM
    print("this took only (merge) " + str(operationsM1) + " operations\n\n\n")

    print("----")

    Random_numbers.clear()
    for x in range(10000):
        Random_numbers.append(random.randint(0, 10000))
    operationsB2 = bubbleSorting(Random_numbers)  # 96.0664993      99160083 ops
    print("\nthis took only (bubble) " + str(operationsB2) + "\n\n\n")

    Random_numbers.clear()
    for x in range(10000):
        Random_numbers.append(random.randint(0, 10000))
    operationM = 0
    mergeSorting(Random_numbers)  # 0.02027810000000005886     9999 ops
    operationsM2 = operationM
    print("this took only (merge) " + str(operationsM2) + " operations\n\n\n")

    print("----")

    Random_numbers.clear()
    for x in range(1000000):
        Random_numbers.append(random.randint(0, 1000000))
    operationsB3 = bubbleSorting(Random_numbers)  # more than 1 day
    print("\nthis took only (bubble) " + str(operationsB3) + "\n\n\n")

    Random_numbers.clear()
    for x in range(1000000):
        Random_numbers.append(random.randint(0, 1000000))
    operationM = 0
    mergeSorting(Random_numbers)  # 7.5 seconds      999999 ops
    operationsM3 = operationM
    print("this took only (merge) " + str(operationsM3) + " operations\n\n\n")

    x1 = [100, 10000, 1000000]  # saving everything in arrays for then to be used in the graph
    y1 = [operationsB1, operationsB2]
    y2 = [operationsM1, operationsM2, operationsM3]

    plt.plot(x1, y1, label="bubble sorting")
    plt.plot(x1, y2, label="merge sorting")

    plt.xlabel('Elements number')
    plt.ylabel('Operations')
    plt.title('Sorting n amount of random numbers')
    plt.legend()
    plt.show()


def mergeSorting(array):  # take in the array
    global operationM  # the operation counter "needs" to be global as it this function cant return the operations number

    if len(array) > 1:  # if the array given has more than one element
        operationM += 1  # add 1 to the global counter

        middle = len(array) // 2  # divide the array given

        left = array[:middle]  # save each half into different sub-arrays
        right = array[middle:]

        mergeSorting(left)  # then send them back to be re-divided (recursion)
        mergeSorting(right)

        x = 0  # index of the left array
        y = 0  # index of the right array
        i = 0  # index of the main array

        while x < len(left) and y < len(
                right):  # conditions to finally merge the list back, run until none of the two lists have been exhausted

            if left[x] > right[y]:  # we see which one is smaller
                array[i] = right[y]  # we replace the value at index k of the main arrays with the smaller value
                i += 1
                y += 1
            else:  # then depending on the left or right chosen array we increment the index to find the next suitable value
                array[i] = left[x]
                i += 1
                x += 1

        while x < len(
                left):  # if one of the arrays were to be exhausted then we just deal with the one that is left, which is also already sorted due to recursion
            array[i] = left[x]
            i += 1
            x += 1

        while y < len(right):
            array[i] = right[y]
            i += 1
            y += 1


if __name__ == '__main__':
    seed(time())
    operationM = 0

    while True:
        player_input = input(
            "\n\nWhat would you like to use, bubble(b) sorting, merge(m) sorting, random numbers(n) with graph or quit(q): ")  # main menu

        if player_input == "m":
            Numbers = [73, 20, 15, 67, 65, 93, 90, 85, 37, 18, 26, 83, 24, 71, 3, 49, 90, 55, 90, 52]
            mergeSorting(Numbers)
            leaderboard(Numbers)
        elif player_input == "b":
            Numbers = [73, 20, 15, 67, 65, 93, 90, 85, 37, 18, 26, 83, 24, 71, 3, 49, 90, 55, 90, 52]
            bubbleSorting(Numbers)
            leaderboard(Numbers)
        elif player_input == "n":
            randomNumber()
        elif player_input == "q":
            break
        else:
            print("sorry dint get that")

    sys.exit(0)
