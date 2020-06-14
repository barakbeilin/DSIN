Thesis 
1. Thesis equation A.1 is not like Equation 14 in the compression paper, did the original paper (the Swiss..) have a typo?
    1. Should there be a ceil operation ?
2. Find where the quantization centers are updated
3. (skip, no need to answer) This model receives Z¯ (latent space quantized to L centers) as input and outputs a per pixel logits (???) vector
in Z¯ (which is the probability of the certain pixel to be assigned to a certain center
C1::CL). The context model consists of four 3D convolution layers with a causality ```answer``` ```logit``` -Per-label activations, typically a linear output. These activation energies are interpreted as unnormalized log probabilities.

Code 
1. AE.py Line 75 - why do you used tf.stop_gradient ? 
2. AE.get_train_op - elaborate what's going on 

Autoencoder Code 
1. autoencoder_imgcomp.py line 102 .. what's going on there?
2. _Network3D.variables what is tf.trainable_variables
3. quantizer_imgcomp.py  - what's the purpose of  ```transpose_NHWC_to_NCHW``` ?
4. how did does context model and the autoencoder train concurrently? 
