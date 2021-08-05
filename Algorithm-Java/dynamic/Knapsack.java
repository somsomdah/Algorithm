package dynamic;

import java.io.*;

public class Knapsack {
	

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String[] temp1=br.readLine().split(" ");
		int N=Integer.parseInt(temp1[0]);
		int C=Integer.parseInt(temp1[1]);
		int[] W=new int[N];
		int[] V=new int[N];
		for(int i=0;i<N;i++) {
			String[] temp2=br.readLine().split(" ");
			W[i]=Integer.parseInt(temp2[0]);
			V[i]=Integer.parseInt(temp2[1]);
		}
		
		int[][] K=new int[N][C+1]; // K[i][w] 물건 i까지만 고려, 배낭 무게 w까지만 고려
		
		for (int i=0;i<N;i++) {
			for(int w=0;w<=C;w++) {
				if(i==0||w==0) {
					K[i][w]=0;
				}else {
					if(W[i]>w) {
						K[i][w]=K[i-1][w];
					}else {
						K[i][w]=Math.max(K[i-1][w], K[i-1][w-W[i]]+V[i]);
					}
				}
			}
			
		}
		
		System.out.println(K[N-1][C]);
	}

}

/*
4 7
6 13
4 8
3 6
5 12
 */