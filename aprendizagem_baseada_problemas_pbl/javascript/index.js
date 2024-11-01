const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let salario = 0;
let beneficio = 0;
let imposto = 0;

rl.question('Informe o valor do salário: ', (inputSalario) => {
    salario = parseFloat(inputSalario);

    if(salario > 0 && salario <= 1100){
        imposto = 0.05 * salario;
    } else if(salario > 1100 && salario <= 2500){
        imposto = 0.1 * salario;
    }else{
        imposto = 0.15 * salario;
    }

    rl.question('Informe o valor do benefício: ', (inputBeneficio) => {
        beneficio = parseFloat(inputBeneficio);

        let salarioTotal = parseFloat((salario - imposto) + beneficio).toFixed(2);
        console.log(`O salário total é: ${salarioTotal}`);

        rl.close();
    });
});