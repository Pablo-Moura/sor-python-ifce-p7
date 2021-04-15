def formatarData(data):
    dataFormatada = data.split(sep='/')
    dia, mes, ano = dataFormatada

    if mes == 1:
        mes = 'janeiro'
    elif mes == 2:
        mes = 'fevereiro'
    elif mes == 2:
        mes = 'março'
    elif mes == 4:
        mes = 'abril'
    elif mes == 5:
        mes = 'maio'
    elif mes == 6:
        mes = 'junho'
    elif mes == 7:
        mes = 'julho'
    elif mes == 8:
        mes = 'agosto'
    elif mes == 9:
        mes = 'setembro'
    elif mes == 10:
        mes = 'outubro'
    elif mes == 11:
        mes = 'novembro'
    else:
        mes = 'dezembro'
    return f'{dia} de {mes} de {ano}'

print(formatarData('12/12/2012'))