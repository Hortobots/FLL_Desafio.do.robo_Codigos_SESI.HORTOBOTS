from base import *  # Importa todas as funções de movimento e controlo do módulo base

def run():  # Função principal de execução da missão 7
    largada("PESADO")  # Inicializa o giroscópio a 0° e aplica o perfil PESADO
    andar(-42.7, velocidade=700, aceleracao=400) #andar 45 cm pra frente, velocidade=700, aceleração=700
    girar_relativo(9, velocidade=500)  # Gira 5 graus para a direita (relativo), velocidade=1000
    mover_garra_a(-1500, velocidade=1000)  # Mover garra A -1500 graus, velocidade=1000
    girar_relativo(-9, velocidade=500)  # Gira 5 graus para a esquerda (relativo), velocidade=1000
    andar(-25, velocidade=700, aceleracao=500)  # Anda 30 cm para trás, velocidade=700, aceleração=500
    girar_relativo(80, velocidade=80)  # Gira 75 graus para a direita (relativo), velocidade=1000
    andar(-35, velocidade=700, aceleracao=500)  # Anda 35 cm para trás, velocidade=700, aceleração=500
    girar_relativo(24, velocidade=500)  # Gira 35 graus para a direita (relativo), velocidade=500
    andar(-23, velocidade=90, aceleracao=50)  # Anda 24 cm para trás, velocidade=300, aceleração=100
    andar(15, velocidade=300, aceleracao=400)  # Anda 15 cm para frente, velocidade=400, aceleração=300
    girar_relativo(50, velocidade=300)
    andar(-43, velocidade=700, aceleracao=500)
    girar_relativo(133, velocidade=200)
    andar(24, velocidade=800)
    mover_garra_b(3000, velocidade=1000, aceleracao=1000)
    mover_garra_b(9000, velocidade=1000, aceleracao=1000, esperar=False)
    andar(-7, velocidade=20)
    girar_relativo(35, velocidade=1000)
    wait(3)
    girar_relativo(-35, velocidade=1000)
    andar(-19, velocidade=100) #missão compartilhada
    girar_relativo(-60, velocidade=400)
    andar(19, velocidade=90)
    andar(-10, velocidade=20)

if __name__ == "__main__":  # Executa a função run se o ficheiro for chamado diretamente
    run()  # Inicia a missão 7