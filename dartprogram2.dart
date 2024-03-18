// Function to add two numbers
double add(double a, double b) {
  return a + b;
}

// Function to multiply two numbers
double multiply(double a, double b) {
  return a * b;
}

void main() {
  double num1 = 10.5;
  double num2 = 5.5;

  // Perform addition
  double sum = add(num1, num2);
  print('The sum of $num1 and $num2 is: $sum');

  // Perform multiplication
  double product = multiply(num1, num2);
  print('The product of $num1 and $num2 is: $product');
}
