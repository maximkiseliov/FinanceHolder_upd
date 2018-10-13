import tkinter as TK
from database import data_insert as INS
from database import display_records as SEL
from database import data_remove as REM
from database import display_records_by_query as SELBYQ
from database import calc_income_expense as CALC
from JSONwork import get_data_from_json as GETDATAJSON
from usefulfeatures import current_date_plus_time

# refresh records in the table - first DELETE all records then ADD
# then back by SELECTing * records FROM finances TABLE
def refresh_table(tree):
    x = tree.get_children()
    for child in x:
        tree.delete(child)
    SEL(tree)


# getting values from fields, sending them to finances TABLE and
# clearing fields
def get_values_send_and_clear(description, income_expense, total, entry_description, entry_money):  
    if entry_money.get() != "" and description.get() != "" and entry_money.get() != 0.0:
        creationdata = current_date_plus_time()
        INS(creationdata, description.get(), income_expense, total.get())
        entry_description.delete(0, 'end')
        entry_money.delete(0, 'end')
    else:
        pass


# getting id from fields, deleting them from finances TABLE and
# clearing fields
def get_values_remove_and_clear(idd, entry_idd):
    if entry_idd.get() != "" and idd.get() != 0 and idd.get() != "":
        REM(idd.get())
        entry_idd.delete(0, 'end')
    else:
        pass


def refresh_table_by_query(tree, values):
    date_before = values[0]+'-'+values[1]+'-'+values[2]
    date_after = values[3]+'-'+values[4]+'-'+values[5]
    selected_option = values[6]
    
    x = tree.get_children()
    for child in x:
        tree.delete(child)
    SELBYQ(tree, date_before, date_after, selected_option)


def get_calculated_value_store_and_set(values, field):
    date_before = values[0]+'-'+values[1]+'-'+values[2]
    date_after = values[3]+'-'+values[4]+'-'+values[5]
    selected_option = values[6]
    calculated = CALC(date_before, date_after, selected_option)
    #if-else added to verify if calculated is str or float in order to corretly use round func
    if isinstance(calculated, str):
        field.set(calculated)
    else:
        field.set(round(calculated, 2))
