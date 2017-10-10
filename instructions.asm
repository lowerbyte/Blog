%define r0 0x00
%define r1 0x01
%define r2 0x02
%define r3 0x03
%define r4 0x04
%define r5 0x05
%define r6 0x06
%define r7 0x07
%define r8 0x08
%define IP 0x09
%define SP 0x0a

%macro lbADD 2
db 0x00, %1, %2
%endmacro

%macro lbCMP 2
db 0x01, %1, %2
%endmacro

%macro lbMOV 2
db 0x02, %1, %2
%endmacro

%macro lbSET 2
db 0x03, %1
dw %2
%endmacro

%macro lbLB 2
db 0x04, %1, %2
%endmacro

%macro lbSB 2
db 0x05, %1, %2
%endmacro

%macro lbJZ 1
db 0x06
dw (%1 - ($ + 2))
%endmacro

%macro lbJNZ 1
db 0x07
dw (%1 - ($ + 2))
%endmacro

%macro lbPUSH 1
db 0x08, %1
%endmacro

%macro lbPOP 1
db 0x09, %1
%endmacro

%macro lbJMP 1
db 0x10
dw (%1 - ($ + 2))
%endmacro

%macro lbCALL 1
db 0x11
dw (%1 - ($ + 2))
%endmacro

%macro lbOUT 1
db 0x10, %1
%endmacro


