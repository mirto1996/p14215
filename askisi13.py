﻿import struct
import Image
import scipy
import scipy.misc
import scipy.cluster

NUM_CLUSTERS = 5

print 'reading image'
im = Image.open('image.jpg')
im = im.resize((150, 150))     
ar = scipy.misc.fromimage(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2])

print 'finding clusters'
codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
print 'cluster centres:\n', codes

vecs, dist = scipy.cluster.vq.vq(ar, codes)         
counts, bins = scipy.histogram(vecs, len(codes))    

index_max = scipy.argmax(counts)                    
peak = codes[index_max]
colour = ''.join(chr(c) for c in peak).encode('hex')
print 'most frequent is %s (#%s)' % (peak, colour)