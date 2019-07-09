import os
import sys
cmp_path = sys.argv[1]
#'../../voice-conversion2/test_0404/cmp'
pcm_path = sys.argv[2]
#'../../voice-conversion2/test_0404/pcm'


if not os.path.exists(pcm_path):
    os.makedirs(pcm_path)

for fi in os.listdir(cmp_path):
    name = fi.split('.cmp')[0]
    cmp_name = os.path.join(cmp_path, fi)
    pcm_name = os.path.join(pcm_path, "%s.pcm"%name)
    os.system('./test_lpcnet %s %s' % (cmp_name, pcm_name))
