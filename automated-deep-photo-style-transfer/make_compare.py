import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import sys

content = mpimg.imread(sys.argv[1])
style = mpimg.imread(sys.argv[2])
output = mpimg.imread(sys.argv[3])

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(content)
plt.xticks([])
plt.yticks([])
plt.subplot(1,3,2)
plt.imshow(style)
plt.xticks([])
plt.yticks([])
plt.subplot(1,3,3)
plt.imshow(output)
plt.xticks([])
plt.yticks([])

plt.savefig("./compare/"+os.path.basename(sys.argv[1])+os.path.basename(sys.argv[2]), bbox_inches='tight')
