exp1: conv = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
inp: (1,3,32,32)
out: (1,16,32,32)
exp2: conv = nn.Conv2d(3, 16, kernel_size=3, stride=2, padding=1)
inp: same
out: (1, 16, 16, 16)
exp3: conv = nn.Conv2d(3, 16, kernel_size=5, stride=1, padding=0)
inp: same
out: (1,16,28,28)
