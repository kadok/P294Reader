#VESSEL DEFINITIONS

'''H10@0 Vessel Reference Point Definition
@ = 1..9,Vessel reference number
Height above sea level [ 7,10] F4.1 metres
Description of reference point [12,80] A69 free text'''
class H10x0:
    def __init__(self,vesselReferenceNumber,height,description):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.height = height
        self.description = description

def getH10x0(line):
    h10x0 = H10x0(line[3:4],line[6:10],line[11:80])
    return h10x0

'''H11@0 Steered Point Definition
@ = 1..9,Vessel reference number
Description of steered point [ 7,80] A74 free text'''
class H11x0:
    def __init__(self,vesselReferenceNumber,description):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.description = description

def getH11x0(line):
    h11x0 = H11x0(line[3:4],line[6:80])
    return h11x0

'''H12@0 Onboard Navigation System Description
@ = 1..9,Vessel reference number
Details of onboard navigation & processing systems [ 7,80] A74 free text'''
class H12x0:
    def __init__(self,vesselReferenceNumber,systemDetails):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.systemDetails = systemDetails

def getH12x0(line):
    h12x0 = H12x0(line[3:4],line[6:80])
    return h12x0

'''H12@1 Definition of Quality Indicators for Field Positioning Derived Data
@ = 1..9,Vessel reference number
Record sequence number [ 7,8] I2
Definition of quality indicator types for field positioning derived data [10,80] A71 free text'''
class H12x1:
    def __init__(self,vesselReferenceNumber,recordSequenceNumber,definitionQualityIndicatorType):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.recordSequenceNumber = recordSequenceNumber
        self.definitionQualityIndicatorType = definitionQualityIndicatorType

def getH12x1(line):
    h12x1 = H12x1(line[3:4],line[6:8],line[9:80])
    return h12x1

'''H13@0 Vessel Time System Definition
@ = 1..9,Vessel reference number
Time correction to ship's time to convert to GMT [ 7,12] F6.2 +/- hours
Time correction to vessel's time system to convert to the master vessel's time system [14,21] N8 seconds'''
class H13x0:
    def __init__(self,vesselReferenceNumber,timeCorrectionShipGMT,timeCorrectionVesselTimeSystem):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.timeCorrectionShipGMT = timeCorrectionShipGMT
        self.timeCorrectionVesselTimeSystem = timeCorrectionVesselTimeSystem

def getH13x0(line):
    h13x0 = H13x0(line[3:4],line[6:12],line[13:21])
    return h13x0

'''H14@# Echo Sounder Definition
@ = 1..9,Vessel reference number
# = 1..9,Echo sounder reference number
Offset A to transducer [ 7,13] F7.1
Offset B to transducer [15,21] F7.1
Offset Z from reference point to transducer [23,28] F6.1
Propagation velocity used [30,36] N7 m/s or ft/s
Calibrated propagation velocity [38,44] N7 m/s or ft/s
Velocity unit [46,46] I1 0 = m/s 1 = ft/s
Water depth reference level [47,47] I1 0 = transducer 1 = sea level
Heave compensated depths? [48,48] I1 0 = depths not heave compensated 1 = depths heave compensated
Echo sounder description [50,80] A31 free text'''
class H14xy:
    def __init__(self,vesselReferenceNumber,echoSounderReferenceNumber,offsetA,offsetB,offsetZ,propagationVelocity,calibratedPropagationVelocity,
    velocityUnit,waterDepthReferenceLevel,heaveCompesatedDepths,echoSounderDescription):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.echoSounderReferenceNumber = echoSounderReferenceNumber
        self.offsetA = offsetA
        self.offsetB = offsetB
        self.offsetZ = offsetZ
        self.propagationVelocity = propagationVelocity
        self.calibratedPropagationVelocity = calibratedPropagationVelocity
        self.velocityUnit = velocityUnit
        self.waterDepthReferenceLevel = waterDepthReferenceLevel
        self.heaveCompesatedDepths = heaveCompesatedDepths
        self.echoSounderDescription = echoSounderDescription

def getH14xy(line):
    h14xy = H14xy(line[3:4],line[4:5],line[6:13],line[14:21],line[22:28],line[29:36],line[37:44],line[45:46],line[46:47],line[47:48],line[49:80])
    return h14xy

'''H1500 Observed Velocity of Sound - Definitions
Profile number [ 7,8] I2
Date [10,17] I4,I2,I2 YYYYMMDD
Time (Master Vessel) [19,22] I2,I2 HHMM
Latitude [24,35] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude [36,47] I3,I2,F6.3,A1 dddmmss.sss E/W
Depth units [48,48] I1 0 = metres 1 = feet
Velocity units [49,49] I1 0 = metres/sec 1 = feet/sec
Temperature units [50,50] I1 0 = degrees Celsius 1 = degrees Fahrenheit
Salinity/Conductivity [51,51] I1 0 = promille (10-3) (salinity) 1 = mmho/cm (conductivity) 2 = Siemens/metre (conductivity)
Instrument description [53,80] A28 free text'''
class H1500:
    def __init__(self,profileNumber,date,time,latitude,longitude,depthUnits,velocityUnits,temperatureUnits,salinity,instrumentDescription):
        self.profileNumber = profileNumber
        self.date = date
        self.time = time
        self.latitude = latitude
        self.longitude = longitude
        self.depthUnits = depthUnits
        self.velocityUnits = velocityUnits
        self.temperatureUnits = temperatureUnits
        self.salinity = salinity
        self.instrumentDescription = instrumentDescription

def getH1500(line):
    h1500 = H1500(line[6:8],line[9:17],line[18:22],line[23:35],line[35:47],line[47:48],line[48:49],line[49:50],line[50:51],line[52:80])
    return h1500

'''H1501 Observed Velocity of Sound - Profile
Profile number [ 7,8] I2
Depth [10,15] F6.1
Velocity [16,21] F6.1
Temperature [22,26] F5.1
Salinity or conductivity [27,31] F5.2
May be repeated for two more observations at [33,54] and [56,77] for the same profile'''
class H1501:
    def __init__(self,profileNumber,depth,velocity,temperature,salinity,observation1,observation2):
        self.profileNumber = profileNumber
        self.depth = depth
        self.velocity = velocity
        self.temperature = temperature
        self.salinity = salinity
        self.observation1 = observation1
        self.observation2 = observation2

def getH1501(line):
    h1501 = H1501(line[6:8],line[9:15],line[15:21],line[21:26],line[26:31],line[32:54],line[55:77])
    return h1501

'''H16@0 USBL System Definition
@ = 1..9,Vessel reference number
USBL system ref. number [ 7,7] I1
Quality indicator type [ 9,9] I1
Sign convention for Z-axis data [11,11] I1 0 = positive upward (height) 1 = positive down-ward (depth)
Recorded data corrected for:
Turn around delays? [12,12] I1 0 = no; 1 = yes
Velocity of propagation? [13,13] I1 0 = assumed; 1 = calibrated
Horizontal alignment? [14,14] I1 0 = no; 1 = ship's axis; 2 = raw gyro
Pitch alignment? [15,15] I1 0 = no; 1 = raw VRU,2 = corrected VRU
Roll alignment? [16,16] I1 0 = no; 1 = raw VRU,2 = corrected VRU
Reduction to ship's reference point? [17,17] I1 0 = no; 1 = yes '''
class H16x0:
    def __init__(self,vesselNumber,systemReferenceNumber,qualityIndicatorType,signConventionZAxisData,
    turnAroundDelay,velocityPropagation,horizontalAlignment,pitchAlignment,rollAlignment,reductionShips):
        self.vesselNumber = vesselNumber
        self.systemReferenceNumber = systemReferenceNumber
        self.qualityIndicatorType = qualityIndicatorType
        self.signConventionZAxisData = signConventionZAxisData
        self.turnAroundDelay = turnAroundDelay
        self.velocityPropagation = velocityPropagation
        self.horizontalAlignment = horizontalAlignment
        self.pitchAlignment = pitchAlignment
        self.rollAlignment = rollAlignment
        self.reductionShips = reductionShips

def getH16x0(line):
    h16x0 = H16x0(line[3:4],line[6:7],line[8:9],line[10:11],line[11:12],line[12:13],line[13:14],line[14:15],line[15:16],line[16,17])
    return h16x0

'''H16@1 USBL System Definition (continued)
@ = 1..9,Vessel reference number
USBL system reference number [ 7,7] I1
Transducer Node identifier [ 9,12] I4
Offsets from ship's reference point to USBL transducer:
Offset A [14,20] F7.1
Offset B [22,28] F7.1
Offset Z [30,35] F6.1
Correction to horizontal alignment [37,41] N5 degrees decimal
Correction to pitch alignment [43,47] N5 degrees decimal
Correction to roll alignment [49,53] N5 degrees decimal
Assumed velocity of propagation [55,61] N7
Calibrated velocity of propagation [63,69] N7
Velocity measurement units [71,71] I1 0 = m/s 1 = ft/s
Turn around delay [73,80] N8 milliseconds'''
class H16x1:
    def __init__(self,vesselNumber,systemReferenceNumber,transducerNodeIdentifier,offsetA,offsetB,offsetZ,correctionHorizontalAlignment,
    correctionPitchAlignment,correctionRollAlignment,AssumedVelocityPropagation,calibratedVelocityPropagation,velocityMeasurementUnits,turnAroundDelay):
        self.vesselNumber = vesselNumber
        self.systemReferenceNumber = systemReferenceNumber
        self.transducerNodeIdentifier = transducerNodeIdentifier
        self.offsetA = offsetA
        self.offsetB = offsetB
        self.offsetZ = offsetZ
        self.correctionHorizontalAlignment = correctionHorizontalAlignment
        self.correctionPitchAlignment = correctionPitchAlignment
        self.correctionRollAlignment = correctionRollAlignment
        self.AssumedVelocityPropagation = AssumedVelocityPropagation
        self.calibratedVelocityPropagation = calibratedVelocityPropagation
        self.velocityMeasurementUnits = velocityMeasurementUnits
        self.turnAroundDelay = turnAroundDelay

def getH16x1(line):
    h16x1 = H16x1(line[3:4],line[6:7],line[8:12],line[13:20],line[21:28],line[29:35],line[36:41],line[42:47],line[48:53],line[54:61],line[62:69],line[70:71],line[72:80])
    return h16x1

'''H16@2 Definition of Quality Indicator Type for USBL
@ = 1..9,Vessel reference number
USBL system ref. number [ 7,7] I1
Definition of quality indicator type [ 9,80] A72 free text
Record may be repeated.'''
class H16x2:
    def __init__(self,vesselNumber,systemReferenceNumber,definitionQualityIndicatorType):
        self.vesselNumber = vesselNumber
        self.systemReferenceNumber = systemReferenceNumber
        self.definitionQualityIndicatorType = definitionQualityIndicatorType

def getH16x2(line):
    h16x2 = H16x2(line[3:4],line[6:7],line[8:80])
    return h16x2

'''H17@0 Pitch,Roll and Heave Sensor Definitions
@ = 1..9,Vessel reference number
Sensor reference number [ 7,7] I1
Rotation convention pitch [ 9,9] I1 0 = positive bow up 1 = positive bow down
Rotation convention roll [10,10] I1 0 = positive heeling to starboard 1 = positive heeling to port
Angular variable measured [11,11] I1 0 = pitch/roll angle 1 = sine of angle
Angular measurement units [12,12] I1 3 = degrees decimal 4 = grads 9 = other
Measurement units heave [13,13] I1 0 = metres 1 = feet 9 = other
If angular measurement units = 9:
Conversion factor to degrees decimal [15,22] N8
If heave measurement units = 9: 
Conversion factor to metres [24,31] N8
Quality indicator type pitch and roll [33,33] I1
Quality indicator type heave [34,34] I1
(C-O) pitch observation [36,42] N7
(C-O) roll observation [44,50] N7
(C-O) heave observation [52,58] N7
Description of pitch,roll,heave system [60,80] A21 free text'''
class H17x0:
    def __init__(self,vesselNumber,sensorReferenceNumber,rotationPitch,rotationRoll,angularMeasured,angularMeasurementUnits,measurementUnitsHeave,
    conversionFactorDegrees,conversionFactorMetres,qualityTypePichtRoll,qualityTypeHeave,pitchObservation,rollObservation,heaveObservation,systemDescription):
        self.vesselNumber = vesselNumber
        self.sensorReferenceNumber = sensorReferenceNumber
        self.rotationPitch = rotationPitch
        self.rotationRoll = rotationRoll
        self.angularMeasured = angularMeasured
        self.angularMeasurementUnits = angularMeasurementUnits
        self.measurementUnitsHeave = measurementUnitsHeave
        self.conversionFactorDegrees = conversionFactorDegrees
        self.conversionFactorMetres = conversionFactorMetres
        self.qualityTypePichtRoll = qualityTypePichtRoll
        self.qualityTypeHeave = qualityTypeHeave
        self.pitchObservation = pitchObservation
        self.rollObservation = rollObservation
        self.heaveObservation = heaveObservation
        self.systemDescription = systemDescription

def getH17x0(line):
    h17x0 = H17x0(line[3:4],line[6:7],line[8:9],line[9:10],line[10:11],line[11:12],line[12:13],
    line[14:22],line[23:31],line[32:33],line[33:34],line[35:42],line[43:50],line[51:58],line[59:80])
    return h17x0


'''H17@1 Definition of Quality Indicator Type for Pitch,Roll and Heave
@ = 1..9,Vessel reference number
Sensor reference number [ 7,7] I1
Definition of quality indicator type [ 9,80] A72 free text'''
class H17x1:
    def __init__(self,vesselNumber,sensorReferenceNumber,definitionQualityIndicatorType):
        self.vesselNumber = vesselNumber
        self.sensorReferenceNumber = sensorReferenceNumber
        self.definitionQualityIndicatorType = definitionQualityIndicatorType

def getH17x1(line):
    h17x1 = H17x1(line[3:4],line[6:7],line[8:80])
    return h17x1