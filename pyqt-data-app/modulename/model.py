"""
model.py

Data & behavior model code for ApplicationName

This is a trivial example which you will entirely blow away.
"""

import numpy as np

class ApplicationNameDataModel( object ):

    def __init__( self, mu=0, sigma=10 ):
        self.mu, self.sigma = mu, sigma

    def getNewData( self ):
        return np.random.normal( self.mu, self.sigma, 1000 )
