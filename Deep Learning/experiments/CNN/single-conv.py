import numpy as np

# define a 3d tensor
# define 2d kernel
# define 1 3d filter which stacks those 2d kernels
# stride, padding, kernel size, original shape step
# write a for loop for i in range(floor(kernel)-1, original_size - floor(kernel), stride):
# stacked in another for loop for j in range(floor(kernel)-1, original_size - floor(kernel), stride):
# for each: we apply each filter in: for k, filter in enumerate(filters): image[:][i-floor(kernel):i+floor(kernel)][j-floor(kernel):j+floor(kernel)] this is the local patch of the image
# then we multiply it with the filter: *filter
# and then add all: np.sum(res, keep_dims=false)
# and then add bias: ans + bias
# and then store in array out[k][i][j] = ans+bias
# this is almost correct but there are still areas to improve


import numpy as np

C, H, W = 3, 32, 32
N = 10
K = 5
S = 1
P = 2

image = np.random.randn(C, H, W)
filters = np.random.randn(N, C, K, K)
bias = np.random.randn(N)

# padding
image = np.pad(image, ((0,0),(P,P),(P,P)))

H_out = (H - K + 2*P)//S + 1
W_out = (W - K + 2*P)//S + 1

out = np.zeros((N, H_out, W_out))

for n in range(N):                  # each filter
    for i in range(H_out):
        for j in range(W_out):

            h = i * S
            w = j * S

            patch = image[:, h:h+K, w:w+K]

            out[n, i, j] = np.sum(patch * filters[n]) + bias[n]

print(out.shape)