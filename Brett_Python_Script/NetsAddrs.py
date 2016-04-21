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
#		 PR 121 addresses.														Bret		2016-03-20
#                     
#  x	 Edits.																	TBD			2016-0x-xx
#
#************************************************************************************************************

# Sub-networks enables.
#			 0	1	2	3	4	5	6	7
#SubNetsEn	=	[1,	0,	0,	0,	0,	0,	0,	0]		# Only sub-network 5 is enabled.
SubNetsEn	=	[0,	0,	0,	0,	1,	1,	0,	0 ]		# Only sub-network 5 is enabled.
# Sub-network address enables.
#				 0	1	2	3
EnabledIn0	=	[1,	1,	1,	1] 
EnabledIn1	=	[1,	1,	1,	1]
EnabledIn2	=	[1,	1,	1,	1]						# Add SparkFun Breakout. 3-27 BH
EnabledIn3	=	[1,	1,	1,	1]
EnabledIn4	=	[0,	0,	0,	0]  # 1 is the top left secion, back side
EnabledIn5	=	[1,	0,	0,	1]  #  Back section				# Only address 0 is active.
EnabledIn6	=	[0,	0,	0,	0] 
EnabledIn7	=	[0,	0,	0,	1]
 
EnabledAll	=	[EnabledIn0, EnabledIn1, EnabledIn2, EnabledIn3, EnabledIn4, EnabledIn5, EnabledIn6, EnabledIn7]

