 Possible paths Top Left to Bottom right

test=int(input())
for _ in range(test):
    N,M=map(int,input().split())
    Matrix=[]
    for i in range(N):
        l=[]
        for j in range(M):
            if i==0 or j==0:
                l.append(1)
            else:
                l.append(0)
        Matrix.append(l)
    for i in range(1,N):
        for j in range(1,M):
            Matrix[i][j]=Matrix[i-1][j]+Matrix[i][j-1]
    print(Matrix[-1][-1]) 

Input:
1 
3 3
Output: 6

Program Logic:
	find all possible way count from [0][0] to [n-1][m-1]
	first row and column possible way is 1 from starting position.
	from [1][1] to all remaing column possible way previous row + previous column.
	a 2*2 matrix has only 2 ways to reach bottom of right.

Program Detailed Expalanation:
	create a M*N matrix ,initialize first row and first column value as 1.
	We know every cells way depend previous cell+previous row cell.so matrix[i][j] value is matrix[i-1][j]+matrix[i][j-1].
	total possible way is stored in [N-1][M-1] index.
       

Final Matrix=	{ 1, 1, 1, 1
		  1, 2, 3, 4
		  1, 3, 6, 10
		  1, 4, 10, 20}
	

