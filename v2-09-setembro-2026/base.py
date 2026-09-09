from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Color
from pybricks.robotics import DriveBase
from pybricks.tools import wait

hub = PrimeHub()
tracao_ok = False

garra_a = None
garra_b = None

try:
    motor_esq = Motor(Port.E, Direction.COUNTERCLOCKWISE)
    motor_dir = Motor(Port.D)
    
    # Configuração dos diâmetros e distância entre rodas (110mm)
    robo = DriveBase(motor_esq, motor_dir, wheel_diameter=58.1, axle_track=110)
    
    # Ativa o giroscópio interno do Spike Prime
    robo.use_gyro(True)
    
    # PID ajustado para amortecer o desvio do motor mais fraco
    robo.heading_control.pid(kp=-6000, ki=-100, kd=-500)
    
    # Ajuste de garras
    garra_a = Motor(Port.A)
    garra_b = Motor(Port.B)
    
    tracao_ok = True
    hub.light.on(Color.GREEN)
except Exception as e:
    hub.light.on(Color.RED)
    hub.speaker.beep(frequency=200, duration=1000)
    print("ERRO NA BASE:", e)

# --- CONFIGURAÇÃO DO PID ORIGINAL ---
# kp=-5000, ki=-150, kd=-500
robo.heading_control.pid(kp=-5000, ki=-150, kd=-500)

def andar(distancia_cm, velocidade=400):
    if not tracao_ok: return
    
    robo.stop()
    wait(50)
    hub.imu.reset_heading(0)
    
    # Guarda as configurações originais
    v_r, a_r, v_g, a_g = robo.settings()
    
    if distancia_cm < 0:
        # --- TRATAMENTO EXCLUSIVO PARA A RÉ ---
        # 1. Limita a velocidade máxima da ré em 300 mm/s para manter tração
        v_execucao = min(abs(velocidade), 300)
        
        # 2. Aceleração bem baixa (150 mm/s²) para o Motor D não patinar na saída
        aceleracao_execucao = 1000
        
        # 3. Aumenta o Kd para -800 APENAS na ré (amortece a traseira e impede a curva)
        robo.heading_control.pid(kp=-5000, ki=-150, kd=-800)
    else:
        # --- MOVIMENTO PARA FRENTE (NORMAL) ---
        v_execucao = abs(velocidade)
        aceleracao_execucao = 1000
        robo.heading_control.pid(kp=-5000, ki=-150, kd=-500)
    
    # Aplica as configurações do movimento
    robo.settings(straight_speed=v_execucao, straight_acceleration=aceleracao_execucao, turn_rate=v_g, turn_acceleration=a_g)
    
    # Executa o movimento em milímetros
    robo.straight(distancia_cm * 10)
    
    # Restaura o PID e as configurações originais para não afetar os próximos comandos
    robo.heading_control.pid(kp=-5000, ki=-150, kd=-500)
    robo.settings(straight_speed=v_r, straight_acceleration=a_r, turn_rate=v_g, turn_acceleration=a_g)

def girar(angulo_graus, velocidade=250):
    if not tracao_ok: return
    v_r, a_r, v_g, a_g = robo.settings()
    robo.settings(straight_speed=v_r, straight_acceleration=a_r, turn_rate=velocidade, turn_acceleration=a_g)
    robo.turn(angulo_graus)
    robo.settings(straight_speed=v_r, straight_acceleration=a_r, turn_rate=v_g, turn_acceleration=a_g)

def mover_garra_a(graus, velocidade=500, esperar=True):
    if garra_a is not None:
        garra_a.run_angle(velocidade, graus, wait=esperar)

def mover_garra_b(graus, velocidade=500, esperar=True):
    if garra_b is not None:
        garra_b.run_angle(velocidade, graus, wait=esperar)