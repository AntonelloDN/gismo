# create location
#
# Gismo is a plugin for GIS environmental analysis (GPL) started by Djordje Spasic.
#
# This file is part of Gismo.
#
# Copyright (c) 2019, Djordje Spasic <djordjedspasic@gmail.com>
# Gismo is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# Gismo is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
#
# The GPL-3.0+ license <http://spdx.org/licenses/GPL-3.0+>

"""
Use this component to construct a location based on latitude, longitude coordinates.
-
Provided by Gismo 0.0.3

    input:
        locationName_: A name of the location.
                       -
                       If nothing added to this input, "unknown location" will be used as default locationName_.
        latitude_: Location's latitude coordinate.
                   It ranges from -90 for locations south of equator, to 90 for locations above the equator.
                   -
                   If nothing added to this input, "40" will be used as default latitude_.
        longitude_: Location's longitude coordinate.
                    It ranges from -180 for locations west of Prime Meridian, to 180 for locations east of Prime Meridian.
                    -
                    If nothing added to this input, "0" will be used as default longitude_.
    
    output:
        readMe!: ...
        location: Joined string containing information about location's components: locationName, latitude, longitude, timeZone and elevation.
                  timeZone and elevation are always set to "0" as they do not affect Gismo components.
        
"""

ghenv.Component.Name = "Gismo_Create Location"
ghenv.Component.NickName = "CreateLocation"
ghenv.Component.Message = "VER 0.0.3\nJAN_29_2019"
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Gismo"
ghenv.Component.SubCategory = "0 | Gismo"
#compatibleGismoVersion = VER 0.0.3\nJAN_29_2019
try: ghenv.Component.AdditionalHelpFromDocStrings = "2"
except: pass

import scriptcontext as sc
import Grasshopper


def checkInputs(locationName, latitude, longitude):
    
    # check inputs
    if (locationName == None):
        locationString = None
        validInputData = False
        printMsg = "Please define the \"locationName_\" input."
        return location, validInputData, printMsg
    
    if (latitude == None):
        locationString = None
        validInputData = False
        printMsg = "Please define the \"latitude_\" input."
        return location, validInputData, printMsg
    elif (latitude < -90) or (latitude > 90):
        locationString = None
        validInputData = False
        printMsg = "\"latitude_\" input can not be larger than 90 nor smaller than -90."
        return location, validInputData, printMsg
    
    if (longitude == None):
        locationString = None
        validInputData = False
        printMsg = "Please define the \"latitude_\" input."
        return location, validInputData, printMsg
    elif (longitude < -180) or (longitude > 180):
        locationString = None
        validInputData = False
        printMsg = "\"longitude_\" input can not be larger than 180 nor smaller than -180."
        return location, validInputData, printMsg
    
    
    correctedLocationName = gismo_preparation.cleanString(locationName)  # removing "/", "\", " ", "," from locationName_
    
    timeZone = 0; elevation = 0  # default. These two inputs are not important for OSM and terrain components
    locationString = gismo_preparation.constructLocation(correctedLocationName, latitude, longitude, timeZone, elevation)
    
    
    validInputData = True
    printMsg = "ok"
    return locationString, validInputData, printMsg


level = Grasshopper.Kernel.GH_RuntimeMessageLevel.Warning  # [do not change this line 
if sc.sticky.has_key("gismoGismo_released"):
    validVersionDate, printMsg = sc.sticky["gismo_check"].versionDate(ghenv.Component)
    if validVersionDate:
        gismo_preparation = sc.sticky["gismo_Preparation"]()
        
        location, validInputData, printMsg = checkInputs(locationName_, latitude_, longitude_)
        if not validInputData:
            print printMsg
            ghenv.Component.AddRuntimeMessage(level, printMsg)
    else:
        print printMsg
        ghenv.Component.AddRuntimeMessage(level, printMsg)
else:
    printMsg = "First please run the Gismo Gismo component."
    print printMsg
    ghenv.Component.AddRuntimeMessage(level, printMsg)
