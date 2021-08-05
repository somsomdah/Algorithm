package sorting;

import java.util.*;

public class HeapSort {

	static ArrayList<Integer> upheap(int[] A) {

		ArrayList<Integer> heap = new ArrayList<>();
		heap.add(9999);

		for (int i = 0; i < A.length; i++) {
			int currentVal = A[i];
			for (int j = heap.size(); j > 0; j /= 2) {
				int parentVal = heap.get(j / 2);
				if (currentVal > parentVal) {
					heap.add(j, parentVal); // 부모노드 끌어내림
					heap.remove(j / 2);
				} else {
					heap.add(j, currentVal);
					break;
				}
			}
		}
		return heap;
	}

	static void downheap(ArrayList<Integer> heap) {// delete max
		
		while (heap.size() > 1) {
			System.out.print(heap.get(1)+" ");
			int currentVal = heap.get(heap.size() - 1);
			heap.set(1, currentVal);
			heap.remove(heap.size() - 1);
			

			for (int j = 1; j < heap.size(); j *= 2) {
				
				// 자식 두명
				if (heap.size() > j * 2 + 2) {
					int child1Val = heap.get(j * 2);
					int child2Val = heap.get(j * 2 + 1);
					if (child1Val > child2Val) {
						if (child1Val > currentVal) {
							Collections.swap(heap, j * 2, j);
						} else {
							break;
						}
					} else if (child1Val < child2Val) {
						if (child2Val > currentVal) {
							Collections.swap(heap, j * 2 + 1, j);
						} else {
							break;
						}
					}
				} 
				
				// 자식 한명
				else if (heap.size() > j * 2 + 1) {
					int child1Val = heap.get(j * 2);
					if (child1Val > currentVal) {
						Collections.swap(heap, j * 2, j);
					} else {
						break;
					}

				}
				
				// 자식 없음
				else {
					break;
				}

			}

		}
	}


	public static void main(String[] args) {
		
		int[] A = { 1, 2, 3, 4, 5, 6, 7, 8 };
		downheap(upheap(A));

	}

}
