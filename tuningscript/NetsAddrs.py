#************************************************************************************************************ 
#  ECE 491 Senior Design
#  Winter 2016
#  Team 6 
#
#  Python Script		: NetsAddrs.py
#
#  Purpose: 
#  Provides a method of disabling the processing of unused TCA9548A 1-to-8 I2C Multiplexer
#  channels, and partial MPR 121 address spaces. TouchCtrl is the exclusive user of this module.
#
#  This module contains a list of:
#									Enabled SubNets
#									8 lists of address space enables
#									a two dimensional list of address spaces. 
#  
#     
#  Primary coder																Benjamin
#  Secondary coder																Bret
#  Code contributor																Katrina
#  Code contributor																Ryan
#************************************************************************************************************ 
#  Revision      
#  0	 Supporting script for disabling multiplexed I2C channels, 				
#		 MPR 121 addresses.														Bret		2016-03-20
#                     
#  1	 Enable sub-networks 0 through 5, and enable communications 				
#        for MPR 121 devices in the sub-netowrk's address space.				Bret		2016-04-18             
#                     
#  2	 Final NetsAddrs edits.													Bret		2016-04-23            
#
#************************************************************************************************************

# Sub-networks enables.
#				 0	1	2	3	4	5	6	7
SubNetsEn	=	[0,	0,	1,	0,	0,	0,	0,	0]		# Only one sub-network is enabled.
#SubNetsEn	=	[1,	1,	1,	1,	1,	1,	0,	0]		# All sub-networks enabled.
# Sub-network address enables.
#				 0	1	2	3
EnabledIn0	=	[1,	1,	1,	1] 						# All Address space enabled
EnabledIn1	=	[1,	1,	1,	1]						# All Address space enabled
#EnabledIn2	=	[0,	0,	0,	1]						# All Address space enabled
EnabledIn2	=	[1,	0,	0,	0]						# Only first address enabled
EnabledIn3	=	[1,	0,	0,	0]
EnabledIn4	=	[1,	0,	0,	0] 						# Only first address enabled
EnabledIn5	=	[1,	1,	1,	1]						# All Address space enabled
EnabledIn6	=	[0,	0,	0,	0] 
EnabledIn7	=	[0,	0,	0,	0]
 
EnabledAll	=	[EnabledIn0, EnabledIn1, EnabledIn2, EnabledIn3, EnabledIn4, EnabledIn5, EnabledIn6, EnabledIn7]

