from base import *  # Importa todas as funções de movimento e controlo do módulo base

def run():  # Função principal de execução da missão 3
    largada("PESADO")  # Inicializa o giroscópio a 0° e aplica o perfil PESADO
    andar(1000, velocidade=1000)  # Anda 1000 cm (10 metros) para a frente, velocidade=1000

if __name__ == "__main__":  # Executa a função run se o ficheiro for chamado diretamente
    run()  # Inicia a missão 3