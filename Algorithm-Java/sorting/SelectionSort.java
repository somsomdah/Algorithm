package sorting;
import java.util.*;
import java.io.*;

public class SelectionSort {
	
	static void selectionSort(ArrayList<Integer> A) {
		
		for(int i=0;i<A.size();i++) {
			int min=i;
			for(int j=i+1;j<A.size();j++) { //최소값의 인덱스 찾기
				if(A.get(j)<A.get(min)) {
					min=j;
				}
			}
			Collections.swap(A, min, i);
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
		
		selectionSort(A);

	}

}
