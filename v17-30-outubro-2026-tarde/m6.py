from base import *
from pybricks.tools import wait

def run():
    largada("PESADO")
    andar(-63, velocidade=1000, aceleracao=600)
    girar(-90, velocidade=500)
    andar(-43, velocidade=1000)
    girar_relativo(90, velocidade=500)
    andar(-24.5, velocidade=900, aceleracao=600)
    mover_garra_a(4000, velocidade=1000, aceleracao=1000, esperar=True)
    andar(5, velocidade=700, aceleracao=1000)
    andar(-10, velocidade=1000, aceleracao=1000)
    andar(5, velocidade=700, aceleracao=1000)
    andar(-10, velocidade=1000, aceleracao=1000)
    andar(5, velocidade=700, aceleracao=1000)
    andar(-10, velocidade=1000, aceleracao=1000)
    #girar_relativo(10, velocidade=500)
    #girar_relativo(-20, velocidade=500)
    #girar_relativo(20, velocidade=500)
    #girar_relativo(-20, velocidade=500)
    #girar_relativo(20, velocidade=500)
    #girar_relativo(-20, velocidade=500)
    #girar_relativo(20, velocidade=500)
    #girar_relativo(-20, velocidade=500)
    #girar_relativo(20, velocidade=500)

if __name__ == "__main__":
    run()
