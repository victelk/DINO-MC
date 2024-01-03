 # copied from SeCo: https://github.com/ServiceNow/seasonal-contrast/blob/main/datasets/oscd_dataset.py
 
from pathlib import Path
from itertools import product

from torch.utils.data import Dataset
import rasterio
import numpy as np
from PIL import Image


class ChangeDetectionDataset(Dataset):

    def __init__(self, root, split='all', transform=None, patch_size=96):
        self.root = Path(root)
        self.split = split
        self.transform = transform

        with open(self.root / f'{split}.txt') as f:
            names = [line.strip() for line in f]

        self.samples = []
        for name in names:
            image_filename = self.root / self.split / 'A' / name
            im = Image.open(image_filename)
            width, height = im.size
            limits = product(range(0, width, patch_size), range(0, height, patch_size))
            for l in limits:
                self.samples.append((name, (l[0], l[1], l[0] + patch_size, l[1] + patch_size)))

    def __getitem__(self, index):
        name, limits = self.samples[index]

        img_1 = Image.open(self.root / self.split / 'A' / name)
        img_2 = Image.open(self.root / self.split / 'B' / name)
        cm = Image.open(self.root / self.split / 'OUT' / name).convert('L')

        img_1 = img_1.crop(limits)
        img_2 = img_2.crop(limits)
        cm = cm.crop(limits)

        if self.transform is not None:
            img_1, img_2, cm = self.transform(img_1, img_2, cm)

        return img_1, img_2, cm

    def __len__(self):
        return len(self.samples)
