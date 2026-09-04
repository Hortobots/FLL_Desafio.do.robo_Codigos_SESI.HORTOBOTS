from pybricks.tools import hub_menu
import m1
import m2
import base  # Só para garantir que a inicialização ocorra no boot

print("Sistema de Menu Iniciado. Aguardando seleção...")

while True:
    # O menu reaparece toda vez que uma missão termina
    selected = hub_menu("1", "2")
    
    if selected == "1":
        m1.run()
    elif selected == "2":
        m2.run()