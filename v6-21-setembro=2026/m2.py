from base import *

def run():
    largada("VELOZ")
    andar(68)
    girar(-80, velocidade=500)
    andar(4)
    girar(-95, velocidade=500)
    andar(-1, velocidade=300)
    girar(-5, velocidade=500)
    andar(-75)

if __name__ == "__main__":
    run()