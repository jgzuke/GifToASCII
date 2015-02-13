from PIL import Image 
image_file = Image.open("test.png")
image_file = image_file.convert('1')
image_file.save('result.png')