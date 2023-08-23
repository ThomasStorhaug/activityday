import pandas

excel_file = pandas.read_excel('Elevrapport_2023.xlsx')

klasser = []


for klasse in excel_file.loc[:,"Klasse"]:
    if klasse not in klasser:
        klasser.append(klasse)
    
with open('klasser.txt', 'w') as file:
    file.write(f'Det er {len(klasser)} unike klasser i denne listen.')
    for klasse in klasser:
        file.write(f'{klasse}, ')
