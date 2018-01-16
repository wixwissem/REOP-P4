"""Custom topology
topology 2 
"""

from mininet.topo import Topo

class MyTopo(Topo):
	"Topology 2 of REOP Project."
	def __init__(self):
		"Create custom topo."

		# Initialize topology
		Topo.__init__(self)

		# Add hosts and switches
		leftHost = self.addHost( 'h1' )
		rightHost = self.addHost( 'h2' )
		leftSwitch = self.addSwitch( 'sw0' )
		rightSwitch = self.addSwitch( 'sw1' )
		sw11 = self.addSwitch ( 'sw11' )
		sw12 = self.addSwitch ( 'sw12' )
		sw13 = self.addSwitch ( 'sw13' )
		sw21 = self.addSwitch ( 'sw21' )
		sw22 = self.addSwitch ( 'sw22' )
		sw23 = self.addSwitch ( 'sw23' )
		sw31 = self.addSwitch ( 'sw31' )
		sw32 = self.addSwitch ( 'sw32' )
		sw33 = self.addSwitch ( 'sw33' )

		# Add Links 
		self.addLink(leftSwitch, sw11 )
		self.addLink(sw11, sw12 )
		self.addLink(sw12, sw13 )
		self.addLink(sw13, rightSwitch )
		self.addLink(leftSwitch, sw21 )
		self.addLink(sw21, sw22 )
		self.addLink(sw22, sw23 )
		self.addLink(sw23, rightSwitch )
		self.addLink(leftSwitch, sw31 )
		self.addLink(sw31, sw32 )
		self.addLink(sw32, sw33 )
		self.addLink(sw33, rightSwitch )
		self.addLink(leftHost, leftSwitch )
		self.addLink(rightSwitch, rightHost)
 
topos = { 'mytopo': ( lambda: MyTopo() ) }
	
