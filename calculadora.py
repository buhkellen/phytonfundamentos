# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print('\nQual operação matemática você quer utilizar?\n')
print ('1 - Soma')
print ('2 - Subtração')
print ('3 - Multiplicação')
print ('4 - Divisão')

operacao = input('\nDigite sua opção (1/2/3/4): ')
num1 = int(input ('\nQual o primeiro número? '))
num2 = int(input ('\nQual o segundo número? '))

if operacao == '1':
    soma = num1 + num2
    print ('\n')
    print (num1, '+', num2, '=', soma)
    print ('\n')
elif operacao == '2':
    subtracao = num1 - num2
    print ('\n')
    print (num1, '-', num2, '=', subtracao)
    print ('\n')
    print (subtracao)
elif operacao == '3':
    multiplicacao = num1 * num2
    print ('\n')
    print (num1, 'x', num2, '=', multiplicacao)
    print ('\n')
else:
    divisao = num1/num2
    print ('\n')
    print (num1, '/', num2, '=', divisao)
    print ('\n')
