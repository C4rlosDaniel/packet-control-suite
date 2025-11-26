# Network Security Toolkit
 
Um repositório demonstrando uma evolução prática de ferramentas simples de segurança de rede (ferramentas educativas / POC).
Projetado para empresas mostrarem um pipeline de evolução: **simulador de firewall → detector por taxa de pacotes → gestor com listas (whitelist/blacklist)**.

## Estrutura do repositório
- `src/` - código fonte (módulos e scripts prontos para rodar)
- `configs/` - arquivos de configuração e listas (whitelist/blacklist)
- `tests/` - testes simples
- `.github/workflows/` - CI para rodar linters e testes
- `Dockerfile` - container para executar o monitor
- `requirements.txt` - dependências
- `docs/` - documentação e roadmap de evolução

## Como usar (local)
> Requer privilégios de root para capturar pacotes ou manipular iptables.

1. Crie um virtualenv e instale requisitos:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
2. Configure `configs/whitelist.txt` e `configs/blacklist.txt` conforme necessário.
3. Executar o monitor (exemplo):
   ```bash
   sudo python -m src.monitor
   ```

## Evolução demonstrada
- **v1 (simples)**: gerador de IPs e verificador local de regras (poC mostrado nas imagens originais).
- **v2 (sniffer)**: detector baseado em taxa de pacotes que aplica regras com `iptables` (requer root).
- **v3 (orquestração)**: leitura de listas (whitelist/blacklist), logging estruturado, testes e containerização.

## Aviso
Ferramentas deste repositório são **para fins educativos e de avaliação interna**. Use em redes controladas e com permissão. Manipular `iptables` e capturar pacotes sem autorização pode ser ilegal.
