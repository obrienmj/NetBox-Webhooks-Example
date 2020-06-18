#Import Nornir Plugins
from nornir import InitNornir
from nornir.plugins.functions.text import print_title, print_result
from nornir.plugins.tasks.networking import netmiko_send_config
import argparse

#Create Command Line Arguments
parser = argparse.ArgumentParser(description='Push configs to Devices.')
parser.add_argument('--switch', '-s', help='Name of the switch')
parser.add_argument('--interface', '-i', help='Interface Name')
parser.add_argument('--vlan', '-v', help='VLAN ID')
args = parser.parse_args()

#Initialize Nornir and Filter Inventory
nr = InitNornir(config_file="config.yaml")
device = nr.filter(name=args.switch)

#Assign creds to device
username = "cisco"
password = "cisco123"
nr.inventory.defaults.username = username
nr.inventory.defaults.password = password

#Run Task to Push Configuration
commands = ['interface ' + args.interface, 'switchport access vlan ' + args.vlan]

result = device.run(
    task=netmiko_send_config,
    config_commands=commands
)
