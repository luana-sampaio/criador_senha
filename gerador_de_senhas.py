import random
import string

def gerar_senha(tamanho:6, incluir_numeros:True, incluir_minusculas:True, incluir_maiusculas:True, incluir_caracteres_especiais: True):
        caracteres = ""
        if incluir_minusculas:
            caracteres += string.ascii_lowercase #inclui letras minúsculas
            
        if incluir_maiusculas:
            caracteres += string.ascii_uppercase #inclui letras maiúsculas

        if incluir_caracteres_especiais:
            caracteres += string.punctuation #inclui caracteres especiais

        if incluir_numeros: 
            caracteres += string.digits

        if not caracteres:
            return "Erro: Você precisa escolher ao menos uma opção de caractere!"


        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        return senha

def obter_tamanho():
    while True:
        try:
            tamanho = int(input("Digite a quantidade de caracteres desejada:"))
            if tamanho < 1:
                print ("Erro: O tamanho da senha deve ser um número inteiro positivo.")
            else:
                return tamanho
        
        except ValueError:
            print ("Erro: Insira um número válido para a quantidade de caracteres!")

def tipos_caracteres(pergunta):
    while True:
        resposta = input(pergunta).lower()
        if resposta == "s":
            return True
        elif resposta == "n":
            return False
        else:
            print("Erro: Resposta inválida! Por favor, digite s para Sim e n para Não.")

def dados_usuario():
    tamanho = obter_tamanho()
    incluir_minusculas = tipos_caracteres("Incluir letras minúsculas? (S/N): ") 
    incluir_maiusculas = tipos_caracteres("Incluir letras maiúsculas? (S/N): ") 
    incluir_numeros = tipos_caracteres("Incluir números? (S/N): ") 
    incluir_caracteres_especiais = tipos_caracteres("Incluir caracteres especiais? (S/N): ") 

    return tamanho, incluir_minusculas, incluir_maiusculas, incluir_numeros, incluir_caracteres_especiais

def main():
    tamanho, incluir_minusculas, incluir_maiusculas, incluir_caracteres_especiais, incluir_numeros = dados_usuario()
    senha = gerar_senha (tamanho, incluir_minusculas, incluir_maiusculas, incluir_numeros, incluir_caracteres_especiais)

    print(f"Sua senha gerada é: {senha}")

if __name__ == "__main__":
    main()