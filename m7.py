from base import *

def run():
    largada("PESADO")
    
    # Recuo inicial em direção ao objetivo com perfil pesado
    andar(-42.7, velocidade=700, aceleracao=400)
    
    # Pequeno alinhamento angular para acionamento da garra A
    girar_relativo(9, velocidade=500)
    mover_garra_a(-1500, velocidade=1000)
    girar_relativo(-9, velocidade=500)
    
    # Recuo e reorientação da trajetória
    andar(-25, velocidade=700, aceleracao=500)
    # Giro de 80° em velocidade baixa (80 deg/s) intencional para evitar derrapagem por inércia da garra carregada (alterar para 800 se foi digitação rápida)
    girar_relativo(80, velocidade=80)
    andar(-35, velocidade=700, aceleracao=500)
    
    # Ajuste angular e aproximação lenta de precisão
    girar_relativo(24, velocidade=500)
    andar(-23, velocidade=90, aceleracao=50)
    andar(15, velocidade=300, aceleracao=400)
    
    # Reposicionamento intermediário
    girar_relativo(50, velocidade=300)
    andar(-43, velocidade=700, aceleracao=500)
    girar_relativo(133, velocidade=200)
    andar(24, velocidade=800)
    
    # Ativação do mecanismo da garra B
    mover_garra_b(3000, velocidade=1000, aceleracao=1000)
    mover_garra_b(9000, velocidade=1000, aceleracao=1000, esperar=False)
    andar(-7, velocidade=20)
    
    # Movimento de alavanca com pausa
    girar_relativo(35, velocidade=1000)
    wait(3)
    girar_relativo(-35, velocidade=1000)
    
    # Missão compartilhada e retorno à base
    andar(-19, velocidade=100)
    girar_relativo(-60, velocidade=400)
    andar(19, velocidade=90)
    andar(-10, velocidade=20)

if __name__ == "__main__":
    run()
