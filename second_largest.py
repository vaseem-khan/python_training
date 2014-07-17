import sys
def func():
	lis=[int(ele) for ele in sys.argv[1].split(",")]
	lis.sort()
	print lis[-2]

if __name__=="__main__":
	func()

