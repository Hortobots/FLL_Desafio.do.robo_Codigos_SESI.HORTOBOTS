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
            "LEVE":     {"kp": 18000, "ki": 150, "kd": 400, "vel": 450, "acel": 800},
            "VELOZ":    {"kp": 12000, "ki": 120, "kd": 600, "vel": 700, "acel": 850},
            "RETORNO":  {"kp": 18000, "ki": 120, "kd": 500, "vel": 650, "acel": 800},
            "PRECISAO": {"kp": 22000, "ki": 150, "kd": 500, "vel": 300, "acel": 600},
            "PESADO":   {"kp": 31000, "ki": 150, "kd": 400, "vel": 320, "acel": 700}
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

    def girar(self, angulo_relativo, velocidade=300):
        """Zera o giroscópio e gira de forma relativa."""
        if not self.tracao_ok: return
        self.drive.stop()  # <--- Para a DriveBase para libertar o controlo do gyro!
        wait(50)
        self.hub.imu.reset_heading(0)
        
        v_r, a_r, v_g, a_g = self.drive.settings()
        self.drive.settings(turn_rate=velocidade)
        self.drive.turn(angulo_relativo)
        self.drive.settings(turn_rate=v_g)

    def alinhar_parede(self, tempo_ms=1200, angulo_pos_alinhamento=0, velocidade_re=-150):
        """Dá ré contra a parede para re-calibrar o giroscópio."""
        if not self.tracao_ok: return
        self.drive.drive(velocidade_re, 0)
        wait(tempo_ms)
        self.drive.stop()
        self.hub.imu.reset_heading(angulo_pos_alinhamento)

    def mover_garra_a(self, graus: float, velocidade: float = 350, esperar: bool = True, raio_cm: float = 4.0, medir_forca: bool = False):
        """
        Aciona a Garra A. Se 'medir_forca=True', exibe no terminal o torque (mN·m), a força (N) e o peso estimado (g).
        """
        if not self.garra_a: return 0
        
        if not medir_forca:
            self.garra_a.run_angle(abs(velocidade), graus, then=Stop.HOLD, wait=esperar)
            return self.garra_a.load()
        
        # Modo Inteligente com Leitura de Esforço
        angulo_alvo = self.garra_a.angle() + graus
        self.garra_a.run_target(abs(velocidade), angulo_alvo, wait=False)
        
        torque_maximo = 0
        while not self.garra_a.done():
            torque_atual = abs(self.garra_a.load())
            if torque_atual > torque_maximo:
                torque_maximo = torque_atual
            
            if self.garra_a.stalled():  # Se a garra travar no objeto, para com segurança
                break
            wait(20)
            
        self.garra_a.hold()
        
        # Cálculo de Força e Peso
        forca_N = (torque_maximo / 1000.0) / (raio_cm / 100.0) if raio_cm > 0 else 0
        peso_g = (forca_N / 9.81) * 1000.0
        
        print(f"[GARRA A] Torque Máx: {torque_maximo:4d} mN·m | Força: {forca_N:.2f} N | Peso Est.: {peso_g:.1f} g")
        return torque_maximo

    def mover_garra_b(self, graus: float, velocidade: float = 350, esperar: bool = True, raio_cm: float = 4.0, medir_forca: bool = False):
        """
        Aciona a Garra B. Se 'medir_forca=True', exibe no terminal o torque (mN·m), a força (N) e o peso estimado (g).
        """
        if not self.garra_b: return 0
        
        if not medir_forca:
            self.garra_b.run_angle(abs(velocidade), graus, then=Stop.HOLD, wait=esperar)
            return self.garra_b.load()
        
        # Modo Inteligente com Leitura de Esforço
        angulo_alvo = self.garra_b.angle() + graus
        self.garra_b.run_target(abs(velocidade), angulo_alvo, wait=False)
        
        torque_maximo = 0
        while not self.garra_b.done():
            torque_atual = abs(self.garra_b.load())
            if torque_atual > torque_maximo:
                torque_maximo = torque_atual
            
            if self.garra_b.stalled():
                break
            wait(20)
            
        self.garra_b.hold()
        
        forca_N = (torque_maximo / 1000.0) / (raio_cm / 100.0) if raio_cm > 0 else 0
        peso_g = (forca_N / 9.81) * 1000.0
        
        print(f"[GARRA B] Torque Máx: {torque_maximo:4d} mN·m | Força: {forca_N:.2f} N | Peso Est.: {peso_g:.1f} g")
        return torque_maximo

    def gabarito_garra(self, porta="B", velocidade=300, limite_torque_mNm=250, raio_cm=4.0) -> bool:
        """
        Fecha a garra até atingir a força/torque desejada ou travar no objeto.
        Garante que a peça foi presa sem forçar o motor.
        """
        garra = self.garra_a if porta.upper() == "A" else self.garra_b
        if not garra: return False
        
        garra.run(velocidade if velocidade > 0 else -velocidade)
        cronometro = StopWatch()
        
        print(f"[GARRA {porta}] Buscando objeto (Limite: {limite_torque_mNm} mN·m)...")
        
        while cronometro.time() < 3000:  # Timeout de 3 segundos
            torque_atual = abs(garra.load())
            
            if torque_atual >= limite_torque_mNm or garra.stalled():
                garra.hold()
                forca_N = (torque_atual / 1000.0) / (raio_cm / 100.0) if raio_cm > 0 else 0
                peso_g = (forca_N / 9.81) * 1000.0
                
                print(f"[GARRA {porta}] OBJETO PRESO! Torque: {torque_atual} mN·m | Força: {forca_N:.2f} N | Peso: {peso_g:.1f} g")
                return True
            wait(20)
            
        garra.stop()
        print(f"[GARRA {porta}] AVISO: Objeto não detectado ou tempo limite excedido.")
        return False

    def checar_bateria(self):
        """Exibe a carga da bateria e emite alerta se estiver abaixo de 20%."""
        tensao = self.hub.battery.voltage()
        
        # Converte milivolts (7200 a 8300 mV) para percentagem (0 a 100%)
        porcentagem = int((tensao - 7200) / (8300 - 7200) * 100)
        porcentagem = max(0, min(100, porcentagem))
        
        print(f"[BATERIA] Tensão: {tensao} mV | Carga: {porcentagem}%")
        
        # Alerta se a bateria estiver crítica (abaixo de 7400 mV / ~20%)
        if tensao < 7400:
            self.hub.light.on(Color.RED)
            self.hub.speaker.beep(frequency=300, duration=1000)
            print("[ATENÇÃO] BATERIA FRACA! Troque ou carregue o Hub.")
        
        return porcentagem

# Instância global
bot = RoboMundial()

# No final do arquivo base.py:
largada = bot.largada
perfil = bot.perfil
andar = bot.andar
girar = bot.girar
alinhar_parede = bot.alinhar_parede
mover_garra_a = bot.mover_garra_a
mover_garra_b = bot.mover_garra_b
checar_bateria = bot.checar_bateria  # <--- Adicione esta linha!
hub = bot.hub
gabarito_garra = bot.gabarito_garra