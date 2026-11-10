from base import *

def run():
    largada("PESADO")
    mover_garra_b(-1900, velocidade=1000, aceleracao=430.767, esperar=False)
    andar(41.75, velocidade=850, aceleracao=450)
    andar(-50, velocidade=500)
    gabarito_garra("B", velocidade=300, limite_torque_mNm=10, raio_cm=9)
if __name__ == "__main__":
    run()