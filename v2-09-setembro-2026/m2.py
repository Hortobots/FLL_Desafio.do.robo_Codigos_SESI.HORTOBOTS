from base import *
from pybricks.tools import StopWatch

def run():
    cronometro = StopWatch()
    cronometro.resume()
    
    print("--- Iniciando Missão 2 ---")
    
    # Movimentos da missão
    andar_direto(69, velocidade=1000)
    girar(-89, velocidade=700)
    andar_direto(5, velocidade=1000)
    andar_direto(-5, velocidade=1000)
    girar(84, velocidade=1000)
    andar_direto(-70, velocidade=500) # Ré com velocidade positiva e segura
    
    tempo_seg = cronometro.time() / 1000.0
    print("--- Missão 2 Concluída! ---")
    print("Tempo de execução: {:.2f} segundos\n".format(tempo_seg))

if __name__ == "__main__":
    run()