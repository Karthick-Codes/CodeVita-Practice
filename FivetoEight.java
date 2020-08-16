import java.util.*;
public class FivetoEight {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner scan=new Scanner(System.in);
		String[] n=scan.next().split("");
		boolean state=false,sc=true;
		int ans=0;
		String t="";
		
		for(int i=0;i<n.length;i++) {
			//System.out.print(n[i]);
			if(n[i].equals("5")&&state==false) {
				state=true;
				}
			if(n[i].equals("8")&&state==true) {
				t+=n[i];
				int x=Integer.parseInt(t);
				ans+=x;
				state=false;
				sc=false;
				
				//System.out.print(" "+t);
				t="";
				
			}
			if(state) {
				t+=n[i];
				//System.out.print(" "+t);
			}
			
			if(state==false) {
				if(sc==true) {
					
					ans+=Integer.parseInt(n[i]);
					//System.out.print(" "+ans);
				}
				else {
					sc=true;
				}
			}
			//System.out.println();
			
			
		}
		//5 without 8
		char[] k=t.toCharArray();
		for(char c:k) {
			ans+=Character.getNumericValue(c);
		}

		//Required OUTPUT
		System.out.println(ans);
		
	}

}
/*
Input
3457890
Output
---------
8

Program Logic:
	3+4+578+9+0
	5-8 consider as single digit.
Program Detailed Explaination:
	1.Input is split into a string array for single digit
	2.initialy state is false and sc=true  based this variable we can find 5-8
	3. when n[i]==5-->state=true.
		after getting 5 until met 8 we append in a string t
		after 8 --> state again false and sc also false.
	4. if state is false and sc is true we add digit individually
	5.incase 5 without 8 above code start appending after 5, so we need to sum individual digit. */
