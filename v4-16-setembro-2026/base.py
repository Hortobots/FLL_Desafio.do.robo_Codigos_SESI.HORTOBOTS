from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Color, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
tracao_ok = False

garra_a = None
garra_b = None

try:
    motor_esq = Motor(Port.E, Direction.COUNTERCLOCKWISE)
    motor_dir = Motor(Port.D)
    
    # Configuração geométrica do robô
    robo = DriveBase(motor_esq, motor_dir, wheel_diameter=58.1, axle_track=110)
    
    # Ativa o giroscópio do PrimeHub
    robo.use_gyro(True)
    
    # PID equilibrado para respostas rápidas sem oscilação
    robo.heading_control.pid(kp=-7000, ki=-150, kd=-300)
    
    # Eleva os limites padrão da base para aceitar velocidades altas (até 1000 mm/s)
    robo.settings(straight_speed=600, straight_acceleration=1200, turn_rate=300, turn_acceleration=1000)
    
    # Motores de acessório
    garra_a = Motor(Port.A)
    garra_b = Motor(Port.B)
    
    tracao_ok = True
    hub.light.on(Color.GREEN)
except Exception as e:
    hub.light.on(Color.RED)
    hub.speaker.beep(frequency=200, duration=1000)
    print("ERRO CRÍTICO NA BASE:", e)

def andar(distancia_cm, velocidade=500, aceleracao=1000):
    if not tracao_ok: return
    
    # Parada preventiva e reset do referencial angular
    robo.stop()
    wait(50)
    hub.imu.reset_heading(0)
    
    # Salva configurações globais
    v_r, a_r, v_g, a_g = robo.settings()
    
    # Aplica exatamente a velocidade solicitada (tanto para frente quanto para trás)
    v_execucao = abs(velocidade)
    robo.settings(straight_speed=v_execucao, straight_acceleration=aceleracao, turn_rate=v_g, turn_acceleration=a_g)
    
    # Executa o movimento em milímetros
    robo.straight(distancia_cm * 10)
    
    # Restaura configurações padrão da base
    robo.settings(straight_speed=v_r, straight_acceleration=a_r, turn_rate=v_g, turn_acceleration=a_g)

def girar(angulo_graus, velocidade=300):
    if not tracao_ok: return
    v_r, a_r, v_g, a_g = robo.settings()
    robo.settings(straight_speed=v_r, straight_acceleration=a_r, turn_rate=velocidade, turn_acceleration=a_g)
    robo.turn(angulo_graus)
    robo.settings(straight_speed=v_r, straight_acceleration=a_r, turn_rate=v_g, turn_acceleration=a_g)

def mover_garra_a(graus, velocidade=350, esperar=True):
    """
    Move a Garra A na Porta A por um ângulo definido.
    :param graus: Ângulo em graus (positivo ou negativo)
    :param velocidade: Velocidade em deg/s (Padrão 350 para torque máximo)
    :param esperar: True para aguardar o término, False para rodar em segundo plano
    """
    if garra_a is not None:
        # abs(velocidade) previne bugs caso o sinal seja invertido na velocidade em vez do ângulo
        garra_a.run_angle(
            speed=abs(velocidade), 
            rotation_angle=graus, 
            then=Stop.HOLD, 
            wait=esperar
        )

def mover_garra_b(graus, velocidade=350, esperar=True):
    """
    Move a Garra B na Porta B por um ângulo definido.
    :param graus: Ângulo em graus (positivo ou negativo)
    :param velocidade: Velocidade em deg/s (Padrão 350 para torque máximo)
    :param esperar: True para aguardar o término, False para rodar em segundo plano
    """
    if garra_b is not None:
        garra_b.run_angle(
            speed=abs(velocidade), 
            rotation_angle=graus, 
            then=Stop.HOLD, 
            wait=esperar
        )