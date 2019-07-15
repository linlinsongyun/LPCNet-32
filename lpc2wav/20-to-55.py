import io,os
import numpy as np
import pickle as p
import struct

#a = np.fromfile("ks01667.wav.s32", dtype = float)
#c = len(a)/55
#print(len(a))
#d = a.reshape((c,55))

rootdir = '/media/disk1/chehao/LPCNet-master_test/king_feature'
list = os.listdir(rootdir)
for i in range(0,len(list)):
   path = os.path.join(rootdir,list[i])  
   f=open(path,"rb")
   d_str = f.read()
   f.close()
   d_len = len(d_str)
   print(list[i])
   print(d_len)
   j=d_len/220
   data = struct.unpack(str(d_len/4)+'f',d_str)
   c=np.array(data)
   d=c.reshape((j,55))
   print(len(d))
   lpc20 = np.delete(d,[18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54],axis=1)
   length = len(list[i])
   path2 = os.path.join(rootdir,list[i][0:length-8]+".mel.npy")
   np.save(path2,lpc20)

#test=np.loadtxt('ks01667.wav.s32')
#print(len(test))
#np.savetxt('1',test)
