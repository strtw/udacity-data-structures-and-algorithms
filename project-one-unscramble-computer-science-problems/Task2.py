"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def longestCall(logList):
    longestCallData = {
        'phoneNumber':None,
        'duration':0
    }
    uniqueCall = {}
    for row in logList:
        sendingNumber = row[0]
        receivingNumber = row[1]
        callDuration = row[3]
        if(uniqueCall.get(sendingNumber)):# if our counting dict has the sending number in this row
            uniqueCall[sendingNumber] = uniqueCall[sendingNumber] + int(callDuration) # increment the duration for this number
        else: 
            uniqueCall[sendingNumber] = int(callDuration)#It's the first instance, set it, and the duration
        if(uniqueCall.get(receivingNumber)):
            uniqueCall[receivingNumber] = uniqueCall[receivingNumber] + int(callDuration)
        else: 
            uniqueCall[receivingNumber] = int(callDuration)
    
    for call in uniqueCall:
        if uniqueCall[call] > longestCallData['duration']:
            longestCallData['duration'] = uniqueCall[call]
            longestCallData['phoneNumber'] = call

    return longestCallData

"""test = [["1","2","01-09-2016 06:01:12","186"],
["3","4","01-09-2016 06:01:59","2093"],
["5","6","01-09-2016 06:03:51","1975"]]
test1 = [["1","2","01-09-2016 06:01:12","186"]] #Ties not handled
"""

longestCallData = longestCall(calls)

print(longestCallData['phoneNumber'] + " spent the longest time, " + str(longestCallData['duration']) + " seconds, on the phone during September 2016.")



"""Worst case Big 0 Analysis:
0(n) time
0(1) space
"""