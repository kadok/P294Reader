#INTER-EVENT VESSEL RELATED DATA

'''T14@0 Inter-event Echo Sounder Data
@ = 1..9,Vessel reference number
Echo sounder ref. number [ 6,6] I1
Echo sounder reading [ 7,12] F6.1 metres
Time of observation [13,19] I2,I2,I3 HH,MM,SSs
May be repeated for four more echo sounders mounted on the same vessel at [21,34],[36,49],[51,64] and [66,79]. Record may be repeated.'''
class T14x0:
    def __init__(self,vesselReferenceNumber,echoSounderNumber,echoSounderReading,timeObservation):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.echoSounderNumber = echoSounderNumber
        self.echoSounderReading = echoSounderReading
        self.timeObservation = timeObservation

def getT14x0(line):
    #Echo Sounder Lists
    refNumberList = []
    readingList = []
    timeObservationList = []

    for i in range(6,79,14):
        refNumberList.append(line[(i-1):(i)])
        readingList.append(line[(i+1):(i+6)])
        timeObservationList.append(line[(i+7):(i+13)])
    t14x0 = T14x0(line[3:4],refNumberList,readingList,timeObservationList)
    return t14x0

'''T16@0 Inter-event USBL Acoustic Data
@ = 1..9,Vessel reference number
USBL system ref. number [ 6,6] I1
To Node number [ 7,10] I4
X range to node [11,17] N7 metres
Y range to node [18,24] N7 metres
Z range to node [25,31] N7 metres
Quality indicator [32,35] N4
Time of observation [36,42] I2,I2,I3 HH,MM,SSs
May be repeated for one more USBL system mounted on the same vessel at [44,80]. Record may be repeated.'''
class T16x0:
    def __init__(self,vesselReferenceNumber,systemReferenceNumber,nodeNumber,xRangeNode,yRangeNode,zRangeNode,qualityIndicator,timeObservation):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.systemReferenceNumber = systemReferenceNumber
        self.nodeNumber = nodeNumber
        self.xRangeNode = xRangeNode
        self.yRangeNode = yRangeNode
        self.zRangeNode = zRangeNode
        self.qualityIndicator = qualityIndicator
        self.timeObservation = timeObservation

def getT16x0(line):
    #USBL Acoustic Lists
    uList = []
    uList.append(line[0:42])
    uList.append(line[38:80])
    t16x0 = T16x0(line[3:4],[uList[0][5:6],uList[1][5:6]],[uList[0][6:10],uList[1][6:10]],[uList[0][10:17],uList[1][10:17]],
    [uList[0][17:24],uList[1][17:24]],[uList[0][24:31],uList[1][24:31]],[uList[0][31:35],uList[1][31:35]],[uList[0][35:42],uList[1][35:42]])
    return t16x0

'''T17@0 Inter-event Pitch,Roll and Heave Sensor Data
@ = 1..9,Vessel reference number
Sensor reference number [ 6,6] I1
Pitch angle [ 7,16] N10
Roll angle [17,26] N10
Heave [27,36] N10
Quality indicator pitch [37,40] N4
Quality indicator roll [41,44] N4
Quality indicator heave [45,48] N4
Time of observation [49,55] I2,I2,I3 HH,MM,SSs'''
class T17x0:
    def __init__(self,vesselReferenceNumber,sensorReferenceNumber,pitchAngle,rollAngle,heave,
    qualityIndicatorPitch,qualityIndicatorRoll,qualityIndicatorHeave,timeObservation):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.sensorReferenceNumber = sensorReferenceNumber
        self.pitchAngle = pitchAngle
        self.rollAngle = rollAngle
        self.heave = heave
        self.qualityIndicatorPitch = qualityIndicatorPitch
        self.qualityIndicatorRoll = qualityIndicatorRoll
        self.qualityIndicatorHeave = qualityIndicatorHeave
        self.timeObservation = timeObservation

def getT17x0(line):
    t17x0 = T17x0(line[3:4],line[5:6],line[6:16],line[16:26],line[26:36],line[36:40],line[40:44],line[44:48],line[48:55])
    return t17x0


#INTER-EVENT NETWORK DATA

'''T52## Inter-event Network Data
## = Observation type
Observation Identifier [ 6,9] I4
Observation [10,19] N10
Quality indicator [20,23] N4
Time of observation [24,30] I2,I2,I3 HH,MM,SSs
May be repeated at [31,55] and at [56,80] for two more observations of the same observation type.'''
class T52xx:
    def __init__(self,observationType,observationIdentifier,observation,qualityIndicator,timeObservation):
        self.observationType = observationType
        self.observationIdentifier = observationIdentifier
        self.observation = observation
        self.qualityIndicator = qualityIndicator
        self.timeObservation = timeObservation

def getT52xx(line):
    #Observation Lists
    observationIdentifierList = []
    observationList = []
    qualityIndicatorList = []
    timeObservationList = []

    for i in range(6,80,25):
        observationIdentifierList.append(line[i-1:(i+3)])
        observationList.append(line[i+3:(i+13)])
        qualityIndicatorList.append(line[i+13:(i+17)])
        timeObservationList.append(line[i+17:(i+24)])
    t52xx = T52xx(line[3:4],observationIdentifierList,observationList,qualityIndicatorList,timeObservationList)
    return t52xx

'''T54## Inter-event Network Observation Parameters
## = Observation type
Observation Identifier [ 6,9] I4
Variable (C-O) [10,17] N8
C/O or propagation speed [18,29] N12
Flag for C/O or speed [30,30] I1 0 = C/O (=scale factor) 1 = propagation speed
Time of observation [31,37] I2,I2,I3 HH,MM,SSs
May be repeated for one more set of observation parameters at [38,69] relating to the same observation type.
Record may be repeated.'''
class T54xx:
    def __init__(self,observationType,observationIdentifier,variableCO,propagationSpeed,speedFlag,timeObservation):
        self.observationType = observationType
        self.observationIdentifier = observationIdentifier
        self.variableCO = variableCO
        self.propagationSpeed = propagationSpeed
        self.speedFlag = speedFlag
        self.timeObservation = timeObservation

def getT54xx(line):
    #Observation Lists
    oList = []
    oList.append(line[0:37])
    oList.append(line[32:69])
    t54xx = T54xx(oList[3:4],[oList[0][5:9],oList[1][5:9]],[oList[0][9:17],oList[1][9:17]],[oList[0][17:29],oList[1][17:29]],
    [oList[0][29:30],oList[1][29:30]],[oList[0][30:37],oList[1][30:37]])
    return t54xx

'''T55## Inter-event network GPS Observations
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
Lost Lock Indicator [70,70] I1 0 to 7
System Time of Receipt [71,77] I2,I2,I3 HH,MM,SSs'''
class T55xx:
    def __init__(self,observationType,observationIdentifier,receiverReceipt,systemTypeCode,observation,qualityIndicator,satelliteHealth,lockIndicator,
    systemTypeCode1,observation1,qualityIndicator1,satelliteHealth1,lockIndicator1,systemReceipt1):
        self.obeservationType = observationType
        self.observationIdentifier = observationIdentifier
        self.receiverReceipt = receiverReceipt
        self.systemTypeCode = systemTypeCode
        self.observation = observation
        self.qualityIndicator = qualityIndicator
        self.satelliteHealth = satelliteHealth
        self.lockIndicator = lockIndicator
        self.systemTypeCode1 = systemTypeCode1
        self.observation1 = observation1
        self.qualityIndicator1 = qualityIndicator1
        self.satelliteHealth1 = satelliteHealth1
        self.lockIndicator1 = lockIndicator1
        self.systemReceipt1 = systemReceipt1

def getT55xx(line):
    t55xx = T55xx(line[3:5],line[5:9],line[9:23],line[23:26],line[26:40],line[40:44],line[44:46],
    line[46:47],line[47:49],line[49:63],line[63:67],line[67:69],line[69:70],line[70:77])
    return t55xx

'''T56## Network GPS Observations (continuation record)
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
class T56xx:
    def __init__(self,observationType,observationIdentifier,systemTypeCode,observation,qualityIndicator,satelliteHealth,lockIndicator,
    systemTypeCode1,observation1,qualityIndicator1,satelliteHealth1,lockIndicator1,
    systemTypeCode2,observation2,qualityIndicator2,satelliteHealth2,lockIndicator2):
        self.obeservationType = observationType
        self.observationIdentifier = observationIdentifier
        self.systemTypeCode = systemTypeCode
        self.observation = observation
        self.qualityIndicator = qualityIndicator
        self.satelliteHealth = satelliteHealth
        self.lockIndicator = lockIndicator
        self.systemTypeCode1 = systemTypeCode1
        self.observation1 = observation1
        self.qualityIndicator1 = qualityIndicator1
        self.satelliteHealth1 = satelliteHealth1
        self.lockIndicator1 = lockIndicator1
        self.systemTypeCode2 = systemTypeCode2
        self.observation2 = observation2
        self.qualityIndicator2 = qualityIndicator2
        self.satelliteHealth2 = satelliteHealth2
        self.lockIndicator2 = lockIndicator2

def getT56xx(line):
    t56xx = T56xx(line[3:5],line[5:9],line[9:11],line[11:25],line[25:29],line[29:31],line[31:32],
    line[32:34],line[34:48],line[58:52],line[52:54],line[54:55],
    line[55:57],line[57:71],line[71:75],line[75:77],line[77:78])
    return t56xx


#INTER-EVENT SATELLITE DATA

'''T620# Inter-event GPS or DGPS Data
# = 1,GPS # = 2,DGPS
"At" Node identifier [ 6,9] I4
Receiver reference number [10,10] I1
Latitude [11,22] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude [23,34] I3,I2,F6.3,A1 dddmmss.sss E/W
Height [35,40] F6.1 metres
Height datum [41,41] I1 0 = height above ellipsoid 1 = height above geoid (~MSL)
Satellites used [42,61] 10*I2 (GPS SV numbers)
Reference stations used [62,70] 9*I1
Position calculation mode [71,72] I2 see below
Time of Observation [73,79] I2,I2,I3 HH,MM,SSs'''
class T620x:
    def __init__(self,gpsType,nodeIdentifier,receiverReferenceNumber,latitude,longitude,height,heightDatum,
    satellites,referenceStations,positionCalculation,timeObservation):
        self.gpsType = gpsType
        self.nodeIdentifier = nodeIdentifier
        self.receiverReferenceNumber = receiverReferenceNumber
        self.latitude = latitude
        self.longitude = longitude
        self.height = height
        self.heightDatum = heightDatum
        self.satellites = satellites
        self.referenceStations = referenceStations
        self.positionCalculation = positionCalculation
        self.timeObservation = timeObservation

def getT620x(line):
    t620x = T620x(line[4:5],line[5:9],line[9:10],line[10:22],line[22:34],line[34:40],line[40:41],line[41:61],line[61:70],line[70:72],line[72:79])
    return t620x

'''T621# Inter-event GPS or DGPS Data (continued)
# = 1,GPS # = 2,DGPS
"At" Node identifier [ 6,9] I4
Receiver reference number [10,10] I1
Standard deviations of:
- Latitude: [11,15] N5 metres
- Longitude: [16,20] N5 metres
- Height: [21,25] N5 metres
DOP type [26,26] I1 0 = GDOP,1 = PDOP,2 = HDOP,3 = TDOP,4 = VDOP,5..9 = user defined on comment cards
DOP figure [27,30] N4 unitless
Time of Observation [74,80] I2,I2,I3 HH,MM,SSs
The "DOP type" and "DOP figure" fields may be repeated for other DOPs or quality indicators in columns [31,35] ... [51,55] as required.'''
class T621x:
    def __init__(self,gpsType,nodeIdentifier,receiverReferenceNumber,latitude,longitude,height,dopTypeFigure,timeObservation):
        self.gpsType = gpsType
        self.nodeIdentifier = nodeIdentifier
        self.receiverReferenceNumber = receiverReferenceNumber
        self.latitude = latitude
        self.longitude = longitude
        self.height = height
        self.dopTypeFigure = dopTypeFigure
        self.timeObservation = timeObservation

def getT621x(line):
    t621x = T621x(line[4:5],line[5:9],line[9:10],line[10:15],line[15:20],line[20:25],line[25:55],line[73:80])
    return t621x

'''T6303 Inter-event TRANSIT Satellite Data
"At" Node identifier [ 6,9] I4
Latitude [10,21] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude [22,33] I3,I2,F6.3,A1 dddmmss.sss E/W
Position includes dead [34,34] I1 0 = no reckoning? 1 = yes
Standard deviations of last accepted satellite fix:
- Latitude [35,39] N5 metres
- Longitude [40,44] N5 metres
Time of Observation [45,51] I2,I2,I3 HH,MM,SSs
Record may be repeated.'''
class T6303:
    def __init__(self,nodeIdentifier,latitude,longitude,position,stdLatitude,stdLongitude,timeObservation):
        self.nodeIdentifier = nodeIdentifier
        self.latitude = latitude
        self.longitude = longitude
        self.position = position
        self.stdLatitude = stdLatitude
        self.stdLongitude = stdLongitude
        self.timeObservation = timeObservation

def getT6303(line):
    t6303 = T6303(line[5:9],line[9:21],line[21:33],line[33:34],line[34:39],line[39:44],line[44:51])
    return t6303

'''T6310 Updated GPS ephemerides & clock
S.V. [ 6,8] A1,I2 System type code,1-32
Transmission time of message [ 9,26] E18.12 GPS week seconds
Time of receipt of data [ 27,26] I2,I2,I3 Recording system time HH,MM,SSs
This record is analogous to H6310,but represents an update to a satellite's ephemeris
during a line. This may be caused by the satellite becoming visible for the first time,or by
an updated ephemeris message.
All records T6310 to T6317 must be recorded sequentially.
T6311 Updated GPS clock parameters
T6312 Updated GPS ephemerides,1
T6313 Updated GPS ephemerides,2
T6314 Updated GPS ephemerides,3
T6315 Updated GPS ephemerides,4
T6316 Updated GPS ephemerides,5
T6317 Updated GPS ephemerides,6
All records T6311 to T6317 have exactly the same format as H6311 to H6317.
Note that these records forms part of the set of records needed to record raw GPS and
DGPS observations,and are not required for the recording of satellite derived positions
only.
The following records contain updates to the Ionospheric and UTC parameters. All three records must
appear together in sequence.'''
class T6310:
    def __init__(self,systemTypeCode,transmissionTime,qualityIndicator,timeObservation,observation):
        self.systemTypeCode = systemTypeCode
        self.transmissionTime = transmissionTime
        self.qualityIndicator = qualityIndicator
        self.timeObservation = timeObservation
        self.observation = observation

def getT6310(line):
    t6310 = T6310(line[5:8],line[8:10],line[10:14],line[14:21],line[21:80])
    return t6310


'''T6320 Updated GPS UTC parameters
term of UTC polynomial A0 [ 6,23] E18.12 seconds
term of UTC polynomial A1 [24,41] E18.12 seconds / second
reference time of time,tot [42,50] I9 seconds
UTC week reference no. WNt [51,59] I9
UKOOA P2/94 Version 1.0 Page 96 of 119
Leap seconds delta time ∆tLSF [60,65] I6 seconds
Time of receipt of data [66,72] I2,I2,I3 Recording system
time HH,MM,SSs
T6321 Updated GPS ionospheric model parameters,1
T6322 Updated GPS ionospheric model parameters,2'''
class T6320:
    def __init__(self,observationReferenceNumber,dataFieldNumber,qualityIndicator,timeObservation,observation):
        self.observationReferenceNumber = observationReferenceNumber
        self.dataFieldNumber = dataFieldNumber
        self.qualityIndicator = qualityIndicator
        self.timeObservation = timeObservation
        self.observation = observation

def getT6320(line):
    t6320 = T6320(line[5:8],line[8:10],line[10:14],line[15:21],line[22:80])
    return t6320

'''T6330 Updated Meteorological data
Surface air pressure [ 6,12] F7.1 millibars
Dry air temperature [13,19] F7.1 degrees Celsius
Wet air temperature [20,26] F7.1 degrees Celsius
Relative humidity [27,33] F7.1 percent
Time of receipt of data [34,40] I2,I2,I3 Recording system time HH,MM,SSs'''
class T6330:
    def __init__(self,observationReferenceNumber,dataFieldNumber,qualityIndicator,timeObservation,observation):
        self.observationReferenceNumber = observationReferenceNumber
        self.dataFieldNumber = dataFieldNumber
        self.qualityIndicator = qualityIndicator
        self.timeObservation = timeObservation
        self.observation = observation

def getT6330(line):
    t6330 = T6330(line[5:8],line[9:10],line[11:14],line[15:21],line[22:80])
    return t6330

'''T640# Inter-event Satellite Data (other systems)
# = 4..9,Satellite system reference number
"At" Node identifier [ 6,9] I4
Latitude [10,21] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude [22,33] I3,I2,F6.3,A1 dddmmss.sss E/W
Height [34,39] F6.1 metres
Height datum [40,40] I1 0 = height above ellipsoid 1 = height above geoid (~MSL)
Standard deviations of:
- Latitude: [41,45] N5 metres
- Longitude: [46,50] N5 metres
- Height: [51,55] N5 metres
Time of Observation [56,62] I2,I2,I3 HH,MM,SSs'''
class T640x:
    def __init__(self,observationReferenceNumber,dataFieldNumber,qualityIndicator,timeObservation,observation):
        self.observationReferenceNumber = observationReferenceNumber
        self.dataFieldNumber = dataFieldNumber
        self.qualityIndicator = qualityIndicator
        self.timeObservation = timeObservation
        self.observation = observation

def getT640x(line):
    t640x = T640x(line[6:8],line[9:10],line[11:14],line[15:21],line[22:80])
    return t640x

'''T65## Inter-event differential correction data
## is the Differential Correction Source (DCS) Identifier.
Correction type [ 6,9] I4
Correction sequence [10,11] I2
GPS Time of Applicability [12,19] I2,I2,HH,MM,UKOOA P2/94 Version 1.0 Page 97 of 119 F4.1 SS.s
DCS status/health [20,21] I2 0 to 7
IOD (Issue of data) key [22,24] I3 0-255
S.V. PRN [25,27] A1,I2
Value 1 [28,41] A14
Value 2 [42,55] A14
Value 3 [56,69] A14
System Time of Receipt [70,76] I2,I2,I3 HH,MM,SSs'''
class T65xx:
    def __init__(self,DCSIdentifier,correctionType,correctionSequence,GPSTime,DCSStatus,IOD,SVPRN,value1,value2,value3,timeReceipt):
        self.DCSIdentifier = DCSIdentifier
        self.correctionType = correctionType
        self.correctionSequence = correctionSequence
        self.GPSTime = GPSTime
        self.DCSStatus = DCSStatus
        self.IOD = IOD
        self.SVPRN = SVPRN
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.timeReceipt = timeReceipt

def getT65xx(line):
    t65xx = T65xx(line[3:5],line[5:9],line[9:11],line[11:19],line[19:21],line[21:24],line[24:27],line[27:41],line[41:55],line[55:69],line[69:76])
    return t65xx

'''T67@0 Updated height aiding values
@ = 1..9 vessel number
@ = 0 fixed or relay station
Node identifier [ 6,9] I4
Positioning system identifier [10,12] I3
Ellipsoid height of antenna [13,23] N11 metres
Time of receipt of data [34,40] I2,I2,I3 Recording system time HH,MM,SSs'''
class T67x0:
    def __init__(self,vesselNumber,nodeIdentifier,positioningSystemIdentifier,heightAntenna,timeReceiptData):
        self.vesselNumber = vesselNumber
        self.nodeIdentifier = nodeIdentifier
        self.positioningSystemIdentifier = positioningSystemIdentifier
        self.heightAntenna = heightAntenna
        self.timeReceiptData = timeReceiptData

def getT67x0(line):
    t67x0 = T67x0(line[3:4],line[5:9],line[9:12],line[12:23],line[33:40])
    return t67x0

#INTER-EVENT USER DEFINED DATA

'''T7010 Inter-event User Defined Observation Set Data
Observation set reference number [ 6,8] I3
Data field number [ 9,10] I2
Quality indicator [11,14] N4
Time of observation [15,21] I2,I2,I3 HH,MM,SSs
Observation [22,.. ] Nx'''
class T7010:
    def __init__(self,observationReferenceNumber,dataFieldNumber,qualityIndicator,timeObservation,observation):
        self.observationReferenceNumber = observationReferenceNumber
        self.dataFieldNumber = dataFieldNumber
        self.qualityIndicator = qualityIndicator
        self.timeObservation = timeObservation
        self.observation = observation

def getT7010(line):
    t7010 = T7010(line[5:8],line[8:10],line[10:14],line[14:21],line[21:80])
    return t7010