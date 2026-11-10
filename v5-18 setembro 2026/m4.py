from base import bot
from pybricks.tools import wait

def run():
    # Perfil suave para encaixes de precisão
    bot.preparar_largada(perfil="M4_PRECISAO")
    
    bot.mover_garra_b(-153.8, velocidade=300, esperar=True)
    bot.andar(78)
    wait(50)

    # Garra opera em segundo plano enquanto a base finaliza o movimento
    bot.mover_garra_b(180, velocidade=350, esperar=False)
    bot.andar(2.5, velocidade=200, aceleracao=400)

if __name__ == "__main__":
    run()