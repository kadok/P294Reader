#SURVEY NETWORK DEFINITIONS

'''H5000 Node Definition (fixed locations)
Node identifier [ 7,10] I4
Name / description [12,27] A16 free text
Flag for geographical or grid [29,29] I1 0 = geographical co-ordinates 1 = grid
Latitude [31,42] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude [44,55] I3,I2,F6.3,A1 dddmmss.sss E/W
or:
Northing [31,41] N11
"N" [42,42] A1
Easting [44,54] N11
"E" [55,55] A1
Height [57,63] N7 metres or feet
Height measurement unit [65,65] I1 0 = metres 1 = feet
Height datum [67,67] I1 0 = MSL 1 = LAT 2 = LLWS 3 = sea level 4 = spheroid 5 = other (define in separate C0001 record)'''

'''H51@0 Node Definition (vessel, gun array, streamer, towed buoy)
@ = 1..9, Vessel reference number
@ = 0 if relay vessel or buoy
Node identifier [ 7,10] I4
Name / description [12,27] A16 free text
Located on: ref. number [29,31] I3
(Local) offset A [33,39] F7.1
(Local) offset B [41,47] F7.1
(Local) offset Z [49,55] F6.1'''

'''H52## Observation Definition
## = Observation Type
Observation identifier [ 7,10] I4
Observation description [12,27] A16 free text
"At" Node identifier [29,32] I4
"To" Node 1 identifier [34,37] I4
"To" Node 2 identifier [39,42] I4
Measurement Unit Code [44,45] I2
Positioning system identifier [47,49] I3
Positioning system description [51,80] A30 free text'''

'''H5306 Differential Observation - follow up record
Differential observation identifier [ 7,10] I4
Observation 1 identifier [12,15] I4
Observation 2 identifier [17,20] I4
Differential observation description [22,80] A59 free text'''

'''H5307 Composite Range - follow up record
Observation identifier [ 7,10] I4
"To" Node identifier [12,15] I4
Positive (addition) or negative (subtraction)? [17,17] I1 0 = negative range section 1 = positive range section
May be repeated at [19,24], [26,31], [33,38], etc.; the Observation identifier is not repeated.'''

'''H54## Observation Definition (cont'd)
## = Observation type
Observation identifier [ 7,10] I4
Propagation speed [12,23] N12 m/s or feet/s
Lanewidth on baseline or frequency [25,36] N12 metres or feet or Hz
Defined length unit [38,38] I1 0 = metres 1 = feet
Lanewidth or frequency? [40,40] I1 0 = lanewidth on baseline 1 = comparison frequency
Scale factor [42,53] N12
Fixed system (C-O) [55,64] N10
Variable (C-O) [66,73] N8
A priori standard deviation [75,78] N4
Quality indicator type used in (inter-)event records [80,80] I1 0 = no qual. info recorded 1 = standard deviation 2 = signal/noise ratio 3 = system specific 4 = subjective scale'''

'''H5500 Definition of System Specific Quality Indicator
Positioning system identifier [ 7, 9] I3
Definition of quality indicator [11,80] A70 free text'''

'''H56@0 Instrument Correction
@ = 1..9 vessel number
@ = 0 fixed or relay station
Node identifier [ 7,10] I4
Positioning system identifier [12,14] I3
Instrument correction [16,26] N11
Instrument description (serial number, etc) [28,80] A53 free text'''