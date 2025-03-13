import torch
from torch import nn
from helper import accuracy_fn

# device agonostic code
device = "cuda" if torch.cuda.is_available() else "cpu"

def train_step(model: nn.Module,
               data_loader: torch.utils.data.DataLoader,
               loss_fn : nn.Module,
               optimizer: torch.optim.Optimizer,
               accuracy_fn = accuracy_fn,
               device: torch.device = device):
    
    """Performs training steps of model with corresponding dataloader"""
    
    train_loss, train_acc = 0, 0
    
    model.train()

    
    for batch, (X,y) in enumerate(data_loader):
        
        X,y = X.to(device), y.to(device)
        
        train_logits = model(X)
        
        # In batch u should accumulate the train loss and acc
        loss = loss_fn(train_logits, y)
        train_loss += loss 
        train_acc  = accuracy_fn(y, train_logits.argmax(dim=1))
        
        optimizer.zero_grad()
        
        loss.backward()
        
        optimizer.step()
        
        if batch % 400 == 0:
            print(f"Look at {batch * len(X)} / {len(data_loader) * 32 } samples")
    
    train_loss = train_loss / len(data_loader)
    train_acc = train_acc / len(data_loader)
    
    print(f"Train loss : {train_loss} | Train Acc : {train_acc} ")
    
    
    
def test_step(model: torch.nn.Module,
              data_loader : torch.utils.data.DataLoader,
              loss_fn: nn.Module,
              accuracy_fn= accuracy_fn,
              device: torch.device = device):
    
    test_loss, test_acc = 0, 0
    
    model.eval()        

    with torch.inference_mode():

        for X,y in data_loader:
            
            X,y = X.to(device), y.to(device)

            test_logits = model(X)
            
            loss = loss_fn(test_logits, y)
            test_loss += loss
            
            test_acc += accuracy_fn(y, test_logits.argmax(dim=1))
        
        test_loss = test_loss / len(data_loader)
        test_acc = test_acc / len(data_loader)
        
        print(f"Test loss : {test_loss} |  Test acc : {test_acc}")
            
    
        
    