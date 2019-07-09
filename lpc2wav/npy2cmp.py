import numpy as np
import os
import sys
file_dir = sys.argv[1]
out_dir = sys.argv[2]
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
for fi in os.listdir(file_dir):
    if fi.endswith('.npy'):
        file_path = os.path.join(file_dir,fi)
        print("file",file_path)
        test=np.load(file_path)
        if(test.dtype == 'float64'):
            test = test.astype(np.float32)
        if(test.dtype == 'float32'):
            out_name = fi.split('.npy')
            output_dir = os.path.join(out_dir,"%s.32"%out_name[0])
            print("out",output_dir)
            fid = open(output_dir, 'wb')
            test.tofile(fid)
            #fid.write(test)
            fid.close()
