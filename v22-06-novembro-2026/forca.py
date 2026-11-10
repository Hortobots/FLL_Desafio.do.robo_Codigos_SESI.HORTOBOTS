from pybricks.hubs import PrimeHub  # Importa a classe do Hub principal da LEGO Pybricks
from pybricks.pupdevices import Motor  # Importa a classe de controlo de Motores
from pybricks.parameters import Port  # Importa as definições de portas físicas do Hub
from pybricks.tools import wait  # Importa a função de espera por tempo

hub = PrimeHub()  # Inicializa a ligação com o Hub principal

PORTA = Port.A  # Define a porta do motor a testar como Porta A
RAIO_CM = 4.0  # Define o raio/comprimento do braço de alavanca da garra em cm

motor = Motor(PORTA)  # Conecta a instância do motor na porta especificada

print("\n=== MEDIDOR STANDALONE DE CARGA E PESO ===")  # Imprime o cabeçalho do medidor no terminal
print("Lendo torque em tempo real... (Pressione Stop no Pybricks para parar)\n")  # Exibe instrução de paragem

motor.run(speed=150)  # Liga o motor com velocidade constante baixa de 150 para medir a resistência

while True:  # Ciclo contínuo de leitura de esforço mecânico
    torque = motor.load()  # Lê o torque instantâneo exercido pelo motor em mN·m
    
    forca_N = (torque / 1000.0) / (RAIO_CM / 100.0) if RAIO_CM > 0 else 0  # Calcula a força exercida na ponta do braço em Newtons (N)
    peso_g = (forca_N / 9.81) * 1000.0  # Estima o peso de carga correspondente em gramas (g)
    
    print(f"Torque: {torque:4d} mN·m  |  Força: {forca_N:5.2f} N  |  Peso Est.: {peso_g:6.1f} g")  # Exibe os dados formatados no terminal
    
    wait(200)  # Aguarda 200 milissegundos antes de fazer a próxima leitura de carga