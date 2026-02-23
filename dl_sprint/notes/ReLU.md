turns out it is a max(0, x) function haha
but it makes me wonder how such a simple graph can produce such sophisticated model like instead of gradient lanscape, you get a linear landscape whichs flats at 0

Can a bias-free ReLU network represent the function:
f(x)=x+3

first question is what is a bias free ReLU network
it is a matrix of W matrix (so layers stack on top of each other) 
transformation is locked to: w.x not w.x + b

second question is what is representing the function f means
well that means: it can do this: pass in an input. it output that input + 3 (input is limited to be a number of course)
that means there has to be a way for 
z -> z+3 so w.x = x+3?
i don't know how to prove this numerically but it seems like it would be very hard if not impossible 
so more theoretical:
x is 1 input.
w is a matrix of: (ix1) so we can have this:
z = w1x + w2x + w3x + ... + wix = x + 3
we need 1 w terms to be 1 so we get x
we need some terms to always be a constant
-> this should be impossible. unless there is some way to vary the size of W depending on the mangitude of x and do some: wi = 3/xsize(w) or something

Can a bias-free ReLU network represent 
f(x)=∣x∣?
homogeneuitiy test f(0) = 0 
good
some combination of ReLU + transformer
E(i)wi*x
needs to represent sign
relu cuts off negative and coerce it to 0
we divide the weight into 2 part:
w1 is 1 w2 is -1
first transform:
w' = [w1.x, w2.x]
then ReLU
ReLU(w')
then tranform again into output
z = w'.x