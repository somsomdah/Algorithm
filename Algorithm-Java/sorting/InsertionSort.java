package sorting;
import java.util.*;
import java.io.*;

public class InsertionSort {
	
	static void insertionSort(ArrayList<Integer> A) {
		
		for(int i=0;i<A.size();i++) {
			int currentVal=A.get(i);
			int currentIdx=i;
			for(int j=i-1;j>=0;j--) {
				if (A.get(j)>currentVal) {
					currentIdx--;
				}
				else {
					break;
				}
			}
			A.remove(i);
			A.add(currentIdx,currentVal);
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
		
		insertionSort(A);

	}

}
