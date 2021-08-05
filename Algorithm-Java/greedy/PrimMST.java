package greedy;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Comparator;

class Edge {
	int v1, v2;
	int weight;

	Edge(int v1, int v2, int weight) {
		this.v1 = v1;
		this.v2 = v2;
		this.weight = weight;
	}

	void print() {
		System.out.println(this.v1 + ", " + this.v2 + " : " + this.weight);
	}
}

class MST {
	ArrayList<Edge> edges = new ArrayList<>();
	ArrayList<Integer> vertices = new ArrayList<>();

	MST(int nV, int nE, int startV) {
		vertices.add(startV);
	}

	void addEdge(Edge e) {
		edges.add(e);
		if (!vertices.contains(e.v1))
			vertices.add(e.v1);
		if (!vertices.contains(e.v2))
			vertices.add(e.v2);
	}

	void print() {
		for (int i = 0; i < edges.size(); i++) {
			edges.get(i).print();
		}
	}

	boolean containsVertex(int v) {
		return vertices.contains(v);
	}

}

public class PrimMST {

	public static void main(String[] args) throws NumberFormatException, IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int nV = Integer.parseInt(br.readLine());
		int nE = Integer.parseInt(br.readLine());
		ArrayList<Integer> vertices = new ArrayList<>();
		ArrayList<Edge> edges = new ArrayList<>();
		for (int i = 0; i < nV; i++) {
			vertices.add(i);
		}

		for (int i = 0; i < nE; i++) {
			String[] input = br.readLine().split(" ");
			Edge edge = new Edge(Integer.parseInt(input[0]), Integer.parseInt(input[1]), Integer.parseInt(input[2]));
			edges.add(edge);
		}
		edges.sort(new Comparator<Edge>() {
			public int compare(Edge e1, Edge e2) {
				if (e2.weight > e1.weight)
					return -1;
				else
					return 1;
			}

		});
		

		MST mst = new MST(nV, nE, 0);
		vertices.remove(vertices.indexOf(0));

		while (vertices.size() > 0) {
			for (int i = 0; i < edges.size(); i++) {
				Edge e = edges.get(i);
				if (mst.containsVertex(e.v1) && vertices.contains(e.v2)) {
					mst.addEdge(e);
					vertices.remove(vertices.indexOf(e.v2));
					edges.remove(i);
					break;
				}
				if (mst.containsVertex(e.v2) && vertices.contains(e.v1)) {
					mst.addEdge(e);
					vertices.remove(vertices.indexOf(e.v1));
					edges.remove(i);
					break;
				}
			}
		}

		mst.print();

	}

}

/*
 
input
7
11
1 2 2
2 0 7
0 6 9
6 5 23
5 4 1
4 1 10
1 3 3
2 3 3
3 0 4
3 6 3
3 5 6
*/
