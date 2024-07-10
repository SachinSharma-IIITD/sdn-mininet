"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class NewTopology( Topo ):
    "Given topology."

    def build( self ):
        # Add switches
        switch_1 = self.addSwitch( 's1' )
        switch_2 = self.addSwitch( 's2' )
        switch_3 = self.addSwitch( 's3' )
        
        # Add hosts
        host_1 = self.addHost( 'h1' )
        host_2 = self.addHost( 'h2' )
        host_3 = self.addHost( 'h3' )
        host_4 = self.addHost( 'h4' )
        host_5 = self.addHost( 'h5' )
        host_6 = self.addHost( 'h6' )
        host_7 = self.addHost( 'h7' )
        host_8 = self.addHost( 'h8' )

        # Add links
        self.addLink( host_1, switch_1 )
        self.addLink( host_2, switch_1 )

        self.addLink( host_3, switch_2 )
        self.addLink( host_4, switch_2 )
        self.addLink( host_5, switch_3 )
        
        self.addLink( host_6, switch_3 )
        self.addLink( host_7, switch_3 )
        self.addLink( host_8, switch_3 )
        
        self.addLink( switch_1, switch_2 )
        self.addLink( switch_2, switch_3 )


topos = { 'newtopo': ( lambda: NewTopology() ) }
