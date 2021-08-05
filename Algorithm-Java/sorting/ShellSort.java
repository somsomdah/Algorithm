package sorting;
import java.util.*;

import java.io.*;

public class ShellSort {
	
	static void shellSort(ArrayList<Integer> A,int[] gap) {

		Arrays.sort(gap);
		
		for(int k=gap.length-1;k>=0;k--) {
			int h=gap[k];
			
			for(int i=h;i<A.size();i++) {
				
				int currentVal=A.get(i);
				int currentIdx=i;
				
				for(int j=i-h;j>=0;j-=h) {
					if(A.get(j)>currentVal) {
						currentIdx-=h;
					}
					else {
						break;
					}
				}
				A.remove(i);
				A.add(currentIdx,currentVal);
			}
		}
		
		System.out.println(A);
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st=new StringTokenizer(br.readLine());
		ArrayList<Integer> A=new ArrayList<>();
		
		while(st.hasMoreTokens()) {
			A.add(Integer.parseInt(st.nextToken()));
		}
		
		int[] gap= {5,2};
		shellSort(A,gap);

	}


}
