import uselect  # Importa biblioteca para escutar entrada de dados sem bloquear o sistema
import usys  # Importa biblioteca de sistema para ler entrada do terminal (stdin)
from pybricks.hubs import PrimeHub  # Importa a classe do Hub principal da LEGO Pybricks
from pybricks.pupdevices import Motor  # Importa a classe de controlo de Motores
from pybricks.parameters import Port, Direction, Color, Stop  # Importa configurações do robô
from pybricks.robotics import DriveBase  # Importa a classe de tração de rodas
from pybricks.tools import wait, StopWatch  # Importa temporizadores

hub = PrimeHub()  # Conecta ao Hub principal

motor_esq = Motor(Port.E, Direction.COUNTERCLOCKWISE)  # Motor esquerdo na porta E com rotação invertida
motor_dir = Motor(Port.D)  # Motor direito na porta D com rotação normal
drive = DriveBase(motor_esq, motor_dir, wheel_diameter=58.1, axle_track=110)  # Configura a base de tração do robô

try:  # Tenta inicializar os motores adicionais das garras
    garra_a = Motor(Port.A)  # Inicializa a garra A na porta A
    garra_b = Motor(Port.B)  # Inicializa a garra B na porta B
except:  # Se não encontrar as garras
    garra_a = None  # Garra A fica desativada
    garra_b = None  # Garra B fica desativada

hub.light.on(Color.GREEN)  # Luz verde no Hub indicando modo teleoperado ativo

poll = uselect.poll()  # Cria o objeto para escutar a porta de dados do terminal
poll.register(usys.stdin, uselect.POLLIN)  # Regista a entrada padrão do teclado no escutador

print("\n==========================================")  # Imprime o cabeçalho
print("     CONTROLE TELEOPERADO (AUTO-STOP)     ")  # Exibe o título do programa
print("==========================================")  # Delimitador
print(" Mantenha a tecla pressionada para mover:")  # Exibe instruções de condução
print(" W : Frente | S : Trás")  # Instruções de avanço e recuo
print(" A : Girar Esquerda | D : Girar Direita")  # Instruções de rotação
print(" (Solte a tecla e o robô para na hora!)")  # Alerta sobre o recurso de auto-stop
print("------------------------------------------")  # Linha divisória
print(" J / K  : Abrir/Fechar Garra A")  # Instruções de controlo da garra A
print(" N / M  : Abrir/Fechar Garra B")  # Instruções de controlo da garra B
print(" Q      : Sair")  # Instrução para terminar a aplicação
print("==========================================")  # Delimitador final
print("Clique na janela do Terminal abaixo para jogar!\n")  # Lembrete para selecionar a janela do terminal

VEL_LIN = 400     # Define a velocidade linear máxima para 400 mm/s
VEL_ROT = 1000    # Define a velocidade de rotação máxima para 1000 graus/s
TIMEOUT_MS = 250  # Define o limite de tempo sem sinal de tecla para acionar o auto-stop em 250 ms

relogio = StopWatch()  # Cria o temporizador para controlar o timeout do teclado
em_movimento = False  # Estado inicial de movimento definido como Falso

while True:  # Ciclo principal de escuta do teclado
    if poll.poll(10):  # Verifica se foi premida uma nova tecla nos últimos 10 ms
        tecla = usys.stdin.read(1).lower()  # Lê o carater premido no terminal e converte para minúscula

        if tecla in ['w', 's', 'a', 'd']:  # Se for uma tecla de movimentação da base
            relogio.reset()  # Reinicia o relógio de timeout do auto-stop
            em_movimento = True  # Marca que o robô está em movimento ativo

            if tecla == 'w':  # Tecla W
                drive.drive(VEL_LIN, 0)  # Move para a frente com velocidade linear=400
            elif tecla == 's':  # Tecla S
                drive.drive(-VEL_LIN, 0)  # Move para trás com velocidade linear=-400
            elif tecla == 'a':  # Tecla A
                drive.drive(0, -VEL_ROT)  # Gira para a esquerda com velocidade de rotação=-1000
            elif tecla == 'd':  # Tecla D
                drive.drive(0, VEL_ROT)  # Gira para a direita com velocidade de rotação=1000

        elif tecla == ' ':  # Tecla de Barra de Espaço
            drive.stop()  # Para os motores da base imediatamente
            em_movimento = False  # Marca o robô como parado

        elif tecla == 'j' and garra_a:  # Tecla J com garra A presente
            garra_a.run_angle(1000, 1000, then=Stop.HOLD, wait=False)  # Abre a garra A a 1000 graus, velocidade=1000, sem esperar
        elif tecla == 'k' and garra_a:  # Tecla K com garra A presente
            garra_a.run_angle(1000, -180, then=Stop.HOLD, wait=False)  # Fecha a garra A a -180 graus, velocidade=1000, sem esperar
        elif tecla == 'n' and garra_b:  # Tecla N com garra B presente
            garra_b.run_angle(1000, 180, then=Stop.HOLD, wait=False)  # Abre a garra B a 180 graus, velocidade=1000, sem esperar
        elif tecla == 'm' and garra_b:  # Tecla M com garra B presente
            garra_b.run_angle(1000, -180, then=Stop.HOLD, wait=False)  # Fecha a garra B a -180 graus, velocidade=1000, sem esperar

        elif tecla == 'q':  # Tecla Q para encerrar o programa
            drive.stop()  # Para a tração
            hub.light.on(Color.RED)  # Acende a luz vermelha no Hub
            print("\nControle encerrado.")  # Imprime mensagem de encerramento
            break  # Sai do ciclo principal

    # Sistema Auto-Stop: se o robô está andando e não recebe novas teclas há mais de 250ms, para automaticamente
    if em_movimento and relogio.time() > TIMEOUT_MS:  # Se passou do tempo limite sem sinal de tecla
        drive.stop()  # Trava o movimento da base de tração
        em_movimento = False  # Marca o estado como parado

    wait(10)  # Pequena pausa de 10 ms para não sobrecarregar o processador do Hub