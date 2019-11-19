#SATELLITE SYSTEM DEFINITIONS

'''H600# Satellite System Description
# = 1..9, Satellite system reference number
Name [ 7,14] A8 free text
Datum and spheroid number [16,16] I1
Diff. system operator [18,35] A18 free text
Diff. system name [37,46] A10 free text
Software description, version number and additional information [48,80] A33 free text'''
class H600x:
    def __init__(self,satelliteReferenceNumber,name,datum,systemOperator,systemName,softwareDescription):
        self.satelliteReferenceNumber = satelliteReferenceNumber
        self.name = name
        self.datum = datum
        self.systemOperator = systemOperator
        self.systemName = systemName
        self.softwareDescription = softwareDescription
    
def getH600x(line):
    h600x = H600x(line[5:5],line[7:14],line[16:16],line[18:35],line[37:46],line[48:80])
    return h600x

'''H610# Definition of Differential Reference Stations
# = 2, 4..9, Satellite system reference number
Reference station number [ 6, 7] I2
Reference station name [ 9,20] A12 free text
Latitude [22,33] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude [35,46] I3,I2,F6.3,A1 dddmmss.sss E/W
Spheroidal height [48,54] F7.2 metres
Geoid-Spheroid separation [56,62] F7.2 metres
Geoidal model [64,80] A17 free text'''
class H610x:
    def __init__(self,satelliteReferenceNumber,referenceStationNumber,referenceStationName,latitude,longitude,spheroidalHeight,geoidalSeparation,geoidalModel):
        self.satelliteReferenceNumber = satelliteReferenceNumber
        self.referenceStationNumber = referenceStationNumber
        self.referenceStationName = referenceStationName
        self.latitude = latitude
        self.longitude = longitude
        self.spheroidalHeight = spheroidalHeight
        self.geoidalSeparation = geoidalSeparation
        self.geoidalModel = geoidalModel
    
def getH610x(line):
    h610x = H610x(line[5:5],line[6:7],line[9:20],line[22:33],line[35:46],line[48:54],line[56:62],line[64:80])
    return h610x

'''H620# Satellite Receiver Definition
# = 1..9, Satellite system reference number
"At" Node identifier [ 7,10] I4
Receiver number [12,12] I1
Located on: ref. number [14,16] I3
Offset A [18,24] F7.1
Offset B [26,32] F7.1
Offset Z [34,39] F6.1
Receiver name, description and additional information [41,80] A40 free text'''
class H620x:
    def __init__(self,satelliteReferenceNumber,nodeIdentifier,receiverNumber,referenceNumber,locationRefNumber,offsetA,offsetB,offsetZ):
        self.satelliteReferenceNumber = satelliteReferenceNumber
        self.nodeIdentifier = nodeIdentifier
        self.receiverNumber = receiverNumber
        self.referenceNumber = referenceNumber
        self.locationRefNumber = locationRefNumber
        self.offsetA = offsetA
        self.offsetB = offsetB
        self.offsetZ = offsetZ
    
def getH620x(line):
    h620x = H620x(line[5:5],line[7:10],line[12:12],line[14:16],line[18:24],line[26:32],line[34:39],line[41:80])
    return h620x

#GPS PARAMETERS

'''H6300 GPS parameter recording strategy
Meteorological records [ 7, 7] A1
Ionospheric model records [ 8, 8] A1
Clock model & ephemerides [ 9, 9] A1
'''
class H6300:
    def __init__(self,meteorologicalRecords,ionosphericModelRecords,clockModel):
        self.meteorologicalRecords = meteorologicalRecords
        self.ionosphericModelRecords = ionosphericModelRecords
        self.clockModel = clockModel
    
def getH6300(line):
    h6300 = H6300(line[7:7],line[8:8],line[9:9])
    return h6300

'''H6301 DGPS differential correction recording strategy
Correction Type [ 7,10] I4
Type Description [11,24] A14
Correction Type [25,28] I4
Type Description [29,42] A14
Correction Type [43,46] I4
Type Description [47,60] A14
Correction Type [61,64] I4
Type Description [65,78] A14'''
class H6301:
    def __init__(self,correctionType,typeDescription):
        self.correctionType = correctionType
        self.typeDescription = typeDescription
    
def getH6301(line):
    h6301 = H6301(line[7:10],line[11:24])
    return h6301

'''
H6310 GPS ephemerides & clock 
S.V. [ 6, 8] A1,I2 System type code, 1-32
Transmission time of message [ 9,26] E18.12 GPS week seconds'''
class H6310:
    def __init__(self,systemTypeCode,transmissionTimeMessage):
        self.systemTypeCode = systemTypeCode
        self.transmissionTimeMessage = transmissionTimeMessage
    
def getH6310(line):
    h6310 = H6310(line[6:8],line[9:26])
    return h6310

'''H6311 GPS clock parameters
S.V. [ 6, 8] A1,I2 System type code, 1-32
S.V. clock drift rate a  f2 [ 9,26] E18.12 seconds/second²
S.V. clock drift a f1 [27,44] E18.12 seconds / second
S.V. clock bias a f0 [45,62] E18.12 seconds
Time of Clock t oc [63,80] E18.12 GPS week seconds
These parameters are available from the GPS message sub-frame 1.'''
class H6311:
    def __init__(self,systemTypeCode,clockF2,clockF1,clockF0,timeClock):
        self.systemTypeCode = systemTypeCode
        self.clockF2 = clockF2
        self.clockF1 = clockF1
        self.clockF0 = clockF0
        self.timeClock = timeClock
    
def getH6311(line):
    h6311 = H6311(line[6:8],line[9:26],line[27:44],line[45:62],line[63:80])
    return h6311

'''H6312 GPS ephemerides, 1
S.V. [ 6, 8] A1,I2 System type code, 1-32
Issue of Data, Ephemerides IODE [ 9,26] E18.12 
Crs [27,44] E18.12 metres
∆n [45,62] E18.12 radians / second 
M0 [63,80] E18.12 radians 
Crs amplitude of the sine harmonic correction term to the orbit radius.
∆n mean motion difference from computed value.
M0 mean anomaly at reference time.
These parameters are available from the GPS message sub-frames 2 and 3.'''
class H6312:
    def __init__(self,systemTypeCode,issueData,crs,deltaN,m0):
        self.systemTypeCode = systemTypeCode
        self.issueData = issueData
        self.crs = crs
        self.deltaN = deltaN
        self.m0 = m0
    
def getH6312(line):
    h6312 = H6312(line[6:8],line[9:26],line[27:44],line[45:62],line[63:80])
    return h6312

'''H6313 GPS ephemerides, 2
S.V. [ 6, 8] A1,I2 System type code, 1-32 
Cuc [ 9,26] E18.12 radians
eccentricity e [27,44] E18.12
Cus [45,62] E18.12 radians
√A [63,80] E18.12 √(metres)'''
class H6313:
    def __init__(self,systemTypeCode,cuc,eccentricity,cus,squareA):
        self.systemTypeCode = systemTypeCode
        self.cuc = cuc
        self.eccentricity = eccentricity
        self.cus = cus
        self.squareA = squareA
    
def getH6313(line):
    h6313 = H6313(line[6:8],line[9:26],line[27:44],line[45:62],line[63:80])
    return h6313

'''H6314 GPS ephemerides, 3
S.V. [ 6, 8] A1,I2 System type code, 1-32
Time of ephemeris, toe [ 9,26] E18.12 GPS week seconds
Cic [27,44] E18.12 radians
Ω0[45,62] E18.12 radians
Cis [63,80] E18.12 radians'''
class H6314:
    def __init__(self,systemTypeCode,timeEphemeris,cic,phi,cis):
        self.systemTypeCode = systemTypeCode
        self.timeEphemeris = timeEphemeris
        self.cic = cic
        self.phi = phi
        self.cis = cis

def getH6314(line):
    h6314 = H6314(line[6:8],line[9:26],line[27:44],line[45:62],line[63:80])
    return h6314

'''H6315 GPS ephemerides, 4
S.V. [ 6, 8] A1,I2 System type code, 1-32
i0 [ 9,26] E18.12 radians
Crc [27,44] E18.12 metres
argument of perigee ω [45,62] E18.12 radians
rate of right ascension Ω• [63,80] E18.12 radians / second'''
class H6315:
    def __init__(self,systemTypeCode,i0,crc,argumentPerigee,rateRightAscension):
        self.systemTypeCode = systemTypeCode
        self.i0 = i0
        self.crc = crc
        self.argumentPerigee = argumentPerigee
        self.rateRightAscension = rateRightAscension

def getH6315(line):
    h6315 = H6315(line[6:8],line[9:26],line[27:44],line[45:62],line[63:80])
    return h6315

'''H6316 GPS ephemerides, 5
S.V. [ 6, 8] A1,I2 System type code, 1-32
Rate of inclination angle i• [ 9,26] E18.12 radians / second
Codes on L2 [27,44] E18.12
GPS week number [45,62] E18.12
L2 P data flag [63,80] E18.12'''
class H6316:
    def __init__(self,systemTypeCode,rateInclinationAngle,codesL2,gpsWeekNumber,dataFlag):
        self.systemTypeCode = systemTypeCode
        self.rateInclinationAngle = rateInclinationAngle
        self.codesL2 = codesL2
        self.gpsWeekNumber = gpsWeekNumber
        self.dataFlag =dataFlag 

def getH6316(line):
    h6316 = H6316(line[6:8],line[9:26],line[27:44],line[45:62],line[63:80])
    return h6316

'''H6317 GPS ephemerides, 6
S.V. [ 6, 8] A1,I2 System type code, 1-32
S.V. accuracy [ 9,26] E18.12
S.V. health [27,44] E18.12
TGD [45,62] E18.12
Issue of data clock, IODC [63,80] E18.12
i0 inclination angle at reference time.
CRC amplitude of the cosine harmonic correction term to the orbit radius.
These parameters are available from the GPS message sub-frames 2 and 3.
Note that this record forms part of the set of records needed to record raw GPS and
DGPS observations, and is not required for the recording of satellite derived positions
only.
The following triplet of records (or their T632# equivalents) must appear at least once prior to the
recording of any raw GPS observations.'''
class H6317:
    def __init__(self,systemTypeCode,accuracy,health,TGD,issueDataClock):
        self.systemTypeCode = systemTypeCode
        self.accuracy = accuracy
        self.health = health
        self.TGD = TGD
        self.issueDataClock = issueDataClock

def getH6317(line):
    h6317 = H6317(line[6:8],line[9:26],line[27:44],line[45:62],line[63:80])
    return h6317

'''H6320 GPS UTC parameters
term of UTC polynomial A0 [ 6,23] E18.12 seconds
term of UTC polynomial A1 [24,41] E18.12 seconds / second
reference time of time, tot [42,50] I9 seconds
UTC week reference no. WNt [51,59] I9
Leap seconds delta time ∆tLSF [60,65] I6 seconds'''
class H6320:
    def __init__(self,polynomialA0,polynomialA1,referenceTime,referenceWeek,deltaTime):
        self.polynomialA0 = polynomialA0
        self.polynomialA1 = polynomialA1
        self.referenceTime = referenceTime
        self.referenceWeek = referenceWeek
        self.deltaTime = deltaTime
    
def getH6320(line):
    h6320 = H6320(line[6:23],line[24:41],line[42:50],line[51:59],line[60:65])
    return h6320

'''H6321 GPS ionospheric model parameters, 1
α0 [ 6,17] E12.4 seconds
α1 [18,29] E12.4 seconds / semicircle
α2 [30,41] E12.4 seconds / semicircle²
α3 [42,53] E12.4 seconds / semicircle³
These parameters are available from the GPS message sub-frame 4, page 18.'''
class H6321:
    def __init__(self,a0,a1,a2,a3):
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

def getH6321(line):
    h6321 = H6321(line[6:17],line[18:29],line[30:41],line[42:53])
    return h6321

'''H6322 GPS ionospheric model parameters, 2
β0 [ 6,17] E12.4 seconds
β1 [18,29] E12.4 seconds / semicircle
β2 [30,41] E12.4 seconds / semicircle²
β3 [42,53] E12.4 seconds / semicircle³'''
class H6322:
    def __init__(self,b0,b1,b2,b3):
        self.b0 = b0
        self.b1 = b1
        self.b2 = b2
        self.b3 = b3

def getH6322(line):
    h6322 = H6322(line[6:17],line[18:29],line[30:41],line[42:53])
    return h6322

'''H6330 Meteorological data
Surface air pressure [ 6,12] F7.1 millibars
Dry air temperature [13,19] F7.1 degrees Celsius
Wet air temperature [20,26] F7.1 degrees Celsius
Relative humidity [27,33] F7.1 percent
Either, but not both, of the last two fields may be left blank.'''
class H6330:
    def __init__(self,surfaceAirPressure,dryAirTemperature,wetAirTemperature,relativeHumidity):
        self.surfaceAirPressure = surfaceAirPressure
        self.dryAirTemperature = dryAirTemperature
        self.wetAirTemperature = wetAirTemperature
        self.relativeHumidity = relativeHumidity

def getH6330(line):
    h6330 = H6330(line[6:12],line[13:19],line[20:26],line[27:33])
    return h6330

#DGPS DEFINITIONS

'''H65## Differential Correction Source Definition
## is the Differential Correction Source Identifier
DCS short name [ 7,14] A8 free text
Datum & Spheroid number [16,16] I1 from H011x
Latitude of correction source [17, 28] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude of correction source [29, 41] I3,I2,F6.3 A1 dddmmss.sss E/W
Spheroidal height [42, 48] F7.2 metres
Geoid - spheroid separation [49, 55] F7.2 metres
Geoidal model [56, 72] A17 free text'''
class H65xx:
    def __init__(self,DCSIdentifier,DCSShortName,datumSpheroidNumber,latitudeCS,longitudeCS,spheroidalHeight,spheroidalSeparation,geoidalModel):
        self.DCSIdentifier = DCSIdentifier
        self.DCSShortName = DCSShortName
        self.datumSpheroidNumber = datumSpheroidNumber
        self.latitudeCS = latitudeCS
        self.longitudeCS = longitudeCS
        self.spheroidalHeight = spheroidalHeight
        self.spheroidalSeparation = spheroidalSeparation
        self.geoidalModel = geoidalModel

def getH65xx(line):
    h65xx = H65xx(line[4:5],line[7:14],line[16:16],line[17:28],line[29:41],line[42:48],line[49:55],line[56:72])
    return h65xx

'''H66## Differential Correction Source Description
## is the Differential Correction Source Identifier
DCS system operator [ 7, 24] A18 free text
DCS component name [25, 43] A18 free text
DCS component description [44, 80] A37 free text'''
class H66xx:
    def __init__(self,DCSIdentifier,DCSSystemOperator,DCSComponentName,DCSComponentDescription):
        self.DCSIdentifier = DCSIdentifier
        self.DCSSystemOperator = DCSSystemOperator
        self.DCSComponentName = DCSComponentName
        self.DCSComponentDescription = DCSComponentDescription

def getH66xx(line):
    h66xx = H66xx(line[4:5],line[7:24],line[25:43],line[44:80])
    return h66xx

'''H67@0 Height aiding values
@ = 1..9 vessel number
@ = 0 fixed or relay station
Node identifier [ 6, 9] I4
Positioning system identifier [10,12] I3
Ellipsoid height of antenna [13,23] N11 metres
Description of source of value [24,80] A57 free text'''
class H67xx:
    def __init__(self,vesselNumber,station,nodeIdentifier,systemIdentifier,ellipsoidHeight,descriptionSource):
        self.vesselNumber = vesselNumber
        self.station = station
        self.nodeIdentifier = nodeIdentifier
        self.systemIdentifier = systemIdentifier
        self.ellipsoidHeight = ellipsoidHeight
        self.descriptionSource = descriptionSource

def getH67xx(line):
    h67xx = H67xx(line[4:4],line[5:5],line[6:9],line[10:12],line[13:23],line[24:80])
    return h67xx