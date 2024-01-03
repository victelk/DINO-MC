# refer to: SeCo https://github.com/ServiceNow/seasonal-contrast

import os
from pathlib import Path

import random
import numpy as np
import rasterio
from PIL import Image
import utils.utils as utils
from torch.utils.data import Dataset
from torchvision import transforms
import torch.multiprocessing
torch.multiprocessing.set_sharing_strategy('file_system')

class MCBase(Dataset):
    def __init__(self, root, bands=None, transform=None):
        super().__init__()
        self.root = Path(root)
        self.transform = transform
        self.dataset = self.get_img_info(root)

    @staticmethod
    def get_img_info(data_dir):
        data_info = list()
        images_file = os.path.join(data_dir, "pretrain.txt")
        with open(images_file, 'r') as f:
            for line in f:
                name = line.strip()
                path_img = os.path.join(data_dir, "train", "A", name)
                data_info.append(path_img)
                path_img = os.path.join(data_dir, "train", "B", name)
                data_info.append(path_img)
        images_file = os.path.join(data_dir, "val90.txt")
        with open(images_file, 'r') as f:
            for line in f:
                name = line.strip()
                path_img = os.path.join(data_dir, "val", "A", name)
                data_info.append(path_img)
                path_img = os.path.join(data_dir, "val", "B", name)
                data_info.append(path_img)
        return data_info

    def __getitem__(self, index):
        path = self.dataset[index]
        img = Image.open(path)
        if self.transform is not None:
            img = self.transform(img)
        return img, 0

    def __len__(self):
        return len(self.dataset)

