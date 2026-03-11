p1: ∀n, n | 2 => n^2 | 2
p2: ∃n ∈ Z,n^2 < 0
p3: prove a|b ^ b|c => a|c
a|b <=> ka = b (k ∈ Z)
b|c <=> lb = c (l ∈ Z)
=> ka = c/l <=> kla = c (kl ∈ Z)
<=> a|c
p4: A ∪	B = {1,2,3,4,5}
A ∩ B = {3,4}
A\B = {1,2}
p5: ∀n ∈ Z, ∃m ∈ Z so that m>n
choose m = n+1, condition m ∈ Z still holds
∀n, m>n <=> n+1>n 
therefore it is true


$\forall x \in \mathbb{Z}, \exists y\ such\ that\ x = y^2$
$The\ statement\ is\ false$
$Choose\ x = -1, \nexists y \in \mathbb{R}\ where\ y^2 = 1$


p2: the two statements are NOT equivalent\
the first one is: for every x in R, there exist a y in R where y>x
the second one is: there exist a y in R where for every x in R, y>x
the first statement is true while the other is false

p3:
A ∩ (B ∪ C)
the LHS contains all the elements that is in A and B or A and C 
the second contains elements that is in A and B or A and C
so they are the same?

i know how it works but i don't know how to prove it because it sounds so obvious

p4: a ~ b mod n => n|(a-b) => kn = (a-b) (k ∈ Z)
a^2 ~ b^2 mod n => n| a^2-b^2 <=> n|(a+b)(a-b) <=> ln = (a-b)(a+b) (l ∈ Z)
yes because a multiple of a number can also divide by that number or something

p5:
a|b => ka = b (k ∈ Z)
a|c => la = c (l ∈ Z)
a|(b+c) must mean:
ma = b+c (m ∈ Z)
<=> ma = (k+l)a 
because both m and k+l are arbitrary integer ∈ Z, the statement is true
a|(b-c) must mean:
ma = b-c (m ∈ Z)
<=> ma = (k-l)a 
because both m and k+l are arbitrary integer ∈ Z, the statement is true

pigeonhole principle
if 13 people are in a room, at least two have birthdays in the same month
Create sets, each for a month. What ever the birth month of the person is, put them in the relative set.
There are 12 sets representing 12 different months. but there are 13 people. Therefore, there must exist at least one set where there are two people
This is equivalent to them having the same birth month

strong piegonhole 
Prove: Among 100 integers, there exist two whose difference is divisible by 99.
the idea is that instead of the integers lying on a line, they line on a table or grid of n columns (this time 99). the row is just labeled from 1 -> inf
we must choose 100 numbers so that no two shares the same column
formally: 
divide choosen integer to sets base on their modulo with 99
integer will fall into one of the set: {Xn | 0<=n >= 98}
if a set contains two number, then their differences is divisible by 99 because:
a~n mod 99 <=> 99k = a-n (k ∈ Z)
b~n mod 99 <=> 99l = b-n (l ∈ Z)
a-b~0 mod 99 <=> 99m = (n+99k)-(n+99l) <=> 99m = (k-l)99 (k-l ∈ Z) (m ∈ Z)
There are 99 sets. But 100 numbers. By the Pegionhole principle, there must be a set that contains 2 numbers. The difference between those two number must be divisbile by 99

Relation
A ∈ Z. R is subset of AxA
aRb ⟺ a−b is even (a Relates to b when a-b is even)
R = {(a, b) | a~b mod 2}
1. Prove R is reflexive
aRa <=> a-a is even
a~a mod 2 <=> 2k | a-a <=> 2k = a <=>
2k = 0 (true when k = 0)
therefore 1. is true
2. Prove R is symmetric
assume a-b is even. We need to prove b-a is even.
with the first assumption, a~b mod 2 <=> 2k = a-b
b-a = -2k. 2|2(-k). Therefore b-a is even, and 2. is true
3. Prove R is transitive 
assume 2|(a-b) ^ 2|(b-c) 
prove 2|(a-c)
From assumption: a-b = 2k; b-c = 2l <=> a = 2k+b; b = 2l+c <=> a = 2k+2l+c(k,l ∈ Z)
we need to prove: a-c = 2m (m ∈ Z)
<=> 2k+2l+c-c = 2m <=> 2(k+l) = 2m
this is true
therefore 3. is true
because 1. 2. and 3. is true, R is an equivalence function

p2: 
[0]={x∈A∣xR0 <=> x-0 even}
[10]={x∈A∣xR0 <=> x-1 even}
all even and all odds integer split into two classes


