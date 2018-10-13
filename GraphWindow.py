import tkinter as TK
from tkinter import ttk as TTK
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
from JSONwork import get_data_from_json as GETANDSET


# GraphWindow
class GraphWindow(TK.Toplevel):
    def __init__(self):
        super().__init__()
        self.init_graph_window()

    # initializing of objects and window widgets
    def init_graph_window(self):
        TK.Tk.iconbitmap(self, default="img/finance.ico")           
        self.title("График")
        self.geometry("810x450+300+200")
        self.resizable(False, False)
    # END initializing of objects and window widgets
    
    # Graph
        #graph style
        style.use("ggplot")

        f = Figure(figsize=(8,4), dpi=100)
        a = f.add_subplot(111)        
        # Graph image
        months_income, total_income, months_expense, total_expense = GETANDSET("2018")
        
        a.plot(months_income, total_income, "g", label="Доходы")
        
        a.plot(months_expense, total_expense, "r", label="Расходы")
        a.set_ylabel('Сумма')
        a.set_xlabel('Месяц')        
        a.legend()
        title = "График ежемесячных доходов / расходов"
        a.set_title(title)
        
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().place(x=5, y=5)
        
        # END Graph image

        # Toolbar
        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        # END toolbar
    # END Graph
           
        # Cancel button
        btn_cancel = TTK.Button(self, text="Назад",
                               command=self.destroy)
        btn_cancel.place(x=630, y=420)
        # END Cancel button
        
        # grabbing all events from app (???)
        self.grab_set()
        # focus on app
        self.focus_set()     
# END GraphWindow
