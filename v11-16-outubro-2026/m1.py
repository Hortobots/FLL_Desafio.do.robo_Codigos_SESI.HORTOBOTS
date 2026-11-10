from base import *

def run():
    largada("PESADO")
    andar(31, velocidade=500, aceleracao=200)
    
    
    girar(49.9, velocidade=300)

    # Inicia o movimento da garra sem esperar terminar
    mover_garra_b(-870, velocidade=510, esperar=False)
    # Mini delay para estabilizar o robô antes de girar
    wait(100)  # 0.1 segundo (100 ms)
    andar(28.5, velocidade=967, aceleracao=800)
    
    # O robô anda enquanto a garra está se movendo
    andar(20, velocidade=600, aceleracao=300)


if __name__ == "__main__":
    run()