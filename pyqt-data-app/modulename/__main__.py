"""
__main__.py

Module main code

Executed via python -m modulename
"""

import argparse

from .application import *

# Parse command line arguments
# Be careful not to step on anything Qt uses in their CLI args
# Anything defined here is passed blindly via kwargs until ApplicationNameDataModel.__init__()
parser = argparse.ArgumentParser( description="Skeleton code for a PyQT Data Application" )
parser.add_argument( "--mu",    type=int, help="Mean of random-normal data." )
parser.add_argument( "--sigma", type=int, help="Standard Deviation of random-normal data." )
kwargs = { k: v for k, v in vars( parser.parse_args() ).items() if v is not None }

# Create and run app
app = ApplicationName( **kwargs )
exit( app.exec_() )
