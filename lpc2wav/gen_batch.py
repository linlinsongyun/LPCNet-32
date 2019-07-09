import os


#utt10/m10/nor-p272

def gen_wav(lpc32):
    model_list = ['m05','m15','m25','m35','m40']
    for fi in list(model_list):
        model = os.path.join(lpc32, fi)
        xvec_lpc32 = os.path.join(model, 'nor-p362/lpc32')
        #print('xvec_lpc32',xvec_lpc32)
        xvec_save = os.path.join(model, 'nor-p362')
        os.system('python mel2wav.py %s %s' %(xvec_lpc32, xvec_save))

        xvec_p275_lpc32 = os.path.join(model, 'nor-p351/lpc32')
        xvec_p275_save = os.path.join(model, 'nor-p351')
        os.system('python mel2wav.py %s %s' %(xvec_p275_lpc32, xvec_p275_save))
'''
def gen_wav(lpc32):
    #model = os.path.join(lpc32, 'm20')
    model = lpc32
    xvec_lpc32 = os.path.join(model, 'nor-p362/lpc32')
    xvec_save = os.path.join(model, 'nor-p362')
    os.system('python mel2wav.py %s %s' %(xvec_lpc32, xvec_save))
    xvec_lpc32 = os.path.join(model, 'nor-p351/lpc32')
    xvec_save = os.path.join(model, 'nor-p351')
    os.system('python mel2wav.py %s %s' %(xvec_lpc32, xvec_save))
'''
def main():
    #xvec_lon2
    #xvec_lon2_lpc32 = '/home/zhangying09/.jupyter/voice-conversion-vector/vc-xvec/vctk89-100/vctk-xvec-lon2/test_0614/xvec100-lon2/utt30'
    #gen_wav(xvec_lon2_lpc32)
    xvec_whole_lpc32 = '/home/zhangying09/.jupyter/voice-conversion-vector/vc-xvec/vctk89-100/vctk100-xvec-whole/test_0608/xvec100-whole/utt05'
    gen_wav(xvec_whole_lpc32)
    xvec_whole_lpc32 = '/home/zhangying09/.jupyter/voice-conversion-vector/vc-xvec/vctk89-100/vctk100-xvec-whole/test_0608/xvec100-whole/utt30'
    gen_wav(xvec_whole_lpc32)
    xvec_whole_lpc32 = '/home/zhangying09/.jupyter/voice-conversion-vector/vc-xvec/vctk89-100/vctk100-xvec-whole/test_0608/xvec100-whole/utt10'
    gen_wav(xvec_whole_lpc32)
    xvec_whole_lpc32 = '/home/zhangying09/.jupyter/voice-conversion-vector/vc-xvec/vctk89-100/vctk100-xvec-whole/test_0608/xvec100-whole/utt01'
    gen_wav(xvec_whole_lpc32)
    
if __name__ == '__main__':
    main()
