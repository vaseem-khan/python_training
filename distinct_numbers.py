import sys
def func():
	lis=[int(i) for i in sys.argv[1].split(",")]
	s=map(int,set(lis))
	print s

if __name__=="__main__":
	func()
