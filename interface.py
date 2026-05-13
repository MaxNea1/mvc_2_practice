import tkinter as tk

from tkinter import messagebox
from tkinter import *
from tkinter import ttk

from connexion import *

class Form_users:

    global base
    base = None
    global groupBox
    groupBox = None
    global combo
    combo = None
    global tree
    tree = None
    global txtbox_id
    txtbox_id = None
    global txtbox_name
    txtbox_name = None
    global txtbox_lastname
    txtbox_lastname = None
    global txtbox_gender
    txtbox_gender = None
    global txtbox_age
    txtbox_age = None

    

def Form():
    try: 
        global base
        global groupBox
        global combo
        global tree
        global txtbox_id
        global txtbox_name
        global txtbox_lastname
        global txtbox_gender
        global txtbox_age

        base = Tk()
        base.geometry('1450x300')
        base.title('CRUD Python + SQLServer')
        
        groupBox = LabelFrame(base, text='Datos del usuario', padx=5, pady=5)
        groupBox.grid(row=0, column = 0)

        LabelId = Label(groupBox, text='Id:', width=13, font=('arial', 12)).grid(row=0, column=0)
        txtbox_id = Entry(groupBox)
        txtbox_id.grid(row=0, column=1)

        LabelName = Label(groupBox, text='Nombre::', width=13, font=('arial', 12)).grid(row=1, column=0)
        txtbox_name = Entry(groupBox)
        txtbox_name.grid(row=1, column=1)

        LabelLastName = Label(groupBox, text='Apellido:', width=13, font=('arial', 12)).grid(row=2, column=0)
        txtbox_lastname = Entry(groupBox)
        txtbox_lastname.grid(row=2, column=1)

        LabelGender = Label(groupBox, text='Genero:', width=13, font=('arial', 12)).grid(row=3, column=0)
        selectGender = tk.StringVar()
        combo = ttk.Combobox(groupBox, values=['Masculino', 'Femenino'], textvariable=selectGender)
        combo.grid(row=3, column=1)
        selectGender.set('Masculino')

        LabelAge = Label(groupBox, text='Edad::', width=13, font=('arial', 12)).grid(row=4, column=0)
        txtbox_age = Entry(groupBox)
        txtbox_age.grid(row=4, column=1)  

        Button(groupBox, text='Guardar', width=10).grid(row = 5, column = 0)  
        Button(groupBox, text='Modificar', width=10).grid(row = 5, column = 1)
        Button(groupBox, text='Eliminar', width=10).grid(row = 5, column = 2)

        groupBox = LabelFrame(base, text='Lista de usuarios', padx=5, pady=5)
        groupBox.grid(row=0, column=1, padx=10, pady=10)

        tree = ttk.Treeview(groupBox, columns=('Id', 'Nombre', 'Apellido', 'Genero', 'Edad'), show='headings', height=5,)
        tree.column('# 1', anchor=CENTER)
        tree.heading('# 1', text='Id')
        tree.column('# 2', anchor=CENTER)
        tree.heading('# 2', text='Nombre')
        tree.column('# 3', anchor=CENTER)
        tree.heading('# 3', text='Apellido')
        tree.column('# 4', anchor=CENTER)
        tree.heading('# 4', text='Genero')
        tree.column('# 5', anchor=CENTER)
        tree.heading('# 5', text='Edad')

        vsb = Scrollbar(groupBox, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        tree.pack(side=LEFT, fill=BOTH)
        vsb.pack(side=RIGHT, fill=Y)

        base.mainloop()
    except ValueError as e:
        print(f'Error al cargar la interfaz: {e}')

#def selectRegistro():

#def updateTable():



#def guardarRegistro():

#def updateRegistro():

#def deleteRegistro():


Form()