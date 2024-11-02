package org.example

import kotlin.test.Test
import kotlin.test.assertEquals
import java.io.ByteArrayInputStream

class AppTest {
    @Test 
    fun testCalculaSalario() {
        val app = App()
        
        // Simulando a entrada do usuário
        val salario = 2000.0
        val beneficio = 500.0
        val aliquota = 0.1
        val imposto = salario * aliquota
        val salarioEsperado = (salario - imposto) + beneficio

        // Função auxiliar para simular a entrada do usuário
        fun simulateInput(vararg inputs: String, block: () -> Double): Double {
            val input = inputs.joinToString("\n").byteInputStream()
            System.setIn(input)
            return block()
        }

        val resultado = simulateInput(salario.toString(), beneficio.toString()) {
            app.calculaSalario()
        }

        assertEquals(salarioEsperado, resultado, "O cálculo do salário líquido está incorreto")
    }
}