import re

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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.
"""

def isBangaloreCall(phoneNumber):
    """Determine whether the given telephone number is from Bangalore"""
    return phoneNumber[:5] == '(080)'

def isTelemarketer(phoneNumber):
    """Determine whether the given telephone number is a know telemarketer"""
    return phoneNumber[:3] == '140'

def isMobile(phoneNumber):
    """Determine whether the given telephone number belongs to a mobile (cell) phone"""
    return phoneNumber[:1] in ['7', '8', '9']
  
def getLandline(phoneNumber):
    patternLandline = re.compile('^\(0[0-9]+\)')
    return patternLandline.search(phoneNumber)[0]

def callCodesFromBanagalore(callLogs):#O(n log n) + 0(n*m) = 0(n^2)
  numbersCalled = []
  for row in callLogs: #0(n)
    sendingNumber = row[0]
    receivingNumber = row[1]
    if isBangaloreCall(sendingNumber):#0(n)
      receivingCode = getNumberCode(receivingNumber)#0(n)
      numbersCalled.append(receivingCode)#0(1)
  return sorted(set(numbersCalled)) #O(n log n)

def getNumberCode(phoneNumber): #0(n)
    if(isMobile(phoneNumber)):
      code = phoneNumber[:4]
    elif(isTelemarketer(phoneNumber)):
      code = phoneNumber[:3]
    else:
      code = getLandline(phoneNumber)
    return code


def printCallsFromBangalore():
  callCodes = callCodesFromBanagalore(calls)
  print("The numbers called by people in Bangalore have codes:")
  for code in callCodes:
   print(code)

printCallsFromBangalore()
"""
Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def interBangaloreFixedCalls(callLogs):
  interBangaloreFixedCallCount = 0
  fixedCallsFromBangalore = 0
  for row in callLogs: #0(n)
    sendingNumber = row[0]
    receivingNumber = row[1]
    if isBangaloreCall(sendingNumber):#0(1)
       fixedCallsFromBangalore = fixedCallsFromBangalore + 1
       if(isBangaloreCall(receivingNumber)):#0(1)
        interBangaloreFixedCallCount = interBangaloreFixedCallCount + 1
  if(fixedCallsFromBangalore == 0):
    return 0
  else:
    return round(interBangaloreFixedCallCount / fixedCallsFromBangalore * 100, 2 )

def printPercentBangaloreInterFixedCalls():
  percent = interBangaloreFixedCalls(calls)
  print('{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.'.format(percent))

printPercentBangaloreInterFixedCalls()

#print(interBangaloreFixedCalls([['(080)','(080)']]))
#print(interBangaloreFixedCalls([['1','(080)']]))
#print(interBangaloreFixedCalls([['(080)','(080)'],['(080)','1']]))

"""Worst case Big 0 Analysis Part A:
#O(n log n) time 
0(n) space
"""


"""Worst case Big 0 Analysis Part B:
0(n) time 
0(1) space
"""