from base import *
from pybricks.tools import wait

def run():
    largada("PESADO")
    andar(-74, velocidade=1000, aceleracao=400)
    girar(-28.5, velocidade=500)
    andar(-43, velocidade=1000, aceleracao=1000)
    andar(20, velocidade=700, aceleracao=100)
if __name__ == "__main__":
    run()