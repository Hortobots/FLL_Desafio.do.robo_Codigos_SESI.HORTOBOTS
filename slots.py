from pybricks.tools import hub_menu, StopWatch
from pybricks.parameters import Color
from base import hub
import m1, m2, m3, m5, m6, m7, saida7

# Sequência das saídas/missões exibidas no display 5x5 do Hub
SEQUENCIA = ["1", "2", "3", "5", "6", "7", "S"]

# Mapeamento de cada caractere do menu para a função de execução da missão
MISSOES = {
    "1": m1.run,       # Saída 1: Missão 1
    "2": m2.run,       # Saída 2: Missão 2
    "3": m3.run,       # Saída 3: Missão 3
    "5": m5.run,       # Saída 5: Missão 5
    "6": m6.run,       # Saída 6: Missão 6
    "7": m7.run,       # Saída 7: Missão 7
    "S": saida7.run,   # Saída S: Rotina com curvas em arco
}

posicao = 0
cronometro = StopWatch()

while True:
    hub.light.on(Color.BLUE)  # Azul = Aguardando seleção na Base
    
    ordem_menu = SEQUENCIA[posicao:] + SEQUENCIA[:posicao]
    escolha = hub_menu(*ordem_menu)
    
    if escolha in MISSOES:
        print(f"\n[SLOT {escolha}] Executando...")
        cronometro.reset()
        
        try:
            hub.light.on(Color.GREEN)  # Verde = Missão em andamento
            MISSOES[escolha]()
            
            tempo = cronometro.time() / 1000.0
            print(f"[OK] Slot {escolha} finalizado em {tempo:.2f}s")
            hub.speaker.beep(frequency=600, duration=150)
            
            # Avança automaticamente para o próximo slot
            posicao = (SEQUENCIA.index(escolha) + 1) % len(SEQUENCIA)
            
        except Exception as e:
            hub.light.on(Color.RED)  # Vermelho = Falha na execução
            hub.speaker.beep(frequency=200, duration=800)
            print(f"[ERRO SLOT {escolha}]:", e)
