BITS 64

org 0x400000

elf_hdr:
  db 0x7f, 'E', 'L', 'F', 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ;e_indent[EI_NIDENT]
  dw 2 ;e_type
  dw 0x3e ;e_machine
  dd 1 ;e_version
  dq _start ;e_entry
  dq phdr - $$ ;e_phoff;
  dq 0 ;e_shoff
  dd 0 ;e_flags
  dw 0x40 ;e_ehsize
  dw phdrsize ;e_phentsize
  dw 1 ;e_phnum
  dw 0 ;e_shentsize
  dw 0 ;e_shnum
  dw 0 ;e_shstrndx

phdr:                       
  dd 1 ;   p_type
  dd 7 ;p_flags
  dq 0 ;   p_offset
  dq $$ 
  dq $$ ;   p_paddr
  dq filesize ;   p_filesz
  dq filesize ;   p_memsz
  dq 0   ;   p_align

phdrsize equ $ - phdr

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

  input resb 2
  success db "That's right! Congratulations!", 0xa
  failure db "Unfortunately no. Try again!", 0xa
  welcome db "Hi! Can you guess about which number I'm thinking of? I can give you a hint! It's from range [0, 9].", 0xa

  filesize equ $ - $$

