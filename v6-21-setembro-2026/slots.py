from pybricks.tools import hub_menu, StopWatch
from pybricks.parameters import Color
from base import hub

import m1, m2, m3, m4, m5

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

while True:
    hub.light.on(Color.BLUE)
    
    ordem_menu = SEQUENCIA[posicao:] + SEQUENCIA[:posicao]
    escolha = hub_menu(*ordem_menu)
    
    if escolha in MISSOES:
        print(f"\n[SLOT {escolha}] Executando...")
        cronometro.reset()
        cronometro.start()
        
        try:
            hub.light.on(Color.GREEN)
            MISSOES[escolha]()
            
            tempo = cronometro.time() / 1000.0
            print(f"[OK] Slot {escolha} em {tempo:.2f}s")
            hub.speaker.beep(frequency=600, duration=150)
            
            posicao = (SEQUENCIA.index(escolha) + 1) % len(SEQUENCIA)
            
        except Exception as e:
            hub.light.on(Color.RED)
            hub.speaker.beep(frequency=200, duration=800)
            print(f"[ERRO SLOT {escolha}]:", e)