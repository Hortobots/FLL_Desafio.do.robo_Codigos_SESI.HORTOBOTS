from base import bot

def run():
    # Perfil de alta velocidade para longa travessia
    bot.preparar_largada(perfil="M2_VELOZ")
    
    bot.andar(68)
    bot.girar_para(-80, velocidade=500)
    bot.andar(4)
    bot.girar_para(-95, velocidade=500)
    bot.andar(-1, velocidade=300) # Ajuste individual de velocidade para encaixe
    bot.girar_para(-5, velocidade=500)
    bot.andar(-75)

if __name__ == "__main__":
    run()