# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input("Digite a vantagem da IA do Azure que deseja conhecer: ")

# Função responsável por receber uma vantagem e retornar sua respectiva descrição.
def descrever_vantagem(vantagem):
    if vantagem == "análise preditiva":
        return "capacidade de prever tendências e comportamentos futuros"
        
    # COMPLETE AQUI: Preencha corretamente cada vantagem, considerando as descrições abaixo:                
    elif vantagem == "processamento de linguagem natural":
        return "habilidade de entender e gerar linguagem humana"
        
    elif vantagem == "automação":
        return "automatização de tarefas repetitivas e processos"

    elif  vantagem == "personalização":
        return "oferecer experiências personalizadas aos usuários"

# Imprime a descrição da vantagem recebida na "entrada" através da função "descrever_vantagem". 
print(descrever_vantagem(entrada))