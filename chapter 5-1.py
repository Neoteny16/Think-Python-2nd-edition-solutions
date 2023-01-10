import time
tp = int(time.time())  # time passed in int. time.time() shows seconds passed since epoch
seconds = tp % 60
minutes = tp // 60 % 60
hours = tp // (60 * 60) % 24
days = tp // (60 * 60 * 24)
year = tp // (60 * 60 * 24 * 365) + 1970
month = tp // (60 * 60 * 24 * 31) % 12  # need some table to convert months to ints and return


print('Current time:\n' + str(hours) + ':' + str(minutes) + ':' + str(seconds) + ' ' + str(year))
print('Days passed since epoch:\n',  days)




