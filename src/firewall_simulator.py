"""Firewall simulator / rule checker (v1)
Este módulo implementa uma verificação simples de regras locais. Útil para demonstração.
"""

from typing import Dict


class FirewallSimulator:
    def __init__(self, rules: Dict[str, str] = None):
        # rules: ip -> action ('block'|'allow')
        self.rules = rules or {}

    def check(self, ip: str) -> str:
        """Retorna a ação para um IP: 'block' ou 'allow'."""
        return self.rules.get(ip, 'allow')

    def add_rule(self, ip: str, action: str):
        self.rules[ip] = action

    def remove_rule(self, ip: str):
        self.rules.pop(ip, None)


def generate_random_ip(seed: int = None):
    import random
    if seed is not None:
        random.seed(seed)
    return f"192.168.1.{random.randint(0, 250)}"


if __name__ == '__main__':
    f = FirewallSimulator({
        '192.168.1.1': 'block',
        '192.168.1.4': 'block',
    })
    for _ in range(10):
        ip = generate_random_ip()
        print(ip, f.check(ip))
