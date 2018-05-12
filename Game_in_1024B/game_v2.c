#include<unistd.h>

int main(){
  char number = 5, ans = 0;
  short input;
  write(1, "Hi! Can you guess about which number I'm thinking of? I can give you a hint! It's from range [0, 9].", 100);
  while(ans != 1){
    read(0, &input, 2);
    ((input & 0x0F) == number) ? (ans = 1) : write(1, "Unfortunately no. Try again!", 28);
  }
  write(1, "That's right! Congratulations!", 30);
  return 0;
}

