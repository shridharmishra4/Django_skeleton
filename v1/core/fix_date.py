import datetime
import dateutil.parser
import logging

class DateNormalizer:

    @staticmethod
    def convert_to_utc(date):
        try:
            date = dateutil.parser.parse(date)
            utc_date = date.astimezone()
            return utc_date
        except:
            #log here
            print("TimeZone maybe missing in tzinfo")
            pass


print(DateNormalizer.convert_to_utc("7 feb 2016"))