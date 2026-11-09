from pybricks.hubs import PrimeHub  # Importa a classe do Hub principal da LEGO Pybricks
from pybricks.pupdevices import Motor  # Importa a classe de controlo de Motores
from pybricks.parameters import Port, Color, Stop  # Importa portas, cores do LED e modos de paragem
from pybricks.tools import wait  # Importa a função de espera

hub = PrimeHub()  # Inicializa a ligação com o Hub principal

PORTA_PARA_TESTAR = Port.E  # Define a porta E como a porta padrão a testar

print(f"\n==========================================")  # Imprime o delimitador superior no terminal
print(f"   TESTANDO MOTOR NA PORTA {PORTA_PARA_TESTAR}")  # Exibe a indicação da porta sob teste
print(f"==========================================")  # Imprime o delimitador inferior no terminal

try:  # Tenta executar a rotina de teste do motor
    motor = Motor(PORTA_PARA_TESTAR)  # Conecta o motor na porta selecionada
    hub.light.on(Color.BLUE)  # Acende a luz azul no Hub durante o teste
    
    motor.reset_angle(0)  # Define a contagem atual de graus do encoder para 0
    
    print("-> Girando para FRENTE (360°)...")  # Imprime mensagem do teste para a frente
    motor.run_angle(speed=500, rotation_angle=360, then=Stop.HOLD, wait=True)  # Gira 360 graus para a frente, velocidade=500, aguardando conclusão
    wait(500)  # Pausa de 500 ms para estabilização
    
    print("-> Girando para TRÁS (-360°)...")  # Imprime mensagem do teste para trás
    motor.run_angle(speed=500, rotation_angle=-360, then=Stop.HOLD, wait=True)  # Gira 360 graus para trás, velocidade=500, aguardando conclusão
    wait(500)  # Pausa de 500 ms para estabilização
    
    angulo_final = motor.angle()  # Lê o desvio/posição final do encoder após a ida e volta
    print(f"-> Leitura do Encoder: {angulo_final}°")  # Exibe a leitura de erro residual no encoder
    
    hub.light.on(Color.GREEN)  # Luz verde no Hub indicando sucesso no teste
    hub.speaker.beep(frequency=1000, duration=200)  # Beep sonoro de confirmação
    print(f"\n[OK] A porta {PORTA_PARA_TESTAR} e o motor estão funcionando perfeitamente!\n")  # Imprime confirmação no terminal

except Exception as e:  # Captura falhas de comunicação ou ausência de motor
    hub.light.on(Color.RED)  # Luz vermelha no Hub indicando erro no teste
    hub.speaker.beep(frequency=200, duration=600)  # Sinal sonoro grave de falha
    print(f"\n[ERRO] Não foi possível ler o motor na porta {PORTA_PARA_TESTAR}.")  # Avisa sobre a falha
    print("1. Verifique se o cabo está bem encaixado.")  # Dá dica de verificação de cabos
    print("2. Confirme se a porta definida no código é a mesma do robô.")  # Dá dica de verificação de porta
    print("Detalhe do erro:", e, "\n")  # Imprime o erro original detalhado