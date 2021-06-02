def search(numbers):
  total = 0
  for num in numbers:
    if int(num) == 4:
      total = total + 1
  
  return total

print(search([1,3,4,5,6]))
print(search([1,3,4,5,6,4,4,4,4]))


def vowel_checker(letter):
  vowel_variables = 'aeiou' 
  return letter in vowel_variables

print(vowel_checker('d', 'e'))