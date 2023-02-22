from PIL import Image, ImageFilter

img = Image.open('./jpg/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save('pik_blurr.png', 'png')
filtered_img2 = img.convert('L')
filtered_img2.save('pik_grey.png', 'png')
print(img)
print(img.size)
print(img.format)
print(img.mode)
# filtered_img2.show()  # otwiera w pliku
filtered_img3 = img.rotate(90)
filtered_img3.save('rotate.png', 'png')
filtered_img_resize = filtered_img.resize((300,300))
filtered_img_resize.save('pik_resize.png', 'png')

box = (100,100,400,400)
region = filtered_img.crop(box)
region.save('pik_croped.png', 'png')

ast = Image.open('./jpg/astro.jpg')
ast.thumbnail((400,400))
ast.save('ast_small.jpg')
print(ast.size)
print(ast.size)