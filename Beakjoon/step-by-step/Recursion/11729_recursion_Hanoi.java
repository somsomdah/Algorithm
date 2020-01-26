package recursion;

import java.util.*;
import java.io.*;

class TowerOfHanoi {
	static ArrayList<String> path = new ArrayList<>();
	static int count = 0;

	TowerOfHanoi() {

	}

	static void stack_tower(int n, int src, int dst) {
		int temp = 6 - (src + dst);
		if (n == 1) {
			path.add(src + " " + dst);
			count++;
		} else {
			stack_tower(n - 1, src, temp);
			stack_tower(1, src, dst);
			stack_tower(n - 1, temp, dst);
		}
	}
	
	void print() {
		System.out.println(count);
		for(int i=0;i<path.size();i++)
			System.out.println(path.get(i));
	}
}

class hanoi {

	public static void main(String[] args) throws NumberFormatException, IOException {

		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		TowerOfHanoi tower = new TowerOfHanoi();
		tower.stack_tower(n, 1, 3);
		tower.print();
		

	}
}
