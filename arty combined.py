import random
from PIL import Image
import ctypes

def combinedRun():
    print("")
    print("")
    typeIn = input("Type of art generated (pixeldots,fadetowhite,fulllines,chunkylines,knitted,knittedlandscape,desktop): ")
    if typeIn == "pixeldots":
        pixelsToGen1 = input("Input pixel no: ")
        pixelsToGen = int(pixelsToGen1)
        im = Image.new("RGB", (pixelsToGen, pixelsToGen), color=(255, 255, 255))
        px = im.load()
        for p in range(pixelsToGen):
            rand1 = random.randrange(1, 255)
            rand2 = random.randrange(1, 255)
            rand3 = random.randrange(1, 255)

            for i in range(pixelsToGen):
                rand1 = random.randrange(1, 255)
                rand2 = random.randrange(1, 255)
                rand3 = random.randrange(1, 255)

                px[i, p] = (rand1, rand2, rand3)
                px[p, i] = (rand1, rand2, rand3)

        im.save("Pixels" + ".png", "PNG")
        combinedRun()
    elif typeIn == "fadetowhite":
        pixelsToGen1 = input("Input pixel no: ")
        pixelsToGen = int(pixelsToGen1)
        im = Image.new("RGB", (pixelsToGen, pixelsToGen), color=(255, 255, 255))
        px = im.load()
        for p in range(pixelsToGen):
            rand1 = random.randrange(1, 255)
            rand2 = random.randrange(1, 255)
            rand3 = random.randrange(1, 255)

            for i in range(pixelsToGen):
                rand1 = rand1 + 1
                rand2 = rand2 + 1
                rand3 = rand3 + 1
                px[i, p] = (rand1, rand2, rand3)
        im.save("Gradient" + ".png", "PNG")
        combinedRun()
    elif typeIn == "fulllines":
        pixelsToGen1 = input("Input pixel no: ")
        pixelsToGen = int(pixelsToGen1)
        im = Image.new("RGB", (pixelsToGen, pixelsToGen), color=(255, 255, 255))
        px = im.load()
        for p in range(pixelsToGen):
            rand1 = random.randrange(1, 255)
            rand2 = random.randrange(1, 255)
            rand3 = random.randrange(1, 255)

            for i in range(pixelsToGen):
                px[i, p] = (rand1, rand2, rand3)
        im.save("Fulllines" + ".png", "PNG")
        combinedRun()
    elif typeIn == "chunkylines":
        pixelsToGen1 = input("Input pixel no: ")
        pixelsToGen = int(pixelsToGen1)
        im = Image.new("RGB", (pixelsToGen, pixelsToGen), color=(255, 255, 255))
        px = im.load()
        for p in range(pixelsToGen):
            rand1 = random.randrange(1, 255)
            rand2 = random.randrange(1, 255)
            rand3 = random.randrange(1, 255)

            for i in range(pixelsToGen):
                if not rand1 == 0:
                    if not rand2 == 0:
                        if not rand3 == 0:
                            rand1 = rand1 - 1
                            rand2 = rand2 - 1
                            rand3 = rand3 - 1
                            px[i, p] = (rand1, rand2, rand3)
        im.save("chunkylines" + ".png", "PNG")
        combinedRun()
    elif typeIn == "knitted":
        pixelsToGen1 = input("Input pixel no: ")
        pixelsToGen = int(pixelsToGen1)


        def pixelMaker():
            for p in range(pixelsToGen):
                rand1 = random.randrange(1, 255)
                rand2 = random.randrange(1, 255)
                rand3 = random.randrange(1, 255)

                for i in range(pixelsToGen):
                    if rand1 == 0:
                        rand1 = random.randrange(1, 255) + 1
                        rand2 = random.randrange(1, 255) + 1
                        rand3 = random.randrange(1, 255) + 1
                    else:
                        rand1 = rand1 - 1

                    if rand2 == 0:
                        rand1 = random.randrange(1, 255) + 1
                        rand2 = random.randrange(1, 255) + 1
                        rand3 = random.randrange(1, 255) + 1
                    else:
                        rand2 = rand2 - 1
                    if rand3 == 0:
                        rand1 = random.randrange(1, 255) + 1
                        rand2 = random.randrange(1, 255) + 1
                        rand3 = random.randrange(1, 255) + 1
                    else:
                        rand3 = rand3 - 1

                    px[i, p] = (rand1, rand2, rand3)


        im = Image.new("RGB", (pixelsToGen, pixelsToGen), color=(255, 255, 255))
        px = im.load()
        pixelMaker()
        im.save("knitted" + ".png", "PNG")
        combinedRun()
    elif typeIn == "knittedlandscape":

        pixelsToGen1 = input("Input pixel no: ")
        pixelsToGen = int(pixelsToGen1)


        def pixelMaker():
            for p in range(pixelsToGen):
                rand1 = random.randrange(1, 255)
                rand2 = random.randrange(1, 255)
                rand3 = random.randrange(1, 255)

                for i in range(pixelsToGen * 2):
                    if rand1 == 0:
                        rand1 = random.randrange(1, 255) + 1
                        rand2 = random.randrange(1, 255) + 1
                        rand3 = random.randrange(1, 255) + 1
                    else:
                        rand1 = rand1 - 1

                    if rand2 == 0:
                        rand1 = random.randrange(1, 255) + 1
                        rand2 = random.randrange(1, 255) + 1
                        rand3 = random.randrange(1, 255) + 1
                    else:
                        rand2 = rand2 - 1
                    if rand3 == 0:
                        rand1 = random.randrange(1, 255) + 1
                        rand2 = random.randrange(1, 255) + 1
                        rand3 = random.randrange(1, 255) + 1
                    else:
                        rand3 = rand3 - 1

                    px[i, p] = (rand1, rand2, rand3)


        im = Image.new("RGB", (pixelsToGen * 2, pixelsToGen), color=(255, 255, 255))
        px = im.load()
        pixelMaker()
        im.save("knittedlandscape" + ".png", "PNG")
        combinedRun()
    elif typeIn == "desktop":
        user32 = ctypes.windll.user32
        width69 = user32.GetSystemMetrics(0)
        height69 = user32.GetSystemMetrics(1)


        def pixelMaker():
            for p in range(height69):
                rand1 = random.randrange(1, 255)
                rand2 = random.randrange(1, 255)
                rand3 = random.randrange(1, 255)

                for i in range(width69):
                    if rand1 == 0:
                        rand1 = random.randrange(1, 255) + 1
                        rand2 = random.randrange(1, 255) + 1
                        rand3 = random.randrange(1, 255) + 1
                    else:
                        rand1 = rand1 - 1

                    if rand2 == 0:
                        rand1 = random.randrange(1, 255) + 1
                        rand2 = random.randrange(1, 255) + 1
                        rand3 = random.randrange(1, 255) + 1
                    else:
                        rand2 = rand2 - 1
                    if rand3 == 0:
                        rand1 = random.randrange(1, 255) + 1
                        rand2 = random.randrange(1, 255) + 1
                        rand3 = random.randrange(1, 255) + 1
                    else:
                        rand3 = rand3 - 1

                    px[i, p] = (rand1, rand2, rand3)


        im = Image.new("RGB", (width69, height69), color=(255, 255, 255))
        px = im.load()
        pixelMaker()
        im.save("DesktopArt" + ".png", "PNG")
        combinedRun()
    else:
        print("Wrong input, try again")
combinedRun()