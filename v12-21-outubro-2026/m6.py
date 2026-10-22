from base import *
from pybricks.tools import wait

def run():
    largada("PESADO")
    andar(-63, velocidade=1000, aceleracao=700)
    girar(-90, velocidade=500)
    andar(-39.5, velocidade=1000)
    girar_relativo(90, velocidade=500)
    andar(-24.5, velocidade=1000, aceleracao=1000)
    mover_garra_a(4000, velocidade=1000, esperar=True)
    andar(10, velocidade=1000)
    girar(-90, velocidade=500)
    curva(raio_cm=45, angulo=120, velocidade=1000)

if __name__ == "__main__":
    run()
