from base import *
from pybricks.tools import wait

def run():
    largada("PRECISAO")
    mover_garra_b(-153.8, velocidade=300, esperar=True)
    andar(78)
    wait(50)
    mover_garra_b(180, velocidade=350, esperar=False)
    andar(2.5, velocidade=200, aceleracao=400)

if __name__ == "__main__":
    run()