###############################################################################
## Import Python
###############################################################################
import math


###############################################################################
## GIS Format Conversions
###############################################################################
def GPRMC2DegDec(lat, latDirn, lng, lngDirn):
    """Converts GPRMC formats (Decimal Minutes) to Degrees Decimal

    Eg.
    """
    x = float(lat[0:2]) + float(lat[2:]) / 60
    y = float(lng[0:3]) + float(lng[3:]) / 60

    if latDirn == 'S':
        x = -x
    if lngDirn == 'W':
        y = -y

    return x, y


def TinyGPS2DegDec(lat, lng):
    """Converts TinyGPS formats (Decimal Degrees to e-5) to Degrees Decimal

    Eg.
    """
    x = float(lat[:-5] + '.' + lat[-5:])
    y = float(lng[:-5] + '.' + lng[-5:])

    return x, y

###############################################################################
## Functions to convert miles to change in lat, long (approx)
###############################################################################
# Distances are measured in miles.
# Longitudes and latitudes are measured in degrees.
# Earth is assumed to be perfectly spherical.

earth_radius = 3960.0
degrees_to_radians = math.pi / 180.0
radians_to_degrees = 180.0 / math.pi


def ChangeInLatitude(miles):
    """Given a distance north, return the change in latitude."""

    return (miles / earth_radius) * radians_to_degrees


def ChangeInLongitude(lat, miles):
    """Given a latitude and a distance west, return the change in longitude."""

    # Find the radius of a circle around the earth at given latitude.
    r = earth_radius * math.cos(lat * degrees_to_radians)
    return (miles / r) * radians_to_degrees


def CalculateBoundingBox(lng, lat, miles):
    """"""

    latChange = ChangeInLatitude(miles)
    latSouth = lat - latChange
    latNorth = lat + latChange
    lngChange = ChangeInLongitude(lat, miles)
    lngWest = lng + lngChange
    lngEast = lng - lngChange
    return (lngWest, latSouth, lngEast, latNorth)
