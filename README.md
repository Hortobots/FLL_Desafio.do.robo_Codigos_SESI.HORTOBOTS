<div align="center">
  <h1>Projeto Robótica LEGO SPIKE Prime / Pybricks</h1>
  <p><strong>Este repositório contém a versão do código de controle e missões para robô LEGO SPIKE Prime utilizando Pybricks.</strong></p>
</div>

<hr/>

## Estrutura do Projeto

- **`base.py` / `backup/01_Base_Controle/`**: <br>Configuração central do robô (Hub, motores de tração com giroscópio PID, garras A e B, funções de movimentação `andar()`, `girar()`, `mover_garra_a()`, `mover_garra_b()`).
- **`slots.py` / `backup/04_Menu_Slots/`**: <br>Menu interativo executado no display do Hub para alternar rapidamente entre as missões durante a execução.

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

## Arquivos Compactados (.zip)

> O arquivo <code>backup_codigo_completo.zip</code> contém todos os módulos e suas documentações detalhadas organizadas por pasta.
