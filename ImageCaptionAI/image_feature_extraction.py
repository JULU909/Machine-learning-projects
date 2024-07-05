import torch
import os
from torchvision import models, transforms
from PIL import Image
import pickle


def feature_extractions(directory):
    """
    Input: directory of images
    Return: A dictionary of features extracted by VGG-16, size 4096.
    
    Run feature extraction on images
    
    """
    
    model = models.vgg16(pretrained=True)
    model.classifier = torch.nn.Sequential(*list(model.classifier.children())[:-1])  # Remove the final layer
    
    model.eval()  # Set model to evaluation mode
    
    # Define image preprocessing
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    
    features = {}
    
    with torch.no_grad():  # Disable gradient calculation
        for f in os.listdir(directory):
            filename = os.path.join(directory, f)
            identifier = f.split('.')[0]
            
            # Load and preprocess the image
            image = Image.open(filename).convert('RGB')
            input_tensor = preprocess(image)
            input_batch = input_tensor.unsqueeze(0)  # Create a mini-batch as expected by the model
            
            # Extract features
            feature = model(input_batch)
            features[identifier] = feature.squeeze().numpy()
            
            print("feature extraction: {}".format(f))
            
    return features


if __name__ == "__main__":
    
    image_dir = r"C:\Users\Harish Vasanth\Desktop\Machine-learning-projects\ImageCaptionAI\Flickr8k_Dataset" 
    
    features = feature_extractions(image_dir)
    
    with open(r"C:\Users\Harish Vasanth\Desktop\Machine-learning-projects\ImageCaptionAI\image_features_VGG16.pkl", "wb") as f:
        pickle.dump(features, f)
    

