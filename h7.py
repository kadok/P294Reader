#USER DEFINED OBSERVATION SETS

'''H7000 Definition of User Defined Observation Sets
Observation set reference number [ 7,9] I3
Number of data fields associated with this set [11,12] I2
Description of observation set [14,80] A67 free text
Record may be repeated.'''
class H7000:
    def __init__(self,observationReferenceNumber,numberDataFields,observationSet):
        self.observationReferenceNumber = observationReferenceNumber
        self.numberDataFields = numberDataFields
        self.observationSet = observationSet
    
def getH7000(line):
    h7000 = H7000(line[6:9],line[10:12],line[13:80])
    return h7000

'''H7010 Data Field Definitions
Observation set reference number [ 7,9] I3
Data field number [11,12] I2
Data field width [14,15] I2
Data field description [17,80] A64 free text
Record may be repeated.'''
class H7010:
    def __init__(self,observationReferenceNumber,dataFieldNumber,dataFieldWidth,dataFieldDescription):
        self.observationReferenceNumber = observationReferenceNumber
        self.dataFieldNumber = dataFieldNumber
        self.dataFieldWidth = dataFieldWidth
        self.dataFieldDescription = dataFieldDescription
    
def getH7010(line):
    h7010 = H7010(line[6:9],line[10:12],line[13:15],line[16:80])
    return h7010

'''H7020 User Defined Observation Parameters
Observation set reference number [ 7,9] I3
Data field number [11,12] I2
Quality indicator type [14,14] I1
(C-O) correction [16,.. ] Nx'''
class H7020:
    def __init__(self,observationReferenceNumber,dataFieldNumber,qualityIndicatorType,correction):
        self.observationReferenceNumber = observationReferenceNumber
        self.dataFieldNumber = dataFieldNumber
        self.qualityIndicatorType = qualityIndicatorType
        self.correction = correction
    
def getH7020(line):
    h7020 = H7020(line[6:9],line[10:12],line[13:14],line[15:80])
    return h7020

'''H7021 Definition of Quality Indicator Type for User Defined Observations
Observation set reference number [ 7,9] I3
Data field number [11,12] I2
Definition of quality indicator type [14,80] A67 free text
Record may be repeated.'''
class H7021:
    def __init__(self,observationReferenceNumber,dataFieldNumber,qualityIndicatorDefinition):
        self.observationReferenceNumber = observationReferenceNumber
        self.dataFieldNumber = dataFieldNumber
        self.qualityIndicatorDefinition = qualityIndicatorDefinition
    
def getH7021(line):
    h7021 = H7021(line[6:9],line[10:12],line[13:80])
    return h7021