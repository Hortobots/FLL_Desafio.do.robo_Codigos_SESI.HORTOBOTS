from base import *

def run():
    VOLTAS = 1
    GRAUS = VOLTAS * 360  # 3600 graus
    
    # Executa as 10 voltas com torque ideal (400 deg/s)
    mover_garra_b(GRAUS, velocidade=400, esperar=True)

if __name__ == "__main__":
    run()