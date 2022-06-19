/* 
Kata: Isograms
Rank: 7 kyu
An isogram is a word that has no repeating letters, consecutive or non-consecutive. 
Implement a function that determines whether a string that contains only letters is an isogram. 
Assume the empty string is an isogram. Ignore letter case.
*/
package kata

func Multiple3And5(number int) int {
  if number < 3 {
    return 0
  }
  
  result := 0
  for i := 1; i < number; i++ {
    if i%3 == 0 || i%5 == 0 {
      result += i
    }
  }
  return result
}

/* 
Kata: Even or Odd
Rank: 8 kyu
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
*/
package kata

func EvenOrOdd(number int) string {
  if number % 2 == 0 {
    return "Even"
  } else {
    return "Odd"
  }
}
