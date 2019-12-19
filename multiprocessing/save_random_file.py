import os
import numpy as np

def main():
    if not os.path.isdir('random_files'):
        os.mkdir('random_files')
    #  random array
    for i in range(1000):
        random_img = np.random.randint(0, 255, size=(3, 1000, 1000))
        file_name = "%d.npy"%i
        np.save(os.path.join('random_files', file_name), random_img)


if __name__ == "__main__":
    main()
