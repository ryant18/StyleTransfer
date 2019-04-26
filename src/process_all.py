import os
import gatys_test

# Run all combinations of images
images = [os.path.join('..', 'images', name) for name in os.listdir(os.path.join('..', 'images'))]
for content in images:
    for style in images:
        if content is not style:
            gatys_test.create_image(content, style, show_output=True)