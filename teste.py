def count_odd(file):
    count_even=0
    count_odd=0
    num=file.read() #Lê o arquivo e passa para 'num'
    num_imp = num.split() #Faz a lista e grava em 'num_imp'
    int_num_imp=list(map(int,num_imp)) #Converte o texto da list para inteiros
    print(int_num_imp)
    for impar in int_num_imp:
        if impar % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print ("ppPrimeira linha do arquivo: ")
    print ("Pares: ",count_even,"\nÍmpares: ",count_odd,"\n")

file=open('odd.txt','r')
count_odd(file)
file.close()
print ('testando git')