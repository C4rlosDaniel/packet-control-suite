# 🎭 Packet Control Suite — Ferramentas de Monitoramento e Análise de Rede

Conjunto de ferramentas modulares para monitoramento, filtragem e análise de tráfego de rede — com firewall simulado, sniffer, whitelist/blacklist e muito mais. Ideal para estudos, testes de segurança ou aplicações práticas em redes.

---

## 🚀 Funcionalidades Principais

-🔐 Simulação de firewall (filtragem de pacotes conforme regras definidas)

-📡 Monitoramento de portas e detecção de serviços ativos / vulnerabilidades

-🛰️ Sniffer de rede para captura e análise de pacotes de tráfego

-📋 Sistema de whitelist / blacklist para controle de acesso e filtragem

-🧩 Arquitetura modular e extensível — facilita manutenção e expansão

---
## 📂 Estrutura do Projeto

```
packet-control-suite/
├── README.md
├── .gitignore
├── configs/        # Arquivos de configuração 
├── src/            # Código-fonte principal
│   ├── __init__.py
│   ├── firewall.py
│   ├── monitor.py
│   ├── sniffer.py
│   ├── acl.py             # Whitelist / blacklist e controle de acesso
│   └── logger.py          # Logging estruturado
├── docs/           # Documentação adicional
├── tests/          # Testes unitários / de integração
└── main.py         # Script principal para rodar a suíte
```

## 📊 Diagrama de Fluxo — Uso Geral (ASCII)

```
 ┌───────────────────────────────┐
 │       Início do Programa      │
 └──────────────┬────────────────┘
                │
                ▼
 ┌───────────────────────────────┐
 │ Carrega configurações         │
 │ (whitelist / blacklist, portas, regras) │
 └──────────────┬────────────────┘
                │
                ▼
 ┌───────────────────────────────┐
 │ Inicializa módulos:           │
 │  • Firewall Simulator         │
 │  • Port Monitor               │
 │  • Network Sniffer            │
 │  • Logger / ACL               │
 └──────────────┬────────────────┘
                │
                ▼
 ┌───────────────────────────────┐
 │  Loop principal / Monitoramento │
 │  • Captura de pacotes         │
 │  • Verificação de regras      │
 │  • Registro de logs           │
 │  • Ações conforme ACL / regras│
 └──────────────┬────────────────┘
                │
                ▼
 ┌───────────────────────────────┐
 │  Saída / Resultado / Logs     │
 │  (alertas, relatórios, logs) │
 └───────────────────────────────┘
```

## 🛠️ Instalação e Execução
git clone https://github.com/C4rlosDaniel/packet-control-suite.git
cd packet-control-suite
# configurar ambiente virtual, se necessário
pip install -r requirements.txt

# Executar a suíte
python main.py

# 📄 Dependências

Python 3.x

Bibliotecas listadas no requirements.txt

## ⚠️ Atenção Para o Uso do Código
Caso utilize funcionalidades de sniffing ou manipulação de pacotes, execute com privilégios elevados (ex: sudo) ou como administrador, conforme o sistema operacional.

## 👨‍💻 Autor & Contato

Carlos Daniel da Silva Alencar
---
🔗 LinkedIn: https://www.linkedin.com/in/carlos-alencar-22b950353

🔗 GitHub: https://github.com/C4rlosDaniel

📖 Licença

Este projeto está distribuído sob MIT — veja o arquivo LICENSE para detalhes.
