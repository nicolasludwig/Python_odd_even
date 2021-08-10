from random import randint

def create_list():
    quant_num=randint(0,20) #Define aleatoriamente a quantidade de números que haverá na list
    lista=[] #Declara uma list vazia
    for i in range(0,quant_num):
        lista.append(randint(1,100)) #Incrementa a list com números aleatórios de 0 a 100
    print ("Lista gerada: ",lista)
    return lista

def write_file(file,lista):
    for i in lista:
        file.write("%s "%i)

def count_odd_even(file):
    count_even=0
    count_odd=0
    num=file.read() #Lê o arquivo e passa para 'num'
    print("Arquivo lido: ",num)
    num_imp = num.split() #Faz a lista e grava em 'num_imp'
    int_num_imp=list(map(int,num_imp)) #Converte o texto da list para inteiros
    print("Arquivo p/ list: ",int_num_imp)
    for impar in int_num_imp:
        if impar % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    dados="\nTotal de números: {}\nPares: {}\nÍmpares: {}\n"
    print (dados.format(len(int_num_imp),count_even,count_odd))
    # print ("\nTotal de números: ", len(int_num_imp),"\nPares: ",count_even,"\nÍmpares: ",count_odd,"\n")

lista_num=create_list() #Cria uma lista de números aleatórios
file=open('arq.txt','w') #Abre o arquivo para escrita
write_file(file,lista_num) #Escreve a lista criada no arquivo
file=open('arq.txt','r') #Abre o arquivo para leitura
count_odd_even(file) #Conta o número de pares e ímpares no arquivo
file.close() #Fecha o arquivo