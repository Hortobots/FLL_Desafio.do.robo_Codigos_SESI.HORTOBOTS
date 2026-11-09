from base import *
from pybricks.tools import wait

def run():
    largada("PESADO")
    curva(raio_cm=-484, angulo=7.0059999)
    curva(raio_cm=-41, angulo=26.4)
    curva(raio_cm=-9.5, angulo=18)
    andar(-8.8, velocidade=1000, aceleracao=1000)
    mover_garra_a(-3200, velocidade=1000, aceleracao=1000)
    andar(0.5, velocidade=500)
    andar(-13, velocidade=1000, aceleracao=1000)
    andar(3, velocidade=1000)
    andar(-10, velocidade=1000)
    andar(3, velocidade=1000)
    andar(-10, velocidade=1000)
    girar_relativo(39, velocidade=1000)
    andar(90, velocidade=1000)
if __name__ == "__main__":
    run()