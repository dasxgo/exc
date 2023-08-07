class Empleado:
    def __init__(self, id_empleado, nombre_empleado,
                salario_empleado, departamento_empleado):
        self.id_empleado = id_empleado
        self.nombre_empleado = nombre_empleado
        self.salario_empleado = salario_empleado
        self.departamento_empleado = departamento_empleado
    
    def calcular_salario_empleado(self, horas_trabajadas):
        if horas_trabajadas > 40:
            horas_extra = horas_trabajadas - 40
            monto_horas_extra = horas_extra * (self.salario_empleado / 40)
            self.salario += monto_horas_extra
        return self.salario_empleado
    
    def asignar_departamento(self, departamento):
        self.departamento_empleado = departamento

    def imprimir_detalles_empleado(self):
        print(f'ID Empleado: {self.id_empleado}')
        print(f'Nombre Emprelado: {self.nombre_empleado}')
        print(f'Salario Empleado: {self.salario_empleado}')
        print(f'ID Departamento Empleado: {self.departamento_empleado}')

emp1 = Empleado('E7875', 'ADAMS', 50000, 'CONTABILIDAD')
emp1.imprimir_detalles_empleado()
emp1.asignar_departamento('VENTAS')

print('='*62)

emp1.imprimir_detalles_empleado()






        