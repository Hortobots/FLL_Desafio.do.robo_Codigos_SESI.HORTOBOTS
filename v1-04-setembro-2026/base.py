from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
tracao_ok = False

# Declaração global dos acessórios para uso nas funções
garra_a = None
garra_b = None

try:
    # Motores de tração
    motor_esq = Motor(Port.E, Direction.COUNTERCLOCKWISE)
    motor_dir = Motor(Port.D)
    
    # Suas medidas oficiais
    robo = DriveBase(motor_esq, motor_dir, wheel_diameter=58.1, axle_track=110)
    
    # Giroscópio LIGADO com PID refinado (ganho escalado x1000)
    robo.use_gyro(True)
    robo.heading_control.pid(kp=-5000, ki=-150, kd=-300)
    
    robo.settings(straight_speed=600, straight_acceleration=1000, turn_rate=300, turn_acceleration=1000)
    
    # Inicialização das garras (Portas A e B)
    garra_a = Motor(Port.A)
    garra_b = Motor(Port.B)
    
    tracao_ok = True
    hub.light.on(Color.GREEN)
except Exception as e:
    hub.light.on(Color.RED)
    hub.speaker.beep(frequency=200, duration=1000)
    print("ERRO CRÍTICO NA BASE:", e)

# Funções universais de movimento
def andar(distancia_cm, velocidade=400):
    if not tracao_ok: return
    
    # Zera qualquer vibração residual antes de calcular o vetor
    robo.stop()
    wait(100)
    hub.imu.reset_heading(0)
    
    v_r, a_r, v_g, a_g = robo.settings()
    robo.settings(straight_speed=velocidade, straight_acceleration=1000, turn_rate=v_g, turn_acceleration=a_g)
    robo.straight(distancia_cm * 10)
    robo.settings(straight_speed=v_r, straight_acceleration=a_r, turn_rate=v_g, turn_acceleration=a_g)

def girar(angulo_graus, velocidade=300):
    if not tracao_ok: return
    v_r, a_r, v_g, a_g = robo.settings()
    robo.settings(straight_speed=v_r, straight_acceleration=a_r, turn_rate=velocidade, turn_acceleration=a_g)
    robo.turn(angulo_graus)
    robo.settings(straight_speed=v_r, straight_acceleration=a_r, turn_rate=v_g, turn_acceleration=a_g)

# Funções universais das garras
# Funções universais das garras
def mover_garra_a(graus, velocidade=500, esperar=True):
    if garra_a is not None:
        garra_a.run_angle(velocidade, graus, wait=esperar)

def mover_garra_b(graus, velocidade=500, esperar=True):
    if garra_b is not None:
        garra_b.run_angle(velocidade, graus, wait=esperar)