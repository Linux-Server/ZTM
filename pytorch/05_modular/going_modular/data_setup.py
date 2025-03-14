
import os
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

NUM_WORKERS = 1

def create_dataloaders(train_dir: str,
                       test_dir: str,
                       transform: transforms.Compose,
                       batch_size:int,
                       num_workers:int=NUM_WORKERS):
    """Create Dataloader for train and test dataset

    Args:
        train_dir (str): path to train dir
        test_dir (str): path to test dir
        transform (transforms.Compose): tranform the 
        batch_size (int): no of items per batch
        num_workers (int, optional):  Defaults to NUM_WORKERS.

    Returns:
        train dataloader and test_dataloader
    """
    train_data = datasets.ImageFolder(root=train_dir,
                                      transform=transform,
                                      )
    
    test_data = datasets.ImageFolder(root=test_dir,
                                      transform=transform,
                                      )
    
    train_dataloader = DataLoader(dataset=train_data, shuffle=True,
                                  batch_size=batch_size,
                                  pin_memory=True)
    
    test_dataloader = DataLoader(dataset=test_data, shuffle=False,
                                 batch_size=batch_size, pin_memory=True)
    
    class_names = train_data.classes
    
    return train_dataloader, test_dataloader, class_names
