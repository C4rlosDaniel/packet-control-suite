from src.firewall_simulator import FirewallSimulator
 
def test_default_allow():
    f = FirewallSimulator()
    assert f.check('1.2.3.4') == 'allow'

def test_block_rule():
    f = FirewallSimulator({'1.2.3.4': 'block'})
    assert f.check('1.2.3.4') == 'block'
