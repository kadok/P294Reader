#GENERAL DEFINITIONS

'''H0000 Line Name
Line Name: [ 6,15] A10
Line name [29,44] A16
Line sequence number [46,49] I4
Line description [50,80] A31 free text'''
class H0000:
    def __init__(self,title,lineName,sequenceNumber,description):
        self.title = title
        self.lineName = lineName
        self.sequenceNumber = sequenceNumber
        self.description = description

def getH0000(line):
    h0000 = H0000(line[5:15],line[28:44],line[45:49],line[49:80])
    return h0000

'''H0001 Project Name
Project Name: [ 6,18] A13
Project identifier [29,36] A8
Project name [38,62] A25 free text
Start date of survey [64,71] I4,I2,I2 YYYYMMDD
End date of survey [73,80] I4,I2,I2 YYYYMMDD'''
class H0001:
    def __init__(self,title,projectIdentifier,projectName,startDateSurvey,endDateSurvey):
        self.title = title
        self.projectIdentifier = projectIdentifier
        self.projectName = projectName
        self.startDateSurvey = startDateSurvey
        self.endDateSurvey = endDateSurvey
    
def getH0001(line):
    h0001 = H0001(line[5:18],line[28:36],line[37:62],line[64:71],line[73:80])
    return h0001

'''H0002 Project Description
Project Description: [ 6,25] A20
Survey type,location [29,80] A52 free text'''
class H0002:
    def __init__(self,projectDescription,surveyTypeLocation):
        self.projectDescription = projectDescription
        self.surveyTypeLocation = surveyTypeLocation
    
def getH0002(line):
    h0002 = H0002(line[5:25],line[28:80])
    return h0002

'''H0003
Media Specification: [ 6,25] A20
Date of issue [29,36] I4,I2,I2 YYYYMMDD
Media label [38,47] A10
Prepared by [49,64] A16 free text
Format name [66,76] A11 e.g. UKOOA P2/94
Format revision code [78,80] F3.1 e.g. 1.0'''
class H0003:
    def __init__(self,mediaSpecification,dataIssue,mediaLabel,preparedBy,formatName,formatRevisionCode):
        self.mediaSpecification = mediaSpecification
        self.dataIssue = dataIssue
        self.mediaLabel = mediaLabel
        self.preparedBy = preparedBy
        self.formatName = formatName
        self.formatRevisionCode = formatRevisionCode
    
def getH0003(line):
    h0003 = H0003(line[5:25],line[28:36],line[37:47],line[48:64],line[65:76],line[77:80])
    return h0003

'''H0004 Client
Client: [ 6,12] A7
Description of client [29,80] A52 free text'''
class H0004:
    def __init__(self,client,descriptionClient):
        self.client = client
        self.descriptionClient = descriptionClient
    
def getH0004(line):
    h0004 = H0004(line[5:12],line[28:80])
    return h0004

'''H0005 Geophysical Contractor
Geophysical Contractor: [ 6,28] A23
Description of geophysical contractor [29,80] A52 free text'''
class H0005:
    def __init__(self,geophysicalContractor,descriptionGeophysicalContractor):
        self.geophysicalContractor = geophysicalContractor
        self.descriptionGeophysicalContractor = descriptionGeophysicalContractor
    
def getH0005(line):
    h0005 = H0005(line[5:28],line[28:80])
    return h0005

'''H0006 Positioning Contractor
Positioning Contractor: [ 6,28] A23
Description of positioning contractor [29,80] A52 free text'''
class H0006:
    def __init__(self,positioningContractor,descriptionPositionigContractor):
        self.positioningContractor = positioningContractor
        self.descriptionPositionigContractor = descriptionPositionigContractor
    
def getH0006(line):
    h0006 = H0006(line[5:28],line[28:80])
    return h0006

'''H0007 Positioning Processing Contractor
"Processing Contractor:" [ 6,27] A22
Description of positioning processing contractor [29,80] A52 free text'''
class H0007:
    def __init__(self,processingContractor,descriptionPositioningProcessingContractor):
        self.processingContractor = processingContractor
        self.descriptionPositioningProcessingContractor = descriptionPositioningProcessingContractor
    
def getH0007(line):
    h0007 = H0007(line[5:27],line[28:80])
    return h0007

'''H00@8 Line Parameters
@ = 0,CMP position
@ = 1..9,Vessel reference number
"Line Parameters Vessel:" [ 6,28] A23
Vessel reference number(0 for CMP) [30,30] I1
Flag for geographical or grid [32,32] I1 0 = geographical co-ordinates 1 = grid
Start Of Line Latitude [34,45] I3,I2,F6.3,A1 dddmmss.sss N/S
Start Of Line Longitude [46,57] I3,I2,F6.3,A1 dddmmss.sss E/W
or:
Start Of Line Northing [34,44] N11 "N" [45,45] A1
Start Of Line Easting [46,56] N11 "E" [57,57] A1
First shotpoint number [59,64] I6
Shotpoint number increment [66,68] I3
Shotpoint interval [70,75] F6.2
Length unit [77,77] I1 metres or feet 0 = metres 1 = feet
Number of additional way points defined in H00@9 records [79,80] I2'''
class H00x8:
    def __init__(self,vesselReference,lineParametersVessel,vesselReferenceNumber,flagGeographicalGrid,startLineLatitude,startLineLongitude,
    startLineNorthing,startLineEasting,N,E,firstShotpointNumber,shotpointInterval,lengthUnit,numberAddtionalWaypoints):
        self.vesselReference = vesselReference
        self.lineParametersVessel = lineParametersVessel
        self.vesselReferenceNumber = vesselReferenceNumber
        self.flagGeographicalGrid = flagGeographicalGrid
        self.startLineLatitude = startLineLatitude
        self.startLineLongitude = startLineLongitude
        self.startLineNorthing = startLineNorthing
        self.startLineEasting = startLineEasting
        self.N = N
        self.E = E
        self.firstShotpointNumber = firstShotpointNumber
        self.shotpointInterval = shotpointInterval
        self.lengthUnit = lengthUnit
        self.numberAddtionalWaypoints = numberAddtionalWaypoints
    
def getH00X8(line):
    h00x8 = H00x8(line[4:4],line[6:28],line[30:30],line[32:32],line[34:45],line[46:56],
    line[34:44],line[46:56],line[45:45],line[57:57],line[66:68],line[70:75],line[77:77],line[79:80])
    return h00x8

'''H00@9 Additional Waypoint Definitions
@ = 0,CMP position
@ = 1..9,Vessel reference number
Vessel reference number (0 for CMP) [ 7,7] I1
Waypoint number [ 9,11] I3
Waypoint Latitude [13,24] I3,I2,F6.3,A1 dddmmss.sss N/S
Waypoint Longitude [26,37] I3,I2,F6.3,A1 dddmmss.sss E/W
or:
Waypoint Northing [13,23] N11 "N" [24,24] A1
Waypoint Easting [26,36] N11 "E" [37,37] A1'''
class H00x9:
    def __init__(self,vesselReference,vesselReferenceNumber,waypointNumber,waypointLatitude,waypointLongitude,waypointNorthing,waypointEasting,N,E):
        self.vesselReference = vesselReference
        self.vesselReferenceNumber = vesselReferenceNumber
        self.waypointNumber = waypointNumber
        self.waypointLatitude = waypointLatitude
        self.waypointLongitude = waypointLongitude
        self.waypointNorthing = waypointNorthing
        self.waypointEasting = waypointEasting
        self.N = N
        self.E = E
    
def getH00x9(line):
    h00x9 = H00x9(line[4:4],line[7:7],line[9:11],line[13:24],line[26:37],line[13:23],line[24:24],line[26:36],line[37:37])
    return h00x9

'''C000x Comments:
C0001 Additional Information - Entire Project Related
Project related additional information [ 6,80] A75 free text

C0002 Additional Information - Line Related
Line related additional information [ 6,80] A75 free text

C0003  Additional Information - (Inter-)Event Related
(Inter-)event related additional information [ 6,80] A75 free text'''
class C000x:
    def __init__(self,commentType,addtionalInformation):
        self.commentType = commentType
        self.addtionalInformation = addtionalInformation
    
def getC000x(line):
    c000x = C000x(line[5:5],line[6:80])
    return c000x


#GEODETIC DEFINITIONS

''' H0100 Magnetic Variation - General Information
Date for which the Magnetic Variation values are valid [ 7,14] I4,I2,I2 YYYYMMDD
Number of points in grid [16,19] I 4
Defined in geographical or grid [21,21] I1 0= geographical co-ordinates 1 = grid
Source of Magnetic Variation [23,80] A58 free text'''
class H0100:
    def __init__(self,magneticVariationDate,gridPointsNumber,magneticVariationType,magneticVariationSource):
        self.magneticVariationDate = magneticVariationDate
        self.gridPointsNumber = gridPointsNumber
        self.magneticVariationType = magneticVariationType
        self.magneticVariationSource = magneticVariationSource
    
def getH0100(line):
    h0100 = H0100(line[7:14],line[16:19],line[21:21],line[23:80])
    return h0100

'''H0101 Magnetic Variation - Grid Data
Point number [ 7,10] I4
If geographical co-ords:
Latitude of point [12,23] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude of point [25,36] I3,I2,F6.3,A1 dddmmss.sss E/W
If rectangular co-ords:
Northing [12,22] N11
"N" [23,23] A1
Easting [25,35] N11
"E" [36,36] A1
Magnetic Variation [38,44] F7.3 +/- degrees decimal
Secular change in Magnetic
Variation in this point [46,51] F6.4 +/- degr.dec./year
Record may be repeated.'''
class H0101:
    def __init__(self,pointNumber,latitudePoint,longitudePoint,Northing,N,Easting,E,magneticVariation,variationPoint):
        self.pointNumber = pointNumber
        self.latitudePoint = latitudePoint
        self.longitudePoint = longitudePoint
        self.Northing = Northing
        self.N = N
        self.Easting = Easting
        self.E = E
        self.magneticVariation = magneticVariation
        self.variationPoint = variationPoint
    
def getH0101(line):
    h0101 = H0101(line[7:10],line[12:23],line[25:36],line[12:22],line[23:23],line[25:35],line[36:36],line[38:44],line[46:51])
    return h0101

'''H011# Datum and Spheroid Definitions
# = 1..9,datum & spheroid number
Datum name [ 7,24] A18
Spheroid name [25,43] A19
Semi-major axis (a) [44,55] N12
Conversion factor to metres [57,68] N12
Inverse flattening (1/f) [70,80] N11'''
class H011x:
    def __init__(self,datumNumber,datumName,spheroidName,semiMajorAxis,conversationFactorMetres,inverseFlattening):
        self.datumNumber = datumNumber
        self.datumName = datumName
        self.spheroidName = spheroidName
        self.semiMajorAxis = semiMajorAxis
        self.conversationFactorMetres = conversationFactorMetres
        self.inverseFlattening = inverseFlattening
    
def getH011x(line):
    h011x = H011x(line[5:5],line[7:24],line[25:43],line[44:55],line[57:68],line[70:80])
    return h011x
    
'''H0120 Seven Parameter Cartesian Datum Shifts
From Datum 1 to Datum 2
Datum 1: datum/spheroid number [ 7,7] I1
Datum 2: datum/spheroid number [ 9,9] I1
Rotation convention [11,11] I1 0 = position vector rotation (BursaWolf) 1 = co-ordinate frame rotation
X shift (δX) [13,22] F10.2 metres
Y shift (δY) [24,33] F10.2 "
Z shift (δZ) [35,44] F10.2 "
X rotation (θx) [46,53] F8.4 seconds of arc
Y rotation (θy) [55,62] F8.4 "
Z rotation (θz) [64,71] F8.4 "
Scale correction (S) [73,80] F8.4 ppm'''
class H0120:
    def __init__(self,datum1,datum2,rotationConvention,xShift,yShift,zShift,xRotation,yRotation,zRotation,scaleCorrection):
        self.datum1 = datum1
        self.datum2 = datum2
        self.rotationConvention = rotationConvention
        self.xShift = xShift
        self.yShift = yShift
        self.zShift = zShift
        self.xRotation = xRotation
        self.yRotation = yRotation
        self.zRotation = zRotation
        self.scaleCorrection = scaleCorrection
    
def getH0120(line):
    h0120 = H0120(line[7:7],line[9:9],line[11:11],line[13:22],line[24:33],line[35:44],line[46:53],line[55:62],line[64:71],line[73:80])
    return h0120

'''H0130 Other Datum Shift Parameters
From Datum 1 to Datum 2
Datum 1: datum/spheroid number [ 7,7] I1
Datum 2: datum/spheroid number [ 8,8] I1
Sequence number of record in this definition [ 9,10] I2 "/" [11,11] A1
Total number of records used for this definition [12,13] I2
Description of datum conversion [15,80] A65 free text'''
class H0130:
    def __init__(self,datum1,datum2,sequenceRecordNumber,totalRecordsNumber,descriptionConversation):
        self.datum1 = datum1
        self.datum2 = datum2
        self.sequenceRecordNumber = sequenceRecordNumber
        self.totalRecordsNumber = totalRecordsNumber
        self.descriptionConversation = descriptionConversation
    
def getH0130(line):
    h0130 = H0130(line[7:7],line[8:8],line[9:11],line[12:13],line[15:80])
    return h0130

'''H0140 Projection Type
Projection type code record [ 7,9] I3 see note following record H0199
Co-ordinates conversion factor to metres [11,20] N10
Projection type and name [22,80] A59 free text'''
class H0140:
    def __init__(self,typeCodeRecord,coordinatesConversion,projectionTypeName):
        self.typeCodeRecord = typeCodeRecord
        self.coordinatesConversion = coordinatesConversion
        self.projectionTypeName = projectionTypeName
    
def getH0140(line):
    h0140 = H0140(line[7:9],line[11:20],line[22:80])
    return h0140

'''H0150 (Universal) Transverse Mercator Projection
Zone number [ 7,8] I2 (UTM only)
Latitude of grid origin [10,21] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude of grid origin [23,34] I3,I2,F6.3,A1 dddmmss.sss E/W
Grid Northing at grid origin [36,46] N11
"N" [47,47] A1
Grid Easting at grid origin [48,58] N11
"E" [59,59] A1
Scale factor at longitude of origin [61,72] N12'''
class H0150:
    def __init__(self,zoneNumber,latitudeGrid,longitudeGrid,gridNorthing,N,gridEasting,E,scaleFactor):
        self.zoneNumber = zoneNumber
        self.latitudeGrid = latitudeGrid
        self.longitudeGrid = longitudeGrid
        self.gridNorthing = gridNorthing
        self.N = N
        self.gridEasting = gridEasting
        self.E = E
        self.scaleFactor = scaleFactor
    
def getH0150(line):
    h0150 = H0150(line[7:8],line[10:21],line[23:34],line[36:46],line[47:47],line[48:58],line[59:59],line[61:72])
    return h0150

'''H0160 Mercator Projection
Latitude of grid origin [ 7,18] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude of grid origin [20,31] I3,I2,F6.3,A1 dddmmss.sss E/W
Grid Northing at grid origin [33,43] N11
"N" [44,44] A1
Grid Easting at grid origin [45,55] N11
"E" [56,56] A1
Scale factor at latitude of origin [58,69] N12'''
class H0160:
    def __init__(self,latitudeGrid,longitudeGrid,gridNorthing,N,gridEasting,E,scaleFactor):
        self.latitudeGrid = latitudeGrid
        self.longitudeGrid = longitudeGrid
        self.gridNorthing = gridNorthing
        self.N = N
        self.gridEasting = gridEasting
        self.E = E
        self.scaleFactor = scaleFactor
    
def getH0160(line):
    h0160 = H0160(line[7:18],line[20:31],line[33:43],line[44:44],line[45:55],line[56:56],line[58:69])
    return h0160

'''H0170 Lambert Projection
Latitude of (first) standard parallel [ 7,18] I3,I2,F6.3,A1 dddmmss.sss N/S
Latitude of second standard parallel [20,31] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude of grid origin [33,44] I3,I2,F6.3,A1 dddmmss.sss E/W
Grid Northing at grid origin [45,55] N11
"N" [56,56] A1
Grid Easting at grid origin [57,67] N11
"E" [68,68] A1
Scale factor at standard parallels [69,80] N12'''
class H0170:
    def __init__(self,firstLatitude,secondLatitude,longitudeGrid,gridNorthing,N,gridEasting,E,scaleFactor):
        self.firstLatitude = firstLatitude
        self.secondLatitude = secondLatitude
        self.longitudeGrid = longitudeGrid
        self.gridNorthing = gridNorthing
        self.N = N
        self.gridEasting = gridEasting
        self.E = E
        self.scaleFactor = scaleFactor
    
def getH0170(line):
    h0170 = H0170(line[7:18],line[20:31],line[33:44],line[45:55],line[56:56],line[57:67],line[68:68],line[69:80])
    return h0170

'''H0180 Skew Orthomorphic and Oblique Mercator Projection
Latitude of start point [ 7,18] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude of start point [19,30] I3,I2,F6.3,A1 dddmmss.sss E/W
Latitude of end point [31,42] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude of end point [43,54] I3,I2,F6.3,A1 dddmmss.sss E/W
Bearing of initial line of projection in end point('true origin') [55,66] N12 degrees decimal
Angle from skew to rectified grid in start point ('false origin') [67,78] N12 degrees decimal clockwise positive'''
class H0180:
    def __init__(self,latitudeStartPoint,longitudeStartPoint,latitudeEndPoint,longitudeEndPoint,bearingProjection,angleGridStartPoint):
        self.latitudeStartPoint = latitudeStartPoint
        self.longitudeStartPoint = longitudeStartPoint
        self.latitudeEndPoint = latitudeEndPoint
        self.longitudeEndPoint = longitudeEndPoint
        self.bearingProjection = bearingProjection
        self.angleGridStartPoint = angleGridStartPoint
    
def getH0180(line):
    h0180 = H0180(line[7:18],line[19:30],line[31:42],line[43:54],line[55:66],line[67:78])
    return h0180

'''H0181 Skew Orthomorphic and Oblique Mercator Projection (continued)
Scale factor at end point [ 7,18] N12
Grid Northing at end point [ 19,29] N11
'N' [ 30,30] A1
Grid Easting at end point [ 31,41] N11
'E' [ 42,42] A1'''
class H0181:
    def __init__(self,scaleFactor,gridNorthing,N,gridEasting,E):
        self.scaleFactor = scaleFactor
        self.gridNorthing = gridNorthing
        self.N = N
        self.gridEasting = gridEasting
        self.E = E
        
    
def getH0181(line):
    h0181 = H0181(line[7:18],line[19:29],line[30:30],line[31:41],line[42:42])
    return h0181

'''H0190 Stereographic Projection
Latitude of grid origin [ 7,18] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude of grid origin [19,30] I3,I2,F6.3,A1 dddmmss.sss E/W
Grid Northing at grid origin [32,42] N11
"N" [43,43] A1
Grid Easting at grid origin [44,54] N11
"E" [55,55] A1
Scale factor at grid origin [56,67] N12
Standard parallel (for polar version only) [69,80] I3,I2,F6.3,A1 dddmmss.sss E/W'''
class H0190:
    def __init__(self,latitudeGrid,longitudeGrid,gridNorthing,N,gridEasting,E,scaleFactor,standardParallel):
        self.latitudeGrid = latitudeGrid
        self.longitudeGrid = longitudeGrid
        self.gridNorthing = gridNorthing
        self.N = N
        self.gridEasting = gridEasting
        self.E = E
        self.scaleFactor = scaleFactor
        self.standardParallel = standardParallel
    
def getH0190(line):
    h0190 = H0190(line[7:18],line[19:30],line[32:42],line[43:43],line[44:54],line[55:55],line[56:67],line[69:80])
    return h0190

'''H0199 Any Other Projection
Sequence number of record in this definition [ 7,8] I2 "/" [ 9,9] A1
Total number of records used for this definition [10,11] I2
Map projection parameters [13,80] A68 free text'''
class H0199:
    def __init__(self,sequenceNumber,totalNumberRecords,mapProjectionParameters):
        self.sequenceNumber = sequenceNumber
        self.totalNumberRecords = totalNumberRecords
        self.mapProjectionParameters = mapProjectionParameters
    
def getH0199(line):
    h0199 = H0199(line[7:9],line[10:11],line[13:80])
    return h0199


#SURVEY SUMMARY DATA

'''H0200 General Summary Information
Number of survey vessels [ 7,7] I1
Number of relay vessels or buoys [ 9,10] I2
Number of external network nodes [12,13] I2
Number of datums/spheroids defined [15,15] I1
Offset mode [17,17] I1 0 = polar 1 = rectangular
Offset measurement units:
for offset distances [19,19] I1 0 = metres 1 = feet
for offset angles [21,21] I1 0 = degrees decimal 1 = grads'''
class H0200:
    def __init__(self,numberSurveyVessels,numberRelayVessels,numberExternalNetworkNodes,numberDatumsDefined,offsetMode,offsetDistances,offsetAngles):
        self.numberSurveyVessels = numberSurveyVessels
        self.numberRelayVessels = numberRelayVessels
        self.numberExternalNetworkNodes = numberExternalNetworkNodes
        self.numberDatumsDefined = numberDatumsDefined
        self.offsetMode = offsetMode
        self.offsetDistances = offsetDistances
        self.offsetAngles = offsetAngles
    
def getH0200(line):
    h0200 = H0200(line[7:7],line[9:10],line[12:13],line[15:15],line[17:17],line[19:19],line[21:21])
    return h0200

'''H021@ Vessel Summary Information
@ = 1..9,Vessel reference number @ = 0 if relay vessel
Vessel name/description [ 6,40] A35 free text
Vessel reference number [43,44] I2
Number of streamers [50,51] I2
Number of gun arrays [53,54] I2
Number of buoys [56,57] I2
Number of echo sounders [59,59] I1
Pitch/Roll/Heave sensors [61,61] I1 0 = no; 1 = yes
Number of USBL systems [63,63] I1
Number of satellite receivers [65,66] I2
Number of network nodes [68,70] I3'''
class H021x:
    def __init__(self,vesselReference,vesselName,vesselReferenceNumber,numberStreamers,numberGunArrays,
    numberBuoys,numberEchoSounders,directionSensors,numberUSBLSystems,numberSatelliteReceivers,numberNetworkNodes):
        self.vesselReference = vesselReference
        self.vesselName = vesselName
        self.vesselReferenceNumber = vesselReferenceNumber
        self.numberStreamers = numberStreamers
        self.numberGunArrays = numberGunArrays
        self.numberBuoys = numberBuoys
        self.numberEchoSounders = numberEchoSounders
        self.directionSensors = directionSensors
        self.numberUSBLSystems = numberUSBLSystems
        self.numberSatelliteReceivers = numberSatelliteReceivers
        self.numberNetworkNodes = numberNetworkNodes
    
def getH021x(line):
    h021x = H021x(line[5:5],line[6:40],line[43:44],line[50:51],line[53:54],line[56:57],line[59:59],line[61:61],line[63:63],line[65:66],line[68:70])
    return h021x

'''H022@ Streamer Summary Information
@ = 1..9,Vessel reference number
Streamer description [ 6,40] A35 free text
Streamer reference number [42,44] I3
"Towed by" ref. number [46,48] I3
Number of buoys [56,57] I2
Number of network nodes exclusive of magnetic compasses [68,70] I3
Number of magnetic compasses [72,73] I2
Number of depth sensors [75,76] I2
Number of seismic receiver groups [78,80] I3'''
class H022x:
    def __init__(self,vesselReferenceNumber,streamerDescription,streamerReferenceNumber,towedReferenceNumber,
    numberBuoys,numberNetworkNodes,numberMagneticCompasses,numberDepthSensors,numberSeismicReceiverGroups):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.streamerDescription = streamerDescription
        self.streamerReferenceNumber = streamerReferenceNumber
        self.towedReferenceNumber = towedReferenceNumber
        self.numberBuoys = numberBuoys
        self.numberNetworkNodes = numberNetworkNodes
        self.numberMagneticCompasses = numberMagneticCompasses
        self.numberDepthSensors = numberDepthSensors
        self.numberSeismicReceiverGroups = numberSeismicReceiverGroups
    
def getH022x(line):
    h022x = H022x(line[5:5],line[6:40],line[42:44],line[46:48],line[56:57],line[68:70],line[72:73],line[75:76],line[78:80])
    return h022x

'''H023@ Gun Array Summary Information
@ = 1..9,Vessel reference number
Gun array description [ 6,40] A35 free text
Gun array ref. number [42,44] I3
"Towed by" ref. number [46,48] I3
Number of buoys [56,57] I2
Number of satellite receivers [65,66] I2
Number of network nodes [68,70] I3
Number of depth sensors [75,76] I2'''
class H023x:
    def __init__(self,vesselReferenceNumber,gunArrayDescription,gunArrayReferenceNumber,towedReferenceNumber,
    numberBuoys,numberSatelliteReceivers,numberNetworkNodes,numberDepthSensors):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.gunArrayDescription = gunArrayDescription
        self.gunArrayReferenceNumber = gunArrayReferenceNumber
        self.towedReferenceNumber = towedReferenceNumber
        self.numberBuoys = numberBuoys
        self.numberSatelliteReceivers = numberSatelliteReceivers
        self.numberNetworkNodes = numberNetworkNodes
        self.numberDepthSensors = numberDepthSensors
    
def getH023x(line):
    h023x = H023x(line[5:5],line[6:40],line[42:44],line[46:48],line[56:57],line[65:66],line[68:70],line[75:76])
    return h023x

'''H024@ Towed Buoy Summary Information
@ = 1..9,Vessel reference number
Towed buoy description [ 6,40] A35 free text
Towed buoy ref. number [42,44] I3
"Towed by" ref. number [46,48] I3
Number of other buoys towed by this buoy [56,57] I2
Number of satellite receivers [65,66] I2
Number of network nodes [68,70] I3'''
class H024x:
    def __init__(self,vesselReferenceNumber,towedBuoyDescription,towedBuoyReferenceNumber,towedReferenceNumber,
    numberOtherBuoys,numberSatelliteReceivers,numberNetworkNodes):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.towedBuoyDescription = towedBuoyDescription
        self.towedBuoyReferenceNumber = towedBuoyReferenceNumber
        self.towedReferenceNumber = towedReferenceNumber
        self.numberOtherBuoys = numberOtherBuoys
        self.numberSatelliteReceivers = numberSatelliteReceivers
        self.numberNetworkNodes = numberNetworkNodes
    
def getH024x(line):
    h024x = H024x(line[5:5],line[6:40],line[42:44],line[46:48],line[56:57],line[65:66],line[68:70])
    return h024x