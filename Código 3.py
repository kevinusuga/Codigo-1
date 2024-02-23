valor_hora = 10000
horas_trabajadas = 8
salario_bruto = valor_hora * horas_trabajadas
retencion = salario_bruto * (12.5/100)
salario_neto = salario_bruto - retencion
print("El salario bruto es:", int(salario_bruto), "dolares")
print("La retención es:", int(retencion), "dolares")
print("El salario neto es:", int(salario_neto), "dolares")
