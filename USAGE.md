# Uso rápido

- `src/firewall_simulator.py` - simula regras de firewall (sem necessidade de root)
- `src/sniffer.py` - captura pacotes ao vivo (requer scapy + root)
- `src/monitor.py` - versão integrada com whitelist/blacklist e modo dry-run

Para testar sem root, rode apenas o firewall_simulator ou execute monitor com `dry_run=True`.
