from pybricks.tools import hub_menu
import base

def run():
    print("Iniciando Missão 1...")
    # Vai e volta usando o PID estabilizado
    base.andar(-39, velocidade=1000)
    base.andar(50, velocidade=-1000)
    base.robo.stop()

# Permite rodar este arquivo diretamente para testes
if __name__ == "__main__":
    run()