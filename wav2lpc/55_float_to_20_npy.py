import io,os
import numpy as np
import pickle as p
import struct
import sys

rootdir = sys.argv[1]
#'../../corpus/arc_test32'
#rootdir = 'bdl'
out_dir = sys.argv[2]
#'../bfcc/arctic_bfcc/'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
list = os.listdir(rootdir)
for i in range(0,len(list)):
   path = os.path.join(rootdir,list[i])
   print(path)
   f=open(path,"rb")
   d_str = f.read()
   f.close()
   d_len = len(d_str)
   print("list",list[i])
   print("len",d_len)
   j=d_len//196
   data = struct.unpack(str(d_len/4)+'f',d_str)
   # 1feature ---byte4
   c=np.array(data)
   d=c.reshape((j,49))
   print(len(d))
   lpc20 = np.delete(d,[32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48],axis=1)
   length = len(list[i])
   print("out_name",list[i][0:length-3])
   path2 = os.path.join(out_dir,list[i][0:length-3]+".mel.npy")
   np.save(path2,lpc20)
   print(path2)
