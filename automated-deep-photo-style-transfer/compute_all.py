import subprocess
import os

images = [os.path.join('.', 'images', name) for name in os.listdir('images')]
for content in images:
    for style in images:
	if style is not content:
	    if not os.path.exists('results/'+ntpath.basename(content)+ntpath.basename(style)):
		print(content, style)
	    	subprocess.call(["python", "style_transfer.py", "--content_image", content, "--style_image", style])


