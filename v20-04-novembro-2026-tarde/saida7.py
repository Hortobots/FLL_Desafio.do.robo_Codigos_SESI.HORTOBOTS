from base import *
from pybricks.tools import wait

def run():
    largada("PESADO")
    curva(raio_cm=-500, angulo=6.55)
    curva(raio_cm=-48, angulo=29.4)
    curva(raio_cm=-5, angulo=15)
    
    andar(-26, velocidade=1000, aceleracao=1000)
    mover_garra_a(-3500, velocidade=1000, aceleracao=1000, esperar=True)
    andar(3, velocidade=1000)
    
    for _ in range(2):
        andar(-5, velocidade=1000, aceleracao=1000)
        andar(3, velocidade=1000, aceleracao=1000)
        
    for _ in range(2):
        girar_relativo(10, velocidade=1000)
        girar_relativo(-10, velocidade=1000)

    mover_garra_a(2300, velocidade=1000, aceleracao=1000, esperar=False)
    andar(3, velocidade=1000)
    girar_relativo(48, velocidade=1000)
    curva(raio_cm=500, angulo=3.50, velocidade=1000)
    curva(raio_cm=90, angulo=-45, velocidade=1000)

if __name__ == "__main__":
    run()