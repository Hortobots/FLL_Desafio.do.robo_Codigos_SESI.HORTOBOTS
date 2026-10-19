from base import *

def run():
    largada("PESADO")
    mover_garra_b(-1900, velocidade=447.767, esperar=False)
    andar(41.75, velocidade=850, aceleracao=450)
    andar(-50, velocidade=500)
if __name__ == "__main__":
    run()