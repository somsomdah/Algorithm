package greedy;

import java.util.*;
import java.io.*;

class Thing {
	float valuePerWeight;
	float weight;
	float value;
	String name;

	Thing(String name, float weight, float value) {
		this.name = name;
		this.value=value;
		this.weight=weight;
		this.valuePerWeight = value/weight;
	}
}

public class FractionalKnapsack {

	public static void fractionalKnapsack(ArrayList<Thing> things, float limit) {
		
		things.sort(new Comparator<Thing>() {
			public int compare(Thing t1, Thing t2) {
				if (t1.valuePerWeight > t2.valuePerWeight)
					return -1;
				else
					return +1;
			}
		});

	
		float totalValue=0;
		float totalWeight=0;
		
		while(totalWeight+things.get(0).weight<=limit) {
			Thing temp=things.get(0);
			totalWeight+=temp.weight;
			totalValue+=temp.value;
			things.remove(0);
			System.out.println(temp.name+" "+temp.weight);
		}
		
		if(limit-totalWeight>0) {
			Thing temp=things.get(0);
			totalValue+=temp.valuePerWeight*(limit-totalWeight);
			System.out.println(temp.name+" "+(limit-totalWeight));
			totalWeight=limit;

		}
		
		System.out.println(totalValue);
		
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		float C=Float.parseFloat(br.readLine()); // limit
		int N=Integer.parseInt(br.readLine()); // number of things
		
		ArrayList<Thing> things=new ArrayList<>();
		for (int i=0;i<N;i++) {
			String[] input=br.readLine().split(" ");
			Thing thing =new Thing(input[0],Float.parseFloat(input[1]),Float.parseFloat(input[2]));
			things.add(thing);
		}
		
		fractionalKnapsack(things,C);

	}
/*
input
40
4
tin 50 5
platinum 10 60
silver 25 10
gold 15 75
 */

}
