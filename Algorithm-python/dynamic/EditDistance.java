package dynamic;

import java.io.*;

public class EditDistance {

	public static void main(String[] args) throws IOException {
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		//str1->str2
		String str1=br.readLine(); int m = str1.length();
		String str2=br.readLine(); int n = str2.length(); 
		
		
		int E[][]=new int[m][n]; // E[i][j]= str1 의 i번째까지, str2의 j번쨰까지
		
		int start;
		if (str1.charAt(0)==str2.charAt(0)) {
			start=0;
		}else {
			start=1;
		}
		
		for (int i=0;i<m;i++) {
			for(int j=0;j<n;j++) {
				if(i==0) {
					E[i][j]=start+j;
				}else if(j==0){
					E[i][j]=start+i;
				}else {
					int a;
					if(str1.charAt(i)==str2.charAt(j)) {
						a=1;
					}else{
						a=0;
					}
					int temp=Math.min(E[i][j-1]+1, E[i-1][j]+1);
					E[i][j]=Math.min(temp, E[i-1][j-1]+a);///
					
				}
				
			}
		}
		
		System.out.print(E[m-1][n-1]);
		
		
	}

}
