package sorting;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class BubbleSort {
	
	static void bubbleSort(ArrayList<Integer> A) {
		int temp;
		for(int k=0;k<A.size();k++) {
			for (int i=1;i<A.size()-k;i++) {
				if(A.get(i-1)>A.get(i)) {
					temp=A.get(i);
					A.set(i, A.get(i-1));
					A.set(i-1, temp);
				}
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
		
		bubbleSort(A);

	}

}
