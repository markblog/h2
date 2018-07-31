from datetime import datetime
import calendar

def int_to_timestamp(timestamp):  
    """
    convert an Integer number to timestamp
    
    :param timestamp: suffix millisecond
    :type timestamp: int.
    
    :returns:  timestamp -- [description]
    
    """
    

    return datetime.fromtimestamp(timestamp/1000).strftime('%Y-%m-%d %H:%M:%S')

def datetime_to_timestamp(datetime):
    """
    convert the datetime object to timestamp
    
    :param datetime: [description]
    :type datetime: datetime.
    
    :returns:  int -- milliseconds
    
    """
    
    timestamp_int = calendar.timegm(datetime.timetuple())
    return timestamp_int * 1000

def datetime_to_timestamp_s(datetime):
    """
    convert the datetime object to timestamp
    
    :param datetime: [description]
    :type datetime: datetime.
    
    :returns:  int -- second
    
    """
    
    timestamp_int = calendar.timegm(datetime.timetuple())
    return timestamp_int

def now():
    return calendar.timegm(datetime.utcnow().utctimetuple())

