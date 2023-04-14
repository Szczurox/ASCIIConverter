import PIL.Image
import os
import time
import re

dir_path = os.path.dirname(os.path.realpath("ascii_image.txt"))
ASCII_CHARS = ["@", "#", "$", "%", "?", "*", "+", ";", ":", ",", "."]

# resize image
def resize_image(image, new_width=500):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * (ratio / 2.5))
    resized_image = image.resize((new_width, new_height))
    return resized_image


# convert image to grayscale
def grayify_image(image):
    grayscale_image = image.convert("L")
    return grayscale_image


# convert grayscale image pixels to ASCII
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ""
    for pixel in pixels:
        characters += ASCII_CHARS[pixel//(256//len(ASCII_CHARS)+2)]
    return characters


# custom ASCII characters set
def ascii_char_check():
    ascii_char = input("Enter the ASCII characters you want to use in the conversion, in one string, eg. @#$%?\n")
    if len(ascii_char) != len(ascii_char.encode()):
        print("you can only use ASCII characters!")
        chars = ascii_char_check()
    else:
        chars = re.findall('.', ascii_char)
    return chars


def main():
    path = input("Enter path to an image:\n")
    image = None
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "is not valid path to an image.")
        main()

    new_width = int(input("Enter width:\n"))

    inp = ""
    while inp != "y" and inp != "n":
        inp = input("Do you want to use basic ASCII characters set? (y/n)\n")
        if inp != "y" and inp != "n":
            print("answer y (yes) or n (no)\n")
            inp = input("Do you want to use basic ASCII characters set?\n")

    if inp == "n":
        ASCII_CHARS[:] = list(ascii_char_check())

    # convert image to ASCII
    new_image = pixels_to_ascii(grayify_image(resize_image(image, new_width)))

    # format
    pixels_count = len(new_image)
    ascii_image = "\n".join(new_image[i:(i+int(new_width))] for i in range(0, pixels_count, new_width))

    # print
    print(ascii_image)

    # save result
    with open("ascii_image.txt", "w") as f:
        f.write(ascii_image)

    time.sleep(1.5)
    print(f'done')
    os.system("start " + "ascii_image.txt")


main()
