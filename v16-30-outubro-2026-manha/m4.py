from base import *
from pybricks.tools import wait

def run():
    largada("PESADO")
    curva(raio_cm=-480, angulo=7.0059999)
    curva(raio_cm=-41, angulo=26.4)
    curva(raio_cm=-9, angulo=18.5)
    andar(-8.4, velocidade=1000, aceleracao=1000)
    mover_garra_a(-3900, velocidade=1000, aceleracao=1000, esperar=True)
    andar(1.1, velocidade=500)
    andar(-16, velocidade=1000, aceleracao=1000)
    andar(-1, velocidade=1000)
    andar(-10, velocidade=1000)
    andar(3, velocidade=1000)
    andar(-10, velocidade=1000)
    girar_relativo(29, velocidade=1000)
    andar(95, velocidade=1000)
if __name__ == "__main__":
    run()