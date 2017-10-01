import csv

def readValues():
    with open("numbers.csv", 'r') as csvfile:
        file = csv.reader(csvfile)
        returned = []

        for number_line in file:
            for number in number_line:
                returned.append(list(number))

def evaluateHand(values):
    returned=[]
    for numbers in values:
        dictionary = {}
        for number in numbers:
            if (number in dictionary):
                dictionary[number]= int(dictionary[number]) +1
            else:
                dictionary[number] = int(dictionary[number])
        returned.append(something(dictionary))

def something(dictionary):
    if (len(dictionary)== 5):
        return "Five different"
    elif (len(dictionary)== 4):
        return "Exactly one pair"
    elif (len)

if __name__ == "__main__":
    values=readValues()
    #stats_for_hands=evaluateHand(values)
    #print_stats(stats_for_hands)