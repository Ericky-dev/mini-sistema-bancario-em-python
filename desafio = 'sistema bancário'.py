desafio = 'sistema bancário \n'

print(desafio.title())


print('Escolha a Opção Desejada!!! ')


menu = """

print('1 = Depósito')
print('2 =  Saque')
print('3 = Exrato')
print('4 = saldo')
print('5 = sair')
print("")
=>"""
print(" ")



saque = " "
extrato = ""
deposito =""
Limite_Saque = 3
limite = 500
saldo = 0
numero_saques = 0



while True: 
        opcao = input(menu)
        if opcao =='1':

            # Tratando se o valor para depósito é maior que zero
                while True:
                    valor = float(input("Informe o valor para Depósito: "))
                    if float(valor) > 0:
                            
                        saldo += float(valor)
                        extrato += (f"Depóstio no valor de R${valor:.2f} \n")
                        
                        break  

                    else:
                            print(f'Informe apenas valores maior que 0')
                            print("\n")

                          

        elif opcao =='2': 
            

            valor = float(input("Informe o valor para Saque "))

            if float(valor) > saldo:
                print(f'Você não possui saldo suficiente para realizar o saque \n')
                print('Limite Máximo permitido para Saque R$ 500')

            elif float(valor) > limite:
                print(f'Falha na operação!!! ')
                print(f'Limite Máximo para Saque R$ 500')
                

            elif numero_saques == Limite_Saque:
            
             print(f'Você excedeu  o número máximo para saques')
            

            elif float(valor) > 0:
                saldo-=float(valor)
                extrato += (f"Saque no valor de R${valor:.2f} \n")
                numero_saques += 1
                print(f'Saques realizados na conta bancária: ', numero_saques)

            elif numero_saques == Limite_Saque:
              print(f'Limite de Saque Diário Excedido!!!!')
        

        elif opcao =='3':
        
         print("************   Extrato  **************** \n")
         print("Não Houve Movimentação na Conta Bancária" if not extrato else extrato)
         print(f'Saldo Disponível R${saldo:.2f}')
         print("********************************** \n")

      
        elif opcao =='4':
   
         print(f"Saldo Disponível = R$ {saldo:.2f} \n")
            
        elif opcao == '5':
         print("Obrigado po Usar nosso Sistema, até mais!!!!")
         break
    
        else:
         print(f'Opção inválida por favor escolha a opção desejada!!!!')
         