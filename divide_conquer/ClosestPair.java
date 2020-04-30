package divide_conquer;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Dictionary;
import java.util.StringTokenizer;

class Coordinate implements Comparable<Coordinate>{
	int x; int y;
	Coordinate(int x, int y){
		this.x=x;
		this.y=y;
	}
	
	static float calcDist(Coordinate p1, Coordinate p2) {
		float dist= (float) Math.sqrt(Math.pow((p1.x-p2.x), 2)+Math.pow((p1.y-p2.y), 2));
		return dist;
	}
	
	static void orderByX(ArrayList<Coordinate> A) {
		Collections.sort(A);
	}
	
	static void printCoordinates(ArrayList<Coordinate> A) {
		for (int i=0;i<A.size();i++) {
			System.out.print("("+A.get(i).x+","+A.get(i).y+") ");
		}
		System.out.println();
	}

	@Override
	public int compareTo(Coordinate p) {
		if (this.x<p.x) {
			return -1;
		}else {
			return 1;
		}
	}

	
}

public class ClosestPair {
	
	static float closestPair(ArrayList<Coordinate> A) {
		
		//Coordinate.printCoordinates(A);
		//System.out.println(A.size());
		
		if (A.size()<=3) {
			
			if (A.size()==3){
				
			
			float dist1=Coordinate.calcDist(A.get(0), A.get(1));
			float dist2=Coordinate.calcDist(A.get(1), A.get(2));
			float dist3=Coordinate.calcDist(A.get(2), A.get(0));
			
			float minDist=Math.min(dist1, dist2);
			minDist=Math.min(minDist, dist3);
			
			return minDist;
			}
			else if(A.size()==2) {
			
				return Coordinate.calcDist(A.get(0), A.get(1));
			}else {
				return 10000;
			}
			

		}
		
		else {
			int mid=(int)A.size()/2;
			ArrayList<Coordinate> left=new ArrayList<>();
			ArrayList<Coordinate> right=new ArrayList<>();
			
			for (int i=0;i<mid;i++) {
				left.add(A.get(i));
			}
			for (int i=mid;i<A.size();i++){
				right.add(A.get(i));
			}
			
			float left_min=closestPair(left);
			float right_min=closestPair(right);
			
			float d=Math.min(left_min, right_min);
			
			ArrayList<Coordinate> center=new ArrayList<>();
			float center_left=left.get(left.size()-1).x-d;
			float center_right=right.get(0).x-d;
			
			for (int i=0;i<A.size();i++) {
				if(A.get(i).x>center_left && A.get(i).x<center_right) {
					center.add(A.get(i));
				}
				if (A.get(i).x>center_right) {
					break;
				}
			}
			
			float center_min=closestPair(center);
			
			float minDist=Math.min(left_min, right_min);
			minDist=Math.min(minDist, center_min);
			
			return minDist;

		}
		
	}
	

	public static void main(String[] args) throws NumberFormatException, IOException {
		
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int num=Integer.parseInt(br.readLine());
		ArrayList<Coordinate> A=new ArrayList<>();
		
		for (int i=0;i<num;i++) {
			String coord=br.readLine();
			StringTokenizer st=new StringTokenizer(coord," ");
			int x= Integer.parseInt(st.nextToken());
			int y= Integer.parseInt(st.nextToken());
			A.add(new Coordinate(x,y));
		}
		
		Coordinate.orderByX(A);
		float result=closestPair(A);
		
		System.out.println(result);
		
		

	}

}
