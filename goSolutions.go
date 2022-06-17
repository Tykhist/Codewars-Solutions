// Kata: Multiples of 3 or 5
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
