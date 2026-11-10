from base import bot

def run():
    # Inicialização automática com perfil leve
    bot.preparar_largada(perfil="M1_LEVE")
    
    # Avanço direto e simples
    bot.andar(40)

if __name__ == "__main__":
    run()