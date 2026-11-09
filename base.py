from pybricks.hubs import PrimeHub  # Importa a classe do Hub principal da LEGO Pybricks
from pybricks.pupdevices import Motor  # Importa a classe de controlo de Motores
from pybricks.parameters import Port, Direction, Color, Stop  # Importa os parâmetros de portas, direções, cores e paragens
from pybricks.robotics import DriveBase  # Importa a base de tração para robôs de duas rodas
from pybricks.tools import wait, StopWatch  # Importa o temporizador e a função de pausa

class RoboMundial:  # Declaração da classe principal que gere todo o robô
    def __init__(self):  # Método construtor para inicializar as variáveis e hardware
        self.hub = PrimeHub()  # Cria a instância do Hub central do robô
        self.tracao_ok = False  # Estado inicial da tração definido como desativado
        self.garra_a = None  # Inicializa a variável da Garra A como nula
        self.garra_b = None  # Inicializa a variável da Garra B como nula
        self.cronometro = StopWatch()  # Cria o temporizador automático para cronometrar a missão

        # Dicionário com os perfis de competição definindo PID (kp, ki, kd), velocidade (vel) e aceleração (acel)
        self.PERFIS = {
            "LEVE":     {"kp": 18000, "ki": 150, "kd": 400, "vel": 450, "acel": 800},
            "VELOZ":    {"kp": 12000, "ki": 120, "kd": 600, "vel": 700, "acel": 850},
            "RETORNO":  {"kp": 18000, "ki": 120, "kd": 500, "vel": 650, "acel": 800},
            "PRECISAO": {"kp": 22000, "ki": 150, "kd": 500, "vel": 300, "acel": 600},
            "PESADO":   {"kp": 31000, "ki": 150, "kd": 600, "vel": 320, "acel": 700}
        }

        self._inicializar_hardware()  # Chama o método privado de inicialização de hardware

    def _inicializar_hardware(self):  # Função interna para conectar os motores e tratar erros de hardware
        try:  # Tenta inicializar os motores de tração principal
            self.motor_esq = Motor(Port.E, Direction.COUNTERCLOCKWISE)  # Motor esquerdo na porta E com rotação invertida
            self.motor_dir = Motor(Port.D)  # Motor direito na porta D com rotação normal
            self.drive = DriveBase(self.motor_esq, self.motor_dir, wheel_diameter=58.1, axle_track=110)  # Define a base com diâmetro da roda de 58.1mm e distância entre eixos de 110mm
            self.drive.use_gyro(True)  # Ativa o uso do giroscópio interno para manter o robô reto
            self.tracao_ok = True  # Marca a tração como operacional após o sucesso
        except Exception as e:  # Captura falhas de conexão nos motores principais
            print(f"[ERRO CRÍTICO] Falha nos Motores de Tração: {e}")  # Imprime mensagem de erro no terminal
            self.hub.light.on(Color.RED)  # Acende a luz vermelha no Hub indicando erro
            return  # Interrompe a inicialização do robô

        try:  # Tenta conectar o motor do acessório A
            self.garra_a = Motor(Port.A)  # Liga o motor da garra A na porta A
        except Exception:  # Trata a ausência da garra A
            print("[AVISO] Garra A (Porta A) não detetada.")  # Avisa no terminal que a garra A não foi ligada

        try:  # Tenta conectar o motor do acessório B
            self.garra_b = Motor(Port.B)  # Liga o motor da garra B na porta B
        except Exception:  # Trata a ausência da garra B
            print("[AVISO] Garra B (Porta B) não detetada.")  # Avisa no terminal que a garra B não foi ligada

        self.hub.light.on(Color.GREEN)  # Acende a luz verde no Hub indicando prontidão
        self.perfil("LEVE")  # Aplica o perfil LEVE por defeito na inicialização

    def perfil(self, nome: str):  # Função para alterar o perfil de condução PID e velocidades
        if not self.tracao_ok: return  # Ignora se a tração não estiver pronta
        cfg = self.PERFIS.get(nome.upper(), self.PERFIS["LEVE"])  # Procura o perfil pelo nome ou usa LEVE como padrão
        self.drive.heading_control.pid(kp=cfg["kp"], ki=cfg["ki"], kd=cfg["kd"])  # Atualiza os ganhos do controlo PID de rumo
        self.drive.settings(straight_speed=cfg["vel"], straight_acceleration=cfg["acel"])  # Atualiza as configurações de velocidade e aceleração

    def largada(self, nome_perfil: str = "LEVE"):  # Prepara o robô para iniciar uma missão
        if not self.tracao_ok: return  # Verifica se os motores de tração estão ativos
        self.drive.stop()  # Garante que a base está totalmente parada
        wait(50)  # Aguarda 50 milissegundos para estabilização
        self.hub.imu.reset_heading(0)  # Reinicia a leitura do giroscópio para 0 graus
        self.perfil(nome_perfil)  # Aplica o perfil selecionado para a largada
        self.hub.light.on(Color.GREEN)  # Luz verde no Hub confirmando início de missão
        self.cronometro.reset()  # Reinicia o temporizador automático para 0 segundos
        print(f"\n[LARGADA] Cronómetro iniciado | Perfil: {nome_perfil}")  # Exibe no terminal as informações da largada

    def tempo(self) -> float:  # Retorna e exibe o tempo decorrido da missão
        segundos = self.cronometro.time() / 1000.0  # Converte o tempo do cronómetro de ms para segundos
        print(f"[TEMPO] {segundos:.2f}s")  # Imprime o tempo atual com duas casas decimais no terminal
        return segundos  # Retorna o valor numérico do tempo em segundos

    def andar(self, distancia_cm: float, velocidade: float = None, aceleracao: float = None):  # Move o robô em linha reta
        if not self.tracao_ok: return  # Aborta o movimento se não houver tração operacional
        v_orig, a_orig, _, _ = self.drive.settings()  # Obtém as definições originais de velocidade e aceleração
        v_exec = abs(velocidade) if velocidade is not None else v_orig  # Define a velocidade de execução ou usa a original
        a_exec = aceleracao if aceleracao is not None else a_orig  # Define a aceleração de execução ou usa a original
        self.drive.settings(straight_speed=v_exec, straight_acceleration=a_exec)  # Aplica a velocidade e aceleração temporárias
        self.drive.straight(distancia_cm * 10.0)  # Converte distância de centímetros para mm e executa o movimento em linha reta
        self.drive.settings(straight_speed=v_orig, straight_acceleration=a_orig)  # Restaura as configurações originais da base
        self.tempo()  # Imprime e regista o tempo decorrido após o movimento

    def girar(self, angulo_absoluto: float, velocidade: float = 300):  # Gira o robô para um ângulo giroscópico absoluto
        if not self.tracao_ok: return  # Cancela o giro se a tração não estiver pronta
        erro = angulo_absoluto - self.hub.imu.heading()  # Calcula a diferença entre o ângulo desejado e o rumo atual
        _, _, v_rot_orig, _ = self.drive.settings()  # Guarda a velocidade de rotação original
        self.drive.settings(turn_rate=velocidade)  # Define a nova velocidade angular de rotação
        self.drive.turn(erro)  # Executa o giro angular preciso para corrigir o erro
        self.drive.settings(turn_rate=v_rot_orig)  # Restaura a velocidade angular original
        self.tempo()  # Imprime e regista o tempo decorrido após o giro

    def girar_relativo(self, angulo_relativo: float, velocidade: float = 300):  # Gira o robô relativamente à posição atual
        if not self.tracao_ok: return  # Cancela o giro se a tração não estiver pronta
        rumo_atual = self.hub.imu.heading()  # Obtém o ângulo giroscópico atual do robô
        self.girar(rumo_atual + angulo_relativo, velocidade)  # Executa o giro somando o ângulo relativo ao rumo atual

    def alinhar_parede(self, tempo_ms: int = 1200, angulo_pos_alinhamento: float = 0, velocidade_re: float = -150):  # Alinha o robô contra uma parede
        if not self.tracao_ok: return  # Aborta se a tração não estiver operacional
        self.drive.drive(velocidade_re, 0)  # Aplica tração contínua para trás na velocidade de marcha-atrás
        wait(tempo_ms)  # Mantém a tração pressionada contra a parede durante o tempo especificado
        self.drive.stop()  # Para os motores de tração
        wait(50)  # Aguarda 50 milissegundos para o robô estabilizar na parede
        self.hub.imu.reset_heading(angulo_pos_alinhamento)  # Redefine a orientação do giroscópio para o valor indicado
        self.tempo()  # Imprime e regista o tempo decorrido após o alinhamento

    def mover_garra_a(self, graus: float, velocidade: float = 350, aceleracao: float = None, esperar: bool = True):  # Move a garra da porta A
        if not self.garra_a: return  # Aborta se o motor da garra A não estiver presente
        v_max_orig, a_max_orig = self.garra_a.control.limits()[:2]  # Salva os limites originais do motor da garra A
        if aceleracao is not None:  # Se uma aceleração foi especificada
            self.garra_a.control.limits(speed=abs(velocidade), acceleration=abs(aceleracao))  # Ajusta velocidade e aceleração
        else:  # Se apenas a velocidade foi informada
            self.garra_a.control.limits(speed=abs(velocidade))  # Ajusta apenas a velocidade do motor
        self.garra_a.run_angle(abs(velocidade), graus, then=Stop.HOLD, wait=esperar)  # Roda a garra A o número de graus especificado e segura no final
        self.garra_a.control.limits(speed=v_max_orig, acceleration=a_max_orig)  # Restaura os limites originais do motor
        if esperar: self.tempo()  # Imprime o tempo decorrido se esperou a conclusão do movimento

    def mover_garra_b(self, graus: float, velocidade: float = 350, aceleracao: float = None, esperar: bool = True):  # Move a garra da porta B
        if not self.garra_b: return  # Aborta se o motor da garra B não estiver presente
        v_max_orig, a_max_orig = self.garra_b.control.limits()[:2]  # Salva os limites originais do motor da garra B
        if aceleracao is not None:  # Se uma aceleração foi especificada
            self.garra_b.control.limits(speed=abs(velocidade), acceleration=abs(aceleracao))  # Ajusta velocidade e aceleração
        else:  # Se apenas a velocidade foi informada
            self.garra_b.control.limits(speed=abs(velocidade))  # Ajusta apenas a velocidade do motor
        self.garra_b.run_angle(abs(velocidade), graus, then=Stop.HOLD, wait=esperar)  # Roda a garra B o número de graus especificado e segura no final
        self.garra_b.control.limits(speed=v_max_orig, acceleration=a_max_orig)  # Restaura os limites originais do motor
        if esperar: self.tempo()  # Imprime o tempo decorrido se esperou a conclusão do movimento

    def gabarito_garra(self, porta: str = "A", velocidade: float = 300, limite_torque_mNm: float = 250, raio_cm: float = 4.0) -> bool:  # Calibra o ponto zero mecânico da garra
        garra = self.garra_a if porta.upper() == "A" else self.garra_b  # Seleciona o motor da garra A ou B conforme o argumento
        if not garra:  # Se a garra selecionada não estiver conectada
            print(f"[GABARITO] Garra {porta} não encontrada.")  # Avisa no terminal
            return False  # Retorna falso indicando erro na calibração
        print(f"[GABARITO] Calibrando Garra {porta} (Limite: {limite_torque_mNm} mN·m)...")  # Imprime aviso de início da calibração
        garra.run(velocidade)  # Liga o motor à velocidade definida para encontrar o batente mecânico
        cronometro_limite = StopWatch()  # Inicializa o cronómetro de segurança contra bloqueios
        while cronometro_limite.time() < 4000:  # Ciclo de verificação durante no máximo 4 segundos (timeout)
            torque_atual = abs(garra.load())  # Lê a carga de torque atual no motor em mN·m
            if torque_atual >= abs(limite_torque_mNm) or garra.stalled():  # Se atingiu o torque limite ou se o motor bloqueou
                garra.hold()  # Segura o motor na posição do batente físico
                garra.reset_angle(0)  # Redefine o encoder do motor para 0 graus no ponto mecânico
                forca_N = (torque_atual / 1000.0) / (raio_cm / 100.0) if raio_cm > 0 else 0  # Calcula a força em Newtons exercida no braço
                peso_g = (forca_N / 9.81) * 1000.0  # Estima o peso equivalente em gramas
                print(f"[GABARITO] Garra {porta} calibrada em 0°! Torque: {torque_atual} mN·m | Força: {forca_N:.2f} N | Peso Est.: {peso_g:.1f} g")  # Imprime telemetria
                self.tempo()  # Regista o tempo da operação
                return True  # Retorna verdadeiro indicando sucesso na calibração
            wait(20)  # Aguarda 20 milissegundos antes da próxima leitura de torque
        garra.stop()  # Desliga o motor caso atinja o tempo limite de segurança
        print(f"[GABARITO] Tempo limite excedido sem detetar ponto mecânico.")  # Avisa que houve timeout
        self.tempo()  # Regista o tempo da operação
        return False  # Retorna falso indicando falha na calibração

    def curva(self, raio_cm: float, angulo: float, velocidade: float = None):  # Executa uma curva em arco suave
        if not self.tracao_ok: return  # Aborta se a tração não estiver pronta
        v_orig, _, _, _ = self.drive.settings()  # Lê a velocidade original configurada na base
        v_exec = abs(velocidade) if velocidade is not None else v_orig  # Define a velocidade de curva ou usa a original
        raio_mm = raio_cm * 10.0  # Converte o raio de centímetros para milímetros
        self.drive.settings(straight_speed=v_exec)  # Ajusta a velocidade linear antes do movimento em curva
        self.drive.curve(radius=raio_mm, angle=angulo)  # Executa o arco com o raio e o ângulo especificados
        self.drive.settings(straight_speed=v_orig)  # Restaura a velocidade original da base
        self.tempo()  # Imprime e regista o tempo decorrido após a curva

    def checar_bateria(self) -> int:  # Monitoriza a tensão e nível da bateria do Hub
        tensao = self.hub.battery.voltage()  # Lê a tensão atual da bateria em milivolts (mV)
        porcentagem = max(0, min(100, int((tensao - 7200) / (8300 - 7200) * 100)))  # Calcula a percentagem da bateria com base na faixa operacional
        print(f"[TELEMETRIA] Tensão: {tensao}mV | Bateria: {porcentagem}%")  # Exibe a leitura de bateria no terminal
        if tensao < 7400:  # Se a tensão estiver abaixo do limite seguro de 7.4V
            self.hub.light.on(Color.RED)  # Liga a luz vermelha no Hub indicando alerta de bateria
            self.hub.speaker.beep(frequency=300, duration=800)  # Emite um aviso sonoro grave de bateria fraca
            print("[ALERTA] Bateria fraca!")  # Imprime aviso de alerta
        return porcentagem  # Retorna a percentagem de bateria

# Criação da instância global do robô e atalhos diretos para facilitar as chamadas nos módulos
bot = RoboMundial()  # Instancia a classe principal RoboMundial
largada = bot.largada  # Mapeia o comando de largada
perfil = bot.perfil  # Mapeia o comando de perfil
tempo = bot.tempo  # Mapeia a leitura de tempo
andar = bot.andar  # Mapeia o comando de andar reto
girar = bot.girar  # Mapeia o comando de girar absoluto
girar_relativo = bot.girar_relativo  # Mapeia o comando de girar relativo
alinhar_parede = bot.alinhar_parede  # Mapeia o alinhamento na parede
mover_garra_a = bot.mover_garra_a  # Mapeia a movimentação da garra A
mover_garra_b = bot.mover_garra_b  # Mapeia a movimentação da garra B
gabarito_garra = bot.gabarito_garra  # Mapeia a calibração de garra
checar_bateria = bot.checar_bateria  # Mapeia a verificação da bateria
curva = bot.curva  # Mapeia o comando de curva em arco
hub = bot.hub  # Mapeia o acesso direto ao Hub