import tkinter as TK
from tkinter import ttk as TTK
from DBhelpers import get_values_remove_and_clear as GETandREMOVEandCLEAR

# RemoveWindow
class RemoveWindow(TK.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_remove_window()

    # initializing of objects and window widgets
    def init_remove_window(self):
        TK.Tk.iconbitmap(self, default="img/finance.ico")          
        self.title("Удалить запись")
        self.geometry("400x120+400+300")
        self.resizable(False, False)
    # END initializing of objects and window widgets        
        
    # ID
        # ID introduction field
        self.id_field_content = TK.IntVar()
        self.entry_id = TTK.Entry(self, width=8, textvariable=self.id_field_content)
        self.entry_id.place(x=200, y=30)
        label_id = TK.Label(self, text="Введите ID записи")
        label_id.place(x=50, y=30)
        # END ID introduction field

        # Remove record button
        btn_remove = TTK.Button(self, text="Удалить",
                            command=lambda: GETandREMOVEandCLEAR(
                                self.id_field_content,
                                self.entry_id))
        btn_remove.place(x=220, y=80)
        btn_remove.bind("<Button-1>")    
        # END Remove record button
    
        # Cancel button
        btn_cancel = TTK.Button(self, text="Назад",
                               command=self.destroy)
        btn_cancel.place(x=300, y=80)
        # END Cancel button
    # END ID
        
        # grabbing all events from app (???)
        self.grab_set()
        # focus on app
        self.focus_set()     
# END RemoveWindow
