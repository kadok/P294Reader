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

'''H32@0 Description of Gun Array Depth Sensors
@ = 1..9 Vessel reference number
Gun array reference number [ 7, 9] I3
Quality indicator type [11,11] I1
Description of depth sensors [13,80] A62 free text'''

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

'''H32@2 Definition of Quality Indicator Type for Gun Array Depth Sensors
@ = 1..9 Vessel reference number
Gun array reference number [ 7, 9] I3
Definition of quality indicator type [11,80] A70 free text
Record may be repeated.'''

'''H33@0 Definition of Intended Gun Firing Sequence
@ = 1..9 Vessel reference number
Gun array reference number [ 7, 9] I3
Starting gun number [11,13] I3
Active gun mask [15,80] 66*I1 0 = inactive 1 = active
Record may be repeated in case more than 66 guns need to be defined or when the
discontinuity in the gun numbers spans more than 66.'''

'''H34@0 Gun Array Pressure Sensor Definitions
@ = 1..9 Vessel reference number
Gun array reference number [ 7, 9] I3
Gun number [11,13] I3
Sensor serial number [15,22] A8
Sensor correction (C-O) [24,28] F5.1
May be repeated for 2 more pressure sensors on the same gun array at [30,47] and [49,66]; the gun array reference number is not repeated.
Record may be repeated.'''

'''H34@1 Description of Gun Array Pressure Sensors
@ = 1..9 Vessel reference number
Gun array reference number [ 7, 9] I3
Description of gun array pressure sensors [11,80] A70 free text'''

