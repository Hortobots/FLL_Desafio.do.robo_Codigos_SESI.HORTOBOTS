from base import andar, girar, mover_garra_a, mover_garra_b
import base

def run():
    print("Iniciando Missão 2...")
    mover_garra_a(-360, velocidade=-10000)
    base.robo.stop()

# Permite rodar este arquivo diretamente para testes
if __name__ == "__main__":
    run()