# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input("Digite o conceito de IA que deseja descrever: ")

# Função responsável por receber um conceito e retornar sua respectiva descrição.
def descrever_conceito(conceito):
    if conceito == "aprendizado supervisionado":
        return "treinamento de modelos com dados rotulados"
        
    # COMPLETE AQUI: Preencha corretamente cada conceito, considerando as descrições abaixo:        
    elif conceito == "aprendizado não supervisionado":
        return "descoberta de padrões em dados não rotulados"
        
    elif conceito == "aprendizado por reforço":
        return "aprendizado baseado em recompensas e punições"
        
    elif conceito == "redes neurais":
        return "sistemas inspirados no cérebro humano para processamento de dados"
        
    elif  conceito == "processamento de linguagem natural":
        return "análise e geração de linguagem humana"

# Imprime a descrição do conceito recebido na "entrada" através da função "descrever_conceito".
print(descrever_conceito(entrada))