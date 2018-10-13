import tkinter as TK
from tkinter import ttk as TTK
from IncomeOutcome import IncomeOutcome
from RemoveWindow import RemoveWindow
from FilterWindow import FilterWindow
from CalcWindow import CalcWindow
from GraphWindow import GraphWindow
from WarningWindow import WarningWindow
from DBhelpers import refresh_table as REFRESH
from database import display_records as SEL



# Main Window
class Main(TK.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    # initializing of objects and window widgets
    def init_main(self):
        # тулбар bg - цвет фона, bb - граница 
        toolbar = TK.Frame(bg="#d7d8e0", bd=2)
        # side=TK.TOP - закрепляет тулбар в верхней части окна
        # fill=TK.X - растягивает по горизонтали
        toolbar.pack(side=TK.TOP, fill=TK.X)
        # END initializing of objects and window widgets
        
        # income_outcome button
        self.add_img = TK.PhotoImage(file="img/add.png")
        btn_open_dialog = TK.Button(toolbar, text="Добавить",
                                    command= lambda: IncomeOutcome(),
                                    bg="#FFFFFF", bd=2,
                                    compound=TK.TOP,
                                    image=self.add_img)
        btn_open_dialog.pack(side=TK.LEFT)
        # END income_outcome button

        # remove record button
        self.remove_img = TK.PhotoImage(file="img/remove.png")
        btn_open_remove_record = TK.Button(toolbar, text="Удалить",
                                           command=lambda: RemoveWindow(),
                                           bg="#FFFFFF", bd=2,
                                           compound=TK.TOP,
                                           image=self.remove_img)
        btn_open_remove_record.pack(side=TK.LEFT)
        # END remove record button

        # filter button
        self.filter_img = TK.PhotoImage(file="img/filter.png")
        btn_open_filter = TK.Button(toolbar, text="Фильтр",
                                    command=lambda: FilterWindow(),
                                    bg="#FFFFFF", bd=2,
                                    compound=TK.TOP,
                                    image=self.filter_img)
        btn_open_filter.pack(side=TK.LEFT)
        # END filter button

        # calc button
        self.calc_img = TK.PhotoImage(file="img/calc.png")
        btn_open_calc = TK.Button(toolbar, text="Калькулятор",
                                  command=lambda: CalcWindow(),
                                  bg="#FFFFFF", bd=2,
                                  compound=TK.TOP,
                                  image=self.calc_img)
        btn_open_calc.pack(side=TK.LEFT)
        # END calc button

        # graph button
        self.graph_img = TK.PhotoImage(file="img/graph.png")
        btn_open_graph = TK.Button(toolbar, text="График",
                                  command=lambda: GraphWindow(),
                                  bg="#FFFFFF", bd=2,
                                  compound=TK.TOP,
                                  image=self.graph_img)
        btn_open_graph.pack(side=TK.LEFT)        
        # END graph button

        # exit button
        self.exit_img = TK.PhotoImage(file="img/exit.png")
        btn_exit = TK.Button(toolbar, text="Выход",
                                command=quit,
                                bg="#FFFFFF", bd=2,
                                compound=TK.TOP,
                                image=self.exit_img)
        btn_exit.pack(side=TK.RIGHT)
        # END exit button

        # refresh button
        self.refresh_img = TK.PhotoImage(file="img/refresh1.png")
        btn_refresh = TK.Button(toolbar, text="Обновить БД",
                                command=lambda: REFRESH(self.tree),
                                bg="#FFFFFF", bd=2,
                                compound=TK.TOP,
                                image=self.refresh_img)
        btn_refresh.pack(side=TK.RIGHT)
        # END refresh button        

        # Upload button
        self.upld_img = TK.PhotoImage(file="img/upld.png")
        btn_upld = TK.Button(toolbar, text="Загрузить файл",
                                command=lambda: WarningWindow(action="загрузить"),
                                bg="#FFFFFF", bd=2,
                                compound=TK.TOP,
                                image=self.upld_img)
        btn_upld.pack(side=TK.RIGHT)        
        # END Upload button        

        # Download button
        self.dnwld_img = TK.PhotoImage(file="img/dwnld.png")
        btn_dwnld = TK.Button(toolbar, text="Скачать файл",
                                command=lambda: WarningWindow(action="скачать"),
                                bg="#FFFFFF", bd=2,
                                compound=TK.TOP,
                                image=self.dnwld_img)
        btn_dwnld.pack(side=TK.RIGHT)
        # END Download button         

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

        # displaying all data in the table by calling SEL function 
        SEL(self.tree)

        # display table
        self.tree.pack(side=TK.BOTTOM)

    # END table with records   
# END Main Window

# if script is running as main programm the it's content will execute
# if script is imported the it's content will NOT execute
if __name__ == "__main__":
    root = TK.Tk()
    TK.Tk.iconbitmap(root, default="img/finance.ico")    
    app = Main(root)
    app.pack()
    # name of the window
    root.title("Finance Holder v1.1")
    # size of the window and point where it will appear
    root.geometry("650x450+300+200")
    # turn off possibility of resize by width and height
    root.resizable(False, False)

    root.mainloop()
