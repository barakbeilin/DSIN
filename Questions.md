1. AE.py Line 75 - why do you used tf.stop_gradient ? \
2. quantizer_imgcomp.py  - it seems that you must run the function to enter the condition
than this the function calls itself again, why is the ```transpose_NHWC_to_NCHW``` so important ?
3. AE.get_train_op