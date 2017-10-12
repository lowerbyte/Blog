%include "instructions.asm"

lbSET r4, data
lbSET r1, 1

lbLB r2, r4
lbOUT r2
lbADD r4, r1
lbLB r2, r4
lbOUT r2
lbADD r4, r1
lbLB r2, r4
lbOUT r2
lbADD r4, r1
lbLB r2, r4
lbOUT r2
lbADD r4, r1
lbLB r2, r4
lbOUT r2
lbADD r4, r1
lbLB r2, r4
lbOUT r2
lbADD r4, r1
lbLB r2, r4
lbOUT r2
lbADD r4, r1
lbLB r2, r4
lbOUT r2
lbADD r4, r1
lbLB r2, r4
lbOUT r2
lbADD r4, r1
lbLB r2, r4
lbOUT r2
lbADD r4, r1
lbLB r2, r4
lbOUT r2
lbADD r4, r1

data:
  db "Hello World", 0xa, 0
