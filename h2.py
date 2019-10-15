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

'''H21@2 Definition of Quality Indicator Type for Streamer Compasses
@ = 1..9, Vessel reference number
Definition of quality indicator type [ 7,80] A74 free text'''

'''H21@3 Definition of Quality Indicator Type for Streamer Depth Sensors
@ = 1..9, Vessel reference number
Definition of quality indicator type [ 7,80] A74 free text'''

'''H22@0 Compass Locations
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Node identifier [11,14] I4
Compass serial number [16,23] A8
Local offset to centre of compass [25,32] F8.1
Clipped-on or inserted? [34,34] I1 0 = clipped-on 1 = inserted
May be repeated for one more compass on the same streamer at [36,59]; the streamer reference number is not repeated.'''

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

'''H2301 Compass Correction Derivation (Dynamic)
Add to static corrections flag [ 7, 7] I1 0 = no; 1 = yes
Description of the algorithm used for the derivation of the corrections [ 9,80] A72 free text'''

'''H23@1 Compass Corrections (Dynamic)
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Compass serial number [11,18] A8
Compass correction [20,24] F5.1 degrees decimal
May be repeated for 3 more compasses on the same streamer at [26,39], [41,54] and [56,69]; the streamer reference number is thereby not repeated.
Line direction [78,80] I3 degrees'''

'''H23@1 Compass Corrections (Dynamic)
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Compass serial number [11,18] A8
Compass correction [20,24] F5.1 degrees decimal
May be repeated for 3 more compasses on the same streamer at [26,39], [41,54] and [56,69]; the streamer reference number is thereby not repeated.
Line direction [78,80] I3 degrees'''

'''H24@0 Seismic Receiver Group Definitions
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Reference number first seismic receiver group in regular section [11,14] I4
Local offset of centre of first receiver group [16,23] F8.1
Reference number last seismic receiver group in regular section [25,28] I4
Local offset of centre of last receiver group [30,37] F8.1
Number of seismic receiver groups in section [39,41] I3
Distance between centres of receiver groups [43,48] F6.1'''

'''H24@1 Auxiliary Seismic Channel Definition
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Auxiliary channel reference number [11,14] I4
Auxiliary channel type [16,16] I1 0 = timebreak 1 = waterbreak 2...9 = user defined; specify on C0001 record
Local offset to centre of auxiliary channel [18,25] F8.1
Description [27,80] A54 free text'''

'''H25@0 Streamer Depth Sensor Definitions
@ = 1..9, Vessel reference number
Streamer reference number [ 7, 9] I3
Depth sensor reference or serial number [11,18] A8
Local offset to centre of depth sensor [20,27] F8.1
Depth correction (C-O) [29,33] F5.1
Clipped-on or inserted? [35,35] I1 0 = clipped-on 1 = inserted
Record may be repeated for one more depth sensor on the same streamer at [37,61]; the streamer reference number is not repeated.
Record may be repeated.'''