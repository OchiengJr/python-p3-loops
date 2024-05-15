/*
  Write a method `happy_new_year` that outputs numbers starting at 10 and
  counting down to 1. After reaching 1, print out "Happy New Year!"
*/
function happyNewYear() {
  for (let counter = 10; counter > 0; counter--) {
    console.log(counter);
  }
  console.log("Happy New Year!");
}

/* 
  Write a method `fizzbuzz_printer` that prints the numbers from 1 to 100. For
  multiples of three, print "Fizz" instead of the number and for the multiples
  of five print "Buzz". For numbers which are multiples of both three and five,
  print "FizzBuzz".
*/
function fizzbuzzPrinter() {
  for (let num = 1; num <= 100; num++) {
    console.log(fizzbuzz(num));
  }
}

function fizzbuzz(num) {
  if (num % 3 === 0 && num % 5 === 0) {
    return "FizzBuzz";
  } else if (num % 3 === 0) {
    return "Fizz";
  } else if (num % 5 === 0) {
    return "Buzz";
  } else {
    return num;
  }
}

/*
  Write a method `reverse_string` that takes one argument, a string, and reverses
  it. Don't use the built-in `.reverse` method. Instead, loop through the
  characters in the input string and reverse it.
*/
function reverseString(str) {
  let reversedStr = "";
  for (let i = str.length - 1; i >= 0; i--) {
    reversedStr += str[i];
  }
  return reversedStr;
}

/*
  Write a function `square_integers()` that takes one argument, a list of
  integers and returns the list of squared elements.
*/
function squareIntegers(intList) {
  return intList.map(num => num ** 2);
}
