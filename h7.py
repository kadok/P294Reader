#USER DEFINED OBSERVATION SETS

'''H7000 Definition of User Defined Observation Sets
Observation set reference number [ 7, 9] I3
Number of data fields associated with this set [11,12] I2
Description of observation set [14,80] A67 free text
Record may be repeated.'''

'''H7010 Data Field Definitions
Observation set reference number [ 7, 9] I3
Data field number [11,12] I2
Data field width [14,15] I2
Data field description [17,80] A64 free text
Record may be repeated.'''

'''H7020 User Defined Observation Parameters
Observation set reference number [ 7, 9] I3
Data field number [11,12] I2
Quality indicator type [14,14] I1
(C-O) correction [16, .. ] Nx'''

'''H7021 Definition of Quality Indicator Type for User Defined Observations
Observation set reference number [ 7, 9] I3
Data field number [11,12] I2
Definition of quality indicator type [14,80] A67 free text
Record may be repeated.
Example of user defined observations
Header data
H7000 001 01 Gravity data: standard sensor S/N 31
H7000 001 Last in-port gravity tie: Aberdeen 31 October 1991
H7010 001 01 06 Gravity count in milligals
H7010 001 02 06 Spring tension in milligals
H7010 001 03 04 Average beam
H7010 001 04 04 Total cross coupling
H7010 001 05 04 Total correction
H7010 001 06 04 Vertical cross coupling
H7010 001 07 04 Along cross coupling
H7010 001 08 04 Across cross coupling
H7010 001 09 04 Vertical correction
H7010 001 10 04 Average across acceleration
H7010 001 11 04 Average along acceleration
H7010 001 12 04 Second order cross coupling
H7010 001 13 04 Offset calibration
Event data
E70100010112341234560212341234560312341234
E70100010412341234051234123406123412340712341234
E70100010812341234091234123410123412341112341234
E701000112123412341312341234
Inter-event data
T701000101123401020311234560212340102031123456
T701000103123401020311234'''