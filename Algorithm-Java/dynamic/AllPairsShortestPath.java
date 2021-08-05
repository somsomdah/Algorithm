package dynamic;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class AllPairsShortestPath {

	public static void main(String[] args) throws NumberFormatException, IOException {
		int max=100000;
		
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int nV=Integer.parseInt(br.readLine());
		int nE=Integer.parseInt(br.readLine());
		
		int[][] D=new int[nV+1][nV+1];
		
		for (int i=0;i<=nV;i++) {
			for (int j=0;j<=nV;j++) {
				if(i==j)
					D[i][j]=0;
				else
					D[i][j]=max;
			}
		}
		
		for (int i=1;i<=nE;i++) {
			String[] in=br.readLine().split(" ");
			D[Integer.parseInt(in[0])][Integer.parseInt(in[1])]=Integer.parseInt(in[2]);
		}
		
		for (int k=1;k<=nV;k++)
			for (int i=1;i<=nV;i++)
				for (int j=1;j<=nV;j++) {
					D[i][j]=Math.min(D[i][k]+D[k][j], D[i][j]);
				}
		
		for (int i=1;i<=nV;i++) {
			for (int j=1;j<=nV;j++) {
				System.out.print(D[i][j]+" ");
			}
			System.out.println();
		}
	}

}
/*
input
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
 */
