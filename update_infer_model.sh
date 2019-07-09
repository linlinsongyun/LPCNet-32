h5_modelfn=$1
CUDA_VISIBLE_DEVICES="1" \
python3 src/dump_lpcnet.py $h5_modelfn

mv nnet_data* src/
make test_lpcnet
