import json
from database import get_total_by_months as GETTOTALBYM

#Creting JSON file from data received from DB
def make_json(years):
    data = GETTOTALBYM(years)
    income_data_by_months = []
    expense_data_by_months = []

    for i in range(len(data)):
        month_data = {#'income_expense': data[i][0],
                    #'year': data[i][1],
                    'month': data[i][2],
                    'total': data[i][3]}
        if data[i][0] == 'Доход':
            income_data_by_months.append(month_data)
        else:
            expense_data_by_months.append(month_data)
        
    json_data_file = dict(Доход= income_data_by_months, Расход= expense_data_by_months)
    
    file = open("json_files\json_file.json", "w", encoding='utf-8')
    json.dump(json_data_file, file, ensure_ascii=False)
    file.close()

# Parsing DATA from json
def get_data_from_json(years):
    make_json(years)
    months_income = []
    total_income = []    
    months_expense = []
    total_expense = []
    file = open("json_files\json_file.json", "r", encoding='utf-8')
    string = file.read()
    data_from_json = json.loads(string)
    
    for i in range(len(data_from_json['Доход'])):
        months_income.append(data_from_json['Доход'][i]['month'])
        total_income.append(data_from_json['Доход'][i]['total'])

    for i in range(len(data_from_json['Расход'])):
        months_expense.append(data_from_json['Расход'][i]['month'])
        total_expense.append(data_from_json['Расход'][i]['total'])
                   
    return months_income, total_income, months_expense, total_expense
