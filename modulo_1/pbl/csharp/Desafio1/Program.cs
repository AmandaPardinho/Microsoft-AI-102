namespace Desafio1
{
    public class Desafio1
    {
        public static void Main()
        {
            Console.WriteLine("Digite o valor do salário bruto: ");
            float salario = float.Parse(Console.ReadLine());

            Console.WriteLine("Digite o valor do benefício: ");
            float beneficio = float.Parse(Console.ReadLine());

            float imposto;
            if (salario > 0 && salario <= 1100.00)
            {
                imposto = 0.05f * salario;
            }
            else if (salario > 1100.00 && salario <= 2500.00)
            {
                imposto = 0.1f * salario;
            }
            else
            {
                imposto = 0.15f * salario;
            }

            float salarioTotal = salario - imposto + beneficio;
            Console.WriteLine("O salário total é: " + salarioTotal.ToString("0.00"));
        }
    }
}