import tkinter as TK
from tkinter import ttk as TTK
from DBhelpers import get_calculated_value_store_and_set as GETCALC


# CalcWindow
class CalcWindow(TK.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_calc_window()

    # initializing of objects and window widgets
    def init_calc_window(self):
        TK.Tk.iconbitmap(self, default="img/finance.ico")           
        self.title("Калькулятор")
        self.geometry("400x220+400+300")
        self.resizable(False, False)
    # END initializing of objects and window widgets


# Date year-month-day        
        years = ["2017", "2018", "2019", "2020", "2021"]
        months = ["01", "02", "03", "04", "05", "06", "07", "08",
                  "09", "10", "11", "12"]
        days = ["01", "02", "03", "04", "05", "06", "07", "08",
                  "09", "10", "11", "12", "13", "14", "15", "16",
                "17", "18", "19", "20", "21", "22", "23", "24",
                "25", "26", "27", "28", "29", "30", "31"]
        
    # Date - BEFORE
        label_date_before = TK.Label(self, text="Начальная дата")
        label_date_before.place(x=5, y=5)
        
        # Year drop-down menu
        self.year_before_combobox = TTK.Combobox(self, width=5, values=years)
        self.year_before_combobox.current(1)
        self.year_before_combobox.place(x=120, y=5)
        # END Year drop-down menu

        # Month drop-down menu
        self.month_before_combobox = TTK.Combobox(self, width=3, values=months)
        self.month_before_combobox.current(0)
        self.month_before_combobox.place(x=180, y=5)
        # END Month drop-down menu
        
        # Day field
        self.day_before_combobox = TTK.Combobox(self, width=3, values=days)
        self.day_before_combobox.current(0)
        self.day_before_combobox.place(x=228, y=5)
        # End day field
    # END Date - BEFORE

    # Date - AFTER
        label_date_after = TK.Label(self, text="Конечная дата")
        label_date_after.place(x=5, y=35)
        
        # Year drop-down menu
        self.year_after_combobox = TTK.Combobox(self, width=5, values=years)
        self.year_after_combobox.current(1)
        self.year_after_combobox.place(x=120, y=35)
        # END Year drop-down menu

        # Month drop-down menu
        self.month_after_combobox = TTK.Combobox(self, width=3, values=months)
        self.month_after_combobox.current(0)
        self.month_after_combobox.place(x=180, y=35)
        # END Month drop-down menu
        
        # Day field
        self.day_after_combobox = TTK.Combobox(self, width=3, values=days)
        self.day_after_combobox.current(0)
        self.day_after_combobox.place(x=228, y=35)
        # End day field
    # END Date - AFTER
# END Date year-month-day

    # Income-outcome
        income_outcome_options = ["Разница", "Доход", "Расход"]
        label_income_expense_combobox = TK.Label(self,
                                                 text="Тип")
        label_income_expense_combobox.place(x=5, y=65)
        
        # drop-down income_expense menu
        self.income_expense_combobox = TTK.Combobox(
            self, width=19, values=income_outcome_options)
        self.income_expense_combobox.current(0)
        self.income_expense_combobox.place(x=120, y=65)
        # END drop-down income_expense menu      
    # END Income-outcome

    # Calculated value introduction field
        label_calc_field = TK.Label(self, text="Результат")
        label_calc_field.place(x=5, y=95)
        
        self.calc_value_content = TK.DoubleVar()
        self.calc_field = TTK.Entry(self, width=22, textvariable=self.calc_value_content)
        self.calc_field.place(x=120, y=95)
    # END Calculated value introduction field

    # Income-outcome Calc record button
        btn_CalcIO = TTK.Button(self, text="Рассчитать",
                               command=lambda: GETCALC((self.year_before_combobox.get(), self.month_before_combobox.get(), self.day_before_combobox.get(),
                                                        self.year_after_combobox.get(), self.month_after_combobox.get(), self.day_after_combobox.get(),
                                                        self.income_expense_combobox.get()),
                                                       self.calc_value_content))
        btn_CalcIO.place(x=220, y=170)
        btn_CalcIO.bind("<Button-1>")
    # END Income-outcome Calc record button      

    # Cancel button
        btn_cancel = TTK.Button(self, text="Назад",
                               command=self.destroy)
        btn_cancel.place(x=300, y=170)
    # END Cancel button
    
        # grabbing all events from app (???)
        self.grab_set()
        # focus on app
        self.focus_set()
# END CalcWindow
