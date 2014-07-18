import sys

from datetime import datetime
def func():
	t1=sys.argv[1:]

	date_format = "%H:%M:%S"
	a = datetime.strptime(t1[0], date_format)
	b = datetime.strptime(t1[1], date_format)
	delta = b - a
	print delta

if __name__ == '__main__':
	func()