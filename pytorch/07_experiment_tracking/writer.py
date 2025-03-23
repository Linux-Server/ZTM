import torch
from torch.utils.tensorboard import SummaryWriter

def create_writer(exp_name:str,
                  model_name:str,
                  extra:str=None
                  ):
    from datetime import datetime
    import os

    timestamp = datetime.now().strftime("%Y-%m-%d")

    if extra:
        log_dir = os.path.join("runs", timestamp,exp_name,  model_name, extra)
    else:
        log_dir = os.path.join("runs", timestamp, exp_name , model_name)

    print(f"[INFO] : Cretaed summary writer and save to logs")

    return SummaryWriter(log_dir)
