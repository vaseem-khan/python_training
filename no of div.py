
def divsor_c_way(A, B, K):
    # O(1) way 
    
    dif=(B-A)/K
    if A%K==0 or B%K==0:
        return dif+1
    return dif


def divsor_pythonic(A,B,K):# the pythonic way using filter though O(n)
	def filter_help(x):
		return (x%K)==0
	return len(filter(filter_help,range(A,B+1)))


print divsor_c_way(6,11,2)
print divsor_pythonic(6,11,2)
