import os
import sys
file_dir = sys.argv[1]
#'test_0404/pcm'
wav_path = sys.argv[2]
#'test_0404/wav'
if not os.path.exists(wav_path):
    os.makedirs(wav_path)

for files in os.listdir(file_dir):
    file_name = files.split('.pcm')[0]
    print("filename",file_name)
    wav_name = os.path.join(wav_path,"%s.wav"%file_name)
    print("wav", wav_name)
    file_path = os.path.join(file_dir, files)
    print("file",file_path)
    os.system('/usr/bin/sox -t raw -c 1 -e signed-integer -b 16 -r 16000 %s %s '% (file_path, wav_name))
