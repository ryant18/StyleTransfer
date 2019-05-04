import tensorflow as tf
import matplotlib.pyplot as plt
import image_util as img
import numpy as np
import model
import os


def create_image(content_path, style_path, show_output=False, save_output=True):
    tf.enable_eager_execution()
    print("Eager execution: {}".format(tf.executing_eagerly()))
    # Run model ---------------------------------------------
    best_img, best_loss, timeline_imgs, total_loss, content_loss, style_loss\
        = model.run_style_transfer(content_path, style_path, num_iterations=1000)

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

    x = np.arange(len(total_loss))
    plt.gca().set_ylim([10e4, 10e7])
    plt.plot(x, np.array(total_loss), label='total loss')
    plt.plot(x, np.array(content_loss), label='content loss')
    plt.plot(x, np.array(style_loss), label='style loss')
    plt.yscale('log')
    plt.xlabel('epoc')
    plt.ylabel('loss')
    plt.legend(loc='upper right')
    fig_loss = plt.gcf()
    if show_output:
        plt.show()

    # Save Images ---------------------------------------------
    if save_output:
        output_name = os.path.basename(content_path).split('.')[0] + ' ' + \
                      os.path.basename(style_path).split('.')[0] + '.jpg'
        fig_output.savefig(os.path.join('..', 'output', output_name), bbox_inches='tight')
        fig_compare.savefig(os.path.join('..', 'compare', output_name), bbox_inches='tight')
        fig_timeline.savefig(os.path.join('..', 'timeline', output_name), bbox_inches='tight')
        fig_loss.savefig(os.path.join('..', 'loss', output_name), bbox_inches='tight')
