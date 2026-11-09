# 🤖 Hortobots — FLL Spike Prime (Temporada 2026)

Repositório oficial de software da equipe **Hortobots** para o robô de competição da **FIRST LEGO League (FLL)**. O projeto foi desenvolvido inteiramente em Python utilizando o ecossistema **Pybricks**, focado em máxima repetibilidade, velocidade nas transições da Base e precisão milimétrica nas missões.

---

## 🚀 Arquitetura de Software (Pybricks)

Diferente do ambiente de programação por blocos tradicional, o uso de Python direto no microcontrolador via Pybricks permite:
- **Controle de Atitude por Giroscópio (IMU):** Navegação com orientação absoluta na mesa, eliminando o acúmulo de erro angular ao longo do percurso.
- **Perfis Dinâmicos de PID:** Ajuste em tempo real dos ganhos $K_p$, $K_i$ e $K_d$ conforme a carga das garras (ex: perfil `PESADO` para lidar com centro de massa deslocado).
- **Curvas em Arco Contínuo:** Execução de manobras curvas em raio definido (`curva(raio_cm, angulo)`), economizando tempo em relação ao método clássico de "andar, parar, girar, andar".
- **Alinhamento Mecânico Passivo:** Re-calibração do zero do giroscópio no meio da mesa via *Wall Squaring* (`alinhar_parede`).

---

## 📁 O que cada arquivo faz

```text
.
├── base.py       # Núcleo cinemático (RoboMundial), PID dinâmico, IMU e controle de garras
├── slots.py      # Gerenciador de saídas oficial com menu interativo e cronômetro
├── saida7.py     # Rotina de alta precisão com curvas em arco e desengate de garra
├── m1.py a m7.py # Rotinas independentes de cada missão da mesa
├── forca.py      # Diagnóstico e telemetria de carga/torque nos motores em tempo real
├── test.py       # Rotinas de bancada para validação de motores e sensores
└── wasd.py       # Controle manual via Hub para calibrações rápidas na mesa
```

### Detalhamento dos Módulos:

* **`base.py`:** É o coração do robô. Instancia o Hub, motores de tração e motores auxiliares (garra A e garra B). Exporta funções globais limpas (`andar()`, `girar()`, `girar_relativo()`, `curva()`, `mover_garra_a()`, `mover_garra_b()`, `alinhar_parede()`), permitindo escrever missões legíveis e diretas.
* **`slots.py`:** Sistema de execução para os 2:30 minutos oficiais de rodada. Apresenta um menu de 1 clique no visor 5x5 do Hub Spike Prime, avança a fila de saídas automaticamente ao final de cada missão e exibe telemetria de tempo com feedback luminoso por LED (Azul = na Base aguardando; Verde = em missão; Vermelho = exceção capturada).
* **`saida7.py`:** Estratégia de saída com sequências de curvas em arco (`curva`) e manobras rápidas de soltura mecânica.
* **`m1.py` a `m7.py`:** Implementação isolada de cada missão/saída da equipe, com trajetórias, velocidades e ângulos ajustados para os modelos da mesa.
* **`forca.py`:** Ferramenta de engenharia para medir o torque exercido pelos motores nos mecanismos, auxiliando no projeto mecânico das garras.
* **`test.py` & `wasd.py`:** Utilitários para bancada e testes manuais de alinhamento e calibração de ângulo de largada.

---

## 🎮 Como Operar o Robô na Mesa

### Modo Competição (Rodadas Oficiais de 2:30 min)
1. Carregue e inicie o arquivo **`slots.py`** no Hub.
2. O visor LED exibirá o caractere da saída atual (`1`, `2`, `3`, `5`, `6`, `7`, `S`).
3. Posicione o robô na Base contra o gabarito e pressione o botão central do Hub para iniciar.
4. Ao término da missão, o robô emite um bipe de confirmação, registra o tempo no console e avança o menu automaticamente para o próximo slot, reduzindo o tempo de troca de acessórios pelos operadores de base.

### Modo de Treino e Ajuste Fino (Missão Individual)
Cada arquivo de missão possui o gatilho padrão do Python:
```python
if __name__ == "__main__":
    run()
```
Isso permite que os programadores testem e refinem uma única missão diretamente na bancada ou na mesa, executando o arquivo da missão (ex: `m7.py`) sem necessidade de abrir o menu geral.

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

- **v22 (06/Nov/2026):** Reestruturação geral com telemetria expandida no `base.py`, novo menu de slots (`1`, `2`, `3`, `5`, `6`, `7`, `S`), rotina de curvas `saida7.py` e rotinas completas de missões.
- **v21 (05/Nov/2026):** Adição da missão `m7.py` e consolidação de 7 rotinas independentes.
- **v20 (04/Nov/2026 - Tarde):** Refinamento de precisão nas missões `m1`, `m3`, `m6` e `saida7`.
- **v19 (04/Nov/2026 - Manhã):** Criação da estratégia `saida7.py` com curvas contínuas em arco.
- **v18 a v14 (Outubro/2026):** Evolução contínua das rotinas de missão `m4` e `m6`, sincronismo de garras e perfis de potência.
- **v12 a v10 (Outubro/2026):** Implementação do medidor de torque (`forca.py`), transição para 6 missões e primeiro sequenciador por slots.
- **v9 a v7 (Outubro/2026):** Adição de controle manual (`wasd.py`) e rotinas `m1` a `m5`.
- **v6 a v1 (Setembro/2026):** Versões iniciais de desenvolvimento, arquitetura modular base e calibração preliminar do IMU.
