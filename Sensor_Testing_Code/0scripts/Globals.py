#************************************************************************************************************ 
#  ECE 491 Senior Design
#  Winter 2016
#  Team 6 
#
#  Python Script		: Global.py
#
#  Purpose: 
#  Provides a list of Global Chip configuration settings for each MPR 121 that can be used 
#  in our touch system. 
#
#  
#     
#  Primary coder																Benjamin
#  Secondary coder																Bret
#  Code contributor																Katrina
#  Code contributor																Ryan
#************************************************************************************************************ 
#  Revision      
#  0	 Supporting script Global Chip configuration settings.					Bret		2016-03-20
#                     
#  x	 Edits.																	TBD			2016-0x-xx
#
#
#************************************************************************************************************
# Global configuration settings
# Address_Subnet
#				 SA		DBT_R	F_CDC	CDT_F	ECR
Global0_0	=	[0x5b,	0x00,	0x07,	0x93,	0x89]
Global1_0	=	[0x5b,	0x00,	0x07,	0x93,	0x89]
Global2_0	=	[0x5b,	0x00,	0x07,	0x93,	0x89]
Global3_0	=	[0x5b,	0x00,	0x07,	0x93,	0x89]
GlobalSn0	=	[Global0_0, Global1_0, Global2_0, Global3_0]

Global0_1	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global1_1	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global2_1	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global3_1	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
GlobalSn1	=	[Global0_1, Global1_1, Global2_1, Global3_1]

Global0_2	=	[0x5b,	0x00,	0x07,	0x93,	0x8c]		# ELE0-ELE11 enabled SparkFun
Global1_2	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global2_2	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global3_2	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
GlobalSn2	=	[Global0_2, Global1_2, Global2_2, Global3_2]

Global0_3	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global1_3	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global2_3	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global3_3	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
GlobalSn3	=	[Global0_3, Global1_3, Global2_3, Global3_3]

Global0_4	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global1_4	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global2_4	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global3_4	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
GlobalSn4	=	[Global0_4, Global1_4, Global2_4, Global3_4]

Global0_5	=	[0x5b,	0x00,	0x07,	0x93,	0x8c]			# ELE0-ELE11 enabled
Global1_5	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global2_5	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global3_5	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
GlobalSn5	=	[Global0_5, Global1_5, Global2_5, Global3_5]

Global0_6	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global1_6	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global2_6	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global3_6	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
GlobalSn6	=	[Global0_6, Global1_6, Global2_6, Global3_6]

Global0_7	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global1_7	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global2_7	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
Global3_7	=	[0x5b,	0x00,	0x07,	0x93,	0x89] 
GlobalSn7	=	[Global0_7, Global1_7, Global2_7, Global3_7]

GlobalAll	=	[GlobalSn0,	GlobalSn1,	GlobalSn2,	GlobalSn3,	GlobalSn4,	GlobalSn5,	GlobalSn6,	GlobalSn7]