/* 
06/16/22
Kata: Multiples of 3 or 5
Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. 
Additionally, if the number is negative, return 0 (for languages that do have them).
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
