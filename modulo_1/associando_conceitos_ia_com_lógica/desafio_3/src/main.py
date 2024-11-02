# Recebe a Entrada do usuário e armazena na variável "entrada"
entrada = input("Qual serviço de IA você deseja saber mais? ").title()

# Função responsável por receber um serviço e retornar sua respectiva descrição.
def descrever_servico(servico):
    servico = servico.title()
    if servico == "Azure Cognitive Services":
        return "serviços pré-construídos para visão, fala, linguagem e tomada de decisão"
        
    # COMPLETE AQUI: Preencha corretamente cada serviço, considerando as descrições abaixo:                        
    elif servico == "Azure Machine Learning":
        return "plataforma para construir, treinar e implantar modelos de machine learning"
        
    elif servico == "Azure Bot Services":
        return "criação e gerenciamento de bots inteligentes"
        
    elif servico == "Azure OpenAI Service":
        return "integração de modelos avançados de linguagem da OpenAI"
        
    elif  servico == "Azure AI Vision":
        return "análise e interpretação de imagens e vídeos"
        
# Imprime a descrição do serviço recebido na "entrada" através da função "descrever_servico". 
print(descrever_servico(entrada))