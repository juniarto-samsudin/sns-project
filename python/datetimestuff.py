from datetime import datetime 

date_string = '2021-02-05'

date_object = datetime.strptime(date_string, '%Y-%m-%d')

print(date_object)  # Output: 2021-02-05 00:00:00