salario_string = input("Digite o valor do salário: ");
salario = float(salario_string);

beneficios_string = input("Digite o valor dos benefícios: ");
beneficios = float(beneficios_string);

def calcularImposto(salario):
    aliquota = 0;
    if salario > 0 and salario <= 1100.00:
        aliquota = 0.05;
    elif salario >= 1100 and salario < 2500:
        aliquota = 0.1;
    else:
        aliquota = 0.15;    
    return aliquota * salario; 

imposto = calcularImposto(salario);
salarioLiquido = (salario - imposto) + beneficios;

#dois possíveis jeitos de formatar a saída
#print("O valor do salário líquido é de ${}".format(salarioLiquido));
print(f'O valor do salário líquido é de $ {salarioLiquido:.2f}');