package greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class CoinChange {
	public static int coinChange(int W) {
		int change=W;
		int n500=0;
		int n100=0;
		int n50=0;
		int n10=0;
		int n5=0;
		int n1=0;
		
		while(change>=500) {
			change-=500;
			n500++;
		}
		while(change>=100) {
			change-=100;
			n100++;
		}
		while(change>=50) {
			change-=50;
			n100++;
		}
		while(change>=10) {
			change-=10;
			n100++;
		}
		while(change>=5) {
			change-=5;
			n100++;
		}
		while(change>=1) {
			change-=1;
			n100++;
		}
		return n500+n100+n50+n10+n5+n1;
		
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int W=Integer.parseInt(br.readLine());
		System.out.println(coinChange(W));
		
	}
}
