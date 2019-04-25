import tensorflow as tf
import matplotlib.pyplot as plt
import image_util as img
import model
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (10,10)
mpl.rcParams['axes.grid'] = False


tf.enable_eager_execution()
print("Eager execution: {}".format(tf.executing_eagerly()))

# Set up some global values here
content_path = '../images/Green_Sea_Turtle_grazing_seagrass.jpg'
style_path =   '../images/The_Great_Wave_off_Kanagawa.jpg'

content = img.load(content_path).astype('uint8')
style = img.load(style_path)

plt.subplot(1, 2, 1)
img.show(content, 'Content Image')

plt.subplot(1, 2, 2)
img.show(style, 'Style Image')
plt.show()

best, best_loss = model.run_style_transfer(content_path, style_path, num_iterations=1000)


def show_results(best_img, content_path, style_path, show_large_final=True):
    plt.figure(figsize=(10, 5))
    content = img.load(content_path)
    style = img.load(style_path)

    plt.subplot(1, 2, 1)
    img.show(content, 'Content Image')

    plt.subplot(1, 2, 2)
    img.show(style, 'Style Image')

    if show_large_final:
        plt.figure(figsize=(10, 10))

        plt.imshow(best_img)
        plt.title('Output Image')
        plt.show()


show_results(best, content_path, style_path)



