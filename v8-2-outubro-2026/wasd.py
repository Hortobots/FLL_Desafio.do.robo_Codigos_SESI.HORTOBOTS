import uselect
import usys
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Color, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

# Configuração mecânica da sua base
motor_esq = Motor(Port.E, Direction.COUNTERCLOCKWISE)
motor_dir = Motor(Port.D)
drive = DriveBase(motor_esq, motor_dir, wheel_diameter=58.1, axle_track=110)

# Mapeamento opcional das garras
try:
    garra_a = Motor(Port.A)
    garra_b = Motor(Port.B)
except:
    garra_a = None
    garra_b = None

hub.light.on(Color.GREEN)

# Configura a escuta do terminal do Pybricks
poll = uselect.poll()
poll.register(usys.stdin, uselect.POLLIN)

print("\n==========================================")
print("     CONTROLE TELEOPERADO (AUTO-STOP)     ")
print("==========================================")
print(" Mantenha a tecla pressionada para mover:")
print(" W : Frente | S : Trás")
print(" A : Girar Esquerda | D : Girar Direita")
print(" (Solte a tecla e o robô para na hora!)")
print("------------------------------------------")
print(" J / K  : Abrir/Fechar Garra A")
print(" N / M  : Abrir/Fechar Garra B")
print(" Q      : Sair")
print("==========================================")
print("Clique na janela do Terminal abaixo para jogar!\n")

VEL_LIN = 400     # Velocidade linear (mm/s)
VEL_ROT = 200     # Velocidade de rotação (graus/s)
TIMEOUT_MS = 100  # Tempo limite sem sinal para parar o robô (ms)

relogio = StopWatch()
em_movimento = False

while True:
    # Verifica se há nova tecla digitada no terminal
    if poll.poll(10):
        tecla = usys.stdin.read(1).lower()

        if tecla in ['w', 's', 'a', 'd']:
            relogio.reset()
            em_movimento = True

            if tecla == 'w':
                drive.drive(VEL_LIN, 0)
            elif tecla == 's':
                drive.drive(-VEL_LIN, 0)
            elif tecla == 'a':
                drive.drive(0, -VEL_ROT)
            elif tecla == 'd':
                drive.drive(0, VEL_ROT)

        elif tecla == ' ':
            drive.stop()
            em_movimento = False

        elif tecla == 'j' and garra_a:
            garra_a.run_angle(500, 180, then=Stop.HOLD, wait=False)
        elif tecla == 'k' and garra_a:
            garra_a.run_angle(500, -180, then=Stop.HOLD, wait=False)
        elif tecla == 'n' and garra_b:
            garra_b.run_angle(500, 180, then=Stop.HOLD, wait=False)
        elif tecla == 'm' and garra_b:
            garra_b.run_angle(500, -180, then=Stop.HOLD, wait=False)

        elif tecla == 'q':
            drive.stop()
            hub.light.on(Color.RED)
            print("\nControle encerrado.")
            break

    # Se o robô estiver andando e ficar sem receber comandos por mais de 250ms, ele para sozinho
    if em_movimento and relogio.time() > TIMEOUT_MS:
        drive.stop()
        em_movimento = False

    wait(10)