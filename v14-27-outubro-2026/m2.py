from base import *

def run():
    largada("PESADO")
    andar(68)
    girar(-80, velocidade=500)
    andar(7.5)
    girar(-5, velocidade=500)
    andar(-1, velocidade=300)
    girar(10, velocidade=400)
    andar(-75, velocidade=700)

if __name__ == "__main__":
    run()