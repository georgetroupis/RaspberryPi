import pandas as pd
import tkinter as tk
from tkinter import filedialog

def chooseFile():

    root = tk.Tk()

    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue')
    canvas1.pack()

    def getExcel():
        global df

        import_file_path = filedialog.askopenfilename()
        df = pd.read_excel(import_file_path)
        


    browseButton_Excel = tk.Button(text= 'Import Excel File', command = getExcel, bg = 'green', fg = 'white', font =('helvetica', 12, 'bold' ))
    quitButton = tk.Button(text = 'Click Here to Quit', command = root.destroy)
    canvas1.create_window(150, 150, window= browseButton_Excel)
    canvas1.create_window(150, 200, window= quitButton)

    root.mainloop()
    return

chooseFile()

print(df.iloc[0])

"""
for grade in df['Grade']:
    a = df.loc(df.'A' == grade, 'GPA')
    print(a)
"""

    

