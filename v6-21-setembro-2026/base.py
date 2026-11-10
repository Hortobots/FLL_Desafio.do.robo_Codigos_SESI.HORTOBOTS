from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Color, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class RoboMundial:
    def __init__(self):
        self.hub = PrimeHub()
        self.tracao_ok = False
        
        # PERFIS DE COMPETIÇÃO: Ajustes de PID, Velocidade (mm/s) e Aceleração (mm/s²)
        self.PERFIS = {
            "LEVE":    {"kp": 7000, "ki": 150, "kd": 300, "vel": 400, "acel": 800},
            "VELOZ":   {"kp": 7500, "ki": 150, "kd": 300, "vel": 1000, "acel": 1200},
            "RETORNO": {"kp": 7500, "ki": 150, "kd": 300, "vel": 900, "acel": 1100},
            "PRECISAO":{"kp": 8000, "ki": 150, "kd": 350, "vel": 500, "acel": 800},
            "PESADO":  {"kp": 9500, "ki": 200, "kd": 450, "vel": 320, "acel": 700}
        }
        
        try:
            self.motor_esq = Motor(Port.E, Direction.COUNTERCLOCKWISE)
            self.motor_dir = Motor(Port.D)
            self.drive = DriveBase(self.motor_esq, self.motor_dir, wheel_diameter=58.1, axle_track=110)
            self.drive.use_gyro(True)
            
            self.garra_a = Motor(Port.A)
            self.garra_b = Motor(Port.B)
            
            self.tracao_ok = True
            self.hub.light.on(Color.GREEN)
            self.perfil("LEVE")
        except Exception as e:
            self.hub.light.on(Color.RED)
            self.hub.speaker.beep(frequency=200, duration=1000)
            print("ERRO CRÍTICO NA BASE:", e)

    def perfil(self, nome_perfil):
        """Aplica os parâmetros dinâmicos do perfil selecionado."""
        if not self.tracao_ok: return
        p = self.PERFIS.get(nome_perfil, self.PERFIS["LEVE"])
        self.drive.heading_control.pid(kp=p["kp"], ki=p["ki"], kd=p["kd"])
        self.drive.settings(straight_speed=p["vel"], straight_acceleration=p["acel"])

    def largada(self, nome_perfil="LEVE"):
        """Zera o giroscópio e aplica o perfil no início de cada missão."""
        if not self.tracao_ok: return
        self.drive.stop()
        wait(50)
        self.hub.imu.reset_heading(0)
        self.perfil(nome_perfil)
        self.hub.light.on(Color.GREEN)

    def andar(self, distancia_cm, velocidade=None, aceleracao=None):
        """Avança ou recua em linha reta com correção via giroscópio."""
        if not self.tracao_ok: return
        v_r, a_r, v_g, a_g = self.drive.settings()
        v_exec = abs(velocidade) if velocidade else v_r
        a_exec = aceleracao if aceleracao else a_r
        
        self.drive.settings(straight_speed=v_exec, straight_acceleration=a_exec)
        self.drive.straight(distancia_cm * 10)
        self.drive.settings(straight_speed=v_r, straight_acceleration=a_r)

    def girar(self, angulo_absoluto, velocidade=300):
        """Gira para uma orientação fixa de bússola."""
        if not self.tracao_ok: return
        erro = angulo_absoluto - self.hub.imu.heading()
        v_r, a_r, v_g, a_g = self.drive.settings()
        self.drive.settings(turn_rate=velocidade)
        self.drive.turn(erro)
        self.drive.settings(turn_rate=v_g)

    def alinhar_parede(self, tempo_ms=1200, angulo_pos_alinhamento=0, velocidade_re=-150):
        """Dá ré contra a parede para re-calibrar o giroscópio."""
        if not self.tracao_ok: return
        self.drive.drive(velocidade_re, 0)
        wait(tempo_ms)
        self.drive.stop()
        self.hub.imu.reset_heading(angulo_pos_alinhamento)

    def mover_garra_a(self, graus, velocidade=350, esperar=True):
        if self.garra_a:
            self.garra_a.run_angle(abs(velocidade), graus, then=Stop.HOLD, wait=esperar)

    def mover_garra_b(self, graus, velocidade=350, esperar=True):
        if self.garra_b:
            self.garra_b.run_angle(abs(velocidade), graus, then=Stop.HOLD, wait=esperar)

# Instância global
bot = RoboMundial()

# Funções exportadas para uso direto nas missões (sem "bot.")
largada = bot.largada
perfil = bot.perfil
andar = bot.andar
girar = bot.girar
alinhar_parede = bot.alinhar_parede
mover_garra_a = bot.mover_garra_a
mover_garra_b = bot.mover_garra_b
hub = bot.hub