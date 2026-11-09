from base import *  # Importa todas as funções de movimento e controlo do módulo base
from pybricks.tools import wait  # Importa a função de espera do Pybricks

def run():  # Função principal de execução da missão 6
    largada("PESADO")  # Inicializa o giroscópio a 0° e aplica o perfil PESADO
    andar(-63, velocidade=1000, aceleracao=600)  # Anda 63 cm para trás, velocidade=1000, aceleração=600
    girar(-90, velocidade=500)  # Gira para o ângulo absoluto de -90 graus, velocidade=500
    andar(-43, velocidade=1000)  # Anda 43 cm para trás, velocidade=1000
    girar_relativo(90, velocidade=500)  # Gira 90 graus para a direita (relativo), velocidade=500
    andar(-24.5, velocidade=900, aceleracao=600)  # Anda 24.5 cm para trás, velocidade=900, aceleração=600
    mover_garra_a(4000, velocidade=1000, aceleracao=1000, esperar=True)  # Mover garra A 4000 graus, velocidade=1000, aceleração=1000, aguardando conclusão
    
    # Ciclo repetitivo otimizado para soltar a peça soltando o mecanismo
    for _ in range(3):  # Repete 3 vezes a sequência de abanar
        andar(5, velocidade=700, aceleracao=1000)  # Anda 5 cm para a frente, velocidade=700, aceleração=1000
        andar(-10, velocidade=1000, aceleracao=1000)  # Anda 10 cm para trás, velocidade=1000, aceleração=1000

if __name__ == "__main__":  # Executa a função run se o ficheiro for chamado diretamente
    run()  # Inicia a missão 6