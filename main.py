from tkinter import *
from tkinter import messagebox
from pandastable import Table, TableModel
import pandas as pd
from module1 import AutocompleteEntry

class TestApp(Frame):    

    def update_output(self, *args):
        for index, row in self.results.iterrows():
            if self.macro_categoria_var.get() == '':
                self.results.sort_index()
                self.pt.redraw()
                return
            elif self.macro_categoria_var.get().lower() in row['MACRO CATEGORIA'].lower():
                self.results.at[index,'rank'] = self.results.at[index,'rank'] + 1
            if self.accumulazione_var.get() != '':
                if self.accumulazione_var.get().lower() in row['ACCUMULAZIONE/DISTRIBUZIONE'].lower():
                    self.results.at[index,'rank'] = self.results.at[index,'rank'] + 1
            if self.efficienza_var.get() != '':
                if self.efficienza_var.get().lower() in row['EFFICIENTE'].lower():
                    self.results.at[index,'rank'] = self.results.at[index,'rank'] + 1
            if self.divisa_var.get() != '':
                if self.divisa_var.get().lower() in row['DIVISA'].lower():
                    self.results.at[index,'rank'] = self.results.at[index,'rank'] + 1
            if self.classe_var.get() != '':
                if self.classe_var.get().lower() in row['CLASSE'].lower():
                    self.results.at[index,'rank'] = self.results.at[index,'rank'] + 1
            if self.sgr_var.get() != '':
                if self.sgr_var.get().lower() in row['SGR/SICAV'].lower():
                    self.results.at[index,'rank'] = self.results.at[index,'rank'] + 1

        self.results.sort_values('rank', inplace =True, ascending=False)
        self.pt.redraw()
        self.results['rank'] = 0
                

    """Basic test frame for the table"""
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('800x600+200+100')
        self.main.title('Table app')

        self.macro_categoria_var = StringVar()
        self.accumulazione_var = StringVar()
        self.efficienza_var = StringVar()
        self.divisa_var = StringVar()
        self.classe_var = StringVar()
        self.sgr_var = StringVar()

        self.s = Frame(self.main)
        self.s.pack(fill = X, expand = 1, side = TOP)
        self.macro_categoria = Label(self.s, text = 'Macro CAT.:', justify = LEFT).pack(fill = X, expand = 1, side = LEFT)
        self.accumulazione = Label(self.s, text = 'Accumulazione/Distribuzione:', justify = LEFT).pack(fill = X, expand = 1, side = LEFT)
        self.efficienza = Label(self.s, text = 'Efficienza:', justify = LEFT).pack(fill = X, expand = 1, side = LEFT)
        self.divisa = Label(self.s, text = 'Divisa:', justify = LEFT).pack(fill = X, expand = 1, side = LEFT)
        self.classe = Label(self.s, text = 'Classe:', justify = LEFT).pack(fill = X, expand = 1, side = LEFT)
        self.sgr = Label(self.s, text = 'SGR:', justify = LEFT).pack(fill = X, expand = 1, side = LEFT)

        self.d = Frame(self.main)
        self.d.pack(fill = X, expand = 1, side = TOP)
        self.input_macro_categoria = AutocompleteEntry(self.d, width = 20, textvariable = self.macro_categoria_var).pack(fill = X, expand = 1, side = LEFT)
        self.input_accumulazione = Entry(self.d, width = 20, textvariable = self.accumulazione_var).pack(fill = X, expand = 1, side = LEFT)
        self.input_efficienza = Entry(self.d, width = 20, textvariable = self.efficienza_var).pack(fill = X, expand = 1, side = LEFT)
        self.input_divisa = Entry(self.d, width = 20, textvariable = self.divisa_var).pack(fill = X, expand = 1, side = LEFT)
        self.input_classe = Entry(self.d, width = 20, textvariable = self.classe_var).pack(fill = X, expand = 1, side = LEFT)
        self.input_sgr = Entry(self.d, width = 20, textvariable = self.sgr_var).pack(fill = X, expand = 1, side = LEFT)

        self.f = Frame(self.main)
        self.f.pack(fill = BOTH, expand = 1, side = TOP)
        #df = TableModel.getSampleData()
        xls = pd.ExcelFile('file.xlsx')
        fondi = pd.read_excel(xls, 'Fondi')
        fondi.columns = fondi.iloc[0]
        self.fondi = fondi[1:]
        self.fondi = self.fondi.fillna('')
        self.fondi['rank'] = 0
        self.results = self.fondi
        self.table = self.pt = Table(self.f, dataframe=self.fondi, showtoolbar=True, showstatusbar=True)
        self.pt.show()
        return


app = TestApp()
app.macro_categoria_var.trace("w", app.update_output)
app.accumulazione_var.trace("w", app.update_output)
app.efficienza_var.trace("w", app.update_output)
app.divisa_var.trace("w", app.update_output)
app.classe_var.trace("w", app.update_output)
app.sgr_var.trace("w", app.update_output)
#launch the app
app.mainloop()
