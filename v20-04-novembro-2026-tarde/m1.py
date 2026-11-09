from base import *

def run():
    largada("PESADO")
    andar(-30, velocidade=1000, aceleracao=1000)
    andar(10, velocidade=100, aceleracao=100)
    mover_garra_a(2200, velocidade=1000, aceleracao=1000, esperar=False)
    andar(-9, velocidade=700, aceleracao=500)
    wait(2500)
    curva(150, angulo=45)

if __name__ == "__main__":
    run()