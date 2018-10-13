import tkinter as TK
from tkinter import ttk as TTK
from DBhelpers import get_values_send_and_clear as GETandSENDandCLEAR

# IncomeOutcome Window
# inherited from Toplevel (top-level window)
class IncomeOutcome(TK.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_income_outcome()

    # initializing of objects and window widgets  
    def init_income_outcome(self):
        TK.Tk.iconbitmap(self, default="img/finance.ico")     
        self.title("Добавить доходы/расходы")
        self.geometry("400x220+400+300")
        self.resizable(False, False)
    # END initializing of objects and window widgets          

        # Наименование Entry field
        self.description_field_content = TK.StringVar()
        self.entry_description = TTK.Entry(self,textvariable=self.description_field_content)
        self.entry_description.place(x=200, y=50)
        label_description = TK.Label(self, text="Наименование")
        label_description.place(x=50, y=50)
        # END Наименование Entry field        

        # drop-down income_expense menu
        self.combobox = TTK.Combobox(self, width=17, values=["Доход","Расход"])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)
        label_combobox = TK.Label(self, text="Доход/Расход")
        label_combobox.place(x=50, y=80)
        # END drop-down income_expense menu        

        # Сумма Entry field
        self.money_field_content = TK.DoubleVar()
        self.entry_money = TTK.Entry(self,textvariable=self.money_field_content)
        self.entry_money.place(x=200, y=110)
        label_entry_money = TK.Label(self, text="Сумма")
        label_entry_money.place(x=50, y=110)
        # END Сумма Entry field

        # add button
        btn_add = TTK.Button(self, text="Добавить",
                            command=lambda: GETandSENDandCLEAR(
                                self.description_field_content,
                                self.combobox.get(),
                                self.money_field_content,
                                self.entry_description,
                                self.entry_money))
        btn_add.place(x=220, y=170)
        btn_add.bind("<Button-1>")
        # END add button
        
        # Cancel button
        btn_cancel = TTK.Button(self, text="Назад",
                               command=self.destroy)
        btn_cancel.place(x=300, y=170)
        # END Cancel button        
      
        # grabbing all events from app (???)
        self.grab_set()
        # focus on app
        self.focus_set()
# END IncomeOutcome Window
