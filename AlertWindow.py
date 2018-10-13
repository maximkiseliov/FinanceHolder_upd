import tkinter as TK
from tkinter import ttk as TTK

# AlertWindow
class AlertWindow(TK.Toplevel):
    def __init__(self, error_text):
        super().__init__()
        self.error_text = error_text
        self.alert_window()

    # initializing of objects and window widgets
    def alert_window(self):
        TK.Tk.iconbitmap(self, default="img/finance.ico")          
        self.title("Ошибка")
        self.geometry("280x120+500+350")
        self.resizable(False, False)
    # END initializing of objects and window widgets        
        
    # Alert message
        # Alert message text
        alert_message = TK.Label(self, text=self.error_text)
        alert_message.place(x=50, y=0)
        # END Alert message text
    
        # Back button
        btn_back = TTK.Button(self, text="Назад",
                               command=self.destroy)
        btn_back.place(x=100, y=80)
        # END Cancel button
    # END Alert message
        
        # grabbing all events from app (???)
        self.grab_set()
        # focus on app
        self.focus_set()     
# END AlertWindow
