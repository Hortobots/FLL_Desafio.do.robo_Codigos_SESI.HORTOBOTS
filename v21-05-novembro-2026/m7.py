from base import *

def run():
    largada("PESADO")
    andar(-43.2, velocidade=700, aceleracao=700) #andar 45 cm pra frente, velocidade=700, aceleração=700
    girar_relativo(5, velocidade=1000)
    mover_garra_a(-1500, velocidade=1000)
    girar_relativo(-5, velocidade=1000)
    andar(-30, velocidade=700, aceleracao=500)
    girar_relativo(75, velocidade=1000)
    andar(-35, velocidade=700, aceleracao=500)
    girar_relativo(39, velocidade=500)
    andar(-30, velocidade=400, aceleracao=100)

if __name__ == "__main__":
    run()