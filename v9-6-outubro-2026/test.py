from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Color, Stop
from pybricks.tools import wait

hub = PrimeHub()

# ---------------------------------------------------------
# ALTERE AQUI A PORTA QUE DESEJA TESTAR (Port.A, Port.B, etc.)
PORTA_PARA_TESTAR = Port.E
# ---------------------------------------------------------

print(f"\n==========================================")
print(f"   TESTANDO MOTOR NA PORTA {PORTA_PARA_TESTAR}")
print(f"==========================================")

try:
    # Conecta o motor na porta selecionada
    motor = Motor(PORTA_PARA_TESTAR)
    hub.light.on(Color.BLUE)
    
    # Reset do contador de graus do motor
    motor.reset_angle(0)
    
    # 1. Gira 1 volta para a frente
    print("-> Girando para FRENTE (360°)...")
    motor.run_angle(speed=500, rotation_angle=360, then=Stop.HOLD, wait=True)
    wait(500)
    
    # 2. Gira 1 volta para trás
    print("-> Girando para TRÁS (-360°)...")
    motor.run_angle(speed=500, rotation_angle=-360, then=Stop.HOLD, wait=True)
    wait(500)
    
    # 3. Leitura do encoder
    angulo_final = motor.angle()
    print(f"-> Leitura do Encoder: {angulo_final}°")
    
    # Sucesso
    hub.light.on(Color.GREEN)
    hub.speaker.beep(frequency=1000, duration=200)
    print(f"\n[OK] A porta {PORTA_PARA_TESTAR} e o motor estão funcionando perfeitamente!\n")

except Exception as e:
    # Falha (Motor desconectado ou mau contato)
    hub.light.on(Color.RED)
    hub.speaker.beep(frequency=200, duration=600)
    print(f"\n[ERRO] Não foi possível ler o motor na porta {PORTA_PARA_TESTAR}.")
    print("1. Verifique se o cabo está bem encaixado.")
    print("2. Confirme se a porta definida no código é a mesma do robô.")
    print("Detalhe do erro:", e, "\n")