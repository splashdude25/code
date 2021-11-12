from datetime import datetime as dt
import matplotlib.pyplot as plt

filename = 'Netflix_stock_history.csv'
file = open(filename, 'r')
#print(file.readlines())

#desired structure: dictionary: Key = Date, Value = List of the attached data

dict = {}
lines = file.readlines()[1:]
#Header is: Date,Open,High,Low,Close,Volume,Dividends,Stock Splits

for line in lines:
   temp = line.strip('\n')
   tempList= temp.split(',')
   dict[tempList[0]] = tempList[1:]
#print(dict)
file.close()
'''What we want to measure


prediction 
std over time frame (6 months)
'''
newFile = open('NetflixStats.txt', 'w')

#What is highest close price and the date it was on?

highest = 0.0
highestDate = ''
for key, value in dict.items():

    if float(value[3]) > highest:
        highest = float(value[3])
        highestDate = key
print('Highest Close:', highestDate, highest)
newFile.write('Highest Close: '+ str(highestDate)+' ' + str(highest)+'\n')
#What is lowest close price and the date it was on?

lowest = highest
lowestDate = ''
for key, value in dict.items():

    if float(value[3]) < lowest:
        lowest = float(value[3])
        lowestDate = key
print('Lowest Close:', lowestDate, lowest)
newFile.write('Lowest Close: '+ str(lowestDate)+' ' + str(lowest)+'\n')
#overall change in closing price from first to last date in data set
earliestDate= highestDate
for key, value in dict.items():
    if dt.strptime(key, "%Y-%m-%d") < dt.strptime(earliestDate, "%Y-%m-%d"):
        earliestDate = key

firstClose = dict[earliestDate][3]
print('Earliest Close Price:', earliestDate, firstClose)
newFile.write('Earliest Close Price: '+ str(earliestDate)+' ' + str(firstClose)+'\n')

latestDate= earliestDate
for key, value in dict.items():
    if dt.strptime(key, "%Y-%m-%d") > dt.strptime(latestDate, "%Y-%m-%d"):
        latestDate = key

lastClose = dict[latestDate][3]
print('Latest Close Price:', latestDate, lastClose)
newFile.write('Latest Close Price: '+ str(latestDate)+' ' + str(lastClose)+'\n')
print('Difference in Close Price between Earliest and Eatest:', float(lastClose)-float(firstClose))
newFile.write('Difference in Close Price between Earliest and Eatest: '+ str(float(lastClose)-float(firstClose))+'\n')
#Date with Largest percentage gain from open to close
greatestGain =0
greatestGainDate = ''
for key, value in dict.items():
    open = float(value[0])
    close = float(value[3])
    if (close-open)/open > float(greatestGain):
        greatestGain = (close-open)/open
        greatestGainDate = key

print('Date with Largest percentage gain from open to close:', greatestGainDate, str(greatestGain*100)+'%')
newFile.write('Date with Largest percentage gain from open to close: '+ str(greatestGainDate)+' ' + str(greatestGain*100)+'%'+'\n')
print('open was:', dict[greatestGainDate][0], 'close was:', dict[greatestGainDate][3])
newFile.write('open was:'+ str(dict[greatestGainDate][0])+ ' close was:' + str(dict[greatestGainDate][3]) + '\n')
#Date with Largest percentage loss from open to close
greatestLoss =0
greatestLossDate = ''
for key, value in dict.items():
    open = float(value[0])
    close = float(value[3])
    if (close-open)/open < float(greatestLoss):
        greatestLoss = (close-open)/open
        greatestLossDate = key

print('Date with Largest percentage Loss from open to close:', greatestLossDate, str(greatestLoss*100)+'%')
newFile.write('Date with Largest percentage Loss from open to close: '+ str(greatestLossDate)+' ' + str(greatestLoss*100)+'%'+'\n')
print('open was:', dict[greatestLossDate][0], 'close was:', dict[greatestLossDate][3])
newFile.write('open was:'+ str(dict[greatestLossDate][0])+ ' close was:' + str(dict[greatestLossDate][3]) + '\n')

newFile.close()

#Moving averaging
tempAvg = []
maxLen = 50

for key, value in dict.items():
    close = float(value[3])
    if len(tempAvg) < maxLen:
        tempAvg.append(close)
    else:
        tempAvg.pop(0)
        tempAvg.append(close)
    #get avg from list
    avg = 0
    for num in tempAvg:
        avg += num
    avg = avg/len(tempAvg)
    #add moving average to the list in dict
    value.append(avg)
    dict[key] = value

y= []
for val in dict.values():
    y.append(val[-1])

plt.plot(dict.keys(), y, 'g^')
plt.show()
