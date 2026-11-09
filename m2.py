from base import *  # Importa todas as funções de movimento e controlo do módulo base

def run():  # Função principal de execução da missão 2
    largada("PESADO")  # Inicializa o giroscópio a 0° e aplica o perfil PESADO
    andar(68)  # Anda 68 cm para a frente com a velocidade padrão do perfil
    girar(-80, velocidade=500)  # Gira para o ângulo absoluto de -80 graus, velocidade=500
    andar(7.5)  # Anda 7.5 cm para a frente com a velocidade padrão
    girar(-5, velocidade=500)  # Gira para o ângulo absoluto de -5 graus, velocidade=500
    andar(-1, velocidade=300)  # Anda 1 cm para trás, velocidade=300
    girar(10, velocidade=400)  # Gira para o ângulo absoluto de 10 graus, velocidade=400
    andar(-75, velocidade=700)  # Anda 75 cm para trás, velocidade=700

if __name__ == "__main__":  # Executa a função run se o ficheiro for chamado diretamente
    run()  # Inicia a missão 2