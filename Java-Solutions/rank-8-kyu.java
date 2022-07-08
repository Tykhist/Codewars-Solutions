/*
Kata: You Can't Code Under Pressure #1
Rank: 8 kyu
Code as fast as you can! You need to double the integer and return it.
*/
class Java {
  public static int doubleInteger(int i) {
    return 2*i;
  }
}

/*
Kata: Basic Mathematical Operations
Rank: 8 kyu
Your task is to create a function that does four basic mathematical operations.
The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
*/
public class BasicOperations
{
  public static Integer basicMath(String op, int v1, int v2)
  {
    int num = 0;
    switch (op) {
        case "+":
          num = v1 + v2;
          break;
        case "-":
          num = v1 - v2;
          break;
        case "*":
          num = v1 * v2;
          break;
        case "/":
          num = v1 / v2;
          break;
    }
    return num;
  }
}

/*
Kata: Convert a Number to a String!
Rank: 8 kyu
We need a function that can transform a number into a string.
What ways of achieving this do you know?

Examples:
123 --> "123"
999 --> "999"
*/
class Kata {
  public static String numberToString(int num) {
    String result = "";
    return result + num;
  }
}
