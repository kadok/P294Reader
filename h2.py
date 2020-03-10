#STREAMER DEFINITIONS

'''H21@0 Streamer Geometry Definitions
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Offsets from ship's reference point to:
- towpoint-on-towing-vessel:
Offset A [11,17] F7.1
Offset B [19,25] F7.1
Offset Z [27,32] F6.1
- towpoint-in-sea:
Offset A [35,41] F7.1
Offset B [43,49] F7.1
Offset Z [51,56] F6.1
Local offsets from the centre of the near receiver group to the towpoint-in-sea:
Local Y-offset [58,64] F7.1
Local Z-offset [66,71] F6.1'''
class H21x0:
    def __init__(self,vesselReferenceNumber,streamerReferenceNumber,towingVesselOffsetA,towingVesselOffsetB,towingVesselOffsetZ,towingSeaOffsetA,towingSeaOffsetB,towingSeaOffsetZ,localOffsetY,localOffsetZ):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.streamerReferenceNumber = streamerReferenceNumber
        self.towingVesselOffsetA = towingVesselOffsetA
        self.towingVesselOffsetB = towingVesselOffsetB
        self.towingVesselOffsetZ = towingVesselOffsetZ
        self.towingSeaOffsetA = towingSeaOffsetA
        self.towingSeaOffsetB = towingSeaOffsetB
        self.towingSeaOffsetZ = towingSeaOffsetZ
        self.localOffsetY = localOffsetY
        self.localOffsetZ = localOffsetZ
    
def getH21x0(line):
    h21x0 = H21x0(line[3:4],line[6:9],line[10:17],line[18:25],line[26:32],line[34:41],line[42:49],line[50:56],line[57:64],line[65:71])
    return h21x0

'''H21@1 Streamer Geometry Definitions - continued
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Nominal front stretch section length [11,15] F5.1
Nominal rear stretch section length [17,21] F5.1
Number of active sections [23,25] I3
Length of first active section [27,31] F5.1
Length of second and subsequent live sections[33,37] F5.1
Number of inserted compass sections [39,41] I3
Length of each inserted compass section [43,47] F5.1
Number of inserted acoustic sections [49,51] I3
Length of each inserted acoustic section [53,57] F5.1
Number of inserted depth sections [59,61] I3
Length of each inserted depth section [63,67] F5.1
Quality indicator type for streamer compasses [69,69] I1
Quality indicator type for streamer depth sensors [71,71] I1'''
class H21x1:
    def __init__(self,vesselReferenceNumber,frontSectionLength,rearSectionLehtgh,numberActiveSections,lengthActiveSection,lengthLiveSection,numberCompassSections,
    lengthCompassSection,numberAcousticSections,lengthAcousticSection,numberDepthSections,lengthDepthSection,qualityIndicatorCompasses,qualityIndicatorDepthSensors):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.frontSectionLength = frontSectionLength
        self.rearSectionLehtgh = rearSectionLehtgh
        self.numberActiveSections = numberActiveSections
        self.lengthActiveSection = lengthActiveSection
        self.lengthLiveSection = lengthLiveSection
        self.numberCompassSections = numberCompassSections
        self.lengthCompassSection = lengthCompassSection
        self.numberAcousticSections = numberAcousticSections
        self.lengthAcousticSection = lengthAcousticSection
        self.numberDepthSections = numberDepthSections
        self.lengthDepthSection = lengthDepthSection
        self.qualityIndicatorCompasses = qualityIndicatorCompasses
        self.qualityIndicatorDepthSensors = qualityIndicatorDepthSensors

def getH21x1(line):
    h21x1 = H21x1(line[3:4],line[6:9],line[10:15],line[16:21],line[22:25],line[26:31],line[32:37],line[38:41],line[42:47],line[48:51],line[52:57],
    line[58:61],line[62:67],line[68:69],line[70:71])
    return h21x1

'''H21@2 Definition of Quality Indicator Type for Streamer Compasses
@ = 1..9, Vessel reference number
Definition of quality indicator type [ 7,80] A74 free text'''
class H21x2:
    def __init__(self,vesselReferenceNumber,definitionQualityIndicatorType):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.definitionQualityIndicatorType = definitionQualityIndicatorType
    
def getH21x2(line):
    h21x2 = H21x2(line[3:4],line[6:80])
    return h21x2

'''H21@3 Definition of Quality Indicator Type for Streamer Depth Sensors
@ = 1..9, Vessel reference number
Definition of quality indicator type [ 7,80] A74 free text'''
class H21x3:
    def __init__(self,vesselReferenceNumber,definitionQualityIndicatorType):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.definitionQualityIndicatorType = definitionQualityIndicatorType
    
def getH21x3(line):
    h21x3 = H21x3(line[3:4],line[6:80])
    return h21x3

'''H22@0 Compass Locations
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Node identifier [11,14] I4
Compass serial number [16,23] A8
Local offset to centre of compass [25,32] F8.1
Clipped-on or inserted? [34,34] I1 0 = clipped-on 1 = inserted
May be repeated for one more compass on the same streamer at [36,59]; the streamer reference number is not repeated.'''
class H22x0:
    def __init__(self,vesselReferenceNumber,streamerReferenceNumber,nodeIdentifier,compassSerialNumber,localOffset,isClipped,compassRepeated):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.streamerReferenceNumber = streamerReferenceNumber
        self.nodeIdentifier = nodeIdentifier
        self.compassSerialNumber = compassSerialNumber
        self.localOffset = localOffset
        self.isClipped = isClipped
        self.compassRepeated = compassRepeated
    
def getH22x0(line):
    h22x0 = H22x0(line[3:4],line[6:9],line[10:14],line[15:23],line[24:32],line[33:34],line[35:59])
    return h22x0

'''H23@0 Compass Corrections (Static)
@ = 1..9, Vessel reference number
Compass serial number [ 7,14] A8
Fixed correction to reading [15,20] F6.1 degrees decimal
Line direction 1 [21,23] I3 degrees
Correction to reading [24,27] F4.1 degrees decimal
Line direction 2 [28,30] I3 degrees
Correction to reading [31,34] F4.1 degrees decimal
...
Line direction 8 [70,72] I3 degrees
Correction to reading [73,76] F4.1 degrees decimal
Record may be repeated.'''
class H23x0:
    def __init__(self,vesselReferenceNumber,compassSerialNumber,fixedCorrectionReading,lineDirection,correctionReading):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.compassSerialNumber = compassSerialNumber
        self.fixedCorrectionReading = fixedCorrectionReading
        self.lineDirection = lineDirection
        self.correctionReading = correctionReading
    
def getH23x0(line):
    #Line Direction and Correction Reading Lists
    lineDirection = []
    correctionReading = []    
    for i in range(20,77,7):
        lineDirection.append(line[i:(i+3)])
        correctionReading.append(line[(i+3):(i+7)])
    h23x0 = H23x0(line[3:4],line[6:14],line[14:20],lineDirection,correctionReading)
    return h23x0

'''H2301 Compass Correction Derivation (Dynamic)
Add to static corrections flag [ 7, 7] I1 0 = no; 1 = yes
Description of the algorithm used for the derivation of the corrections [ 9,80] A72 free text'''
class H2301:
    def __init__(self,addStaticCorrectionsFlag,descriptionAlgorithm):
        self.addStaticCorrectionsFlag = addStaticCorrectionsFlag
        self.descriptionAlgorithm = descriptionAlgorithm
    
def getH2301(line):
    h2301 = H2301(line[6:7],line[8:80])
    return h2301

'''H23@1 Compass Corrections (Dynamic)
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Compass serial number [11,18] A8
Compass correction [20,24] F5.1 degrees decimal
May be repeated for 3 more compasses on the same streamer at [26,39], [41,54] and [56,69]; the streamer reference number is thereby not repeated.
Line direction [78,80] I3 degrees'''
class H23x1:
    def __init__(self,vesselReferenceNumber,streamerReferenceNumber,compassSerialNumber,compassCorrection,lineDirection):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.streamerReferenceNumber = streamerReferenceNumber
        self.compassSerialNumber = compassSerialNumber
        self.compassCorrection = compassCorrection
        self.lineDirection = lineDirection
    
def getH23x1(line):
    h23x1 = H23x1(line[3:4],line[6:9],line[10:18],line[19:69],line[77:80])
    return h23x1

'''H24@0 Seismic Receiver Group Definitions
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Reference number first seismic receiver group in regular section [11,14] I4
Local offset of centre of first receiver group [16,23] F8.1
Reference number last seismic receiver group in regular section [25,28] I4
Local offset of centre of last receiver group [30,37] F8.1
Number of seismic receiver groups in section [39,41] I3
Distance between centres of receiver groups [43,48] F6.1'''
class H24x0:
    def __init__(self,vesselReferenceNumber,streamerReferenceNumber,firstSeismicReceiver,localOffsetFirstReceiver,lastSeismicReceiver,localOffsetLastReceiver,
    numberSeismicReceiverGroups,distanceReceiverGroups):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.streamerReferenceNumber = streamerReferenceNumber
        self.firstSeismicReceiver = firstSeismicReceiver
        self.localOffsetFirstReceiver = localOffsetFirstReceiver
        self.lastSeismicReceiver = lastSeismicReceiver
        self.localOffsetLastReceiver = localOffsetLastReceiver
        self.numberSeismicReceiverGroups = numberSeismicReceiverGroups
        self.distanceReceiverGroups = distanceReceiverGroups
    
def getH24x0(line):
    h24x0 = H24x0(line[3:4],line[6:9],line[10:14],line[15:23],line[24:28],line[29:37],line[38:41],line[42:48])
    return h24x0

'''H24@1 Auxiliary Seismic Channel Definition
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Auxiliary channel reference number [11,14] I4
Auxiliary channel type [16,16] I1 0 = timebreak 1 = waterbreak 2...9 = user defined; specify on C0001 record
Local offset to centre of auxiliary channel [18,25] F8.1
Description [27,80] A54 free text'''
class H24x1:
    def __init__(self,vesselReferenceNumber,streamerReferenceNumber,auxiliarChannelRefNumber,auxiliarChannelType,localOffset,description):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.streamerReferenceNumber = streamerReferenceNumber
        self.auxiliarChannelRefNumber = auxiliarChannelRefNumber
        self.auxiliarChannelType = auxiliarChannelType
        self.localOffset = localOffset
        self.description = description

def getH24x1(line):
    h24x1 = H24x1(line[3:4],line[6:9],line[10:14],line[15:16],line[17:25],line[26:80])
    return h24x1

'''H25@0 Streamer Depth Sensor Definitions
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Depth sensor reference or serial number [11,18] A8
Local offset to centre of depth sensor [20,27] F8.1
Depth correction (C-O) [29,33] F5.1
Clipped-on or inserted? [35,35] I1 0 = clipped-on 1 = inserted
Record may be repeated for one more depth sensor on the same streamer at [37,61]; the streamer reference number is not repeated.
Record may be repeated.'''
class H25x0:
    def __init__(self,vesselReferenceNumber,streamerReferenceNumber,depthSensor,localOffset,depthCorrection,isClipped):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.streamerReferenceNumber = streamerReferenceNumber
        self.depthSensor = depthSensor
        self.localOffset = localOffset
        self.depthCorrection = depthCorrection
        self.isClipped = isClipped
    
def getH25x0(line):
    h25x0 = H25x0(line[3:4],line[6:9],line[10:18],line[19:27],line[28:33],line[34:61])
    return h25x0