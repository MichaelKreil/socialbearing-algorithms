import math

def calculate_initial_compass_bearing(pointA, pointB):
    """
    Calculates the bearing between two points.
    The formulae used is the following:
        θ = atan2(sin(Δlong).cos(lat2),
                  cos(lat1).sin(lat2) − sin(lat1).cos(lat2).cos(Δlong))
    :Parameters:
      - `pointA: The tuple representing the latitude/longitude for the
        first point. Latitude and longitude must be in decimal degrees
      - `pointB: The tuple representing the latitude/longitude for the
        second point. Latitude and longitude must be in decimal degrees
    :Returns:
      The bearing in degrees
    :Returns Type:
      float
    """
    if (type(pointA) != tuple) or (type(pointB) != tuple):
        raise TypeError("Only tuples are supported as arguments")
    lat1 = math.radians(pointA[0])
    lat2 = math.radians(pointB[0])
    diffLong = math.radians(pointB[1] - pointA[1])
    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1)
            * math.cos(lat2) * math.cos(diffLong))
    initial_bearing = math.atan2(x, y)
    # Now we have the initial bearing but math.atan2 return values
    # from -180° to + 180° which is not what we want for a compass bearing
    # The solution is to normalize the initial bearing as shown below
    initial_bearing = math.degrees(initial_bearing)
    compass_bearing = (initial_bearing + 360) % 360
    return compass_bearing

def calculateBuoyPosition(bearing, lat1, lon1, dist, quadrant):
	if quadrant = 1
		alpha = 90.0 - bearing
		beta = 180.0 - (alpha + 90.0)
		lat3diff = dist * math.sin(beta)
		lon3diff = dist * math.sin(alpha)
		lat3 = lat1 + lat3diff
		lon3 = lon3 + lon3diff
	if quadrant = 2
		alpha = 180.0 - bearing
		beta = 180.0 - (alpha + 90.0)
		lat3diff = dist * math.sin(beta)
		lon3diff = dist * math.sin(alpha)
		lat3 = lat1 + lat3diff
		lon3 = lon3 - lon3diff
	if quadrant = 3
		alpha = 270.0 - bearing
		beta = 180.0 - (alpha + 90.0)
		lat3diff = dist * math.sin(beta)
		lon3diff = dist * math.sin(alpha)
		lat3 = lat1 - lat3diff
		lon3 = lon3 - lon3diff
	if quadrant = 4
		alpha = 360.0 - bearing
		beta = 180.0 - (alpha + 90.0)
		lat3diff = dist * math.sin(beta)
		lon3diff = dist * math.sin(alpha)
		lat3 = lat1 - lat3diff
		lon3 = lon3 + lon3diff
	buoyposition = lat3, lon3
	return buoyposition
	
"""
hier wird auf magische weise die variablen:
lat1, lon1, lat2, lon2, bearing1, bearing2 gefüllt. magnetic-declination-korrektur muss vorher diesem punkt passieren.
"""

pointA = (lat1,lon1,)
pointB = (lat2,lon2,)

alpha = math.fabs(bearing1 - bearing2) # Berechnung des Winkels zwischen den Schenkeln auf Seiten der Tonne a=|b1-b2|

distance = math.sqrt((lat1-lat2)^2 + (lon1-lon2)^2) # Berechnung der bewegten Distanz zwischen der ersten und zweiten Peilung

cog = calculate_initial_compass_bearing(pointA, pointB)

delta1 = math.fabs(cog - bearing1)
delta2 = math.fabs(cog - bearing2)


"""
das peildreieck ist nun definiert mit zwei winkeln und einer strecke.
distance ist die strecke
delta1 und delta2 sind die beiden winkel
"""

point1Dist = distance * math.sin(delta2) / math.sin(alpha) # berechnung der schenkellängen des peildreiecks für punkt 1
point2Dist = distance * math.sin(delta1) / math.sin(alpha) # und hier für punkt2


if bearing1 >= 0 and <= 90
	quadrant = 1
	justOneGuess = calculateBuoyPosition(bearing1, lat1, lon1, point1Dist, quadrant)
if bearing1 > 90 and <= 180
	quadrant = 2
	justOneGuess = calculateBuoyPosition(bearing1, lat1, lon1, point1Dist, quadrant)
if bearing1 > 180 and <= 270
	quadrant = 3
	justOneGuess = calculateBuoyPosition(bearing1, lat1, lon1, point1Dist, quadrant)
if bearing1 > 270 and <= 360
	quadrant = 4
	justOneGuess = calculateBuoyPosition(bearing1, lat1, lon1, point1Dist, quadrant)
if bearing2 >= 0 and <= 90
	quadrant = 1
	anotherGuess = calculateBuoyPosition(bearing2, lat2, lon2, point2Dist, quadrant)
if bearing2 > 90 and <= 180
	quadrant = 2
	anotherGuess = calculateBuoyPosition(bearing2, lat2, lon2, point2Dist, quadrant)
if bearing2 > 180 and <= 270
	quadrant = 3
	anotherGuess = calculateBuoyPosition(bearing2, lat2, lon2, point2Dist, quadrant)
if bearing2 > 270 and <= 360
	quadrant = 4
	anotherGuess = calculateBuoyPosition(bearing2, lat2, lon2, point2Dist, quadrant)

"""
et voila.. wir haben zwei (vermutlich, muss ich erst sehen!)verschiedene guesses auf die tonnenposition, eine von der ersten position und eine von der zweiten position
die stecken nun im tupel anotherGuess und im tupel justOneGuess

bisher ist dieser code mangels daten kein einziges mal gelaufenh
"""
