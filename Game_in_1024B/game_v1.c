#include<stdio.h>

int main(){
  char number = 5, input, ans = 0;
  puts("Hi! Can you guess about which number I'm thinking of? I can give you a hint! It's from range [0, 9].");
  while(ans != 1){
    scanf("%hhi", &input);
    (input == number) ? (ans = 1) : puts("Unfortunately no. Try again!");
  }
  puts("That's right! Congratulations!");
  return 0;
}
