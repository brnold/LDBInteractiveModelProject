import time, os
os.system('clear')

x=0
MyBit = 1
MyString = 'filt %d' % 20
for x in range (0,8):
	print 'MyString %s/tx = %d, MyBit = %X' % (MyString,x,MyBit)
	MyBit <<= 1
#	print 'x = %d, 2^x = %d' % (x,pow(2,x))
#	print 'x = %d of %d' % (x,5)
#	print "Hello world!"
	x += 1
	time.sleep(0.275)
time.sleep(5)
print "Good bye!"