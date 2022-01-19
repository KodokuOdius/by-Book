import numpy as np


a = np.array([[0, 1, 2], [3, 4, 5]])
print(a)

b = np.zeros((2, 3))
print(b)

c = np.ones((5, 4))
print(c)

d = np.zeros_like(c)
print(d)

e = np.eye(9)
print(e)

f = np.arange(2.1, 9, 0.5)
print(f)

g = np.ones_like(c, "complex")
print(g)

h = c.astype("bytes")
print(h)

print(c[:][1])

r = np.array([
    [1, 2, 3, 4], 
    [5, 6, 7, 8]
])

r[np.logical_or(r < 4, r >7)] = 0
print(r)

q = np.arange(30)
q1 = q.reshape(5, 6)

q2 = q.reshape(3, 2, 5)

print(q1)
print(q2)

print(q2.ndim)


print(q2.ravel())
