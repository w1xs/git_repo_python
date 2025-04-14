from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont
import sys


def check_float(number: str):
    for c in number:
        if c not in ".0123456789":
            return False
    return True


def check_coords(coords: str):
    result = []
    coords = coords.split()
    if len(coords) > 4:
        return None
    for i in range(len(coords)):
        if not coords[i].isdigit():
            return None
        if int(coords[i]) < 0:
            return None
        result.append(int(coords[i]))
    if len(result) == 4:
        if result[0] > result[2] or result[1] > result[3]:
            return None

    return result


def set_rotate(type: int, im):
    if type == 0:
        im = im.transpose(Image.FLIP_LEFT_RIGHT)
    elif type == 1:
        im = im.transpose(Image.FLIP_TOP_BOTTOM)
    elif type == 2:
        im = im.transpose(Image.TRANSPOSE)
    elif type == 3:
        im = im.transpose(Image.TRANSVERSE)
    else:
        return None
    return im


def set_sepia_filter(im):
    width, height = im.size
    pixels = im.load()

    for py in range(height):
        for px in range(width):
            r, g, b = im.getpixel((px, py))

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            if tr > 255:
                tr = 255

            if tg > 255:
                tg = 255

            if tb > 255:
                tb = 255

            pixels[px, py] = (tr, tg, tb)

    return im


def set_bright(coefficient: float, im):
    enchancer = ImageEnhance.Brightness(im)
    im = enchancer.enhance(coefficient)
    return im


def get_middle_color(im):
    mr = mg = mb = 0
    width, height = im.size
    all_pixels = width * height

    for py in range(height):
        for px in range(width):
            r, g, b = im.getpixel((px, py))

            mr += r
            mg += g
            mb += b

    mr = mr // all_pixels
    if mr > 255:
        mr = 255
    mg = mg // all_pixels
    if mg > 255:
        mg = 255
    mb = mb // all_pixels
    if mb > 255:
        mb = 255

    middle_color = (mr, mg, mb)

    new_im = Image.new(mode="RGB", size=(900, 900), color=middle_color)

    return new_im


def set_text(x: int, y: int, text: str, im):
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("arial.ttf", size=20)
    draw.text((x, y), text=text, font=font)
    return im


def set_figure(type: int, coords: (), im):
    draw = ImageDraw.Draw(im)
    if type == 0:
        draw.ellipse(coords, fill=(0, 191, 255), outline='black', width=3)
    if type == 1:
        draw.line(coords, fill=(0, 191, 255), width=3)
    if type == 2:
        draw.arc(coords, start=0, end=230, fill=(0, 191, 255), width=3)
    if type == 3:
        draw.rectangle(coords, fill=(0, 191, 255), outline='black', width=3)
    return im


def caller(im):
    print("Choose a number of an action from list:")
    print("1) Reflect the image vertically")
    print("2) Reflect the image horizontally")
    print("3) Reflect the image along the main diagonal")
    print("4) Reflect the image along the side diagonal")
    print("5) Apply a Sepia filter to the image")
    print("6) Increase the brightness of the image by k")
    print("7) Decrease the brightness of the image by k.")
    print("8) Demonstrate the average color of the image")
    print("9) Add text on top of the image according to the coordinates")
    print("10) Add a graphic primitive to the image")
    chose = input()
    match chose:
        case "1":
            im = set_rotate(0, im)
        case "2":
            im = set_rotate(1, im)
        case "3":
            im = set_rotate(2, im)
        case "4":
            im = set_rotate(3, im)
        case "5":
            im = set_sepia_filter(im)
        case "6":
            print("Enter the coefficient: ")
            k = input()
            if check_float(k):
                if float(k) > 0:
                    im = set_bright(float(k), im)
                else:
                    print("Coefficient if incorrect")
            else:
                print("Coefficient if incorrect")
            return None
        case "7":
            print("Enter the coefficient: ")
            k = input()
            if check_float(k):
                if float(k) > 0:
                    im = set_bright(float(k), im)
                else:
                    print("Coefficient if incorrect")
            else:
                print("Coefficient if incorrect")
            return None
        case "8":
            im = get_middle_color(im)
        case "9":
            print("Enter x coordinate: ")
            x = input()
            print("Enter y coordinate: ")
            y = input()
            print("Enter text: ")
            text = input()
            coords = "" + x + " " + y
            coords = check_coords(coords)
            if coords:
                im = set_text(coords[0], coords[1], text, im)
            else:
                print("Coordinates are incorrect")
        case "10":
            print()
            print("Choose a number of a primitive from list:")
            print("1) Ellips")
            print("2) Line")
            print("3) Arc")
            print("4) Rectangle")
            primitive = input()
            match primitive:
                case "1":
                    print("Enter coordinates of the figure: ")
                    coords = input()
                    coords = check_coords(coords)
                    if coords:
                        im = set_figure(0, coords, im)
                    else:
                        print("Coordinates are incorrect")
                        return None
                case "2":
                    print("Enter coordinates of the figure: ")
                    coords = input()
                    coords = check_coords(coords)
                    if coords:
                        im = set_figure(1, coords, im)
                    else:
                        print("Coordinates are incorrect")
                        return None
                case "3":
                    print("Enter coordinates of the figure: ")
                    coords = input()
                    coords = check_coords(coords)
                    if coords:
                        im = set_figure(2, coords, im)
                    else:
                        print("Coordinates are incorrect")
                        return None
                case "4":
                    print("Enter coordinates of the figure: ")
                    coords = input()
                    coords = check_coords(coords)
                    if coords:
                        im = set_figure(3, coords, im)
                    else:
                        print("Coordinates are incorrect")
                        return None
                case _:
                    print("No such number in the list")
                    return None
        case _:
            print("No such number in the list")
            return None
    return im


def main():
    print("Enter the path to the image: ")
    path = input()
    try:
        im = Image.open(path)
    except:
        print("Unable to load image")
        sys.exit(1)

    im = caller(im)

    if im:
        im.show()
        im.save("result.png")
        print("Result of work is saved as 'result.png' ")
    else:
        print("Something goes wrong, try again.")

    return


if __name__ == "__main__":
    main()
