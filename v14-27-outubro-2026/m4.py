from base import *
from pybricks.tools import wait

def run():
    largada("PESADO")
    curva(raio_cm=-505, angulo=6.7)8
    curva(raio_cm=-41, angulo=26.4)
    curva(raio_cm=-7, angulo=17.4)
    andar(-11, velocidade=1000, aceleracao=1000)
    mover_garra_a(-1700, velocidade=1000)
if __name__ == "__main__":
    run()