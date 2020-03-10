#GENERAL AND VESSEL RELATED EVENT DATA

''' E1000 General Event Data
Line name [ 7,22] A16
Shot/Event number [24,31] I8
Seismic record identifier [33,48] A16
Year,month,day [50,57] I4,I2,I2 YYYYMMDD
Time [59,66] I2,I2,F4.1 HH,MM,SS.S
Gun Array Fired [68,70] I3'''
class E1000:
    def __init__(self,lineName,shotNumber,seismicRecordId,date,time,gunArrayFired):
        self.lineName = lineName
        self.shotNumber = shotNumber
        self.seismicRecordId = seismicRecordId
        self.date = date
        self.time = time
        self.gunArrayFired = gunArrayFired

def getE1000(line):
    e1000 = E1000(line[6:22],line[23:31],line[32:48],line[49:57],line[58:66],line[67:70])
    return e1000

'''E12@0 Field Positioning Derived Data
@ = 1..9,Vessel reference number
Record sequence number [ 6,7] I2
Node identifier [ 8,11] I4
Flag for geographical or grid co-ordinates [12,12] I1 0 = geographical 1 = grid
If geographicals:
Latitude [13,24] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude [25,36] I3,I2,F6.3,A1 dddmmss.sss E/W
If grid:
Northing [13,23] N11
"N" [24,24] A1
Easting [25,35] N11
"E" [36,36] A1
Course made good or (nominal) ship's heading [37,42] F6.2 degrees decimal
Flag for course made good or ship's heading [43,43] I1 0 = course made good 1 = ship's heading
Quality indicator 1 [44,47] N4
Quality indicator 2 [48,51] N4
Quality indicator 3 [52,55] N4
Processing details [56,80] A25 free text'''
class E12x0:
    def __init__(self,vesselReferenceNumber,recordSequenceNumber,nodeIdentifier,flagCoordinates,latitude,longitude,northing,N,
    easting,E,courseShipsHeading,flagCourseShipsHeading,qualityIndicator1,qualityIndicator2,qualityIndicator3,processingDetails):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.recordSequenceNumber = recordSequenceNumber
        self.nodeIdentifier = nodeIdentifier
        self.flagCoordinates = flagCoordinates
        self.latitude = latitude
        self.longitude = longitude
        self.northing = northing
        self.N = N
        self.easting = easting
        self.E = E
        self.courseShipsHeading = courseShipsHeading
        self. flagCourseShipsHeading = flagCourseShipsHeading
        self.qualityIndicator1 = qualityIndicator1
        self.qualityIndicator2 = qualityIndicator2
        self.qualityIndicator3 = qualityIndicator3
        self.processingDetails = processingDetails

def getE12x0(line):
    e12x0 = E12x0(line[3:4],line[5:7],line[7:11],line[11:12],line[12:24],line[24:36],line[12:23],
    line[23:24],line[24:35],line[35:36],line[36:42],line[42:43],line[43:47],line[47:51],line[51:55],line[55:80])
    return e12x0

'''E14@0 Echo Sounder Data
@ = 1..9,Vessel reference number
Echo sounder ref. number [ 6,6] I1
Echo sounder reading [ 7,12] F6.1 metres
May be repeated for four more echo sounders mounted on the same vessel at [21,27],
[36,42],[51,57] and [66,72].'''
class E14x0:
    def __init__(self,vesselReferenceNumber,echoSounderReferenceNumber,echoSounderReading1,echoSounderReading2,
     echoSounderReading3,echoSounderReading4,echoSounderReading5):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.echoSounderReferenceNumber = echoSounderReferenceNumber
        self.echoSounderReading1 = echoSounderReading1
        self.echoSounderReading2 = echoSounderReading2
        self.echoSounderReading3 = echoSounderReading3
        self.echoSounderReading4 = echoSounderReading4
        self.echoSounderReading5 = echoSounderReading5

def getE14x0(line):
    e14x0 = E14x0(line[3:4],line[5:6],line[6:12],line[20:27],line[35,42],line[50:57],line[65:72])
    return e14x0

'''E16@0 USBL Acoustic Data
@ = 1..9,Vessel reference number
USBL system ref. number [ 6,6] I1
Target Node identifier [ 7,10] I4
X co-ordinate of target [11,17] N7 metres
Y co-ordinate of target [18,24] N7 metres
Z co-ordinate of target [25,31] N7 metres
Quality indicator [32,35] N4
May be repeated for one more USBL system mounted on the same vessel at [44,73].'''
class E16x0:
    def __init__(self,vesselReferenceNumber,systemReferenceNumber,targetNodeIdentifier,xCoordinate,yCoordinate,zCoordinate,qualityIndicator1,qualityIndicator2):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.systemReferenceNumber = systemReferenceNumber
        self.targetNodeIdentifier = targetNodeIdentifier
        self.xCoordinate = xCoordinate
        self.yCoordinate = yCoordinate
        self.zCoordinate = zCoordinate
        self.qualityIndicator = qualityIndicator1
        self.qualityIndicator = qualityIndicator2

def getE16x0(line):
    e16x0 = E16x0(line[3:4],line[5:6],line[6:10],line[10:17],line[17,24],line[24:31],line[31:35],line[43:73])
    return e16x0


#STREAMER EVENT DATA

'''E22@0 Streamer Compass Data
@ = 1..9,Vessel reference number
Streamer reference number [ 6,8] I3
Node identifier [ 9,12] I4
Compass reading [13,17] F5.1 degrees decimal
Quality indicator [18,21] N4
May be repeated for 4 more compasses on the same streamer at [22,34],[35,47],[48,60],[61,73]; the streamer reference number is not repeated.
Record may be repeated.'''
class E22x0:
    def __init__(self,vesselReferenceNumber,streamerReferenceNumber,nodeIdentifier,compassReading,qualityIndicator,compassReading2,compassReading3,compassReading4,compassReading5):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.streamerReferenceNumber = streamerReferenceNumber
        self.nodeIdentifier = nodeIdentifier
        self.compassReading = compassReading
        self.qualityIndicator = qualityIndicator
        self.compassReading2 = compassReading2
        self.compassReading3 = compassReading3
        self.compassReading4 = compassReading4
        self.compassReading5 = compassReading5

def getE22x0(line):
    e22x0 = E22x0(line[3:4],line[5:8],line[8:12],line[12:17],line[17,21],line[21:34],line[34:47],line[47:60],line[60:73])
    return e22x0

'''E24@1 Auxiliary Seismic Channel Data
@ = 1..9,Vessel reference number
Auxiliary channel reference number [ 6,9] I4
Time observed [10,17] N8 milliseconds
May be repeated for 5 more channels at [18,29] ... [66,77].'''
class E24x1:
    def __init__(self,vesselReferenceNumber,channelReferenceNumber,timeObserved):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.channelReferenceNumber = channelReferenceNumber
        self.timeObserved = timeObserved

def getE24x1(line):
    e24x1 = E24x1(line[3:4],line[5:9],line[9:77])
    return e24x1


#GUN ARRAY EVENT DATA

'''E32@0 Gun Array Depth Sensor Data
@ = 1..9,Vessel reference number
Gun array reference number [ 6,8] I3
Sensor reference number [ 9,10] I2
Depth reading [11,15] N5
Quality indicator [16,19] N4
May be repeated for 5 more depth sensors on the same gun array,at [20,30],[31,41] ...[64,74]; the gun array reference number is not repeated.
Record may be repeated.'''
class E32x0:
    def __init__(self,vesselReferenceNumber,gunArrayNumber,sensorNumber,depthReading,qualityIndicator,depthSensors):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.gunArrayNumber = gunArrayNumber
        self.sensorNumber = sensorNumber
        self.depthReading = depthReading
        self.qualityIndicator = qualityIndicator
        self.depthSensors = depthSensors
        
def getE32x0(line):
    e32x0 = E32x0(line[3:4],line[5:8],line[8:10],line[10:15],line[15:19],line[19:74])
    return e32x0

'''E33@0 Gun Fired Mask
@ = 1..9,Vessel reference number
Gun array reference number [ 6,8] I3
Starting gun number [ 9,11] I3
Guns fired mask [15,80] 66*I1 0 = not fired 1 = fired
Record may be repeated as necessary to define all guns that have fired on any event.'''
class E33x0:
    def __init__(self,vesselReferenceNumber,gunArrayNumber,gunNumber,gunsFiredMask):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.gunArrayNumber = gunArrayNumber
        self.gunNumber = gunNumber
        self.gunsFiredMask = gunsFiredMask
        
def getE33x0(line):
    e33x0 = E33x0(line[3:4],line[5:8],line[8:11],line[14:80])
    return e33x0

''' E34@0 Gun Pressure Sensor Data
@ = 1..9,Vessel reference number
Gun array reference number [ 6,8] I3
Gun number [ 9,11] I3
Pressure reading [12,17] N6
May be repeated for 7 more sensors in the same gun array at [18,26],[27,35],[36,44],[45,53],[54,62],[63,71],[72,80];
the gun array reference number is not repeated.'''
class E34x0:
    def __init__(self,vesselReferenceNumber,gunArrayNumber,gunNumber,p0,p1,p2,p3,p4,p5,p6,p7):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.gunArrayNumber = gunArrayNumber
        self.gunNumber = gunNumber
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4
        self.p5 = p5
        self.p6 = p6
        self.p7 = p7

def getE34x0(line):
    e34x0 = E34x0(line[3:4],line[4:8],line[7:11],line[10:17],line[16:26],line[25:35],line[35:44],line[44:53],line[53:62],line[62:71],line[71:80])
    return e34x0


#NETWORK EVENT DATA

'''E52## Network Observations
## = Observation type
Observation identifier [ 6,9] I4
Observation [10,19] N10
Quality indicator [20,23] N4
May be repeated at [31,48] and at [56,73] for two more observations:
- of the same observation type,and provided that:
- the observations were also observed at the same event time.
Record may be repeated.'''
class E52xy:
    def __init__(self,observationType,observationIdentifier,observation,qualityIndicator):
        self.observationType = observationType
        self.observationIdentifier = observationIdentifier
        self.observation = observation
        self.qualityIndicator = qualityIndicator
        
def getE52xy(line):
    e52xy = E52xy(line[3:5],line[5:9],line[9:19],line[19:73])
    return e52xy

'''E54## Network Observation Parameters
## = Observation type
Observation identifier [ 6,9] I4
Variable (C-O) [10,17] N8
C/O or propagation speed [18,29] N12
Flag for C/O or speed [30,30] I1 0 = C/O (=scale factor) 1 = propagation speed
May be repeated for one more set of observation parameters at [38,62]:
- relating to the same observation type,and provided that:
- the change in observation parameters relate to the same event time.
Record may be repeated.'''
class E54xy:
    def __init__(self,observationType,observationIdentifier,variable,propagationSpeed,flagSpeed, observation):
        self.observationType = observationType
        self.observationIdentifier = observationIdentifier
        self.variable = variable
        self.propagationSpeed = propagationSpeed
        self.flagSpeed = flagSpeed
        self.observation = observation
        
def getE54xy(line):
    e54xy = E54xy(line[3:5],line[5:9],line[9:17],line[17:29],line[29:30],line[30:62])
    return e54xy

'''E55## Network GPS Observations
## = Observation type
Observation ID [ 6,9] I4
Receiver time of receipt [10,23] I2,I2,HH,MM,F10.7 SS.sssssss
S.V. PRN [24,26] A1,I2 System type code,1 to 32
Observation [27,40] N14 metres,phase cycles or Hertz
Quality indicator [41,44] N4
Satellite health [45,46] I2 0 to 63
Lost Lock Indicator [47,47] I1 0 or 1
S.V. PRN [48,49] I2 1 to 32
Observation [50,63] N14 metres,phase cycles or Hertz
Quality indicator [64,67] N4
Satellite health [68,69] I2 0 to 63
Lost Lock Indicator [70,70] I1 0 to 7'''
class E55xy:
    def __init__(self,observationType,observationIdentifier,receiverTime,systemTypeCode,observation,qualityIndicator,satelliteHealth,lostLockIndicator,
    systemTypeCode2,observation2,qualityIndicator2,satelliteHealth2,lostLockIndicator2):
        self.observationType = observationType
        self.observationIdentifier = observationIdentifier
        self.receiverTime = receiverTime
        self.systemTypeCode = systemTypeCode
        self.observation = observation
        self.qualityIndicator = qualityIndicator
        self.satelliteHealth = satelliteHealth
        self.lostLockIndicator = lostLockIndicator
        self.systemTypeCode2 = systemTypeCode2
        self.observation2 = observation2
        self.qualityIndicator2 = qualityIndicator2
        self.satelliteHealth2 = satelliteHealth2
        self.lostLockIndicator2 = lostLockIndicator2
        
def getE55xy(line):
    e55xy = E55xy(line[3:5],line[5:9],line[9:23],line[23:26],line[26:40],line[40:44],line[44:46],line[46:47],line[47:49],line[49:63],line[63:67],line[67:69],line[69:70])
    return e55xy

'''E56## Network GPS Observations (continuation record)
## = Observation type
Observation ID [ 6,9] I4
S.V. PRN [10,11] I2 1 to 32
Observation [12,25] N14 metres,phase cycles or Hertz
Quality indicator [26,29] N4
Satellite health [30,31] I2 0 to 63
Lost Lock Indicator [32,32] I1 0 or 1
S.V. PRN [33,34] I2 1 to 32
Observation [35,48] N14 metres,phase cycles or Hertz
Quality indicator [49,52] N4
Satellite health [53,54] I2 0 to 63
Lost Lock Indicator [55,55] I1 0 or 1
S.V. PRN [56,57] I2 1 to 32
Observation [58,71] N14 metres,phase cycles or Hertz
Quality indicator [72,75] N4
Satellite health [76,77] I2 0 to 63
Lost Lock Indicator [78,78] I1 0 or 1'''
class E56xy:
    def __init__(self,observationType,observationIdentifier,systemTypeCode,observation,qualityIndicator,satelliteHealth,lostLockIndicator,
    systemTypeCode2,observation2,qualityIndicator2,satelliteHealth2,lostLockIndicator2,systemTypeCode3,observation3,qualityIndicator3,satelliteHealth3,lostLockIndicator3):
        self.observationType = observationType
        self.observationIdentifier = observationIdentifier
        self.systemTypeCode = systemTypeCode
        self.observation = observation
        self.qualityIndicator = qualityIndicator
        self.satelliteHealth = satelliteHealth
        self.lostLockIndicator = lostLockIndicator
        self.systemTypeCode2 = systemTypeCode2
        self.observation2 = observation2
        self.qualityIndicator2 = qualityIndicator2
        self.satelliteHealth2 = satelliteHealth2
        self.lostLockIndicator2 = lostLockIndicator2
        self.systemTypeCode3 = systemTypeCode3
        self.observation3 = observation3
        self.qualityIndicator3 = qualityIndicator3
        self.satelliteHealth3 = satelliteHealth3
        self.lostLockIndicator3 = lostLockIndicator3
        
def getE56xy(line):
    e56xy = E56xy(line[3:5],line[5:9],line[9:11],line[11:25],line[25:29],line[29:31],line[31:32],line[32:34],line[34:48],line[48:52],line[52:54],line[54:55],
    line[55:57],line[57:71],line[71:75],line[75:77],line[77:78])
    return e56xy


#SATELLITE POSITIONING EVENT DATA

'''E620# GPS or DGPS Data
# = 1,GPS # = 2,DGPS
"At" Node identifier [ 6,9] I4
Receiver reference number [10,10] I1
Latitude [11,22] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude [23,34] I3,I2,F6.3,A1 dddmmss.sss E/W
Height [35,40] F6.1 metres
Height datum [41,41] I1 0=height above ellipsoid 1=height above geoid (~MSL)
Satellites used [42,61] 10*I2 (GPS SV numbers)
Reference stations used [62,70] 9*I1
Position calculation mode [71,72] I2 see below'''
class E620x:
    def __init__(self,gpsType,nodeIdentifier,receiverNumber,latitude,longitude,height,heightDatum,satellitesUsed,
    referenceStationsUsed,positionCalculationMode):
        self.gpsType = gpsType
        self.nodeIdentifier = nodeIdentifier
        self.receiverNumber = receiverNumber
        self.latitude = latitude
        self.longitude = longitude
        self.height = height
        self.heightDatum = heightDatum
        self.satellitesUsed = satellitesUsed
        self.referenceStationsUsed = referenceStationsUsed
        self.positionCalculationMode = positionCalculationMode
        
def getE620x(line):
    e620x = E620x(line[4:5],line[5:9],line[9:10],line[10:22],line[22:34],line[34:40],line[40:41],line[41:61],line[61:70],line[70:72])
    return e620x

'''E621# GPS or DGPS Data (continued)
# = 1,GPS # = 2,DGPS
"At" Node identifier [ 6,9] I4
Receiver reference number [10,10] I1
Standard deviations of:
- Latitude: [11,15] N5 metres
- Longitude: [16,20] N5 metres
- Height: [21,25] N5 metres
DOP type [26,26] I1 0 = GDOP 1 = PDOP 2 = HDOP 3 = TDOP 4 = VDOP 5..9 = user defined on comment records
DOP figure [27,30] N4 unitless
The "DOP type" and "DOP figure" fields may be repeated for other DOPs or quality
indicators in columns [31,35] ... [51,55] as required.'''
class E621x:
    def __init__(self,gpsType,nodeIdentifier,receiverNumber,latitude,longitude,height,dopType,dopFigure,dops):
        self.gpsType = gpsType
        self.nodeIdentifier = nodeIdentifier
        self.receiverNumber = receiverNumber
        self.latitude = latitude
        self.longitude = longitude
        self.height = height
        self.dopType = dopType
        self.dopFigure = dopFigure
        self.dops = dops
        
def getE621x(line):
    e621x = E621x(line[4:5],line[5:9],line[9:10],line[10:15],line[15:20],line[20:25],line[25:26],line[26:30],line[30:55])
    return e621x

'''E6303 TRANSIT Satellite Data
"At" Node identifier [ 6,9] I4
Latitude [10,21] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude [22,33] I3,I2,F6.3,A1 dddmmss.sss E/W
Position includes dead reckoning? [34,34] I1 0 = no 1 = yes
Standard deviations of last accepted satellite fix:
- Latitude [35,39] N5 metres
- Longitude [40,44] N5 metres
Record may be repeated.'''
class E6303:
    def __init__(self,nodeIdentifier,latitude,longitude,positionDeadReckoning,latitudeDeviation,longitudeDeviation):
        self.nodeIdentifier = nodeIdentifier
        self.latitude = latitude
        self.longitude = longitude
        self.positionDeadReckoning = positionDeadReckoning
        self.latitudeDeviation = latitudeDeviation
        self.longitudeDeviation = longitudeDeviation
        
def getE6303(line):
    e6303 = E6303(line[5:9],line[9:21],line[21:33],line[33:34],line[34:39],line[39:44])
    return e6303

'''E640# Satellite Data (other systems)
# = 4..9,Satellite system reference number
"At" Node identifier [ 6,9] I4
Latitude [10,21] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude [22,33] I3,I2,F6.3,A1 dddmmss.sss E/W
Height [34,39] F6.1 metres
Height datum [40,40] I1 0 = height above ellipsoid 1 = height above geoid (~MSL)
Standard deviations of:
- Latitude: [41,45] N5 metres
- Longitude: [46,50] N5 metres
- Height: [51,55] N5 metres'''
class E640x:
    def __init__(self,satelliteSystemReferenceNumber,nodeIdentifier,latitude,longitude,height,heightDatum,latitudeDeviation,
    longitudeDeviation,heightDeviation):
        self.satelliteSystemReferenceNumber = satelliteSystemReferenceNumber
        self.nodeIdentifier = nodeIdentifier
        self.latitude = latitude
        self.longitude = longitude
        self.height = height
        self.heightDatum = heightDatum
        self.latitudeDeviation = latitudeDeviation
        self.longitudeDeviation = longitudeDeviation
        self.heightDeviation = heightDeviation
        
def getE640x(line):
    e640x = E640x(line[4:5],line[5:9],line[9:21],line[21:33],line[33:39],line[39:40],line[40:45],line[45:50],line[50:55])
    return e640x

'''E65## Differential correction data
## is the Differential Correction Source (DCS) Identifier.
Correction type [ 6,9] I4
Correction sequence [10,11] I2
GPS Time of Applicability [12,19] I2,I2,HH,MM,F4.1 SS.s 
DCS status/health [20,21] I2 0 to 7
IOD (Issue of data) key [22,24] I3 0-255
S.V. PRN [25,27] A1,I2
Value 1 [28,41] A14
Value 2 [42,55] A14
Value 3 [56,69] A14'''
class E65xx:
    def __init__(self,dcsIdentifier,correctionType,correctionSequence,gpsTime,dcsStatus,iodKey,svPRN,value1,value2,value3):
        self.dcsIdentifier = dcsIdentifier
        self.correctionType = correctionType
        self.correctionSequence = correctionSequence
        self.gpsTime = gpsTime
        self.dcsStatus = dcsStatus
        self.iodKey = iodKey
        self.svPRN = svPRN
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
    def __init__(self,dcsIdentifier,correctionType,correctionSequence,gpsTime,dcsStatus,iodKey,svPRN,freeText):
        self.dcsIdentifier = dcsIdentifier
        self.correctionType = correctionType
        self.correctionSequence = correctionSequence
        self.gpsTime = gpsTime
        self.dcsStatus = dcsStatus
        self.iodKey = iodKey
        self.svPRN = svPRN
        self.freeText = freeText
        
def getE65xx(line):
    correctionType = line[5:9]
    if (correctionType == "0016"):
        e65xx = E65xx(line[3:5],line[5:9],line[9:11],line[11:19],line[19:21],line[21:24],line[24:27],line[27:72])
    else:
        e65xx = E65xx(line[3:5],line[5:9],line[9:11],line[11:19],line[19:21],line[21:24],line[24:27],line[27:41],line[41:55],line[55:69])
    return e65xx

#USER DEFINED EVENT DATA

'''E7010 User Defined Observation Set Data
Observation set reference number [ 6,8] I3
Data field number [ 9,10] I2
Quality indicator [11,14] N4
Observation [15,.. ] Nx'''
class E7010:
    def __init__(self,observationReferenceNumber,dataFieldNumber,qualityIndicator,observation):
        self.observationReferenceNumber = observationReferenceNumber
        self.dataFieldNumber = dataFieldNumber
        self.qualityIndicator = qualityIndicator
        self.observation = observation

def getE7010(line):
    e7010 = E7010(line[5:8],line[8:10],line[10:14],line[14:80])
    return e7010

