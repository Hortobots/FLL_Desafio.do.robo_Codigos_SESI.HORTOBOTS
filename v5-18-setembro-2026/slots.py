from pybricks.tools import hub_menu, StopWatch
from pybricks.parameters import Color
from base import bot

import m1, m2, m3, m4, m5

# Sequência padrão da mesa
SEQUENCIA = ["1", "2", "3", "4", "5"]
MISSOES = {
    "1": m1.run,
    "2": m2.run,
    "3": m3.run,
    "4": m4.run,
    "5": m5.run
}

posicao = 0
cronometro = StopWatch()

print("--- SISTEMA DE COMPETIÇÃO INICIADO ---")

while True:
    bot.hub.light.on(Color.BLUE) # LED azul indica aguardando acionamento
    
    # Reordena a fila para colocar a próxima missão no topo do visor
    ordem_menu = SEQUENCIA[posicao:] + SEQUENCIA[:posicao]
    escolha = hub_menu(*ordem_menu)
    
    if escolha in MISSOES:
        print(f"\n[SLOT {escolha}] Rodando missão...")
        cronometro.reset()
        cronometro.start()
        
        try:
            bot.hub.light.on(Color.GREEN)
            MISSOES[escolha]() # Executa a missão
            
            tempo = cronometro.time() / 1000.0
            print(f"[OK] Slot {escolha} concluído em {tempo:.2f}s")
            bot.hub.speaker.beep(frequency=600, duration=150)
            
            # Fila avança sozinha no visor
            posicao = (SEQUENCIA.index(escolha) + 1) % len(SEQUENCIA)
            
        except Exception as e:
            bot.hub.light.on(Color.RED)
            bot.hub.speaker.beep(frequency=200, duration=800)
            print(f"[ERRO NO SLOT {escolha}]:", e)