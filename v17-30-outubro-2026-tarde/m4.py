from base import *
from pybricks.tools import wait

def run():
    largada("PESADO")
    curva(raio_cm=-500.567, angulo=6.9456789)
    curva(raio_cm=-48, angulo=25.5)
    curva(raio_cm=-5, angulo=17.8)
    #chegamos na missão
    andar(-17.65, velocidade=900, aceleracao=700)
    mover_garra_a(-3900, velocidade=1000, aceleracao=1000, esperar=True)
    andar(3, velocidade=500)
    andar(-11, velocidade=400, aceleracao=1000)
    girar_relativo(10, velocidade=1000)
    girar_relativo(-10, velocidade=1000)
    girar_relativo(10, velocidade=1000)
    girar_relativo(-10, velocidade=1000)
    mover_garra_a(2300, velocidade=1000, aceleracao=1000, esperar=False)
    girar_relativo(30, velocidade=30)
    andar(110, velocidade=1000)
if __name__ == "__main__":
    run()