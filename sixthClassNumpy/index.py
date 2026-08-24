import numpy as np
a = np.array([2, 3, 4], dtype=np.uint32)
b = np.array([5, 6, 7], dtype=np.uint32)
c_unsigned32 = a - b
print('unsigned c:', c_unsigned32, c_unsigned32.dtype)
c_signed32 = a - b.astype(np.int32)
print('signed c:', c_signed32, c_signed32.dtype)