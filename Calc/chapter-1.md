Ex:
Q11
a) z = x^2y^3 x = u cos v, y = u sin v
dz/du = dz/dx * dx/du + dz/dy * dy/du
= 2xy^3 * cosv + 3x^2y^2 * sinv
= 2 * u cosv * u^3 sin^3v * cosv + 3 * u^2 cos^2v * u^2 sin^2v * sinv
dz/dv = dz/dx * dx/dv + dz/dy * dy/dv
= -2xy^3 * usinv + 3x^2y^2 * ucosv
b) z = sin x cos y, x = uv^2, y = u^2v
dz/du = cosxcosy * v^2 - sinxsiny * 2uv
dz/dv = cosxcosy * 2uv - sinxsiny * u^2

Q12:
A = r cost * du/dx * cost + r sint * du/dy * sint

Q13:
a. <fx,fy> = 7, 7
theta = pi/6 => (sqrt(3)/2, 1/2) (normalized) 
U = 7sqrt(3)/2, 7/2 = 7(sqrt(3)+1)/2
b. <fx,fy> = 1, 0
theta = pi/4 => (sqrt(2)/2, sqrt(2)/2) (normalized)
U = sqrt(2)/2, 0 = sqrt(2)/2

Q14:
a. fx = (x^2+y^2 - 2x^2)/(x^2+y^2)^2 = 3/25
fy = -2xy/(x^2+y^2)^2 = -4/25
3/sqrt(34), 5/sqrt(34)
directional derivative = 3/25 * 3/sqrt(34) - 4/25 * 5/sqrt(34)
b. fx = y/(1+(xy)^2) = 2/5
fy = x/(1+(xy)^2) = 1/5
1/sqrt(5), 2/sqrt(5)
dd = 4/5sqrt(5)
c. 
fx = yz/2sqrt(xyz) = 1
fy = xz/2sqrt(xyz) = 3/2
fz = xy/2sqrt(xyz) = 1/2
i = -1/3; j = -2/3; k = 2/3
dd = -1/3 - 1 + 1/3 = -1
d. 
fx = 3/18 = 1/6
fy = 6/18 = 1/3
fz = 9/18 = 1/2
v = (
  2/7
  6/7
  3/7
)
dd = 1/6 * 2/7+1/3 * 6/7+1/2 * 3/7 = 23/42 = 0.54761904761

Q15. 
a. 
fx = 2y/sqrt(x) = 1
fy = 4sqrt(x) = 8
maximum rate of change: sqrt(65)
direction: (1/sqrt(65), 8/sqrt(65))
b.
fx = ycos(xy) = 0
fy = xcos(xy) = 1
max roc: 1
direction: (0,1)
c.
fx = x/sqrt(x^2+y^2+z^2) = 3/7
fy = 6/7
fz = -2/7
max roc: 1
direction: (3/7, 6/7, -2/7)
d.
fx = yz/(1+(xyz)^2) = 2/5
fy = xz/(1+(xyz)^2) = 1/5
fz = xy/(1+(xyz)^2) = 2/5
max roc: 3/5
direction: (2/3,1/3,2/3)

Q16.
fx = -y^2*e^(-xy) = -4
fy = 0
v=(cost,sint)
dd = -4cost = 1
cost = -1/4
t = arcos(-1/4) +2kpi
t = -arcos(-1/4) +2kpi
dd = dot product of the gradient vs the unit vector
(this one is not quite right)

Q17.
fx = 2x-2 
fy = 2y-4
v = (1,1)
normalized: (1/sqrt(2), 1/sqrt(2))
dd= sqrt(4x^2-8x+4+4y^2-16y+16)
(2x-2)/sqrt(4x^2-8x+4+4y^2-16y+16) = 1/sqrt(2)
(2y-4)/sqrt(4x^2-8x+4+4y^2-16y+16) = 1/sqrt(2)
<=>
4y^2-16y+16 = 4x^2-8x+4

Q18.
T(d) = k/d
T(3) = 120 (k = 360)
d=sqrt(x^2+y^2+z^2)
fx = k2/3
fy = k4/3
fz = k4/3
v = 2/sqrt(14),1/sqrt(14),3/sqrt(14)
dot between gradient and v


Q19.
a. 
vx = 10x-3y+yz = 38
vy = -3x+xz = 6
vz = xy = 12
v' = (1/sqrt(3), 1/sqrt(3), -1/sqrt(3))
RoC@v' = 32/sqrt(3)
b.
changes quickest in: (38, 6, 12) or normalized (19/sqrt(406), 3/sqrt(406), 6/sqrt(406))
c.
max roc:
Dd = |GradientV| = 2sqrt(406)

Q20.
a.
Tangent plane
8x−y−6z=7
Normal line
x=4+8t,y=7−t,z=3−6t
b. 
fx = yz^2-6 = -4
fy = xz^2-6 = -3
fz = 2xyz-6 = 0
normal v(-4, -3, 0)
tang -4x-3y+18=0
normal L: x = 3-4t;y = 2-3t;z=1
c. 
fx = 1-yze^(xyz) = 1
fy = 1-xze^(xyz) = 1
fz = 1-yze^(xyz) = 1
normal v(1,1,1)
tang x+y+z-1=0
normal L: x=t;y=t;z=1+t
d.
fx = 4x^3+y4+z^4-6xy^2z^2 = 4+1+1-6 = -2
fy = x^4+4y^3+z^4-6x^2yz^2 = 4+1+1-6 = -2
fz = x^4+y4+4z^3-6x^2y^2z = 4+1+1-6 = -2



