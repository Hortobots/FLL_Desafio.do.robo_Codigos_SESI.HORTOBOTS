from pybricks.tools import hub_menu, StopWatch  # Importa a função de menu no ecrã do hub e o temporizador
from pybricks.parameters import Color  # Importa as cores do LED do Hub
from base import hub  # Importa a instância do Hub configurada no módulo base
import m1, m2, m3, m4, m5  # Importa os módulos de código das missões 1, 2, 3, 4 e 5

SEQUENCIA = ["1", "2", "3", "4", "5"]  # Lista com a ordem dos números de missões a exibir no menu
MISSOES = {  # Dicionário que associa a opção do menu à função de execução da respetiva missão
    "1": m1.run,  # Associa a opção 1 à função run() do módulo m1
    "2": m2.run,  # Associa a opção 2 à função run() do módulo m2
    "3": m3.run,  # Associa a opção 3 à função run() do módulo m3
    "4": m4.run,  # Associa a opção 4 à função run() do módulo m4
    "5": m5.run   # Associa a opção 5 à função run() do módulo m5
}

posicao = 0  # Inicializa o índice de navegação do menu no slot 0
cronometro = StopWatch()  # Inicializa o temporizador para medir a duração total de cada missão executada

while True:  # Ciclo principal de seleção do menu no robô
    hub.light.on(Color.BLUE)  # Acende a luz azul no Hub indicando que o menu está aguardando escolha
    
    ordem_menu = SEQUENCIA[posicao:] + SEQUENCIA[:posicao]  # Reordena a lista do menu para iniciar na posição atual
    escolha = hub_menu(*ordem_menu)  # Abre o menu interativo no visor do Hub para seleção com os botões
    
    if escolha in MISSOES:  # Se a opção escolhida pelo utilizador for válida
        print(f"\n[SLOT {escolha}] Executando...")  # Imprime aviso de início no terminal
        cronometro.reset()  # Reinicia o cronómetro para 0 ms antes de arrancar a missão
        
        try:  # Tenta executar a missão selecionada
            hub.light.on(Color.GREEN)  # Acende a luz verde no Hub indicando missão em andamento
            MISSOES[escolha]()  # Executa a rotina da missão selecionada no dicionário
            
            tempo = cronometro.time() / 1000.0  # Converte o tempo decorrido para segundos
            print(f"[OK] Slot {escolha} em {tempo:.2f}s")  # Imprime mensagem de sucesso e tempo de conclusão
            hub.speaker.beep(frequency=600, duration=150)  # Emite sinal sonoro agudo indicando conclusão bem-sucedida
            
            posicao = (SEQUENCIA.index(escolha) + 1) % len(SEQUENCIA)  # Avança automaticamente para o próximo slot na sequência
            
        except Exception as e:  # Captura falhas de execução durante a missão
            hub.light.on(Color.RED)  # Acende a luz vermelha no Hub indicando erro durante a missão
            hub.speaker.beep(frequency=200, duration=800)  # Emite sinal sonoro grave indicando falha
            print(f"[ERRO SLOT {escolha}]:", e)  # Imprime os detalhes do erro no terminal