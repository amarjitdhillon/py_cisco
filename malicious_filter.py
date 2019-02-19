import datetime,sqlite3,json,re

"""
__author__ = "Amarjit Singh Dhillon"
__copyright__ = "Copyright (C) 2019 Amarjit Singh Dhillon"
__license__ = "GPL GNU"
__version__ = "1.0"
__email__ = 'amarjitdhillon@cmail.carleton.ca'
__status__ = 'Development'


------------ Assumptions are written below ------------
pt is a integer lying in range of 1-100 values.  It can't be null.

ts should be a valid date. It can't be null.

si/uu/bg is 36 digit long having lowercase alphanumeric chars of 32 length having ^[a-f0-9]{8}-[a-f0-9]{4}-[1-5][a-f0-9]{3}-[89ab][a-z0-9]{3}-[a-f0-9]{12}$ format,  It can't be null.

sha is 64 digit of lowercase alphanumeric chars having ^[a-fA-F0-9]$ pattern. It can't be null.

nm is a filename which can consist of lowercase+uppercase alphanumeric chars with -(hyphen) and spaces allowed having ^[a-zA-Z- ]+\.[a-z43]+$ pattern.  It can't be null.
        Filenames in nm can have alphanumeric chars but no special chars.
        
pg is a file dirctory structure which can consist ^[/a-zA-Z0-9- ]|[/a-zA-Z0-9]|[/a-zA-Z0-9 ]+\.[a-z43]{2,}$ pattern.  It can't be null.

dp is a value which can be 1|2|3. It can't be null.
"""

def json_validator(log,log_count=0,dirty_count=1,testing=True):
    clean       = True

    # ------------ testing the values of ts ------------
    if log['ts'] != None:                                                           # the value of ts should not be null
        if type(log['ts']) == type(1):                                              # the type of ts should be int
            value = datetime.datetime.fromtimestamp(log['ts'])                      # validate time
            formatted_time = value.strftime('%Y-%m-%d %H:%M:%S')
            if not re.search("^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01]) (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$",formatted_time):
                if not testing: print("Timestamp %s is not valid as per ^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01]) (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9])$ pattern" % (formatted_time))
        else:
            if not testing: print("Error# %6d,log# %6d: The type of ts should be int instead of %s" % (
            dirty_count, log_count, type(log['ts'])))
            clean = False
    else:
        if not testing: print("Error# %6d,log# %6d: The value of ts is not present" % (dirty_count, log_count))
        clean = False

    # ------------ testing the values of pt ------------
    if log['pt'] != None:                                                           # the value of pt should not be null
        if type(log['pt']) != type(1):                                              # the type of pt should be int
            if not testing: print("Error# %6d,log# %6d: The value of pt should be int instead of %s"%(dirty_count,log_count,type(log['pt'])))
            clean = False
    else:
        if not testing: print("Error# %6d,log# %6d: The value of pt is not present"%(dirty_count,log_count))
        clean = False

    # ------------ testing the values of si ------------
    if log['si'] != None:                                                           # the value of si should not be null
        if (len(log['si']) == 36):                                                  # 32 is the length + 4 hyphens
            if not re.search("^[a-f0-9]{8}-[a-f0-9]{4}-[1-5][a-f0-9]{3}-[89ab][a-z0-9]{3}-[a-f0-9]{12}$",log['si']):  # we will check the format only if  the length is fine
                if not testing: print("Error# %6d,log# %6d: The format of si does not follow ^[a-f0-9]{8}-[a-f0-9]{4}-[1-5][a-f0-9]{3}-[89ab][a-z0-9]{3}-[a-f0-9]{12}$ pattern"%(dirty_count,log_count))
                clean = False
        else:
            if not testing: print("Error# %6d,log# %6d: The length of si should be 36 instead of %6d"%(dirty_count,log_count,len(log['si'])))
            clean = False
    else:
        if not testing: print("Error# %6d,log# %6d: The value of si is not present"%(dirty_count,log_count))
        clean = False


    # ------------ testing the values of uu ------------
    if log['uu'] != None:                                                           # the value of uu should not be null
        if (len(log['uu']) == 36):                                                  # 32 is the length + 4 hyphens
            if not re.search("^[a-f0-9]{8}-[a-f0-9]{4}-[1-5][a-f0-9]{3}-[89ab][a-z0-9]{3}-[a-f0-9]{12}$",log['uu']):
                if not testing: print("Error# %6d,log# %6d: The format of uu should follow ^[a-f0-9]{8}-[a-f0-9]{4}-[1-5][a-f0-9]{3}-[89ab][a-z0-9]{3}-[a-f0-9]{12}$ pattern"%(dirty_count,log_count))
                clean = False
        else:
            if not testing: print("Error# %6d,log# %6d: The length of uu should be 36(including 4 hyphens) instead of %d"%(dirty_count,log_count,len(log['uu'])))
            clean = False
    else:
        if not testing: print("Error# %6d,log# %6d: The value of uu is not present"%(dirty_count,log_count))
        clean = False


    # ------------ testing the values of bg ------------
    if log['bg'] != None:                                                           # the value of bg should not be null
        if (len(log['bg']) == 36):                                                  # 32 is the length + 4 hyphens
            if not re.match("^[a-f0-9]{8}-[a-f0-9]{4}-[1-5][a-f0-9]{3}-[89ab][a-z0-9]{3}-[a-f0-9]{12}$",log['bg']):
                if not testing: print("Error# %6d,log# %6d: The format of bg should follow ^[a-f0-9]{8}-[a-f0-9]{4}-[1-5][a-f0-9]{3}-[89ab][a-z0-9]{3}-[a-f0-9]{12}$ pattern"%(dirty_count,log_count))
                clean = False
        else:
            if not testing: print("Error# %6d,log# %6d: The length of bg should be 32 instead of %d"%(dirty_count,log_count,len(log['bg'])))
            clean = False
    else:
        if not testing: print("Error# %6d,log# %6d: The value of bg is not present".format(dirty_count,log_count))
        clean = False



    # ------------ testing the values of sha ------------
    if log['sha'] != None:                                                          # the value of sha should not be null
        if (len(log['sha']) == 64):                                                 # length is is checked only if value is present
            if not re.search("^[a-fA-F0-9]{64}$",log['sha']):  # format will not be checked if length of sha != 64
                if not testing: print("Error# %6d,log# %6d: The format of sha should follow ^[a-fA-F0-9]$ pattern"%(dirty_count,log_count))
                clean = False
        else:
            if not testing: print("Error# %6d,log# %6d: The length of sha should be 64 instead of %d for %s sha value"%(dirty_count,log_count,len(log['sha']), log['sha']))
            clean = False
    else:
        if not testing: print("Error# %6d,log# %6d: The value of sha is not present"%(dirty_count,log_count))
        clean = False


    # ------------ testing the values of nm ------------
    if log['nm'] != None:                                                       # the value of nm should not be null
        if not re.search("^[a-zA-Z- ]+\.[a-z43]+$", log['nm']):
            clean = False
            if not testing: print("Error# %6d,log# %6d: The format of nm %s does not adhere to ^[a-zA-Z- ]+\.[a-z43]+$ pattern"%(dirty_count,log_count,log['nm']))
    else:
        if not testing: print("Error# %6d,log# %6d: File name for nm is not present"%(dirty_count,log_count))
        clean = False



    # ------------ testing the values of ph ------------
    if log['ph'] != None:                                                       # the value of ph should not be null
        if not re.search("^[/a-zA-Z0-9- ]|[/a-zA-Z0-9]|[/a-zA-Z0-9 ]+\.[a-z43]{2,}$", log['ph']):
            if not testing: print("Error# %6d,log# %6d: The format of ph is not as per ^[/a-zA-Z0-9- ]|[/a-zA-Z0-9]|[/a-zA-Z0-9 ]+\.[a-z43]{2,}$ pattern"%(dirty_count,log_count))
            clean = False
    else:
        if not testing: print("Error# %6d,log# %6d: The value of ph is not present"%(dirty_count,log_count))
        clean = False


    # ------------ testing the values of dp ------------
    if log['dp'] != None:                                                      # the value of dp should not be null
        if log['dp'] not in [1, 2, 3]:                                         # the value of dp can be 1|2|3
            if not testing: print("Error# %6d,log# %6d: The value of dp should be 1 or 2 or 3 instead of %d"%(dirty_count,log_count,log['dp']))
            clean = False
    else:
        if not testing: print("Error# %6d,log# %6d: The value of dp is not present".format(dirty_count,log_count))
        clean = False


    if clean:
        return True
    else:
        dirty_count += 1
        return False


if __name__ == "__main__":

    log_count,dirty_count,clean_count = 0,1,0

    try:
        conn = sqlite3.connect("cisco_takehome.sqlite")                                                 # Connect to a database, will create if it does not exists
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE if not exists logs (count_id INTEGER, sha VARCHAR, dp INTEGER )')  # Create the table once
        cursor.execute('Delete from logs')                                                              # Deleting the old data if older table exists

        with open("log.json", "r") as user_logs:                                                        # load the log file
            for log_value in user_logs:                                                                 # iterate over each log value
                log_count += 1  # total number of log entries tested
                log = json.loads(log_value)
                result = json_validator(log,log_count,dirty_count,False)

                # ------------ If clean then save to database, else show error in terminal ------------
                if result:
                    clean_count += 1
                    # cursor.execute('INSERT INTO logs (count_id,sha, dp) VALUES (?,?, ?)',(clean_count, log['sha'], log['dp']))
                    conn.commit()
                else:
                    dirty_count += 1

        print(" \n \n{} logs scanned from which {} number of values have issues while {} entries reported clean".format(log_count, dirty_count - 1, clean_count))

    except sqlite3.Error as e:
        conn.close()
        print("DB connection closed successfully as exception occured")
        print(e)

    finally:
        conn.close()
        print("DB connection closed successfully")