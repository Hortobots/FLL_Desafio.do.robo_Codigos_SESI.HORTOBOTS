from base import *
from pybricks.tools import StopWatch

def run():
    cronometro = StopWatch()
    cronometro.resume()
    
    print("--- Iniciando Missão 3 ---")
    
         # Movimentos da missão
    andar(-72, velocidade=1000)
    girar(-30, velocidade=1000)
    andar(-6, velocidade=1000) 
    
    tempo_seg = cronometro.time() / 1000.0
    print("--- Missão 3 Concluída! ---")
    print("Tempo de execução: {:.2f} segundos\n".format(tempo_seg))

if __name__ == "__main__":
    run()