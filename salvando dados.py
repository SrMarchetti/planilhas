import openpyxl

workbook = openpyxl.Workbook()
del workbook['Sheet']
workbook.create_sheet('Instrumentos')
#selecionar a planilha
sheet_instrumentos = workbook['Instrumentos']
#Sempre colocar cabeçalhos se não existir
sheet_instrumentos.append(['instrumento','marca','preço'])
workbook.save('instrumentos.xlsx')
#para adicionar dados em uma linha
sheet_instrumentos.append(['violão','shimano',1200])
sheet_instrumentos.append(['guitarra','fender',3500.10])
sheet_instrumentos.append(['baixo','GC',2500.50])
sheet_instrumentos.append(['bateria','metal',4500])
#como mudar o valor de cada celula
sheet_instrumentos['A7'].value = 'teclado'
sheet_instrumentos['B7'].value = 'Marca'
sheet_instrumentos['C7'].value = 2500.30

workbook.save('instrumentos.xlsx')
