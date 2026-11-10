from base import *
from pybricks.tools import wait

def run():
    largada("PESADO")
    andar(-92.5, velocidade=950, aceleracao=500)
    mover_garra_a(3500, velocidade=1000)
    andar(5, velocidade=700, aceleracao=500)
    mover_garra_a(3000, velocidade=1000, esperar=False)
    andar(-6.7, velocidade=1000)
    mover_garra_a(3000, velocidade=1000)
    andar(110, velocidade=1000, aceleracao=1000)
if __name__ == "__main__":
    run()