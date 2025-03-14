# lets create train and test loop engine

from torch import nn
# create the train setup
from torchmetrics import Accuracy


def train_step(model:nn.Module,
               data_loader: torch.utils.data.DataLoader,
               loss_fn : nn.Module,
               optimizer:torch.optim.Optimizer,
               num_class = 3,
               device = device):
    
    accuracy = Accuracy(task="multiclass", num_classes=num_class)

    
    # 1. put the model in train model
    model.train()
    # set metric
    train_loss, train_acc = 0, 0
    
    #loop on dataloader
    for batch, (X,y) in enumerate(data_loader):
        #send the data to target device
        X , y = X.to(device),  y.to(device)
        # forward pass
        train_logits = model_0(X)
        # calc the loss
        loss = loss_fn(train_logits, y)
        train_loss += loss
        # optimizer zero grad
        optimizer.zero_grad()
        #back pass
        loss.backward()
        # adjust the optimizer
        optimizer.step()
        
        # calc accuracy
        
        y_pred_class = torch.argmax(torch.softmax(train_logits, dim=1), dim=1)
        train_acc += accuracy(y_pred_class, y)
    
    
    train_acc = train_acc / len(data_loader)
    train_loss = train_loss / len(data_loader)
    
    return train_loss, train_acc
        
    

def test_step(model:nn.Module,
              data_loader: torch.utils.data.DataLoader,
              loss_fn : nn.Module,
              num_class = 3,
              device = device):
    
    accuracy = Accuracy(task="multiclass", num_classes=num_class)

    
    model.eval()
    # since its a dataloader, set test_loss and acc
    test_loss, test_acc = 0, 0
    
    # turn thr infereance mode
    with torch.inference_mode():
    
        for X,y in data_loader:
            
            # send data to target device
            X, y = X.to(device), y.to(device)
            
            #forward pass
            y_preds = model(X)
            
            loss = loss_fn(y_preds, y)
            
            test_loss += loss
            
            y_pred_label = torch.argmax(y_preds , dim=1)
            
            test_acc += accuracy(y_pred_label, y)
            
    test_loss = test_loss /len(data_loader)
    test_acc = test_acc / len(data_loader)
    
    return test_loss, test_acc
         
    
    
    
    
    

