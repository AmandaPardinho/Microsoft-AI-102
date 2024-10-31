import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Digite o valor do salário: ");
        float salario = scanner.nextFloat();
        
        System.out.println("Digite o valor do benefício: ");
        float beneficio = scanner.nextFloat();
        
        float imposto = 0f;
        float salarioTotal = (salario - imposto) + beneficio;

        if(salario > 0 && salario <= 1100.00f){
            imposto = 0.05f * salario;
            salarioTotal = (salario - imposto) + beneficio;
            System.out.println("Salário total: " + salarioTotal);
        }else if(salario > 1100.00f && salario <= 2500.00f){
            imposto = 0.10f * salario;
            salarioTotal = (salario - imposto) + beneficio;
            System.out.println("Salário total: " + salarioTotal);
        }else{
            imposto = 0.15f * salario;
            salarioTotal = (salario - imposto) + beneficio;
            System.out.println("Salário a receber: " + String.format("%.2f",salarioTotal));
        }

        scanner.close();
    }
}
