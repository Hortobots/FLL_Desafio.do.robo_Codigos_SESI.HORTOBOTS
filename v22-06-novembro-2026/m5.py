from base import *  # Importa todas as funções de movimento e controlo do módulo base
from pybricks.tools import wait  # Importa a função de espera do Pybricks

def run():  # Função principal de execução da missão 5
    largada("PESADO")  # Inicializa o giroscópio a 0° e aplica o perfil PESADO
    andar(-92.5, velocidade=950, aceleracao=500)  # Anda 92.5 cm para trás, velocidade=950, aceleração=500
    mover_garra_a(3500, velocidade=1000, aceleracao=1000)  # Mover garra A 3500 graus, velocidade=1000, aceleração=1000
    andar(5, velocidade=700, aceleracao=500)  # Anda 5 cm para a frente, velocidade=700, aceleração=500
    mover_garra_a(3000, velocidade=1000, esperar=False)  # Mover garra A 3000 graus, velocidade=1000, sem esperar
    andar(-6.7, velocidade=1000)  # Anda 6.7 cm para trás, velocidade=1000
    mover_garra_a(3000, velocidade=1000)  # Mover garra A 3000 graus, velocidade=1000
    andar(110, velocidade=1000, aceleracao=1000)  # Anda 110 cm para a frente, velocidade=1000, aceleração=1000

if __name__ == "__main__":  # Executa a função run se o ficheiro for chamado diretamente
    run()  # Inicia a missão 5