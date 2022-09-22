import random

def CreateRandomList(N):
	A=[]
	for i in range(N):
		r=random.randrange(0,N)
		A.append(r)
	return A

def BubbleSort(A):
	movingthings = True
	while movingthings:
		movingthings= False
		for i in range(len(A)-1):
			if A[i]>A[i+1]:
				A[i],A[i+1] = A[i+1],A[i]
				movingthings = True
	return

def ShakerSort(A):
	movingthings = True
	while movingthings:
		movingthings = False
		for i in range(len(A)-1):
			if A[i]>A[i+1]:
				A[i],A[i+1]=A[i+1],A[i]
				movingthings = True
		for i in range(len(A)-1,0,-1):
			if A[i]<A[i-1]:
				A[i-1],A[i]=A[i],A[i-1]
				movingthings = True
	return

def CountingSort(A):
	F=[0]*len(A)
	for v in A:
		F[v]+=1
	k=0
	for i in range(len(F)):
		value=i
		count=F[i]
		for j in range(count):
			A[k]=value
			k+=1
	return

def MergeSort(A):
	if len(A)<=1:
		return
	mid=len(A)//2
	L=A[:mid]
	R=A[mid:]
	MergeSort(L)
	MergeSort(R)
	i=0
	j=0
	k=0
	while i<len(L) and j<len(R):
		if L[i]<=R[j]:
			A[k]=L[i]
			i+=1
		else:
			A[k]=R[j]
			j+=1
		k+=1
	while i<len(L):
		A[k]=L[i]
		i+=1
		k+=1
	while j<len(R):
		A[k]=R[j]
		j+=1
		k+=1
	return

def QuickSort(A,low,high):
	if high-low<=0:
		return
	Lmgt=low+1
	for i in range(low+1, high):
		if A[i]<A[low]:
			A[i],A[Lmgt]=A[Lmgt],A[i]
			Lmgt+=1
	A[low],A[Lmgt-1]=A[Lmgt-1],A[low]
	QuickSort(A,low,Lmgt-1)
	QuickSort(A,Lmgt,high)
	return

def ModQuickSort(A,low,high):
	if high-low<=0:
		return
	mid = (high+low)//2
	A[low],A[mid]=A[mid],A[low]
	Lmgt=low+1
	for i in range(low+1, high):
		if A[i]<A[low]:
			A[i],A[Lmgt]=A[Lmgt],A[i]
			Lmgt+=1
	A[low],A[Lmgt-1]=A[Lmgt-1],A[low]
	ModQuickSort(A,low,Lmgt-1)
	ModQuickSort(A,Lmgt,high)
	return

def main():
	A=CreateRandomList(10)
	B=A[:]
	B.sort()

	BubbleSort(A)
	if B != A:
		print("Error in Bubble Sort")
	else:	
		print("bubble", A)

	A=CreateRandomList(10)
	B=A[:]
	B.sort()
	ShakerSort(A)
	if B != A:
		print("Error in Shaker Sort")
	else:	
		print("shaker", A)

	A=CreateRandomList(10)
	B=A[:]
	B.sort()
	CountingSort(A)
	if B != A:
		print("Error in Counting Sort")
	else:	
		print("counting", A)


	A=CreateRandomList(10)
	B=A[:]
	B.sort()
	MergeSort(A)
	if B != A:
		print("Error in Merge Sort",A)
	else:	
		print("merge", A)
	
	A=CreateRandomList(10)
	B=A[:]
	B.sort()
	QuickSort(A, 0, len(A))
	if B != A:
		print("Error in Quick Sort",A,B)
	else:	
		print("quick", A)

	A=CreateRandomList(10)
	B=A[:]
	B.sort()
	ModQuickSort(A,0,len(A))
	if B!=A:
		print("Error in ModQuickSort",A,B)
	else:	
		print("mod", A)

main()
