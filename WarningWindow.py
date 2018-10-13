import tkinter as TK
from tkinter import ttk as TTK
from database import dwnld_file as DWNLD
from database import upld_file as UPLD

# WarningWindow
class WarningWindow(TK.Toplevel):
    def __init__(self, action):
        super().__init__()
        self.action = action
        self.warning_message()

    # initializing of objects and window widgets
    def warning_message(self):
        TK.Tk.iconbitmap(self, default="img/finance.ico")          
        self.title("%s файл" % (self.action.capitalize()))
        self.geometry("255x120+500+350")
        self.resizable(False, False)
    # END initializing of objects and window widgets        
        
    # Message
        # Warning message text
        warning_message = TK.Label(self, text="""Вы действительно хотите %s файл?
При %s файла, текущий файл
будет заменен и безвозвратно утерян.""" % (self.action, self.action[:-3]+"ке"))
        warning_message.place(x=10, y=0)
        # Warning message text

        # Action button
        btn_action = TTK.Button(self, text=self.action.capitalize(),
                                command=lambda:DWNLD(self) if self.action == 'скачать' else UPLD(self))
        btn_action.place(x=30, y=80)
        btn_action.bind("<Button-1>")    
        # END Action button
    
        # Cancel button
        btn_cancel = TTK.Button(self, text="Назад",
                               command=self.destroy)
        btn_cancel.place(x=150, y=80)
        # END Cancel button
    # END Message
        
        # grabbing all events from app (???)
        self.grab_set()
        # focus on app
        self.focus_set()     
# END WarningWindow
