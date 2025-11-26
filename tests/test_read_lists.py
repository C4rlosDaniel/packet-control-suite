from pathlib import Path
from src.monitor import read_ip_list
 
def test_read_ip_list(tmp_path):
    p = tmp_path / 'list.txt'
    p.write_text('1.1.1.1\n#comment\n2.2.2.2\n')
    s = read_ip_list(p)
    assert '1.1.1.1' in s
    assert '2.2.2.2' in s
