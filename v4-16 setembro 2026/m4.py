from base import *
from pybricks.tools import StopWatch, wait

def run():
    cronometro = StopWatch()
    cronometro.resume()
    
    print("--- Iniciando Missão 1 ---")
    
    # 1. Posiciona a garra primeiro (esperando concluir para garantir o ponto inicial correto)
    mover_garra_b(-153.8, velocidade=300, esperar=True)
    
    # 2. Deslocamento principal da base
    andar(78, velocidade=1000, aceleracao=1200) # Mantém aceleração padrão saudável da base
    wait(50)

    # 3. Movimento sincronizado controlado (garra a 350 para torque máximo)
    mover_garra_b(180, velocidade=350, esperar=False) # Ajustado para um valor real de graus da garra
    
    # 3. Movimento sincronizado controlado (garra a 350 para torque máximo)
    mover_garra_b(1000, velocidade=1000, esperar=False) # Ajustado para um valor real de graus da garra
    andar(2.5, velocidade=500)
    
    tempo_seg = cronometro.time() / 1000.0
    print("--- Missão 1 Concluída! ---")
    print("Tempo de execução: {:.2f} segundos\n".format(tempo_seg))

if __name__ == "__main__":
    run()