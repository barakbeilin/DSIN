1. AE.py Line 75 - why do you used tf.stop_gradient ? \
2. quantizer_imgcomp.py  - it seems that you must run the function to enter the condition
than this the function calls itself again, why is the ```transpose_NHWC_to_NCHW``` so important ?
3. AE.get_train_op
4. _Network3D.variables what is tf.trainable_variables
5. Thesis equation A.1 is not like Equation 14 in the compression paper, did they have a typo?

    1. In addition wasn't there a ceil operation ?

6. This model receives Z¯ (latent space quantized to L centers) as input and outputs a per pixel logits (???) vector
in Z¯ (which is the probability of the certain pixel to be assigned to a certain center
C1::CL). The context model consists of four 3D convolution layers with a causality
7. how did you train the context model and the autoencoder concurrently? 