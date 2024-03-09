import openpyxl
from openpyxl.drawing.image import Image
import os

workbook = openpyxl.Workbook()
del workbook['Sheet']
workbook.create_sheet('produtos')
sheet_produtos = workbook['produtos']
sheet_produtos.append(['item', 'imagem', 'preço'])
sheet_produtos['A2'].value = 'Celular'
sheet_produtos['C2'].value = 2500

#adicionando imagem
pasta = os.getcwd()
print (pasta)
img = Image(os.getcwd() + os.sep + 'fone1.png')
#img = Image('fone1.png')
sheet_produtos.add_image(img, 'B2')
workbook.save('produtos.xlsx')