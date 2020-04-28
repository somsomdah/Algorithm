package divide_conquer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class QuickSort {
	
	static void QuickSort_(ArrayList<Integer> A,int p,int q){
		
		if(p<q) {
			int pivotIdx=(int)(p+q)/2;
			int pivot=A.get(pivotIdx);
			
			int tempIdx=0;
			while (tempIdx<pivotIdx) {
				int temp=A.get(tempIdx);
				if(temp<pivot) {
					tempIdx++;
				}else {
					A.remove(tempIdx);
					pivotIdx--;
					A.add(pivotIdx+1,temp);
				}
			}
			
			tempIdx=pivotIdx+1;
			while(tempIdx<p) {
				int temp=A.get(tempIdx);
				if(temp>pivot) {
					tempIdx++;
				}else {
					A.remove(tempIdx);
					A.add(0,temp);
					pivotIdx++;
				}
			}


			QuickSort_(A,p,pivotIdx);
			QuickSort_(A,pivotIdx+1,q);
		}
	}

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		String input=br.readLine();
		StringTokenizer st=new StringTokenizer(input," ");
		ArrayList<Integer> A=new ArrayList<>();
		
		while(st.hasMoreTokens()) {
			A.add(Integer.parseInt(st.nextToken()));
		}
		
		QuickSort_(A,0,A.size());
		
		System.out.println(A);

	}

}
