import time
import datetime


def current_date_plus_time():
    current_time = time.time()
    date = str(datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S'))
    return date

def get_date_of_file_modif():
    '''Returning the last modification date of the file'''
    
    loc_of_db_file = "db/FinanceHolderDB.sqlite"
    modif_date = str(time.ctime(os.path.getmtime(loc_of_db_file)))

    temp_arr = modif_date.split(' ') 
    temp_arr.pop(2)
    temp_arr[3], temp_arr[4] = temp_arr[4], temp_arr[3]
    modif_date = ' '.join(temp_arr)

    return modif_date
