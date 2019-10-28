#TOWED BUOY DEFINITIONS
'''H41@0 Towed Buoy Geometry Definitions
@ = 1..9 Vessel reference number
Towed buoy ref. number [ 7,9] I3
Towed by: ref. number [11,13] I3
Offsets from towing body's Reference Point to:
- towpoint-on-towing-body:
Offset A [15,21] F7.1
Offset B [23,29] F7.1
Offset Z [31,36] F6.1
- towpoint-in-sea:
Offset A [39,45] F7.1
Offset B [47,53] F7.1
Offset Z [55,60] F6.1
Description of the towed buoy [62,80] A19 free text'''
class H41x0:
    def __init__(self,vesselReferenceNumber,towedBuoyReferenceNumber,towedByReferenceNumber,bodyOffsetA,bodyOffsetB,bodyOffsetZ,
    seaOffsetA,seaOffsetB,seaOffsetZ,descriptionTowedBuoy):
        self.vesselReferenceNumber = vesselReferenceNumber
        self.towedBuoyReferenceNumber = towedBuoyReferenceNumber
        self.towedByReferenceNumber = towedByReferenceNumber
        self.bodyOffsetA = bodyOffsetA
        self.bodyOffsetB = bodyOffsetB
        self.bodyOffsetZ = bodyOffsetZ
        self.seaOffsetA = seaOffsetA
        self.seaOffsetB = seaOffsetB
        self.seaOffsetZ = seaOffsetZ
        self.descriptionTowedBuoy = descriptionTowedBuoy

def getH41x0(line):
    h41x0 = H41x0(line[4:4],line[7:9],line[11:13],line[15:21],line[23:29],line[31:36],line[39:45],line[47:53],line[55:60],line[62:80])
    return h41x0
