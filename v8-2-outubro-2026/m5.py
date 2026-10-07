from base import *
from pybricks.tools import wait

def run():
    largada("VELOZ")
    andar(120, velocidade=800)
    andar(-120, velocidade=800)

if __name__ == "__main__":
    run()