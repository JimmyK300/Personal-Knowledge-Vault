Problem 1 — Two-State Weather Model (Warm-up)
A city’s weather evolves as follows:
If today is Sunny, tomorrow is Sunny with probability 0.8.
If today is Rainy, tomorrow is Sunny with probability 0.4.

Tasks
Construct the transition matrix.
Is the chain irreducible?
Is it aperiodic?
Find the stationary distribution.
Does the chain converge? Why?

transistion matrix:
0.8 0.4
0.2 0.6

it is irreducible:  eigenvalue 1 is simple.
Aperiodic: No other eigenvalues lies on the unit circle.

Stationary distribution: 
0.66 0.33

It does, because it is aperiodic

Problem 2 — Exam Classic: Absorbing Chain
A student repeatedly attempts a test.
If they Fail, next attempt:
Fail again with probability 0.6
Pass with probability 0.4
If they Pass, they stop forever.

Tasks
Construct the transition matrix.
Identify absorbing states.
What is the probability the student eventually passes?
What is the expected number of attempts?
(Hint: This is geometric.)

Transistion matrix:
state: 1 fail 2 pass
0.6 0.4
0 1

Absorbing state is state 2 pass
100% they will pass given enough time.
Expected number of attempts: 2.5

Problem 3 — Periodicity Trap

Consider:

P=
	​c1
0
0
1
	​c2
1
0
0
	​c3
0
1
0

Tasks
Draw the state diagram. S1->S2->S3
Determine if the chain is irreducible. Yes: eigenvalue of simple 1
Determine the period. d = 3
Find eigenvalues. 1 e^(2/3pi.i) e^(4/3pi.i)
Does it converge? no: it is periodic
Does a stationary distribution exist? yes: 1/3 1/3 1/3

Problem 4 — Mixing Time Intuition
Let:
𝑃=(
0.9 0.1
0.1 0.9
)
Compute eigenvalues. 0.80
Compute spectral gap. 0.8^k
Is mixing fast or slow? moderate to slow
Approximate how many steps until error < 0.01. 0.8^k = 0.01 => maybe somewhere 10 or more. (this is through spectral decomposistion: Pkv= pi * c1 * 0.8^k *v1)