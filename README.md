<div align="center">
  <p><strong>Este repositório contém a versão do código de controle e missões para robô LEGO SPIKE Prime utilizando Pybricks.</strong></p>
</div>

<hr/>

## Estrutura do Projeto

- **`base.py`**: <br>Configuração central do robô (Hub, motores de tração com giroscópio PID, garras A e B, funções de movimentação `andar()`, `girar()`, `mover_garra_a()`, `mover_garra_b()`).
- **`slots.py`**: <br>Menu interativo executado no display do Hub para alternar rapidamente entre as missões durante a execução.
- **`m1.py` - `m5.py`**: <br>Módulos das missões do robô.
- **`test.py`**: <br>Arquivo de testes para validação das funções do robô.
- **`wasd.py`**: <br>Controle manual do robô através do Hub (similar a controle de jogo).

<br/>

## Mapeamento de Portas e Hardware

| Componente | Porta | Detalhes |
|:---|:---:|:---|
| **Motor de Tração Esquerdo** | **Porta E** | Invertido *(Counterclockwise)* |
| **Motor de Tração Direito** | **Porta D** | Padrão |
| **Garra Motorizada A** | **Porta A** | Acessório frontal/superior |
| **Garra Motorizada B** | **Porta B** | Acessório auxiliar |
| **Giroscópio** | **Hub Integrado** | PID configurado *(Kp: -5000, Ki: -150, Kd: -300)* |
| **Rodas / Dimensões** | **Diâmetro:** 58.1mm | **Distância entre rodas:** 110mm |

<br/>

## Histórico de Versões

- **v9-6-outubro-2026**: Versão mais recente com 5 missões (m1-m5), controle WASD e testes
- **v3-10-setembro-2026**: Versão com 3 missões
- **v2-09-setembro-2026**: Versão anterior com 2 missões
- **v1-04-setembro-2026**: Versão inicial
