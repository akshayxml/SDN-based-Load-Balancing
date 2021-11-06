#!/usr/bin/python

'This is the topology for ACN project'
from import_topology import *

def topology():
    'Create a network and controller'
    net = Mininet(controller=RemoteController, switch=OVSKernelSwitch)
    protocolName = "OpenFlow13"

    c0 = net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)
    c1 = net.addController('c1', controller=RemoteController, ip='127.0.0.2', port=6654)
    
    info("*** Creating the nodes\n")
     
    h1 = net.addHost('h1', ip='10.0.0.1/24', position='10,10,0')
    h2 = net.addHost('h2', ip='10.0.0.2/24', position='20,10,0')
    
    switch1 = net.addSwitch('switch1', protocols=protocolName, position='12,10,0')
    switch2 = net.addSwitch('switch2', protocols=protocolName, position='15,20,0')
    switch3 = net.addSwitch('switch3', protocols=protocolName, position='18,10,0')
    switch4 = net.addSwitch('switch4', protocols=protocolName, position='14,10,0')
    switch5 = net.addSwitch('switch5', protocols=protocolName, position='16,10,0')
    switch6 = net.addSwitch('switch6', protocols=protocolName, position='14,0,0')
    switch7 = net.addSwitch('switch7', protocols=protocolName, position='16,0,0')
    switch8 = net.addSwitch('switch8', protocols=protocolName, position='16,0,2')
    switch9 = net.addSwitch('switch9', protocols=protocolName, position='16,0,3')

    
    info("*** Adding the Link\n")
    net.addLink(h1, switch1)
    net.addLink(switch1, switch2)
    net.addLink(switch1, switch4)
    net.addLink(switch1, switch6)
    net.addLink(switch2, switch3)
    net.addLink(switch4, switch5)
    net.addLink(switch5, switch3)
    net.addLink(switch6, switch7)
    net.addLink(switch7, switch3)
    net.addLink(switch7, switch9)
    net.addLink(switch8, switch5)
    net.addLink(switch3, h2)


    info("*** Starting the network\n")
    net.build()
    c0.start()
    switch1.start([c0])
    switch2.start([c0])
    switch3.start([c0])
    switch4.start([c0])
    switch5.start([c0])
    switch6.start([c0])
    switch7.start([c0])
    switch8.start([c1])
    switch9.start([c1])
    

    net.pingFull()
    
    info("*** Running the CLI\n")
    CLI( net )

    info("*** Stopping network\n")
    net.stop()


if __name__ == '__main__':
    setLogLevel('info')
    topology()
