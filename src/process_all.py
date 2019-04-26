import os
import gatys_test

# Run all combinations of images
images = [os.path.join('..', 'images', name) for name in os.listdir(os.path.join('..', 'images'))]
for content in images:
    for style in images:
        if content is not style:
            output_name = os.path.basename(content).split('.')[0] + ' ' + \
                          os.path.basename(style).split('.')[0] + '.jpg'
            if not os.path.isfile(os.path.join('..', 'output', output_name)):
                gatys_test.create_image(content, style, show_output=True)