2.Candy Distribution

import java.util.*;
public class CandyDistribution {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		int testcase=sc.nextInt();
		for(int i=0;i<testcase;i++) {
			int prisoner=sc.nextInt();
			int candy=sc.nextInt();
			int start=sc.nextInt();
			if(prisoner>candy) {
				int ans=candy+start-1;
				System.out.println(ans);
			}
			else {
				
				int lastpos=candy%prisoner; // it find last position as starting from 1
				//add start gives current position ,we need last one so -1
				System.out.println(lastpos+start-1); 
			}
		}
		sc.close();
	}

}

Sample Input 0

2
5 2 1
5 2 2
Output:
2
3
/*
Program Logic :
	we need who get last candy. they are in circular way.
	candy%prisoner helps to find last position as starting from 1.
Program Detailed Explaination:
	if candy less than number of prisoner then its simple add, number of candy + start it gives current positon which is out of candy.
	so, subtract -1 from previous answer.

	if candy greater than prisoner then distribution start in circular way, we know mod gives last positon 
	candy%prisoner gives last position . but this is a result for starting position 1.
	but we requested to find for given starting position ,
		add previous result+start ===> this is current position which is out of candy.
		subtract -1 from previous answer.*/
