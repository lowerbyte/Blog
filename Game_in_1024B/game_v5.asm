segment .text
  global _start

_start:
  mov rax, 1
  mov rdi, 1 
  lea rsi, [welcome]
  mov rdx, 101
  syscall

game:
  mov rax, 0
  mov rdi, 0 
  mov rsi, input
  mov rdx, 2
  syscall
  
  mov rax, [input]
  cmp al, 0x35
  je end
  mov rax, 1
  mov rdi, 1 
  lea rsi, [failure]
  mov rdx, 28
  syscall
  jmp game
 
end:
  mov rax, 1
  mov rdi, 1 
  lea rsi, [success]
  mov rdx, 30
  syscall
  mov rax, 60
  xor rdi, rdi
  syscall

segment .bss
  input resb 2

segment .data
  success db "That's right! Congratulations!", 0xa
  failure db "Unfortunately no. Try again!", 0xa
  welcome db "Hi! Can you guess about which number I'm thinking of? I can give you a hint! It's from range [0, 9].", 0xa
