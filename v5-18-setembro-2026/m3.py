from base import bot

def run():
    # Perfil focado em retorno rápido à Base
    bot.preparar_largada(perfil="M3_RETORNO")
    
    bot.andar(-72)
    bot.girar_para(-30, velocidade=400)
    bot.andar(-6)

if __name__ == "__main__":
    run()