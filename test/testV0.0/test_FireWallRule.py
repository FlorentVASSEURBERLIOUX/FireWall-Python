# Import de la classe FirewallRule
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))
from FirewallRule import FirewallRule


# Test de base pour une règle de pare-feu
def test_rule1():
    rule = FirewallRule("192.168.1.1", "192.168.1.2", "80", "tcp", "ACCEPT")
    rule.to_command()
    command = rule.get_command()
    expected_command = "iptables -A INPUT -s 192.168.1.1 -d 192.168.1.2 -p tcp --dport 80 -j ACCEPT"

    assert command == expected_command, f"Test 1 KO : Commande attendue {expected_command}, mais obtenue {command}"
    print("Test 1 OK")

def test_rule2():
    rule = FirewallRule(src_ip="8.8.8.8", dest_ip="8.8.4.4", port="53", protocol="udp", action="ACCEPT")
    command = rule.get_command()
    assert command is None, "Test 2 KO : La commande ne devrait pas être définie sans appel à `to_command`."
    print("Test 2 OK")