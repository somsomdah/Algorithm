import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _2828_AppleGame {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String[] NM = br.readLine().split(" ");
		int N = Integer.parseInt(NM[0]);
		int M = Integer.parseInt(NM[1]);
		int nApples = Integer.parseInt(br.readLine());
		int totalDist = 0;
		int p = 1, q = M;
		for (int i = 0; i < nApples; i++) {
			int a = Integer.parseInt(br.readLine());
			if (p <= a && a <= q) {
				totalDist += 0;
			}
			if (a < p) {
				totalDist += p - a;
				p = a;
				q = a + M - 1;
			}
			if (q < a) {
				totalDist += a - q;
				p = a - (M - 1);
				q = a;
			}
		}
		System.out.println(totalDist);

	}
}
