import os
import sys
import numpy as np
sec_path = sys.argv[1]
cmp_path = sys.argv[2]

if not os.path.exists(cmp_path):
    os.makedirs(cmp_path)

'''
# 20-55
for fi in os.listdir(sec_path):
    name = fi.split('.32')[0]
    print('name',name)
    sec_name = os.path.join(sec_path, fi)
    cmp_name = os.path.join(cmp_path, "%s.cmp"%name)
    os.system('./20-55 %s %s' % (sec_name, cmp_name))
'''
#20-37

for fi in os.listdir(sec_path):
    name = fi.split('.32')[0]
    print('name',name)
    sec_name = os.path.join(sec_path, fi)
    cmp_name = os.path.join(cmp_path, "%s.cmp"%name)
    lpc20 = np.fromfile(sec_name, dtype=np.float32)
    lpc20 = lpc20.reshape(-1,32)
    lpc55_1=np.insert(lpc20,32,[[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]],axis=1)
    print("lpc37",lpc55_1.shape)
    lpc55_1.flatten()
    data = np.array(lpc55_1,'float32')
    data.tofile(cmp_name)
