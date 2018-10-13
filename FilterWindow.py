import tkinter as TK
from tkinter import ttk as TTK
from DBhelpers import refresh_table_by_query as REFQ

# FilterWindow
class FilterWindow(TK.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_filter_window()

    # initializing of objects and window widgets
    def init_filter_window(self):
        TK.Tk.iconbitmap(self, default="img/finance.ico")        
        self.title("Фильтры")
        self.geometry("650x450+300+200")
        self.resizable(False, False)
    # END initializing of objects and window widgets        
        
    # Date
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
        income_outcome_options = ["Все", "Доход", "Расход"]
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

        # Income-outcome Filter record button
        btn_CalcIO = TTK.Button(self, text="Показать", command=lambda: REFQ(self.tree,
                                                                           (self.year_before_combobox.get(), self.month_before_combobox.get(), self.day_before_combobox.get(),
                                                                            self.year_after_combobox.get(), self.month_after_combobox.get(), self.day_after_combobox.get(),
                                                                            self.income_expense_combobox.get())))
        btn_CalcIO.place(x=470, y=90)
        btn_CalcIO.bind("<Button-1>")  
        # END Income-outcome Filter record button        
    
    # Cancel button
        btn_cancel = TTK.Button(self, text="Назад",
                               command=self.destroy)
        btn_cancel.place(x=550, y=90)
    # END Cancel button
    
# table with records
        self.tree = TTK.Treeview(self, columns=("id", "creationdata",
                                                "description",
                                                "income_expense",
                                                "total"),
                                 height=15, show="headings")
        self.tree.column("id", width=30, anchor=TK.CENTER)
        self.tree.column("creationdata", width=150, anchor=TK.CENTER)
        self.tree.column("description", width=215, anchor=TK.W)
        self.tree.column("income_expense", width=150, anchor=TK.CENTER)
        self.tree.column("total", width=100, anchor=TK.W)

        # giving displayment names for columns
        self.tree.heading("id", text="id")
        self.tree.heading("creationdata", text="Дата")        
        self.tree.heading("description", text="Наименование")
        self.tree.heading("income_expense", text="Доход / Расход")
        self.tree.heading("total", text="Сумма")
      
        # display table
        self.tree.pack(side=TK.BOTTOM)
# END table with records    
        
        # grabbing all events from app (???)
        self.grab_set()
        # focus on app
        self.focus_set()     
# END FilterWindow

