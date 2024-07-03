import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from openpyxl import Workbook

wb=Workbook()
ws=wb.active
wdw = tk.Tk()
wdw.configure(bg="grey")
wdw.geometry("900x600")
wdw.resizable(True,True)
wdw.title("FORM PENDAFTARAN SISWA BERMASALAH")

#FUNGSI
def simpan():
    ws.append([name.get(),gender.get(),phone.get()])
    pesan=f"data telah tersimpan"
    wb.save("sample.xlsx")
    showinfo(title="INFO", message=pesan)

#VARIABEL
name=tk.StringVar()
gender=tk.StringVar()
phone=tk.StringVar()

input_frame=ttk.Frame(wdw)
input_frame.pack(padx=5,pady=5,fill="x",expand=True)

name_label= ttk.Label(input_frame,text="name")
name_label.pack(padx=5,pady=5,fill="x",expand=True)
#input
name_entry=ttk.Entry(input_frame, textvariable=name)
name_entry.pack(padx=5,pady=5,fill="x",expand=True)

gender_label= ttk.Label(input_frame,text="gender")
gender_label.pack(padx=5,pady=5,fill="x",expand=True)
#input
gender_entry=ttk.Entry(input_frame, textvariable=gender)
gender_entry.pack(padx=5,pady=5,fill="x",expand=True)

phone_label= ttk.Label(input_frame,text="phone")
phone_label.pack(padx=5,pady=5,fill="x",expand=True)
#input
phone_entry=ttk.Entry(input_frame, textvariable=phone)
phone_entry.pack(padx=5,pady=5,fill="x",expand=True)

#tombol
tombol_fungsi=ttk.Button(input_frame, text="simpan", command=simpan)
tombol_fungsi.pack(padx=200,pady=20,fill="x",expand=True)

wdw.mainloop()

