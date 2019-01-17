birthday = "1-May-12"
from datetime import datetime
date_format = "%d-%B-%y"

#Print 5/1/2012
parsed_date = datetime.strptime(birthday, date_format)
date_str = parsed_date.strftime("%-m/%-d/%Y")
print(date_str)