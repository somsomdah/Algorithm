package divide_conquer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class MergeSort {
	
	static void merge(ArrayList<Integer> A,int p, int q, int k) {
		
		ArrayList<Integer> B=new ArrayList<>();
		
		int a1=p, a2=k; // a1의 index 지정 a1은 왼쪽 부분의 첫번째, a2는 오른쪽 부분의 첫번째
		
		while(a1<k && a2<q) {

			// 부분리스트를 차례대로 비교하여 작거나 같은 원소 B에 삽입
			if(A.get(a1)<=A.get(a2)) { 
				B.add(A.get(a1));
				a1++;
			}else {
				B.add(A.get(a2));
				a2++;
			}

		}
		
		// 부분리스트에 남아있는 원소 B에 삽입
		if(a1>=k) {
			while(a2<q) {
				B.add(A.get(a2));
				a2++;
			}
		}
		if(a2>=p) {
			while(a1<k) {
				B.add(A.get(a1));
				a1++;
			}
		}
		

		// A의 인덱스 p이상 q미만의 위치에 B의 원소 순서대로 수정
		for (int i=p;i<q;i++) {
			A.set(i, B.get(i-p));
		}

	}
	
	static void mergeSort(ArrayList<Integer> A,int p, int q) {
		
		if (p+1<q) { // devide 가능한 조건
			int k=(int)(p+q)/2;
			mergeSort(A,p,k);
			mergeSort(A,k,q);
			merge(A,p,q,k);

		}

	}

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = br.readLine();
		StringTokenizer st = new StringTokenizer(input," ");
		ArrayList<Integer> A=new ArrayList<>();
		
		while(st.hasMoreTokens()) {
			A.add(Integer.parseInt(st.nextToken()));
		}

		mergeSort(A,0,A.size());
		
		System.out.println(A);


	}

}
