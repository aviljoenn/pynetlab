from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": "88newclass",
    "device_type": 'cisco_ios',
    # "session_log": 'my_session_log.txt',
}

device2 = {
    "host": 'nxos1.lasthop.io',
    "username": 'pyclass',
    "password": "88newclass",
    "device_type": 'cisco_nxos',
    # "session_log": 'my_session_log.txt',
}

for device in (device1,device2):
    net_connect = ConnectHandler(**device)
    print (net_connect.find_prompt())

output = net_connect.send_command("show version")
with open("send_text.txt","w") as f:
    f.write(output)

#print(device2.net_connect.find_prompt())
