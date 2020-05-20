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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def uniqueTelephoneNumbers():
    uniqueNumbers = {}
    uniqueCount = 0 
   
    def incrementUniqueCount(callLog):#0(n)
        nonlocal uniqueCount
        nonlocal uniqueNumbers
      
        for row in callLog:
            sendingNumber = row[0]
            receivingNumber = row[1]
            if(uniqueNumbers.get(sendingNumber)):
                uniqueNumbers[sendingNumber] = uniqueNumbers[sendingNumber] + 1
            else: 
                uniqueNumbers[sendingNumber] = 1
                uniqueCount = uniqueCount + 1
            if(uniqueNumbers.get(receivingNumber)):
                uniqueNumbers[receivingNumber] = uniqueNumbers[receivingNumber] + 1
            else: 
                uniqueNumbers[receivingNumber] = 1
                uniqueCount = uniqueCount + 1
        
    incrementUniqueCount(calls)
    incrementUniqueCount(texts)
    
    return uniqueCount



    

totalUniqueNumbers = str(uniqueTelephoneNumbers())

print("There are " + totalUniqueNumbers + " different telephone numbers in the records.")

"""Worst case Big 0 Analysis:
0(n) time 
0(n) space
"""