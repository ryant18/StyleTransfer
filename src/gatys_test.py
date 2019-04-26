import tensorflow as tf
import matplotlib.pyplot as plt
import image_util as img
import model
import matplotlib as mpl
import os
mpl.rcParams['figure.figsize'] = (10, 10)
mpl.rcParams['axes.grid'] = False

# Set Images --------------------------------------------
content_image_name = 'cardinal'
style_image_name = 'wave'

# Load Images -------------------------------------------
tf.enable_eager_execution()
print("Eager execution: {}".format(tf.executing_eagerly()))
content_path = os.path.join('..',  'images', content_image_name+'.jpg')
style_path = os.path.join('..', 'images', style_image_name+'.jpg')

# Run model ---------------------------------------------
best_img, best_loss, timeline_imgs = model.run_style_transfer(content_path, style_path, num_iterations=1000)

# Plot outputs ------------------------------------------
content = img.load(content_path)
style = img.load(style_path)

plt.figure(figsize=(15, 5))
plt.subplot(1, 3, 1)
img.show(content)
plt.xticks([])
plt.yticks([])
plt.subplot(1, 3, 2)
img.show(style)
plt.xticks([])
plt.yticks([])
plt.subplot(1, 3, 3)
plt.imshow(best_img)
plt.xticks([])
plt.yticks([])
fig_compare = plt.gcf()
plt.show()

plt.figure(figsize=(10, 10))
plt.imshow(best_img)
plt.xticks([])
plt.yticks([])
fig_output = plt.gcf()
plt.show()

num_rows = 2
num_cols = 5
plt.figure(figsize=(14, 4))
for i, img in enumerate(timeline_imgs):
    plt.subplot(num_rows, num_cols, i+1)
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
fig_timeline = plt.gcf()
plt.show()

# Save Images ---------------------------------------------
output_name = content_image_name + ' '+style_image_name+'.jpg'
fig_output.savefig(os.path.join('..', 'output', output_name), bbox_inches='tight')
fig_compare.savefig(os.path.join('..', 'compare', output_name), bbox_inches='tight')
fig_timeline.savefig(os.path.join('..', 'timeline', output_name), bbox_inches='tight')




