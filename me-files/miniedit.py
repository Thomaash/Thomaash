#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch)
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch)
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    h11 = net.addHost('h11', cls=Host, ip='10.0.0.16', defaultRoute=None)
    h16 = net.addHost('h16', cls=Host, ip='10.0.0.21', defaultRoute=None)
    h26 = net.addHost('h26', cls=Host, ip='10.0.0.18', defaultRoute=None)
    h23 = net.addHost('h23', cls=Host, ip='10.0.0.8', defaultRoute=None)
    h8 = net.addHost('h8', cls=Host, ip='10.0.0.12', defaultRoute=None)
    h13 = net.addHost('h13', cls=Host, ip='10.0.0.24', defaultRoute=None)
    h25 = net.addHost('h25', cls=Host, ip='10.0.0.19', defaultRoute=None)
    h17 = net.addHost('h17', cls=Host, ip='10.0.0.9', defaultRoute=None)
    h3 = net.addHost('h3', cls=Host, ip='10.0.0.10', defaultRoute=None)
    h10 = net.addHost('h10', cls=Host, ip='10.0.0.17', defaultRoute=None)
    h21 = net.addHost('h21', cls=Host, ip='10.0.0.20', defaultRoute=None)
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.11', defaultRoute=None)
    h15 = net.addHost('h15', cls=Host, ip='10.0.0.2', defaultRoute=None)
    h9 = net.addHost('h9', cls=Host, ip='10.0.0.3', defaultRoute=None)
    h19 = net.addHost('h19', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h24 = net.addHost('h24', cls=Host, ip='10.0.0.22', defaultRoute=None)
    h12 = net.addHost('h12', cls=Host, ip='10.0.0.13', defaultRoute=None)
    h5 = net.addHost('h5', cls=Host, ip='10.0.0.23', defaultRoute=None)
    h18 = net.addHost('h18', cls=Host, ip='10.0.0.4', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.5', defaultRoute=None)
    h7 = net.addHost('h7', cls=Host, ip='10.0.0.26', defaultRoute=None)
    h22 = net.addHost('h22', cls=Host, ip='10.0.0.14', defaultRoute=None)
    h20 = net.addHost('h20', cls=Host, ip='10.0.0.15', defaultRoute=None)
    h14 = net.addHost('h14', cls=Host, ip='10.0.0.6', defaultRoute=None)
    h6 = net.addHost('h6', cls=Host, ip='10.0.0.7', defaultRoute=None)
    h4 = net.addHost('h4', cls=Host, ip='10.0.0.25', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(s13, s11)
    net.addLink(s11, s4)
    net.addLink(s6, s11)
    net.addLink(s11, s3)
    net.addLink(s5, s11)
    net.addLink(s11, s8)
    net.addLink(s2, s1)
    net.addLink(s1, s9)
    net.addLink(s7, s1)
    net.addLink(s1, s12)
    net.addLink(s1, s10)
    net.addLink(s1, s13)
    net.addLink(h19, s4)
    net.addLink(h15, s4)
    net.addLink(h9, s4)
    net.addLink(h18, s6)
    net.addLink(s6, h2)
    net.addLink(h14, s3)
    net.addLink(s3, h6)
    net.addLink(h23, s3)
    net.addLink(s5, h17)
    net.addLink(h3, s8)
    net.addLink(s8, h1)
    net.addLink(h8, s8)
    net.addLink(s8, h12)
    net.addLink(h22, s2)
    net.addLink(s2, h20)
    net.addLink(h11, s9)
    net.addLink(s9, h10)
    net.addLink(h26, s7)
    net.addLink(s7, h25)
    net.addLink(h21, s12)
    net.addLink(s12, h16)
    net.addLink(h24, s12)
    net.addLink(s10, h5)
    net.addLink(h13, s10)
    net.addLink(s10, h4)
    net.addLink(h7, s10)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s13').start([])
    net.get('s12').start([])
    net.get('s5').start([])
    net.get('s11').start([])
    net.get('s8').start([])
    net.get('s2').start([])
    net.get('s10').start([])
    net.get('s4').start([])
    net.get('s1').start([])
    net.get('s9').start([])
    net.get('s6').start([])
    net.get('s3').start([])
    net.get('s7').start([])

    info( '*** Configuring switches\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

