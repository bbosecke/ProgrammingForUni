import java.util.*;

/**
* Two lines at a time and reading in from stdin,
* passes it to Arith.java to perform arithmetic task
* 
* @author Brodie Bosecke.
**/

public class ArithApp{
	
	public static void main(String[] args){
		String firstLine, secondLine;

		Scanner scan = new Scanner(System.in);
		Arith start = new Arith();
		while(scan.hasNextLine()){
			firstLine = scan.nextLine();
			if(scan.hasNextLine()){
				secondLine = scan.nextLine();
			} else {
				break;
			}
			start.manipulate_data(firstLine, secondLine);
			
		}
	}

}