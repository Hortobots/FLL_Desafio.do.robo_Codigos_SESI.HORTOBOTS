from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Direction, Color, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class RoboMundial:
    def __init__(self):
        self.hub = PrimeHub()
        self.tracao_ok = False
        self.garra_a = None
        self.garra_b = None
        self.cronometro = StopWatch()  # Temporizador automático de missão

        # PERFIS DE COMPETIÇÃO
        self.PERFIS = {
            "LEVE":     {"kp": 18000, "ki": 150, "kd": 400, "vel": 450, "acel": 800},
            "VELOZ":    {"kp": 12000, "ki": 120, "kd": 600, "vel": 700, "acel": 850},
            "RETORNO":  {"kp": 18000, "ki": 120, "kd": 500, "vel": 650, "acel": 800},
            "PRECISAO": {"kp": 22000, "ki": 150, "kd": 500, "vel": 300, "acel": 600},
            "PESADO":   {"kp": 30000, "ki": 150, "kd": 450, "vel": 320, "acel": 700}
        }

        self._inicializar_hardware()

    def _inicializar_hardware(self):
        try:
            self.motor_esq = Motor(Port.E, Direction.COUNTERCLOCKWISE)
            self.motor_dir = Motor(Port.D)
            self.drive = DriveBase(self.motor_esq, self.motor_dir, wheel_diameter=58.1, axle_track=110)
            self.drive.use_gyro(True)
            self.tracao_ok = True
        except Exception as e:
            print(f"[ERRO CRÍTICO] Falha nos Motores de Tração: {e}")
            self.hub.light.on(Color.RED)
            return

        try:
            self.garra_a = Motor(Port.A)
        except Exception:
            print("[AVISO] Garra A (Porta A) não detetada.")

        try:
            self.garra_b = Motor(Port.B)
        except Exception:
            print("[AVISO] Garra B (Porta B) não detetada.")

        self.hub.light.on(Color.GREEN)
        self.perfil("LEVE")

    def perfil(self, nome: str):
        if not self.tracao_ok: return
        cfg = self.PERFIS.get(nome.upper(), self.PERFIS["LEVE"])
        self.drive.heading_control.pid(kp=cfg["kp"], ki=cfg["ki"], kd=cfg["kd"])
        self.drive.settings(straight_speed=cfg["vel"], straight_acceleration=cfg["acel"])

    def largada(self, nome_perfil: str = "LEVE"):
        """Inicia a missão: zera o giroscópio, ativa o perfil e reinicia o cronómetro."""
        if not self.tracao_ok: return
        self.drive.stop()
        wait(50)
        self.hub.imu.reset_heading(0)
        self.perfil(nome_perfil)
        self.hub.light.on(Color.GREEN)
        self.cronometro.reset()
        print(f"\n[LARGADA] Cronómetro iniciado | Perfil: {nome_perfil}")

    def tempo(self) -> float:
        """Retorna e exibe no terminal o tempo decorrido desde a largada."""
        segundos = self.cronometro.time() / 1000.0
        print(f"[TEMPO] {segundos:.2f}s")
        return segundos

    def andar(self, distancia_cm: float, velocidade: float = None, aceleracao: float = None):
        if not self.tracao_ok: return
        v_orig, a_orig, _, _ = self.drive.settings()
        v_exec = abs(velocidade) if velocidade is not None else v_orig
        a_exec = aceleracao if aceleracao is not None else a_orig

        self.drive.settings(straight_speed=v_exec, straight_acceleration=a_exec)
        self.drive.straight(distancia_cm * 10.0)
        self.drive.settings(straight_speed=v_orig, straight_acceleration=a_orig)
        self.tempo()

    def girar(self, angulo_absoluto: float, velocidade: float = 300):
        if not self.tracao_ok: return
        erro = angulo_absoluto - self.hub.imu.heading()
        _, _, v_rot_orig, _ = self.drive.settings()
        self.drive.settings(turn_rate=velocidade)
        self.drive.turn(erro)
        self.drive.settings(turn_rate=v_rot_orig)
        self.tempo()

    def girar_relativo(self, angulo_relativo: float, velocidade: float = 300):
        if not self.tracao_ok: return
        rumo_atual = self.hub.imu.heading()
        self.girar(rumo_atual + angulo_relativo, velocidade)

    def alinhar_parede(self, tempo_ms: int = 1200, angulo_pos_alinhamento: float = 0, velocidade_re: float = -150):
        if not self.tracao_ok: return
        self.drive.drive(velocidade_re, 0)
        wait(tempo_ms)
        self.drive.stop()
        wait(50)
        self.hub.imu.reset_heading(angulo_pos_alinhamento)
        self.tempo()

    def mover_garra_a(self, graus: float, velocidade: float = 350, aceleracao: float = None, esperar: bool = True):
        if not self.garra_a: return
        v_max_orig, a_max_orig = self.garra_a.control.limits()[:2]
        
        if aceleracao is not None:
            self.garra_a.control.limits(speed=abs(velocidade), acceleration=abs(aceleracao))
        else:
            self.garra_a.control.limits(speed=abs(velocidade))
            
        self.garra_a.run_angle(abs(velocidade), graus, then=Stop.HOLD, wait=esperar)
        self.garra_a.control.limits(speed=v_max_orig, acceleration=a_max_orig)
        if esperar: self.tempo()

    def mover_garra_b(self, graus: float, velocidade: float = 350, aceleracao: float = None, esperar: bool = True):
        if not self.garra_b: return
        v_max_orig, a_max_orig = self.garra_b.control.limits()[:2]
        
        if aceleracao is not None:
            self.garra_b.control.limits(speed=abs(velocidade), acceleration=abs(aceleracao))
        else:
            self.garra_b.control.limits(speed=abs(velocidade))
            
        self.garra_b.run_angle(abs(velocidade), graus, then=Stop.HOLD, wait=esperar)
        self.garra_b.control.limits(speed=v_max_orig, acceleration=a_max_orig)
        if esperar: self.tempo()

    def gabarito_garra(self, porta: str = "A", velocidade: float = 300, limite_torque_mNm: float = 250, raio_cm: float = 4.0) -> bool:
        """
        Recalibra/encosta a garra até detetar resistência física (ponto zero mecánico).
        Registos em tempo real da força em Newtons e massa estimada em gramas.
        """
        garra = self.garra_a if porta.upper() == "A" else self.garra_b
        if not garra:
            print(f"[GABARITO] Garra {porta} não encontrada.")
            return False

        print(f"[GABARITO] Calibrando Garra {porta} (Limite: {limite_torque_mNm} mN·m)...")
        garra.run(velocidade)
        
        cronometro_limite = StopWatch()
        while cronometro_limite.time() < 4000:  # Timeout de segurança
            torque_atual = abs(garra.load())
            
            if torque_atual >= abs(limite_torque_mNm) or garra.stalled():
                garra.hold()
                garra.reset_angle(0)  # Redefine o encoder para 0° no ponto mecânico
                
                forca_N = (torque_atual / 1000.0) / (raio_cm / 100.0) if raio_cm > 0 else 0
                peso_g = (forca_N / 9.81) * 1000.0
                
                print(f"[GABARITO] Garra {porta} calibrada em 0°! Torque: {torque_atual} mN·m | Força: {forca_N:.2f} N | Peso Est.: {peso_g:.1f} g")
                self.tempo()
                return True
            wait(20)

        garra.stop()
        print(f"[GABARITO] Tempo limite excedido sem detetar ponto mecânico.")
        self.tempo()
        return False

    def checar_bateria(self) -> int:
        tensao = self.hub.battery.voltage()
        porcentagem = max(0, min(100, int((tensao - 7200) / (8300 - 7200) * 100)))
        print(f"[TELEMETRIA] Tensão: {tensao}mV | Bateria: {porcentagem}%")

        if tensao < 7400:
            self.hub.light.on(Color.RED)
            self.hub.speaker.beep(frequency=300, duration=800)
            print("[ALERTA] Bateria fraca!")
        return porcentagem

# Instância Global e Mapeamento de Atalhos
bot = RoboMundial()

largada = bot.largada
perfil = bot.perfil
tempo = bot.tempo
andar = bot.andar
girar = bot.girar
girar_relativo = bot.girar_relativo
alinhar_parede = bot.alinhar_parede
mover_garra_a = bot.mover_garra_a
mover_garra_b = bot.mover_garra_b
gabarito_garra = bot.gabarito_garra
checar_bateria = bot.checar_bateria
hub = bot.hub