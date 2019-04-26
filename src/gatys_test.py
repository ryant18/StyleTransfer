import tensorflow as tf
import matplotlib.pyplot as plt
import image_util as img
import model
import matplotlib as mpl
import os
mpl.rcParams['figure.figsize'] = (10, 10)
mpl.rcParams['axes.grid'] = False


def create_image(content_path, style_path, show_output=False, save_output=True):
    tf.enable_eager_execution()
    print("Eager execution: {}".format(tf.executing_eagerly()))
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
    if show_output:
        plt.show()

    plt.figure(figsize=(10, 10))
    plt.imshow(best_img)
    plt.xticks([])
    plt.yticks([])
    fig_output = plt.gcf()
    if show_output:
        plt.show()

    num_rows = 2
    num_cols = 5
    plt.figure(figsize=(14, 4))
    for i, image in enumerate(timeline_imgs):
        plt.subplot(num_rows, num_cols, i+1)
        plt.imshow(image)
        plt.xticks([])
        plt.yticks([])
    fig_timeline = plt.gcf()
    if show_output:
        plt.show()

    # Save Images ---------------------------------------------
    output_name = os.path.basename(content_path.split('.')[0]) + ' ' + \
                  os.path.basename(style_path.split('.')[0]) + '.jpg'

    if save_output:
        fig_output.savefig(os.path.join('..', 'output', output_name), bbox_inches='tight')
        fig_compare.savefig(os.path.join('..', 'compare', output_name), bbox_inches='tight')
        fig_timeline.savefig(os.path.join('..', 'timeline', output_name), bbox_inches='tight')


content_path = os.path.join('..',  'images', 'cardinal' + '.jpg')
style_path = os.path.join('..', 'images', 'starry night' + '.jpg')
create_image(content_path, style_path)

