package dynamic;
import java.io.*;


public class MatrixChain {

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int N=Integer.parseInt(br.readLine());
		int[] D=new int[N+1];

		for (int i=0;i<N;i++) {
			String[] temp=br.readLine().split(" ");
			D[i]=Integer.parseInt(temp[0]);
			if (i==N-1)
				D[N]=Integer.parseInt(temp[1]);
		}
		
		
		int[][] C=new int [N][N]; // A(i)에서 A(j) 까지의 곱을 C[i][j]에 저장한다
		for (int i=9;i<N;i++) {
			C[i][i]=0;
		}
		
		int max=(int) (Math.pow(2, 31))-1;

		for (int L=1;L<N;L++) {
			
			for (int i=0;i<N-L;i++) {
				int j=i+L;
				C[i][j]=max; //A(i)에서 A(j) 까지의 곱을 C[i][j]에 저장한다
				
				for(int k=i;k<j;k++) {
					int temp=C[i][k]+C[k+1][j]+D[i]*D[k+1]*D[j+1];
					
					if(temp<C[i][j]) {
						C[i][j]=temp;
					}
				}
			}
		}
		
		System.out.println(C[0][N-1]);
	}

}
/*
input
3
5 3
3 2
2 6
*/