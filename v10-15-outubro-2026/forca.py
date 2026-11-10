from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub()

# ---------------------------------------------------------
# CONFIGURAÇÃO RÁPIDA
PORTA = Port.A     # Porta da garra/motor a ser medido
RAIO_CM = 4.0      # Comprimento do braço em cm (do centro do motor até a ponta)
# ---------------------------------------------------------

motor = Motor(PORTA)

print("\n=== MEDIDOR STANDALONE DE CARGA E PESO ===")
print("Lendo torque em tempo real... (Pressione Stop no Pybricks para parar)\n")

# Ligas o motor a uma velocidade baixa constante para medir a resistência
motor.run(speed=150)

while True:
    # 1. Leitura bruta de torque do motor (mN·m)
    torque = motor.load()
    
    # 2. Conversão para Força (N) e Peso Estimado (g)
    forca_N = (torque / 1000.0) / (RAIO_CM / 100.0) if RAIO_CM > 0 else 0
    peso_g = (forca_N / 9.81) * 1000.0
    
    # Exibe no terminal
    print(f"Torque: {torque:4d} mN·m  |  Força: {forca_N:5.2f} N  |  Peso Est.: {peso_g:6.1f} g")
    
    wait(200)