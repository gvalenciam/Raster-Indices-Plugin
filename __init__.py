# -*- coding: utf-8 -*-
"""
/***************************************************************************
 RasterIndices
                                 A QGIS plugin
 This plugin calculates indices for raster images
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2020-06-22
        copyright            : (C) 2020 by Gerardo Valencia
        email                : gvalenciam@pucp.pe
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load RasterIndices class from file RasterIndices.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .raster_indices import RasterIndices
    return RasterIndices(iface)