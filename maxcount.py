#maxcount O(N+M)
#problem and accuracy details at https://codility.com/demo/results/demo6CY6Y8-HP3/


def max_count(N, A):
    counter=[0]*N
    max_cnt=0
    back=0
    for i in A:
        if i==N+1:
            back=max_cnt
            
        else:
            counter[i-1]=max(back,counter[i-1])+1
            max_cnt=max(counter[i-1],max_cnt)
    for i in range(len(counter)):
       counter[i]=max(back,counter[i])
    return counter

if __name__=="__main__":
	print max_count(5,[3,4,4,6,1,4,4])