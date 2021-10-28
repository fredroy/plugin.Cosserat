# -*- coding: utf-8 -*-
"""
The Cosserat plugin for SOFA: Templates Library Documentation
===============================================================

Utility functions and scene templates for the real-time simulation framework `SOFA <https://www.sofa-framework.org/>`_
and the `SoftRobots <https://project.inria.fr/softrobot/>`_ plugin.

The library can be used with scenes written in python and `PSL <https://github.com/sofa-framework/sofa/tree/master/applications/plugins/PSL>`_.

Contents of the library
**********************

.. autosummary::
    :toctree: _autosummary

    cosserat.cosseratObject
    cosserat.actuators
    cosserat.inverse
    cosserat.testScene
    

"""

from createFemRegularGrid import createFemCube
from usefulFunctions import BuildCosseratGeometry

__all__ = ["cosseratObject", "actuators", "scenes", "needle", "inverse"]
