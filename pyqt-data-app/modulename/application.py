"""
application.py

General application code
"""

import sys

from PyQt5 import Qt, QtGui, QtWidgets, QtCore
import pyqtgraph as pg

from . import model

class ApplicationName( QtWidgets.QApplication ):
    """
    TODO: Document your application.
    """

    def __init__( self, *args, **kwargs ):
        """
        Initialize a new ApplicationName.
        """
        super( ApplicationName, self ).__init__( sys.argv )
        self.__configure( *args, **kwargs )
        self.__initUi()
        self.__initSignals()

    def __configure( self, *args, **kwargs ):
        """
        Parse and save any arguments given to this Application at creation.
        Create basic book-keeping objects.
        """
        self.data_model = model.ApplicationNameDataModel( *args, **kwargs )

    def __initUi( self ):
        """
        Create root window.
        """
        self.main_window = ApplicationNameMainWindow()

    def __initSignals( self ):
        """
        Initialize and/or connect application signals/slots
        """
        pass

class ApplicationNameMainWindow( QtWidgets.QMainWindow ):
    """
    QMainWindow for ApplicationName
    """

    def __init__( self ):
        """
        Build and show self.
        """
        super( ApplicationNameMainWindow, self ).__init__()
        self.__initWindow()
        self.__initWidgets()
        self.__initSignals()
        self.__initLayout()
        self.show()

    def __initWindow( self ):
        """
        Set basic window properties
        """
        self.setWindowTitle( "ApplicationName" )

    def __initWidgets( self ):
        """
        Create and configure widgets used in window layout.
        """
        self.plot_widget    = ApplicationNamePlotWidget()
        self.example_button = QtWidgets.QPushButton( "Plot Random Data" )

    def __initSignals( self ):
        """
        Connect or create any signals as needed.
        """
        self.example_button.clicked.connect( self.__onExampleButtonClick )

    def __initLayout( self ):
        """
        Set basic window layout and insert widgets into it.
        """

        # setup everything in a vertical box
        top_layout = QtWidgets.QVBoxLayout()
        central_widget = QtWidgets.QWidget()
        central_widget.setLayout( top_layout )
        self.setCentralWidget( central_widget )

        # add plot widget, then button underneath
        top_layout.addWidget( self.plot_widget )
        top_layout.addWidget( self.example_button )

    def __onExampleButtonClick( self ):
        """
        Slot for self.example_button.clicked
        """
        app = ApplicationName.instance()
        self.plot_widget.clear()
        self.plot_widget.plot( ApplicationName.instance().data_model.getNewData() ) # <- You'll want to devise a better API around this sort of thing in the body of ApplicationName above
        print( "That tickles!" )

class ApplicationNamePlotWidget( pg.PlotWidget ):
    """
    Subclass of pyqtgraph.PlotWidget with some changes that I personally prefer.
    """

    def __init__( self, *args, **kwargs ):
        """
        Call superclass init, but also setup some special settings.
        """
        super( ApplicationNamePlotWidget, self ).__init__( *args, **kwargs )
        self.showGrid( True, True )
