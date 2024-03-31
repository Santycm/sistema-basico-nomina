class trabajador:
    def __init__(self, nombre, apellido, dias, salario, aumento):
        self.nombre = nombre
        self.apellido = apellido
        self.dias = dias
        self.salario = salario
        self.aumento = aumento

    def calculo_primas(self):
        return (self.salario * self.dias)/360

    def calculo_cesantias(self):
        return (self.salario * self.dias) / 360

    def calculo_intereses_cesantias(self):
        return (((self.salario * self.dias) / 360)*self.dias*0.12)/360

    def calculo_vacaciones(self):
        return (self.salario * self.dias)/720
    
    def calculo_aumento(self):
        salario = self.salario + (self.salario*(self.aumento/100))
    
        if salario < 2600000:
            return (salario + 140606), salario
        else:
            return salario, salario
        
    def calcular_liquidacion(self):
        return self.calculo_primas() + self.calculo_cesantias() + self.calculo_intereses_cesantias() + self.calculo_vacaciones()  
        
    def exportar(self):
        try:
            archivo = open("NOMINA/Nominas.txt", "a")
            archivo.write(f'\nNOMBRE: {self.nombre} \n')
            archivo.write(f'APELLIDO: {self.apellido} \n')
            archivo.write(f'PRIMA: {round(self.calculo_primas())} \n')
            archivo.write(f'CESANTIAS: {round(self.calculo_cesantias())} \n')
            archivo.write(f'INTERESES CESANTIAS: {round(self.calculo_intereses_cesantias())} \n')
            archivo.write(f'VACACIONES A LA FECHA: {round(self.calculo_vacaciones())} \n')
            SalarioAT, salarioA  = self.calculo_aumento()
            archivo.write(f'SALARIO CON AUMENTO: {round(salarioA)} \n')
            archivo.write(f'SALARIO CON SUB TRANSPORTE: {round(SalarioAT)} \n')
            archivo.write(f'TOTAL LIQUIDACION: {round(self.calcular_liquidacion())} \n')
            archivo.write("------------------------------------------------------------")
        except Exception as e:
            print(e)