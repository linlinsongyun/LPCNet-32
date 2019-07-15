import os
import sys
wav_dir = sys.argv[1]
save_dir = sys.argv[2]
out16 = save_dir + '/out16'
out32 = save_dir + '/out32'
mel_20 = save_dir + '/mel_20'
if not os.path.exists(out16):
    os.makedirs(out16)
if not os.path.exists(out32):
    os.makedirs(out32)
if not os.path.exists(mel_20):
    os.makedirs(mel_20)
os.system('python wav2sec.py %s %s %s' %(wav_dir, out16, out32))
os.system('python 55_float_to_20_npy.py %s %s ' %(out32, mel_20))
