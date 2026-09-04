# Projeto Robótica LEGO SPIKE Prime / Pybricks

Este repositório contém a versão do código de controle e missões para robô LEGO SPIKE Prime utilizando Pybricks.

## Estrutura do Projeto

- **`base.py` / `backup/01_Base_Controle/`**: Configuração central do robô (Hub, motores de tração com giroscópio PID, garras A e B, funções de movimentação `andar()`, `girar()`, `mover_garra_a()`, `mover_garra_b()`).
- **`m1.py` / `backup/02_Missao_1/`**: Rotina da Missão 1.
- **`m2.py` / `backup/03_Missao_2/`**: Rotina da Missão 2.
- **`slots.py` / `backup/04_Menu_Slots/`**: Menu interativo executado no display do Hub para alternar rapidamente entre as missões durante a execução.

## Mapeamento de Portas e Hardware

| Componente | Porta | Detalhes |
|---|---|---|
| Motor de Tração Esquerdo | **Porta E** | Invertido (Counterclockwise) |
| Motor de Tração Direito | **Porta D** | Padrão |
| Garra Motorizada A | **Porta A** | Acessório frontal/superior |
| Garra Motorizada B | **Porta B** | Acessório auxiliar |
| Giroscópio | **Hub Integrado** | PID configurado (Kp: -5000, Ki: -150, Kd: -300) |
| Rodas / Dimensões | Diâmetro: 58.1mm | Distância entre rodas: 110mm |

## Arquivos Compactados (.zip)

O arquivo `backup_codigo_completo.zip` contém todos os módulos e suas documentações detalhadas organizadas por pasta.
