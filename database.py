import sqlite3
import dropbox
from shutil import copyfile
from usefulfeatures import current_date_plus_time
from AlertWindow import AlertWindow


# name of DB + connection
sqlite_file = 'db/FinanceHolderDB.sqlite'
conn = sqlite3.connect(sqlite_file)

# Drop-box part
drop_box_file = '/FinanceHolderDB.sqlite'
token_MK = 'lNvVQGGrElgAAAAAAAB6lMUT80T8ShPtdNp4u8z0iiHPPcJiEs0vvkWBBoFJFyDF'


# CREATE finances TABLE
def create_table():
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS finances (
id INTEGER PRIMARY KEY ASC, creationdata TEXT, description TEXT,
income_expense TEXT, total REAL)
''')
    c.close()


# INSERT new record in finances TABLE
def data_insert(creationdata, description, income_expense, total):
    c = conn.cursor()
    c.execute('''INSERT INTO finances (creationdata, description,
income_expense, total) VALUES (?, ?, ?, ?)''', (creationdata,
                                                description,
                                                income_expense, total))
    conn.commit()
    c.close


# DELETEing record from finances TABLE by ID
def data_remove(idd):
    c = conn.cursor()
    c.execute("DELETE FROM finances WHERE id=?", (idd,))
    conn.commit()
    c.close


# SELECT * records from finances and DISPLAY them in the TABLE
def display_records(tree):
    c = conn.cursor()
    db_rows = c.execute("SELECT * FROM finances ORDER BY id ASC")
    for row in db_rows:
        tree.insert('', 0, values=(row[0], row[1], row[2], row[3], row[4]))


# SELECT recods from finances by QUERY
def display_records_by_query(tree, date_before, date_after, selected_option):
    c = conn.cursor()
    if selected_option == 'Все':
        db_rows = c.execute("SELECT * FROM finances WHERE date(creationdata) BETWEEN ? AND ? ORDER BY id DESC",
                            (date_before, date_after,))
        for row in db_rows:
            tree.insert('', 0, values=(row[0], row[1], row[2], row[3], row[4]))
    else:
        db_rows = c.execute("SELECT * FROM finances WHERE date(creationdata) BETWEEN ? AND ? AND income_expense = ? ORDER BY id DESC",
                  (date_before, date_after, selected_option,))                        
        for row in db_rows:
            tree.insert('', 0, values=(row[0], row[1], row[2], row[3], row[4]))        
        

# Calculating depending from query (based on dates and selected option (income/expense/balance))
def calc_income_expense(date_before, date_after, selected_option):    
    c = conn.cursor()
    c.execute("SELECT SUM(total) FROM finances WHERE date(creationdata) BETWEEN ? AND ? AND income_expense = 'Доход'",
              (date_before, date_after,))
    income = c.fetchone()[0]
    c.execute("SELECT SUM(total) FROM finances WHERE date(creationdata) BETWEEN ? AND ? AND income_expense = 'Расход'",
              (date_before, date_after,))
    expense = c.fetchone()[0]

    if selected_option == 'Разница' and income != None and expense != None:
        return income - expense
    elif selected_option == 'Доход' and income != None:
        return income
    elif selected_option == 'Расход' and expense != None:
        return expense
    else:
        return 'Nothing for these dates...'


# Upload file from Drop Box
def upld_file(window):
    try:
        local_file = open(sqlite_file, 'rb')
        dbx = dropbox.Dropbox(token_MK)
        dbx.files_upload(local_file.read(), drop_box_file, mode=dropbox.files.WriteMode.overwrite)
        local_file.close()
        window.destroy()
    except:
        AlertWindow("""
Интернет соеденение отсутвует...
Проверьте соединение и
повторите попытку.""")    

    
# Download file to Drop Box
def dwnld_file(window):
    try:
        backup_function()
        local_file = sqlite_file
        dbx = dropbox.Dropbox(token_MK)
        dbx.files_download_to_file(local_file, drop_box_file)
        window.destroy()
    except:
        AlertWindow("""
Интернет соеденение отсутвует...
Проверьте соединение и
повторите попытку.""")


# Get a list of totals by months
def get_total_by_months(year):
    c = conn.cursor()
    dataa = []
    db_rows = c.execute('''
SELECT income_expense as INCOME_EXPENSE, strftime('%Y', creationdata), strftime('%m', creationdata) as MONTH, SUM(total) as TOTAL 
FROM finances
WHERE  strftime('%Y', creationdata) = ? AND (income_expense = "Расход" OR  income_expense = "Доход")
GROUP BY Month, INCOME_EXPENSE''', (year,))
    for row in db_rows:
        dataa.append(list(row))
    return dataa


#backup function creation copy of the current DB file and store it to backup folder
def backup_function():
    current_date_and_time = current_date_plus_time()
    current_date_and_time = current_date_and_time.replace(":", "-")
    
    current_db_name = sqlite_file
    new_db_name = "db/backup/" + current_date_and_time + "_FinanceHolderDB.sqlite"
    copyfile(current_db_name, new_db_name)
      

# UPDATE THIS PART
# every time script is running it will try to create DB    
create_table()
