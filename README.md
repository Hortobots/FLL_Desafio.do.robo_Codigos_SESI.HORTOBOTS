# 🤖 Hortobots — FLL Spike Prime (Temporada 2026)

Repositório oficial de software da equipe **Hortobots** para o robô de competição da **FIRST LEGO League (FLL)**. O projeto foi desenvolvido em Python utilizando o ecossistema **Pybricks**, estruturado de forma modular para facilitar o desenvolvimento, a calibração de missões e a operação ágil na Base.

---

## 🚀 Arquitetura de Software (Pybricks)

Diferente do ambiente de programação por blocos tradicional, o uso de Python direto no microcontrolador via Pybricks permite:
- **Controle de Atitude por Giroscópio (IMU):** Navegação com orientação absoluta na mesa com base no giroscópio interno do Hub.
- **Perfis Dinâmicos de PID:** Ajuste dos ganhos $K_p$, $K_i$ e $K_d$ conforme a carga das garras (ex: perfil `PESADO` para lidar com centro de massa deslocado).
- **Curvas em Arco Contínuo:** Execução de manobras curvas em raio definido (`curva(raio_cm, angulo)`), reduzindo pausas em relação ao método de parar e girar no próprio eixo.
- **Alinhamento Mecânico Passivo:** Re-calibração do zero do giroscópio na mesa através de alinhamento em anteparo ou parede (`alinhar_parede`).
- **Telemetria de Bateria:** Monitoramento de tensão (mV) e corrente (mA) na inicialização do Hub, prevenindo variações de desempenho por bateria baixa.

---

## 📁 O que cada arquivo faz

```text
.
├── base.py                   # Núcleo cinemático (RoboMundial), PID dinâmico, IMU e controle de garras
├── slots.py                  # Gerenciador de saídas oficial com menu interativo e cronômetro
├── saida7.py                 # Rotina com sequências de curvas em arco e desengate mecânico
├── m1.py a m7.py             # Rotinas independentes de cada missão da mesa
├── forca.py                  # Diagnóstico e telemetria de carga/torque nos motores em tempo real
├── test.py                   # Rotinas de bancada para validação de motores e sensores
├── wasd.py                   # Controle manual via Hub para calibrações rápidas na mesa
└── v1/ a v22/                # Pastas de histórico de evolução da temporada (evidências para os juízes)
```

### Detalhamento dos Módulos:

* **`base.py`:** Centraliza a cinemática do robô. Instancia o Hub, motores de tração e motores auxiliares (garra A e garra B). Exporta funções de conveniência (`andar()`, `girar()`, `girar_relativo()`, `curva()`, `mover_garra_a()`, `mover_garra_b()`, `alinhar_parede()`, `checar_bateria()`).
* **`slots.py`:** Sistema de execução para os 2:30 minutos oficiais de rodada. Apresenta menu interativo no visor 5x5 do Hub Spike Prime, avança a fila de saídas automaticamente ao final de cada missão e exibe telemetria de tempo com feedback luminoso por LED (Azul = na Base aguardando; Verde = em missão; Vermelho = exceção capturada).
* **`saida7.py`:** Estratégia de saída com sequências de curvas em arco (`curva`) e manobras de desengate mecânico.
* **`m1.py` a `m7.py`:** Implementação isolada de cada missão/saída da equipe, com trajetórias, velocidades e ângulos parametrizados.
* **`forca.py`:** Ferramenta de bancada para medir o torque exercido pelos motores nos mecanismos, auxiliando no projeto mecânico das garras.
* **`test.py` & `wasd.py`:** Utilitários para bancada e testes manuais de alinhamento de sensores, atuadores e calibração de ângulo de largada.
* **`v1/` a `v22/`:** Registros das 22 versões iterativas desenvolvidas durante a temporada, servindo de evidência comprobatória do processo de engenharia para a avaliação de Robot Design.

---

## 🎮 Como Operar o Robô na Mesa

### Modo Competição (Rodadas Oficiais de 2:30 min)
1. Carregue e inicie o arquivo **`slots.py`** no Hub.
2. O Hub executa a checagem de bateria (`checar_bateria`) e exibe o caractere da saída atual no visor LED (`1`, `2`, `3`, `5`, `6`, `7`, `S`).
3. Posicione o robô na Base contra o gabarito e pressione o botão central do Hub para iniciar.
4. Ao término da missão, o robô emite um bipe de confirmação, registra o tempo no console e avança o menu automaticamente para o próximo slot, otimizando o tempo de troca de acessórios pelos operadores de base.

### Modo de Treino e Ajuste Fino (Missão Individual)
Cada arquivo de missão possui o gatilho padrão do Python:
```python
if __name__ == "__main__":
    run()
```
Isso permite que os programadores testem e refinem uma única missão diretamente na bancada ou na mesa, executando o arquivo da missão (ex: `m7.py`) sem necessidade de abrir o menu geral.

---

## 🏅 Evidências do Processo de Engenharia (Para os Juízes da FLL)

Para demonstrar o ciclo de engenharia (Planejar ➔ Construir ➔ Testar ➔ Melhorar), o repositório mantém:
1. **Código Atual Ativo (Raiz):** Pronto para execução direta no robô.
2. **Pastas Datadas (`v1/` a `v22/`):** Evidência física de cada iteração, documentando desde os primeiros protótipos de 2 saídas em setembro até a arquitetura final de 7 saídas em novembro.
3. **Histórico do Git e Tags:** Linha do tempo auditável de cada ajuste com tags nos marcos principais (`v12-outubro`, `v22-oficial-novembro`).

---

## 🧭 Padrão de Versionamento da Equipe (Diretrizes Git)

Para manter a integridade do código e evitar perdas de versões estáveis durante a temporada, a equipe Hortobots adota as seguintes práticas:

### 1. Commits Pequenos e Frequentes
Em vez de commits gigantes que misturam alterações de várias missões, cada ajuste testado na mesa deve gerar um commit focado com mensagem descritiva:
```bash
git add m7.py
git commit -m "fix(m7): ajusta angulo de saida para 24 graus e reduz velocidade de aproximacao"
```

### 2. Uso de Branches para Experimentações
Quando for testar uma mecânica nova, outro perfil de PID ou uma trajetória de risco, utilize uma branch dedicada para não interferir na versão homologada:
```bash
git switch -c teste-arco-saida7   # Cria e entra na branch de teste
# Realiza os testes na mesa...
# Se aprovado, une à main; se não, descarta sem afetar o robô principal.
```

### 3. Tags para Congelar Versões de Competição
Antes de cada etapa classificatória, regional ou torneio oficial, crie uma tag fixa para congelar o código exato que competiu:
```bash
git tag regional-2026
git push --tags
```

---

## 📜 Histórico Consolidado da Temporada

- **v22 (06/Nov/2026) - Tag `v22-oficial-novembro`:** Versão atual na raiz com 7 saídas, telemetria de bateria, slots otimizado e rotinas completas de missões.
- **v21 (05/Nov/2026):** Adição da missão `m7.py` e consolidação de 7 rotinas independentes.
- **v20 (04/Nov/2026 - Tarde):** Refinamento de precisão nas missões `m1`, `m3`, `m6` e `saida7`.
- **v19 (04/Nov/2026 - Manhã):** Criação da estratégia `saida7.py` com curvas contínuas em arco.
- **v18 a v14 (Outubro/2026):** Evolução contínua das rotinas de missão `m4` e `m6`, sincronismo de garras e perfis de potência.
- **v12 a v10 (Outubro/2026) - Tag `v12-outubro`:** Implementação do medidor de torque (`forca.py`), transição para 6 missões e primeiro sequenciador por slots.
- **v9 a v7 (Outubro/2026):** Adição de controle manual (`wasd.py`) e rotinas `m1` a `m5`.
- **v6 a v1 (Setembro/2026):** Versões iniciais de desenvolvimento, arquitetura modular base e calibração preliminar do IMU.
