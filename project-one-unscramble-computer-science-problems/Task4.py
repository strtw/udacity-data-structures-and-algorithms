"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def isPossibleTeleMarketer(callLog,textLog):#0(n) time
    def makesCalls(callLog):
        makesCalls = set()
        receivesCalls = set()
        for row in callLog:#0(n)
            sendingNumber = row[0]
            receivingNumber = row[1]
            makesCalls.update([sendingNumber])
            receivesCalls.update([receivingNumber])
        return  makesCalls.difference(receivesCalls)
    def makesTexts(textLog):
        texts = set()
        for row in textLog:#0(n)
            sendingNumber = row[0]
            receivingNumber = row[1]
            texts.update([sendingNumber],[receivingNumber])
        return texts  
    onlyMakesCalls = makesCalls(calls)
    numbersThatText = makesTexts(texts)
    return sorted(list(onlyMakesCalls.difference(numbersThatText)))


def printAnswer():
    possibleTelemarketers = isPossibleTeleMarketer(calls,texts) #0(n)
    print("These numbers could be telemarketers:")
    for number in possibleTelemarketers:#0(n)
        print(number)

printAnswer()

"""Worst case Big 0 Analysis in printAnswer:
#O(n log n)
"""