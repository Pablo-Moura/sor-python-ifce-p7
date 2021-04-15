"""

3.Escrever uma função chamada sed que recebe 4 argumentos: uma string padrão, uma string de
substituição e dois arquivos. O primeiro arquivo deve ser lido e caso a string padrão seja
encontrada, deve ser substituída pela string de substituição e o conteúdo escrito no segundo
arquivo.

1 - stringPadrao
2 - stringSubs
3 - arquivo1;
    arquivo2
4 - ler arquivo1;
    arquivo1 encontrar stringPadrao;
    stringPadrao virar stringSubs e o arquivo2

"""

def sed(padrao, substituicao, arquivo1, arquivo2):
    arquivo = open(arquivo1)
    linhas = arquivo.readlines()

    for indice, linha in enumerate(linhas):
        palavras = linha.split()
        for palavra in palavras:
            if palavra == padrao:
                linhas[indice] = linhas[indice].replace(padrao, substituicao)
                arquivoNovo = open(arquivo2, 'w')
                novo = ''.join(linhas)
                arquivoNovo.write(novo)


sed('BANANA', 'MELANCIA', 'arquivoUm.txt', 'arquivoDois.txt')