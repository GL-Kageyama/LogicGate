# =====================================
# ------------ Logic Gate -------------
# =====================================
#               XOR Gate
# =====================================
import numpy as np

def AND(x1, x2):
	x1_x2 = np.array([x1, x2])
	w0 = -0.8
	w1_w2 = np.array([0.5, 0.5])
	tmp = w0 + np.sum(w1_w2*x1_x2)
	if tmp <= 0:
		return 0
	elif tmp > 0:
		return 1

def NAND(x1, x2):
	x1_x2 = np.array([x1, x2])
	w0 = 0.8
	w1_w2 = np.array([-0.5, -0.5])
	tmp = w0 + np.sum(w1_w2*x1_x2)
	if tmp <= 0:
		return 0
	elif tmp > 0:
		return 1

def OR(x1, x2):
	x1_x2 = np.array([x1, x2])
	w0 = -0.4
	w1_w2 = np.array([0.5, 0.5])
	tmp = w0 + np.sum(w1_w2*x1_x2)
	if tmp <= 0:
		return 0
	elif tmp > 0:
		return 1

def XOR(x1, x2):
	_nand = NAND(x1, x2)
	_or = OR(x1, x2)
	_xor = AND(_nand, _or)
	return _xor

print(XOR(0, 0))
print(XOR(1, 0))
print(XOR(0, 1))
print(XOR(1, 1))

# =====================================
# x1  x2   
# 0   0  -> 0
# 1   0  -> 1
# 0   1  -> 1
# 1   1  -> 0
# =====================================