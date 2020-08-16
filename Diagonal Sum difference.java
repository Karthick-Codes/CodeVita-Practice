import java.util.*;
public class DiagnoalSum {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		int[][]matrix=new int[n][n];
		int RD=0,LD=0;
		for(int i=0;i<n;i++) 
		{
			for(int j=0;j<n;j++) {
				matrix[i][j]=sc.nextInt();
  //task 1
				if(i==j) 
				{
					LD+=matrix[i][j];
				}
				if(i+j==n-1) 
				{
					RD+=matrix[i][j];
				}
			}
		}
  //task 2
		int ans=Math.abs(RD-LD);
		System.out.println(ans);
	}

}

/*
Input:

1 2 3
4 5 6
9 8 9  
 
Output:
2

  
  
  Program Logic:
  
  Find the absolute difference of two diagonal sum.
  Explanation
  1.we need to find diagonal sum of both left and right
  2.Find difference of two sum

Program Detailed Explanation:
  
  Task 1 portion code :
  Left Diagonal:
  i==j then add a[I][j] to a variable LD
  Right Diagonal:
  i+j==n-1 then add a[I][j] to a variable RD.
Task 2 portion Code:
    	 Find absolute difference between LD and RD.
  
  
Finally output in ans variable . print ans. */
