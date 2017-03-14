import java.util.*;
public class Main {
	public static void main(String[] args) {
		Scanner in = new Scanner (System.in); 
		int n = in.nextInt();
		int [] input = new int[n];
		for (int i = 0; i < n; i++) { 
			input [i] = in.nextInt(); 
		}
		boolean sorted  = false; 
		int placeholder ; 
		while (sorted ==false) {
			sorted = true;
			for (int i= 0; i<input.length-1; i++) {
				if (input [i] > input [i+1]) {
					sorted = false; 
					placeholder = input [i];
					input[i]=input [i+1]; 
					input [i+1] = placeholder;
				}
			}
		}
		if (input.length%2 ==0) { 
			int middle = (input.length/2)-1;
			for (int i = 0; i< middle +1; i++) {		
				System.out.print(input[middle - i] + " "); 
				System.out.print(input[middle + i  +1] + " "); 
			}
		}
		if (input.length%2 ==1) {
			int middle = ((input.length + 1) /2)-1; 	
			System.out.print(input[middle]); 
			for (int i = 1; i< middle +1; i++ ) {
				System.out.print(input[middle + i] + " ");
				System.out.print(input[middle - i] + " "); 
			}
		}
	}
}