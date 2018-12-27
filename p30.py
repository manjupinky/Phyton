
date_format = "%m-%d-%Y %H:%M:%S"
 

time1  = datetime.strptime('8-01-2008 00:00:00', date_format)
time2  = datetime.strptime('8-02-2008 01:30:00', date_format)
 

diff = time2 - time1
 
 
''' days and overall hours between two dates '''
print ('Days & Overall hours from the above two dates')
#print days
days = diff.days
print (str(days) + ' day(s)')
 
#print overall hours
days_to_hours = days * 24
diff_btw_two_times = (diff.seconds) / 3600
overall_hours = days_to_hours + diff_btw_two_times
print (str(overall_hours) + ' hours');
 
 
 
''' now print only the time difference '''
''' between two times (date is ignored) '''
 
print ('\nTime difference between two times (date is not considered)')
 

 
hours = (diff.seconds) / 3600  
print (str(hours) + ' Hours')
 
 

 
minutes = (diff.seconds) / 60
print (str(minutes) + ' Minutes')
 

 
print (str(diff.seconds) + ' secs')

