import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
import sys
import nomina

#Login
ventana = tk.Tk()
ventana.geometry("200x250")
ventana.title("Login")

#Nomina
ventanaNomina = tk.Tk()

def cargar_elementos():
    ventanaNomina.withdraw()
    lblUser.grid(row=0, column=1, pady=10, padx=10)
    txtUser.grid(row=1, column=1, padx=10)
    lblPss.grid(row=2, column=1, pady=10, padx=10)
    txtPss.grid(row=3, column=1, padx=10)
    btnEntrar.grid(row=4, column=1, pady=10, padx=10)

def autenticar():
    if (txtUser.get() != 'admin') and (txtPss.get() != 'useradmin'):
        messagebox.showerror('ERROR AL INGRESAR', "Usuario y Contraseña incorrectos")
    elif txtUser.get() != 'admin':
        messagebox.showerror('ERROR AL INGRESAR', "Usuario incorrecto")
    elif txtPss.get() != 'useradmin':
        messagebox.showerror('ERROR AL INGRESAR', "Contraseña incorrecta")
    elif (txtUser.get() == 'admin') and (txtPss.get() == 'useradmin'):
        ventana.quit()
        ventana.destroy()
        ventanaNomina.geometry("650x500")
        ventanaNomina.title("Registro de nomina")
        ventanaNomina.deiconify()
        cargar_mye()

def salir():
    ventanaNomina.quit()
    ventanaNomina.destroy()
    sys.exit()

def mostrarIntegrantes():
    messagebox.showinfo('Integrantes', "Santiago Castaño Moreno \n Jhon Alexander Munera")

def limpiar_campos():
    txtNombre.delete(0, tk.END)
    txtApellido.delete(0, tk.END)
    txtDiasLaborados.delete(0, tk.END)
    txtSalario.delete(0, tk.END)
    txtAumento.delete(0, tk.END)

def cargar_mye():
    # Configurar el menu prinicpal de  la aplicacion = menú
    menu_principal = Menu(ventanaNomina)

    # tearoff = False. Para evitar que no se separe el menu de la interfaz (estatico)
    submenu_archivo = Menu(menu_principal, tearoff=0)

    # agregar una nueva opcion al menu de archivo
    submenu_archivo.add_command(label='Nuevo', command=limpiar_campos)

    # Agregar el submenu principal
    menu_principal.add_cascade(menu=submenu_archivo, label="Archivo")
    submenu_archivo.add_command(label='Salir', command=salir)

    # Crear submenu ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    submenu_ayuda.add_command(label='Integrantes', command=mostrarIntegrantes)
    menu_principal.add_cascade(menu=submenu_ayuda, label='Acerca de proyecto')

    #Mostramos el menu en la ventana principal
    ventanaNomina.config(menu=menu_principal)

    #ELEMENTOS PARA INGRESO DE NOMINA
    lblNombre.grid(row=0, column=1, padx=15)
    txtNombre.grid(row=0, column=2, padx=20, pady=8)

    lblApellido.grid(row=1, column=1, padx=15)
    txtApellido.grid(row=1, column=2, padx=20, pady=8)

    lblDiasLaborados.grid(row=2, column=1, padx=15)
    txtDiasLaborados.grid(row=2, column=2, padx=20, pady=8)

    lblSalario.grid(row=3, column=1, padx=15)
    txtSalario.grid(row=3, column=2, padx=20, pady=8)

    lblAumento.grid(row=4, column=1, padx=15)
    txtAumento.grid(row=4, column=2, padx=20, pady=8)

    lblPrestCaus.grid(row=5, column=1)
    btnCalcular.grid(row=6, column=1, pady=8)

    btnExportar.grid(row=6, column=2)

    ventanaNomina.mainloop()

def calculos_nomina():
    nom = nomina.trabajador(txtNombre.get(), txtApellido.get(), int(txtDiasLaborados.get()), float(txtSalario.get()), float(txtAumento.get()))

    lblEmpleado = ttk.Label(ventanaNomina, text=f'EMPLEADO: {txtNombre.get()} {txtApellido.get()}')
    lblPrima = ttk.Label(ventanaNomina, text=f'PRIMA: {round(nom.calculo_primas())}')
    lblCesantias = ttk.Label(ventanaNomina, text=f'CESANTIAS: {round(nom.calculo_cesantias())}')
    lblCesantiasIntereses = ttk.Label(ventanaNomina, text=f'INTERESES CESANTIAS: {round(nom.calculo_intereses_cesantias())}')
    lblVacaciones = ttk.Label(ventanaNomina, text=f'VACACIONES A LA FECHA: {round(nom.calculo_vacaciones())}')
    SalarioAT, salarioA  = nom.calculo_aumento()
    lblSalAum = ttk.Label(ventanaNomina, text=f'SALARIO CON AUMENTO: {round(salarioA)}')
    lblSalTra = ttk.Label(ventanaNomina, text=f'SALARIO CON SUBSIDIO TRANSPORTE: {round(SalarioAT)}')
    lblTL = ttk.Label(ventanaNomina, text=f'TOTAL LIQUIDACIÓN {round(nom.calcular_liquidacion())}')

    lblEmpleado.grid(row=7, column=1)
    lblPrima.grid(row=8, column=1)
    lblCesantias.grid(row=9, column=1)
    lblCesantiasIntereses.grid(row=10, column=1)
    lblVacaciones.grid(row=11, column=1)
    lblSalAum.grid(row=12, column=1)
    lblSalTra.grid(row=13, column=1)
    lblTL.grid(row=14, column=1)

def exportar_nomina():
    nom = nomina.trabajador(txtNombre.get(), txtApellido.get(), int(txtDiasLaborados.get()), float(txtSalario.get()), float(txtAumento.get()))
    nom.exportar()

    messagebox.showinfo("Mensaje informativo", "Datos exportados")

#Elementos Login
lblUser = ttk.Label(ventana, text='User')
txtUser = ttk.Entry(ventana, width=30)
lblPss = ttk.Label(ventana, text='Password')
txtPss = ttk.Entry(ventana, width=30, show='*')
btnEntrar = ttk.Button(ventana, text="ENTER", command=autenticar)

#Elementos Nomina
lblNombre = ttk.Label(ventanaNomina, text='Ingrese nombre: ')
lblApellido = ttk.Label(ventanaNomina, text='Ingrese apellido: ')
lblDiasLaborados = ttk.Label(ventanaNomina, text='Ingrese dias laborados: ')
lblSalario = ttk.Label(ventanaNomina, text='Ingrese salario: ')
lblAumento = ttk.Label(ventanaNomina, text='Ingrese aumento en %: ')
lblPrestCaus = ttk.Label(ventanaNomina, text='Prestaciones causadas')

txtNombre = ttk.Entry(ventanaNomina, width=30)
txtApellido = ttk.Entry(ventanaNomina, width=30)
txtDiasLaborados = ttk.Entry(ventanaNomina, width=30)
txtSalario = ttk.Entry(ventanaNomina, width=30)
txtAumento = ttk.Entry(ventanaNomina, width=30)

btnCalcular = ttk.Button(ventanaNomina, text="CALCULAR", command=calculos_nomina)
btnExportar = ttk.Button(ventanaNomina, text="EXPORTAR", command=exportar_nomina)

cargar_elementos()
ventana.mainloop()