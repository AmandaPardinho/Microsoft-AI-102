/*

O CÓDIGO ABAIXO SÓ PODE SER EXECUTADO NA PLATAFORMA DO DESAFIO
PARA EXECUTAR O CÓDIGO NO AMBIENTE LOCAL, É NECESSÁRIO DEFINIR OS MÉTODOS GETS() E PRINT() PARA LER AS ENTRADAS E EXIBIR AS SAÍDAS, RESPECTIVAMENTE ==> VIDE CÓDIGO DO ARQUIVO INDEX.JS

*/

//gets(): lê dados de entrada do usuário
//a função gets não é nativa do javascript, ela é disponibilizada pela plataformado desafio para ler as entradas(inputs) dos usuários
const salario = parseFloat(gets());
const beneficio = parseFloat(gets());

//calcula o imposto usando a função "calcularImposto"
const imposto = calcularImposto(salario);

//calcula e imprime a saída com 2 casas decimais
const saida = salario - imposto + beneficio;

//imprime o valor a ser recebido
//a função print não é nativa do javascript, ela é disponibilizada pela plataforma do desafio para exibir as saídas(outputs) para o usuário
print(`O valor a ser recebido é de ${saida.toFixed(2)}`);

//função que calcula o imposto
function calcularImposto(salario){
    let aliquota;
    if(salario > 0 && salario <= 1100){
        aliquota = 0.05;
    } else if(salario > 1100 && salario <= 2500){
        aliquota = 0.1;
    }else{
        aliquota = 0.15;  
    }
    return salario * aliquota;
}; 