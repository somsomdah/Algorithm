package divide_conquer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class SelectionProblem {

	// find k-th small number
	static Integer selectionProblem(ArrayList<Integer> A, int p, int q, int k) {

		int pivotIdx = (int) (p + q) / 2;
		int pivot = A.get(pivotIdx);

		int tempIdx = 0;
		while (tempIdx < pivotIdx) {
			int temp = A.get(tempIdx);
			if (temp < pivot) {
				tempIdx++;
			} else {
				A.remove(tempIdx);
				pivotIdx--;
				A.add(pivotIdx + 1, temp);
			}
		}

		tempIdx = pivotIdx + 1;
		while (tempIdx < q) {
			int temp = A.get(tempIdx);
			if (temp > pivot) {
				tempIdx++;
			} else {
				A.remove(tempIdx);
				A.add(0, temp);
				pivotIdx++;
			}
		}

		// size of the group of small numbers
		int s = pivotIdx - p;

		// if pivot is the k-th small number
		if (s + 1 == k) {
			return A.get(pivotIdx);
		}
		// find in the group of small numbers
		else if (s + 1 > k) {
			return selectionProblem(A, p, pivotIdx, k);
		}

		// find in the gorup of large numbers
		else { // if (pivotIdx + 1 < k) {
			return selectionProblem(A, pivotIdx + 1, q, k - s - 1);
		}

	}

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int k = Integer.parseInt(br.readLine());
		String input = br.readLine();
		StringTokenizer st = new StringTokenizer(input, " ");
		ArrayList<Integer> A = new ArrayList<>();

		while (st.hasMoreTokens()) {
			A.add(Integer.parseInt(st.nextToken()));
		}

		System.out.println(selectionProblem(A, 0, A.size(), k));

	}

}
