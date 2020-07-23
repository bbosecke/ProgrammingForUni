
	import java.util.ArrayList;
	import java.util.List;
	import java.util.Arrays;

	/**
	* Given two lines of input from stdin, determine if can achieve ans,
	* and print out appropiate outputs depending on if the answer can be,
	* achieved or not.
	*
	* @author Brodie Bosecke.
	*/
	public class Arith{
			
		ArrayList<Integer> arrayLine1 = new ArrayList<Integer>();
		int ans = 0;
		char method = 'a';
		static String finalResult = "";

	public void manipulate_data(String firstLine, String secondLine){

		for(String s:firstLine.split(" ")){
			arrayLine1.add(Integer.parseInt(s));
		}
		//arr is all input in int form, in array (accessible by [n])
		int[] arr = new int[arrayLine1.size()];

		for(int j = 0; j < arr.length; j++){
			arr[j] = arrayLine1.get(j);
		}
		int i = 0;
		for(String s:secondLine.split(" ")){
			if(i == 0){
				ans = Integer.parseInt(s);
				i++;
			} else if(i == 1){
				method = s.charAt(0);
			}
		}
		//TESTING PURPOSES TO MONITOR ARRAYS AND ANS AND METHOD. Currently Works
		/*System.out.println(method + ":::: METHOD\n" + ans + ":::: ANS <----");
		for(int f = 0; f < arr.length; f++){
			System.out.println(arr[f]);
		}*/

		//https://www.geeksforgeeks.org/arraylist-array-conversion-java-toarray-methods/
		Integer[] numbers = arrayLine1.toArray(new Integer[0]);

			//Used to access the suitable methods to complete the arithmetic program. If incorrect char
			// then program stops
		if(method == 'N'){
				List<Character> temp = normal(arr, ans, numbers[0], 0, 1, new ArrayList<>());
				if(!temp.isEmpty() && temp.get(0) == '$'){
					System.out.println(method + " " + ans + " " + arr[0]);
				} else {
				int allMult = arr[0];
				if(temp.isEmpty()){
					for(int j = 0; j < arr.length-1; j++){
						allMult *= arr[j];
						temp.add('*');
					}
					if(allMult == ans){
						toPrint(temp, method, ans, arr);
					} else {
					temp.clear();
					toPrint(temp, method, ans, arr);
					}
				} else {
				toPrint(temp, method, ans, arr);
			}
		}
			} else if(method == 'L'){
				List<Character> temp = leftToRight(arr, ans, numbers[0], 1, new ArrayList<>());
				if(!temp.isEmpty() && temp.get(0) == '$'){
					System.out.println(method + " " + ans + " " + arr[0]);
				} else {
				toPrint(temp, method, ans, arr);
				}
		} else {
				System.out.println("Must give N or L! You gave: '" + method + "'");
				return;
		}
			//should clear the arrayLine somewhere
		arrayLine1.clear();
		finalResult = "";
		return;
	}

	/**
	 * toPrint organises and prints to terminal in a tidy format as specified by the etude
	 * 
	 * @param temp the list of operators that were built to get desired answer
	 * @param method the method used (either leftToRight or Normal) to get desired answer
	 * @param ans the answer that was target
	 * @param arr array of ints holding values used for the 'arithmetic'
	 */
	public static void toPrint(List<Character> temp, char method, int ans, int[]arr){
		if(temp.isEmpty()){
			System.out.println(method + " " + ans + " impossible");
		} else {
			int firstPos = arr[0];
			String finalList = Integer.toString(firstPos);
			for(int j = 0; j < temp.size(); j++){
				finalList = finalList + " " + temp.get(j) + " " + arr[j+1];
			}
			System.out.println(method + " " + ans + " " + finalList);
		}
	}


	/**
	 * normal adds and multiples every possible combination of the elements of the 
	 * array in BEDMAS form. Therefore all multiplications happen first, and then 
	 * the additions. We are trying to get the ans value
	 * 
	* @param arr the array of integers to perform the calculations on
	* @param ans is the answer we are aiming for 
	* @param runningTotal is the current total arithmetic value of the multiplied values
	* @param addition is the addition values which adds at the end of the running total to ensure BEDMAS
	* @param depth is an integer value representing the depth of recursion
	* @param operators is a list of operators being built as either a + or * is used
	* @return a list of operators representing how we got the to the final ans
	*/
	public static List<Character> normal(int[] arr, int ans, int runningTotal, int addition, int depth, List<Character> operators){
		if(depth == arr.length){
			if(arr.length == 1 && ans == runningTotal){
				var singleoperator = new ArrayList<Character>();
				singleoperator.add('$');
				return singleoperator;
			}
			//System.out.println("ADDITION --> " + addition + " THE RUNNING TOTAL -->" + runningTotal);
			int sum = addition + runningTotal;
			//System.out.println(sum + " BEFORE TRUTH + operators -> " + operators);
			if(ans == sum){
				return operators;
			} else { 
				return new ArrayList<Character>();
			}
		}

		if ((runningTotal + addition) > ans){
			return new ArrayList<Character>();
		}

		var nextoperators = new ArrayList<Character>(operators);
		nextoperators.add('+');
		var result = normal(arr, ans, runningTotal + addition, arr[depth], depth+1, nextoperators);
		if (!result.isEmpty()){
			return result;
		}
		nextoperators = new ArrayList<Character>(operators);
		nextoperators.add('*');
		return normal(arr, ans, runningTotal, addition * arr[depth], depth+1, nextoperators);

	}


	/**
	* leftToRight adds and multiplies every possible combination of the elements of the
	* array in order to try get the ans. 
	*
	* @param arr the array of integers to perform the calculations on
	* @param ans is the answer we are aiming for 
	* @param runningTotal is the current total arithmetic value (begins at first position of array)
	* @param depth is an integer value representing the depth of recursion
	* @param operators is a list of operators being built as either a + or * is used
	* @return a list of operators representing how we got the to the final ans
	*/
	public static List<Character> leftToRight(int[] arr, int ans, int runningTotal, int depth, List<Character> operators){
		if (depth == arr.length){ //Filled all the operators
			if(arr.length == 1 && ans == runningTotal){
				var singleoperator = new ArrayList<Character>();
				singleoperator.add('$');
				return singleoperator;				
			}
			if(ans==runningTotal){
				return operators;
			} else {
				return new ArrayList<Character>();
			}
		}

		if (runningTotal > ans){	// Total is too big
			return new ArrayList<Character>();
		}

		var nextoperators = new ArrayList<Character>(operators);
		nextoperators.add('+');
		var result = leftToRight(arr, ans, runningTotal + arr[depth], depth+1, nextoperators);
		if (!result.isEmpty()){
			return result;
		}
		nextoperators = new ArrayList<Character>(operators);
		nextoperators.add('*');
		return leftToRight(arr, ans, runningTotal * arr[depth], depth+1, nextoperators);


	} 
	}