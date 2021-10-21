from PIL import Image
import torch
import glob


class CustomDataSet(torch.utils.data.Dataset):
    def __init__(self, path, transform):
        self.transform = transform
        self.image_list = []

        for filename in glob.glob(f"{path}/*.png"):  # assuming gif
            im = Image.open(filename)
            self.image_list.append(im)

    def __len__(self):
        return len(self.image_list)

    def __getitem__(self, index):
        image = Image.open(self.image_list[index]).convert("RGB")
        tensor_image = self.transform(image)
        return tensor_image
