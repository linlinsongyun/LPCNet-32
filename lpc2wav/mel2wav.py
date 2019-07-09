import sys
import os
import numpy as np


mel_dir = sys.argv[1]
save_dir = sys.argv[2]
out32 = save_dir + '/out32'
cmp_dir = save_dir +'/cmp'
pcm_dir = save_dir + '/pcm'
wav_dir = save_dir + '/wav'
if not os.path.exists(out32):
    os.makedirs(out32)
if not os.path.exists(cmp_dir):
    os.makedirs(cmp_dir)
if not os.path.exists(pcm_dir):
    os.makedirs(pcm_dir)
if not os.path.exists(wav_dir):
    os.makedirs(wav_dir)




print('begin npy2cmp')
os.system('python npy2cmp.py %s %s' %(mel_dir, out32))
print('32-to-49')
os.system('python 32-to-49.py %s %s' %(out32, cmp_dir))
print('cmp2pcm')
os.system('python cmp2pcm.py %s %s' % (cmp_dir, pcm_dir))
print('pcm2wav')
os.system('python pcm2wav.py %s %s' % (pcm_dir, wav_dir))
print('success')
