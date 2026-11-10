from base import *
from pybricks.tools import StopWatch

def run():
    cronometro = StopWatch()
    cronometro.resume()
    
    print("--- Iniciando Missão 2 ---")
    
    # Movimentos da missão
    andar(68, velocidade=1000)
    girar(-80, velocidade=1000)
    andar(4, velocidade=1000)
    girar(-15, velocidade=1000)
    andar(-1, velocidade=1000)
    girar(90, velocidade=1000)
    andar(-75, velocidade=1000)
    
    tempo_seg = cronometro.time() / 1000.0
    print("--- Missão 2 Concluída! ---")
    print("Tempo de execução: {:.2f} segundos\n".format(tempo_seg))

if __name__ == "__main__":
    run()