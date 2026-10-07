# 🤖 FLL Spike Prime — Código de Competição (Pybricks)

Este repositório contém a arquitetura de software de alta precisão desenvolvida em Python (Pybricks) para o robô da equipe na **FIRST LEGO League (FLL)**. 

O sistema foi projetado focado em **repetibilidade, alta velocidade de execução e facilidade de operação** durante as rodadas oficiais de 2:30 minutos.

---

## 🌟 Principais Destaques do Código

* **Arquitetura Modular Limpa:** Separação entre a central de controle (`base.py`), missões individuais (`m1.py` a `m5.py`) e gerenciador de execução (`main.py`).
* **Troca Dinâmica de Perfis de PID (`perfil`):** Ajuste automático dos ganhos $K_p$, $K_i$ e $K_d$ de acordo com a carga física das garras (ex: perfil `PESADO` para combater desvios por centro de massa descompensado).
* **Navegação Absoluta por Bússola (`girar`):** Curvas calculadas com base no giroscópio interno (IMU), eliminando o acúmulo de erros angulares ao longo do percurso.
* **Alinhamento Passivo na Parede (`alinhar_parede`):** Re-calibração física do zero do giroscópio no meio da mesa usando o efeito *Wall Squaring*.
* **Menu de Avanço Automático (1-Clique):** Interface no visor Matrix do Hub que avança a fila de missões sozinha ao término de cada rotina, reduzindo o tempo de troca na Base.
* **Sintaxe Direta:** Exportação global de funções no `base.py` permitindo chamadas limpas como `andar(40)` ou `girar(-90)` sem necessidade de prefixos.

---

## 📁 Estrutura do Projeto

```text
.
├── base.py       # Classe principal (RoboMundial), gerenciador de PID e funções exportadas
├── m1.py         # Missão 1 - Avanço rápido / Teste de Base
├── m2.py         # Missão 2 - Travessia de alta velocidade
├── m3.py         # Missão 3 - Retorno emergencial / rápido à Base
├── m4.py         # Missão 4 - Encaixe de precisão com acionamento assíncrono de garra
├── m5.py         # Missão 5 - "Reaching Roots" (PID reforçado para garras pesadas)
├── main.py       # Menu principal do Hub e sequenciador de rodada
├── test.py       # Arquivo de testes para validação das funções do robô
└── wasd.py       # Controle manual do robô através do Hub (similar a controle de jogo)
```

---

## 📜 Histórico de Versões

- **v9-6-outubro-2026**: Versão mais recente com 5 missões (m1-m5), controle WASD e testes
- **v8-2-outubro-2026**: Versão com 5 missões, arquivo Bateria.py, controle WASD e testes
- **v7-1-outubro-2026**: Versão com 5 missões (m1-m5)
- **v6-21-setembro-2026**: Versão com 4 missões (m1-m4)
- **v5-18 setembro 2026**: Versão com 4 missões (m1-m4)
- **v4-16 setembro 2026**: Versão com 4 missões (m1-m4)
- **v3-10-setembro-2026**: Versão com 3 missões
- **v2-09-setembro-2026**: Versão anterior com 2 missões
- **v1-04-setembro-2026**: Versão inicial
