import tkinter as tk
from functools import partial

class aplikasi(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Kalkulator")
        self.Tombol()
        self.nilai = False
    def Tombol(self):
        self.layar = tk.Entry(self,width=39)
        self.layar.grid(row=0,column=0,columnspan=20)

        list_tombol = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0', '+', '-',
            'C', '*', '/',
            '=',
        ]
        baris = 1
        kolom = 0

        for tampung in list_tombol:
            fungsi = partial(self.hitung, tampung)
            if tampung == '=':
                tk.Button(self, text='=', width=22, command=fungsi).grid(row=baris, column=kolom, columnspan=5)
            else:
                tk.Button(self, text=tampung,width=10,command=fungsi).grid(row=baris, column=kolom)
            kolom += 1
            if kolom > 2:
                kolom = 0
                baris +=1

    def hitung(self,key):
        if key == '=':
            self.nilai = True
            try:
                result = eval(self.layar.get())
                self.layar.delete(0, tk.END)
                self.layar.insert(tk.END, str(result))
            except:
                self.layar.insert(tk.END, "->Error!")
        elif key == 'C':
            self.layar.delete(0,tk.END)
        else:
            if self.nilai:
                self.layar.delete(0, tk.END)
                self.nilai=False
            self.layar.insert(tk.END, key)

main = aplikasi()
main.mainloop()
