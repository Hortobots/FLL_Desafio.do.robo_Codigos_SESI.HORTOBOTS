from base import *
from pybricks.tools import wait

def run():
    largada("PESADO")
    andar(-75.5, velocidade=1000, aceleracao=400)
    girar(30, velocidade=500)
    andar(-45, velocidade=1000, aceleracao=1000)
    andar(10, velocidade=1000, aceleracao=100)
    andar(-21, velocidade=1000, aceleracao=1000)
    andar(20, velocidade=1000, aceleracao=100)
if __name__ == "__main__":
    run()