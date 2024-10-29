from PIL import Image

img_src="1.png"
image = Image.open(img_src)
# image.show()
print(image.size)
crpp = image.resize((100, 100))
print(crpp.size)
#crpp.show()

out_converted = "avatar_converted.png"
image.save(out_converted, format="PNG")
image.show()


