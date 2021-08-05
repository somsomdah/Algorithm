import java.io.*;

class _11729_Hanoi {
	
	static int count=0;
	static StringBuilder sb = new StringBuilder();

	static void stack_tower(int n, int src, int dst) {
		int temp = 6 - (src + dst);
		if (n <= 1) {
			count++;
			sb.append(src + " " + dst+"\n");
		} else {
			stack_tower(n - 1, src, temp);
			stack_tower(1, src, dst);
			stack_tower(n - 1, temp, dst);
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		stack_tower(n, 1, 3);
		
		System.out.println(count);
		System.out.println(sb);

	}

}
