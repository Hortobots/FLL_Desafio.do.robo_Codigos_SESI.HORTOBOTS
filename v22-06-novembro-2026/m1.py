from base import *  # Importa todas as funções de movimento e controlo do módulo base

def run():  # Função principal de execução da missão 1
    largada("PESADO")  # Inicializa o giroscópio a 0° e aplica o perfil PESADO (Kp=31000, Kd=600, Vel=320, Acel=700)
    andar(-30, velocidade=1000, aceleracao=1000)  # Anda 30 cm para trás, velocidade=1000, aceleração=1000
    andar(10, velocidade=100, aceleracao=100)  # Anda 10 cm para a frente, velocidade=100, aceleração=100
    mover_garra_a(2200, velocidade=1000, aceleracao=1000, esperar=False)  # Mover garra A 2200 graus, velocidade=1000, aceleração=1000, sem esperar terminar
    andar(-9, velocidade=700, aceleracao=500)  # Anda 9 cm para trás, velocidade=700, aceleração=500
    wait(2500)  # Pausa de 2.5 segundos para aguardar a conclusão do movimento da garra
    curva(150, angulo=45)  # Faz uma curva com raio de 150 cm e ângulo de 45 graus

if __name__ == "__main__":  # Executa a função run se o ficheiro for chamado diretamente
    run()  # Inicia a missão 1