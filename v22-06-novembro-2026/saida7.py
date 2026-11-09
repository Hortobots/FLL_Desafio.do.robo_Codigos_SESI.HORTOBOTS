from base import *  # Importa todas as funções de movimento e controlo do módulo base
from pybricks.tools import wait  # Importa a função de espera do Pybricks

def run():  # Função principal de execução da rotina de saída 7
    largada("PESADO")  # Inicializa o giroscópio a 0° e aplica o perfil PESADO
    curva(raio_cm=-500, angulo=6.55)  # Faz curva em arco com raio -500 cm, ângulo 6.55 graus
    curva(raio_cm=-48, angulo=29.4)  # Faz curva em arco com raio -48 cm, ângulo 29.4 graus
    curva(raio_cm=-5, angulo=15)  # Faz curva fechada em arco com raio -5 cm, ângulo 15 graus
    
    andar(-26, velocidade=1000, aceleracao=1000)  # Anda 26 cm para trás, velocidade=1000, aceleração=1000
    mover_garra_a(-3500, velocidade=1000, aceleracao=1000, esperar=True)  # Mover garra A -3500 graus, velocidade=1000, aceleração=1000
    andar(3, velocidade=1000)  # Anda 3 cm para a frente, velocidade=1000
    
    for _ in range(2):  # Repete 2 vezes a sequência de avanço/recuo linear
        andar(-5, velocidade=1000, aceleracao=1000)  # Anda 5 cm para trás, velocidade=1000, aceleração=1000
        andar(3, velocidade=1000, aceleracao=1000)  # Anda 3 cm para a frente, velocidade=1000, aceleração=1000
        
    for _ in range(2):  # Repete 2 vezes a sequência de rotação rápida de desengate
        girar_relativo(10, velocidade=1000)  # Gira 10 graus para a direita (relativo), velocidade=1000
        girar_relativo(-10, velocidade=1000)  # Gira 10 graus para a esquerda (relativo), velocidade=1000

    mover_garra_a(2300, velocidade=1000, aceleracao=1000, esperar=False)  # Mover garra A 2300 graus, velocidade=1000, aceleração=1000, sem esperar
    andar(3, velocidade=1000)  # Anda 3 cm para a frente, velocidade=1000
    girar_relativo(48, velocidade=1000)  # Gira 48 graus para a direita (relativo), velocidade=1000
    curva(raio_cm=500, angulo=3.50, velocidade=1000)  # Faz curva em arco com raio 500 cm, ângulo 3.50 graus, velocidade=1000
    curva(raio_cm=90, angulo=-45, velocidade=1000)  # Faz curva em arco com raio 90 cm, ângulo -45 graus, velocidade=1000

if __name__ == "__main__":  # Executa a função run se o ficheiro for chamado diretamente
    run()  # Inicia a rotina de saída 7