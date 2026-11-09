# 🤖 FLL Spike Prime — Código de Competição (Pybricks)

Este repositório contém a arquitetura de software de alta precisão desenvolvida em Python (Pybricks) para o robô da equipe na **FIRST LEGO League (FLL)**. 

O sistema foi projetado focado em **repetibilidade, alta velocidade de execução e facilidade de operação** durante as rodadas oficiais de 2:30 minutos.

---

## 🌟 Principais Destaques do Código

* **Arquitetura Modular Limpa:** Separação entre a central de controle (`base.py`), missões individuais (`m1.py` a `m7.py`), rotina de saída (`saida7.py`) e gerenciador de execução (`slots.py`).
* **Troca Dinâmica de Perfis de PID (`perfil`):** Ajuste automático dos ganhos $K_p$, $K_i$ e $K_d$ de acordo com a carga física das garras (ex: perfil `PESADO` para combater desvios por centro de massa descompensado).
* **Navegação Absoluta por Bússola (`girar`):** Curvas calculadas com base no giroscópio interno (IMU), eliminando o acúmulo de erros angulares ao longo do percurso.
* **Alinhamento Passivo na Parede (`alinhar_parede`):** Re-calibração física do zero do giroscópio no meio da mesa usando o efeito *Wall Squaring*.
* **Menu de Avanço Automático (1-Clique):** Interface no visor Matrix do Hub que avança a fila de missões sozinha ao término de cada rotina, reduzindo o tempo de troca na Base.
* **Sintaxe Direta:** Exportação global de funções no `base.py` permitindo chamadas limpas como `andar(40)` ou `girar(-90)` sem necessidade de prefixos.

---

## 📁 Estrutura do Projeto

```text
.
├── base.py       # Classe principal (RoboMundial), gerenciador de PID, IMU e funções exportadas
├── forca.py      # Medidor em tempo real de carga, torque e peso estimado nos motores
├── m1.py a m7.py # Missões individuais do robô na mesa da competição
├── saida7.py     # Rotina especializada de posicionamento/saída da base
├── slots.py      # Menu sequenciador de missões no Hub com avanço automático e cronômetro
├── test.py       # Arquivo de testes para validação das funções do robô
└── wasd.py       # Controle manual do robô através do Hub (similar a controle de jogo)
```

---

## 🧭 Guia de Versionamento e Boas Práticas (Git na FLL)

Versionamento é um histórico com botão de voltar. Em vez de copiar a pasta e chamar de v12, o Git guarda cada mudança do mesmo projeto, com data e uma descrição do que você fez.

### 📌 Os 4 conceitos que você precisa:

- **Commit:** uma “foto” do projeto naquele momento, com uma mensagem. Ex.: `ajusta giro da m2 de 90 para 88`.
- **Branch:** uma linha paralela para testar uma ideia sem estragar a versão que funciona. Se der certo, você junta; se não, descarta.
- **Tag:** uma etiqueta numa versão importante. Ex.: `regional-2026`, o código exato que foi para a competição.
- **GitHub:** o armazenamento na nuvem do seu histórico. Git é a ferramenta, GitHub é o site.

### ⚡ O fluxo do dia a dia (4 comandos):

```bash
git status                       # o que mudou
git add .                        # separa o que vai entrar
git commit -m "ajusta giro da m2"
git push                         # envia para o GitHub
```

### 🛠️ Outros comandos úteis:

```bash
git log --oneline                # histórico resumido
git switch -c teste-pid          # cria uma branch para experimentar
git tag regional-2026            # marca uma versão
git push --tags                  # envia as tags
```

### 🏆 Aplicando na FLL:

- Faça um commit a cada ajuste que funcionou (ou que você quer lembrar), com mensagem clara. Suas anotações da tabela viram boas mensagens.
- Antes de uma competição, crie uma tag. Se algo quebrar depois, você volta para o código que funcionava.
- Para testar algo arriscado (um PID novo, por exemplo), use uma branch.

> [!TIP]
> **Uma regra que evita dor de cabeça:** commits pequenos e frequentes. Um commit gigante de “mudei tudo” é inútil quando você precisa achar o que quebrou.

---

## 📜 Histórico de Versões

- **v22-06-novembro-2026**: Grande reestruturação e expansão do sistema (base.py com telemetria avançada, slots.py otimizado, 7 missões m1-m7 e rotina saida7.py)
- **v21-05-novembro-2026**: Adição da missão m7.py (totalizando 7 rotinas com drible em saida7.py)
- **v20-04-novembro-2026-tarde**: Ajustes finos de precisão nas missões m1, m3, m6 e na rotina saida7.py
- **v19-04-novembro-2026**: Substituição da m4 anterior e criação do módulo dedicado saida7.py para nova estratégia
- **v18-03-novembro-2026**: Refinamento e aumento de alcance na rotina da missão m4
- **v17-30-outubro-2026-tarde**: Ajuste de curvas e sincronismo de garras na missão m4
- **v16-30-outubro-2026-manha**: Calibração fina de parâmetros e potências em m4 e m5
- **v15-29-outubro-2026**: Expansão das rotinas m4 e m5
- **v14-27-outubro-2026**: Expansão da rotina completa da missão m6 e ajustes em m4
- **v13-22-outubro-2026**: Ponto de checagem intermediário (registro de backup)
- **v12-21-outubro-2026**: Versão com 6 missões (m1-m6), nova rotina m6, menu por slots, medidor de força/torque, controle WASD e testes
- **v11-16-outubro-2026**: Versão com 5 missões (m1-m5), ajustes de precisão em base.py e trajetórias, menu por slots e medidor de força
- **v10-15-outubro-2026**: Versão com 5 missões (m1-m5), introdução do medidor de força/torque (forca.py), menu por slots e testes
- **v9-6-outubro-2026**: Versão com 5 missões (m1-m5), controle WASD e testes
- **v8-2-outubro-2026**: Versão com 5 missões, arquivo Bateria.py, controle WASD e testes
- **v7-1-outubro-2026**: Versão com 5 missões (m1-m5)
- **v6-21-setembro-2026**: Versão com 4 missões (m1-m4)
- **v5-18 setembro 2026**: Versão com 4 missões (m1-m4)
- **v4-16 setembro 2026**: Versão com 4 missões (m1-m4)
- **v3-10-setembro-2026**: Versão com 3 missões
- **v2-09-setembro-2026**: Versão anterior com 2 missões
- **v1-04-setembro-2026**: Versão inicial
