#GUN ARRAY DEFINITIONS

'''H31@0 Gun Array Geometry Definitions
@ = 1..9, Vessel reference number
Gun array reference number [ 7, 9] I3
Offsets from Towing Vessel's Reference Point to:
- towpoint-on-towing-body:
Offset A [11,17] F7.1
Offset B [19,25] F7.1
Offset Z [27,32] F6.1
- towpoint-in-sea:
Offset A [34,40] F7.1
Offset B [42,48] F7.1
Offset Z [50,55] F6.1
Local offsets from the towpoint-in-sea to the horizontal centre of the gun array:
Local offset A [57,63] F7.1
Local offset B [64,70] F7.1
Nominal firing pressure [72,77] N6
Pressure units code [78,78] I1 0 = kgf/cm2 1 = lbs/in2 2 = bar
Volumes units code [79,79] I1 0 = cm3 1 = in3 
Depth units code [80,80] I1 0 = metres 1 = feet'''
class H31xx:
    def __init__(self,vesselReferenceNumber,gunArrayReferenceNumber,bodyOffsetA,bodyOffsetB,bodyOffsetZ,
    seaOffsetA,seaOffsetB,seaOffsetZ,localOffsetA,localOffsetB,firingPressure,pressureUnits,volumeUnits,depthUnits):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.gunArrayReferenceNumber = gunArrayReferenceNumber
        self.bodyOffsetA = bodyOffsetA
        self.bodyOffsetB = bodyOffsetB
        self.bodyOffsetZ = bodyOffsetZ
        self.seaOffsetA = seaOffsetA
        self.seaOffsetB = seaOffsetB
        self.seaOffsetZ = seaOffsetZ
        self.localOffsetA = localOffsetA
        self.localOffsetB = localOffsetB
        self.firingPressure = firingPressure
        self.pressureUnits = pressureUnits
        self.volumeUnits = volumeUnits
        self.depthUnits = depthUnits

def getH31xx(line):
    h31xx = H31xx(line[3:4],line[6:9],line[10:17],line[18:25],line[26:32],line[33:40],line[41:48],line[49:55],line[56:63],line[63:70],line[71:77],line[77:78],line[78:79],line[79:80])
    return h31xx

'''H31@1 Individual Gun Definition
@ = 1..9 Vessel reference number
Gun array reference number [ 7, 9] I3
Gun reference number [11,13] I3
Local offset A [15,21] F7.1
Local offset B [23,29] F7.1
Local offset Z [31,36] F6.1
Gun volume [38,43] I6
May be repeated for one more gun in the same array at [45,77]; the gun array reference number is not repeated.
Record may be repeated.'''
class H31x1:
    def __init__(self,vesselReferenceNumber,gunArrayReferenceNumber,gunReference,localOffsetA,localOffsetB,localOffsetZ,gunVolume,repeated):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.gunArrayReferenceNumber = gunArrayReferenceNumber
        self.gunReference = gunReference
        self.localOffsetA = localOffsetA
        self.localOffsetB = localOffsetB
        self.localOffsetZ = localOffsetZ
        self.gunVolume = gunVolume
        self.repeated = repeated

def getH31x1(line):
    h31x1 = H31x1(line[3:4],line[6:9],line[10:13],line[14:21],line[22:29],line[30:36],line[37:43],line[44:77])
    return h31x1

'''H32@0 Description of Gun Array Depth Sensors
@ = 1..9 Vessel reference number
Gun array reference number [ 7, 9] I3
Quality indicator type [11,11] I1
Description of depth sensors [13,80] A62 free text'''
class H32x0:
    def __init__(self,vesselReferenceNumber,gunArrayReferenceNumber,qualityIndicatorType,descriptionDepthSensors):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.gunArrayReferenceNumber = gunArrayReferenceNumber
        self.qualityIndicatorType = qualityIndicatorType
        self.descriptionDepthSensors = descriptionDepthSensors

def getH32x0(line):
    h32x0 = H32x0(line[3:4],line[6:9],line[10:11],line[12:80])
    return h32x0

'''H32@1 Gun Array Depth Sensor Definitions
@ = 1..9 Vessel reference number
Gun array reference number [ 7, 9] I3
Sensor number [11,12] I2
Sensor serial number [14,21] A8
Local offset A [23,29] F7.1
Local offset B [31,37] F7.1
Depth correction (C-O) [39,44] F6.1
May be repeated for one more depth sensor on the same gun array at [46,79]; the gun array number is not repeated.
Record may be repeated.'''
class H32x1:
    def __init__(self,vesselReferenceNumber,gunArrayReferenceNumber,sensorNumber,sensorSerialNumber,localOffsetA,localOffsetB,depthCorrection,repeated):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.gunArrayReferenceNumber = gunArrayReferenceNumber
        self.sensorNumber = sensorNumber
        self.sensorSerialNumber = sensorSerialNumber
        self.localOffsetA = localOffsetA
        self.localOffsetB = localOffsetB
        self.depthCorrection = depthCorrection
        self.repeated = repeated

def getH32x1(line):
    h32x1 = H32x1(line[3:4],line[6:9],line[10:12],line[13:21],line[22:29],line[30:37],line[38:44],line[45:79])
    return h32x1

'''H32@2 Definition of Quality Indicator Type for Gun Array Depth Sensors
@ = 1..9 Vessel reference number
Gun array reference number [ 7, 9] I3
Definition of quality indicator type [11,80] A70 free text
Record may be repeated.'''
class H32x2:
    def __init__(self,vesselReferenceNumber,gunArrayReferenceNumber,definitionQualityIndicatorType):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.gunArrayReferenceNumber = gunArrayReferenceNumber
        self.definitionQualityIndicatorType = definitionQualityIndicatorType

def getH32x2(line):
    h32x2 = H32x2(line[3:4],line[6:9],line[10:80])
    return h32x2

'''H33@0 Definition of Intended Gun Firing Sequence
@ = 1..9 Vessel reference number
Gun array reference number [ 7, 9] I3
Starting gun number [11,13] I3
Active gun mask [15,80] 66*I1 0 = inactive 1 = active
Record may be repeated in case more than 66 guns need to be defined or when the
discontinuity in the gun numbers spans more than 66.'''
class H33x0:
    def __init__(self,vesselReferenceNumber,gunArrayReferenceNumber,startingGunNumber,activeGunMask):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.gunArrayReferenceNumber = gunArrayReferenceNumber
        self.startingGunNumber = startingGunNumber
        self.activeGunMask = activeGunMask

def getH33x0(line):
    h33x0 = H33x0(line[3:4],line[6:9],line[10:13],line[14:80])
    return h33x0

'''H34@0 Gun Array Pressure Sensor Definitions
@ = 1..9 Vessel reference number
Gun array reference number [ 7, 9] I3
Gun number [11,13] I3
Sensor serial number [15,22] A8
Sensor correction (C-O) [24,28] F5.1
May be repeated for 2 more pressure sensors on the same gun array at [30,47] and [49,66]; the gun array reference number is not repeated.
Record may be repeated.'''
class H34x0:
    def __init__(self,vesselReferenceNumber,gunArrayReferenceNumber,gunNumber,sensorSerialNumber,sensorCorrection):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.gunArrayReferenceNumber = gunArrayReferenceNumber
        self.gunNumber = gunNumber
        self.sensorSerialNumber = sensorSerialNumber
        self.sensorCorrection = sensorCorrection

def getH34x0(line):
    h34x0 = H34x0(line[3:4],line[6:9],line[10:13],line[14:22],line[23:66])
    return h34x0

'''H34@1 Description of Gun Array Pressure Sensors
@ = 1..9 Vessel reference number
Gun array reference number [ 7, 9] I3
Description of gun array pressure sensors [11,80] A70 free text'''
class H34x1:
    def __init__(self,vesselReferenceNumber,gunArrayReferenceNumber,descriptionGunArrayPressureSensors):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.gunArrayReferenceNumber = gunArrayReferenceNumber
        self.descriptionGunArrayPressureSensors = descriptionGunArrayPressureSensors

def getH34x1(line):
    h34x1 = H34x1(line[3:4],line[6:9],line[10:80])
    return h34x1
