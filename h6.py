#SATELLITE SYSTEM DEFINITIONS

'''H600# Satellite System Description
# = 1..9, Satellite system reference number
Name [ 7,14] A8 free text
Datum and spheroid number [16,16] I1
Diff. system operator [18,35] A18 free text
Diff. system name [37,46] A10 free text
Software description, version number and additional information [48,80] A33 free text'''

'''H610# Definition of Differential Reference Stations
# = 2, 4..9, Satellite system reference number
Reference station number [ 6, 7] I2
Reference station name [ 9,20] A12 free text
Latitude [22,33] I3,I2,F6.3,A1 dddmmss.sss N/S
Longitude [35,46] I3,I2,F6.3,A1 dddmmss.sss E/W
Spheroidal height [48,54] F7.2 metres
Geoid-Spheroid separation [56,62] F7.2 metres
Geoidal model [64,80] A17 free text'''

'''H620# Satellite Receiver Definition
# = 1..9, Satellite system reference number
"At" Node identifier [ 7,10] I4
Receiver number [12,12] I1
Located on: ref. number [14,16] I3
Offset A [18,24] F7.1
Offset B [26,32] F7.1
Offset Z [34,39] F6.1
Receiver name, description and additional information [41,80] A40 free text'''


#GPS PARAMETERS

'''H6300 GPS parameter recording strategy
Meteorological records [ 7, 7] A1
Ionospheric model records [ 8, 8] A1
Clock model & ephemerides [ 9, 9] A1
This record is provided to allow recording systems to inform processing software of their
intentions with respect to recording slowly changing GPS parameters. Each of the fields
will take one of three values :
0 = Not logged at all, even in header
H = Recorded in header, but not updated in T records
T = Recorded in header and updated in corresponding T records.
however, the following restrictions will apply :
• Clock & ephemerides records (H631#) must be "T" (logged and updated). This is
necessary since the ephemerides of the constellation in view at start of line (or
header writing time) will not necessarily be sufficient to cover all constellations
used during the line.
• The ionospheric records must be either "H" (logged in header) or, for very long
lines, "T" (logged and updated).
Note that this record forms part of the set of records needed to record raw GPS and
DGPS observations, and is not required for the recording of satellite derived positions
only.'''

'''H6301 DGPS differential correction recording strategy
Correction Type [ 7,10] I4
Type Description [11,24] A14
Correction Type [25,28] I4
Type Description [29,42] A14
Correction Type [43,46] I4
Type Description [47,60] A14
Correction Type [61,64] I4
Type Description [65,78] A14
etc.
This record is provided to allow recording systems to inform processing software of their
intentions with respect to recording DGPS correction types parameters. If a Correction
Type is declared here, then it is the recording system's intention that corrections of that
type will be recorded when available. A description of the correction must also be
included to a void ambiguity between the arbitrary message types used by different
service providers.
The correction type field, and the record itself, may repeated as often as is necessary.
Note that this record forms part of the set of records needed to record raw GPS and
DGPS observations, and is not required for the recording of satellite derived positions
only
'''

'''
H6310 GPS ephemerides & clock 
S.V. [ 6, 8] A1,I2 System type code, 1-32
Transmission time of message [ 9,26] E18.12 GPS week seconds'''

'''H6311 GPS clock parameters
S.V. [ 6, 8] A1,I2 System type code, 1-32
S.V. clock drift rate a  f2 [ 9,26] E18.12 seconds/second²
S.V. clock drift a f1 [27,44] E18.12 seconds / second
S.V. clock bias a f0 [45,62] E18.12 seconds
Time of Clock t oc [63,80] E18.12 GPS week seconds
These parameters are available from the GPS message sub-frame 1.'''

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

'''H6313 GPS ephemerides, 2
S.V. [ 6, 8] A1,I2 System type code, 1-32 
Cuc [ 9,26] E18.12 radians
eccentricity e [27,44] E18.12
Cus [45,62] E18.12 radians
√A [63,80] E18.12 √(metres)
Cuc amplitude of the cosine harmonic correction term to the argument of latitude.
Cus amplitude of the sine harmonic correction term to the argument of latitude.
√A square root of the semi-major axis.
These parameters are available from the GPS message sub-frames 2 and 3.'''

'''H6314 GPS ephemerides, 3
S.V. [ 6, 8] A1,I2 System type code, 1-32
Time of ephemeris, toe [ 9,26] E18.12 GPS week seconds
Cic [27,44] E18.12 radians
Ω0[45,62] E18.12 radians
Cis [63,80] E18.12 radians
CIc amplitude of the cosine harmonic correction term to the angle of inclination.
Ω0 right ascension at reference time.
CIS amplitude of the sine harmonic correction term to the angle of inclination.
These parameters are available from the GPS message sub-frames 2 and 3.'''

'''H6315 GPS ephemerides, 4
S.V. [ 6, 8] A1,I2 System type code, 1-32
i0 [ 9,26] E18.12 radians
Crc [27,44] E18.12 metres
argument of perigee ω [45,62] E18.12 radians
rate of right ascension Ω• [63,80] E18.12 radians / second
i0 inclination angle at reference time.
CRC amplitude of the cosine harmonic correction term to the orbit radius.
These parameters are available from the GPS message sub-frames 2 and 3.'''

'''H6316 GPS ephemerides, 5
S.V. [ 6, 8] A1,I2 System type code, 1-32
Rate of inclination angle i• [ 9,26] E18.12 radians / second
Codes on L2 [27,44] E18.12
GPS week number [45,62] E18.12
L2 P data flag [63,80] E18.12'''

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
recording of any raw GPS observations.
H6320 GPS UTC parameters
term of UTC polynomial A0 [ 6,23] E18.12 seconds
term of UTC polynomial A1 [24,41] E18.12 seconds / second
reference time of time, tot [42,50] I9 seconds
UTC week reference no. WNt [51,59] I9
Leap seconds delta time ∆tLSF [60,65] I6 seconds'''

'''H6321 GPS ionospheric model parameters, 1
α0 [ 6,17] E12.4 seconds
α1 [18,29] E12.4 seconds / semicircle
α2 [30,41] E12.4 seconds / semicircle²
α3 [42,53] E12.4 seconds / semicircle³
These parameters are available from the GPS message sub-frame 4, page 18.'''

'''H6322 GPS ionospheric model parameters, 2
β0 [ 6,17] E12.4 seconds
β1 [18,29] E12.4 seconds / semicircle
β2 [30,41] E12.4 seconds / semicircle²
β3 [42,53] E12.4 seconds / semicircle³'''

'''H6330 Meteorological data
Surface air pressure [ 6,12] F7.1 millibars
Dry air temperature [13,19] F7.1 degrees Celsius
Wet air temperature [20,26] F7.1 degrees Celsius
Relative humidity [27,33] F7.1 percent
Either, but not both, of the last two fields may be left blank.'''


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

'''H66## Differential Correction Source Description
## is the Differential Correction Source Identifier
DCS system operator [ 7, 24] A18 free text
DCS component name [25, 43] A18 free text
DCS component description [44, 80] A37 free text'''

'''H67@0 Height aiding values
@ = 1..9 vessel number
@ = 0 fixed or relay station
Node identifier [ 6, 9] I4
Positioning system identifier [10,12] I3
Ellipsoid height of antenna [13,23] N11 metres
Description of source of value [24,80] A57 free text'''