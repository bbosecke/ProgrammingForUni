import java.util.Scanner;
import java.io.File;
import java.util.*;
import java.lang.*;

/**
* Etude 4: Counting it up!
* This program takes user input for the values N and K and computes the NCK
*   NCK being the number of unique possibilites from the given input
*
* @author Meggie Morrison, 7777435.
* @author Brodie Bosecke, 5471718.
*
*/

public class Counting{

  public static void main(String[] args){

    long temp = 0;
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter an integer N: ");
    long n = scan.nextLong();
    System.out.println("Enter an integer K: ");
    long k = scan.nextLong();

    // Mathmatically, n - k if it less than 0.5n then we can use the other half
    // of the 'pascals triangle' value therefore never needing to go above an
    // array of size 2^32
    // Only enter this statement if k is greater than 0.5n
    if(n/2 < k){
        temp = n - k;
        k = temp;
    }


    long[] numo = new long[(int)k];
    long[] deno = new long[(int)k];

    simplifyNumerator(n, k, numo);
    simplifyDenominator(k, deno);

    // test for n = 10 and k = 3 to ensure the array stores the right stuff
    //System.out.println("Array numo: " + numo[0] + numo[1] + numo[2] + numo[3]);
    //System.out.println("Array numo: " + deno[0] + deno[1] + deno[2]);

    // AT THIS POINT WE HAVE THE ARRAYS, and now call method, simplify and multiply
    System.out.println("Number of possibilities: " + finalAns(numo, deno));

    }

    /**
    * This method is taking the value of n, and storing the values from the original n
    * until it has k digits in the array numo
    * e.g. n = 10, k = 3 therefore numo[] = 10, 9, 8
    *
    * @param n the user input used to create array from n--
    * @param k the user input used to give array length of k
    * @param numo is the array to store the numerator values in
    */
    static void simplifyNumerator(long n, long k, long[] numo){
        long temp = n;
        int pos = 0;
        for(int i = 0; i < k; i++){
            numo[pos] = temp;
            //System.out.println("Numo:" + temp);
            temp--;
            pos++;
        }
    }

    /**
    * This method is taking the value of k and storing the values k all the way to 1 
    * in an array deno
    * e.g. n = 10, k = 3 therefore deno[] = 3, 2, 1
    *
    * @param k is the value to use from k --> 1
    * @param deno stores the denominator values from k-- to 1
    */
    static void simplifyDenominator(long k, long[] deno){
        long tempD = k;
        int pos = 0;
        long g = k;
        for(int i = 0; i < g; i++){
            deno[pos] = tempD;
            //System.out.println("deno: " + tempD);
            tempD--;
            pos++;
        }
    }

    /**
    * This method will simplify the numerator and denominator by the GCD if it can.
    * Then it will calculate the number of possibilities available for the given
    * n and k value. 
    * 
    * @param numo is used to iterate through the numerator values
    * @param deno is used to iterate through the denominator values
    *   calculations are made with both numo and deno values
    * @return the number of possibilities of unique values for n and k
    */
    public static long finalAns(long[] numo, long[] deno){
        long temp = 1;
        long tempted = 1;
        long x, y;
        int i, j, k, gcd;
        long[] lastArray = new long[numo.length];

        for(i = 0; i < numo.length; i++){
            for(j = 0; j < numo.length; j++){
                x = numo[i];
                y = deno[j];
                gcd = 1;
                for(k = 1; k <= x && k <= y; k++){
                    if(x % k == 0 && y % k == 0){
                        gcd = k;
                        //System.out.println("GCD: " + gcd);
                    }
                    numo[i] = x/gcd;
                    deno[j] = y/gcd;
                }

            }
            //System.out.println("NUMO: " + numo[i] + " over DENO: " + deno[i]);
        }
        for(i = 0; i < numo.length; i++){
            temp = numo[i] * temp;
        }
        for(i = 0; i < numo.length; i++){
            tempted = deno[i] * tempted;
        }
        //System.out.println(temp + " " + tempted);

        return temp/tempted;
    }

}