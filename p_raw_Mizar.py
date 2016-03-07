# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt 

# to install rawpy do
# sudo apt-get install libraw-dev
# pip install rawpy
import rawpy

# determine offset of JPG image relative to RAW
# use astrophoto of Mizar (zeta UMa)
m=3   # draw small square around the star
m2=10 # square limits of the plot
ic=1  # use green color for finding maxima

FN=FNCR2 ='T6i_IMG_1413_MizarA-B-Alcor.CR2'
raw=rawpy.imread(FN)
rr=raw.raw_image.copy()
print 'full',rr.shape
rv=raw.raw_image_visible.copy()
print 'visible',rv.shape
#my_params = rawpy.Params(output_bps=16)
#rgb = raw.postprocess(my_params)
rgb = raw.postprocess()

j,i=np.unravel_index(rgb[:,:,ic].argmax(),rgb[:,:,ic].shape)
print rgb.shape, np.min(rgb),np.max(rgb),np.unravel_index(rgb[:,:,ic].argmax(),rgb[:,:,ic].shape),np.mean(rgb),np.std(rgb)
plt.figure()
plt.imshow(rgb)
plt.plot([i-m,i+m,i+m,i-m,i-m],[j+m,j+m,j-m,j-m,j+m],'r-') # plot small red square around the star
plt.axis([i-m2,i+m2,j-m2,j+m2])
plt.title(FN)
plt.show()

ir,jr=i,j
rgbraw=rgb.copy()


#FNJPG=FN.replace('.CR2','.JPG')
FN=FNJPG='T6i_IMG_1413_MizarA-B-Alcor.JPG'
rgb=plt.imread(FN)

j,i=np.unravel_index(rgb[:,:,ic].argmax(),rgb[:,:,ic].shape)
print rgb.shape, np.min(rgb),np.max(rgb),np.unravel_index(rgb[:,:,ic].argmax(),rgb[:,:,ic].shape),np.mean(rgb),np.std(rgb)
plt.figure()
plt.imshow(rgb)
plt.plot([i-m,i+m,i+m,i-m,i-m],[j+m,j+m,j-m,j-m,j+m],'r-') # plot small red square around the star
plt.axis([i-m2,i+m2,j-m2,j+m2])
plt.title(FN)
plt.show()

ij,jj=i,j
rgbjpg=rgb.copy()


print 'jpg offset from raw:',ir-ij,jr-jj
print 'jpg offset from visible:',ir-ij-72,jr-jj-34

"""
In [1]: run p_raw_Mizar
full (4056, 6096)
visible (4056, 6096)
(4056, 6096, 3) 127 255 (1865, 3074) 180.62224112 53.760719183
(4000, 6000, 3) 0 255 (1819, 2990) 0.0388426944444 0.26577840724
jpg offset from raw: 84 46
jpg offset from visible: 12 12
"""