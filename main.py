import timm
import torch
import requests
from PIL import Image
from io import BytesIO
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.multiprocessing as mp
from torch.utils.data.sampler import Sampler
from torchvision import datasets, transforms
import json 


def inferencing_model(model, img_url): 
    #loading the image from url
    image = Image.open(requests.get(img_url, stream=True).raw)
    #defining a pretrained model from timm
    model = timm.create_model(model, pretrained=True).eval()
    transform = timm.data.create_transform(
        **timm.data.resolve_data_config(model.pretrained_cfg)
        ) 
    #preparing the image for the model 
    image_tensor = transform(image)
    output = model(image_tensor.unsqueeze(0))
    probabilities = torch.nn.functional.softmax(output[0], dim=0) #applying softmax to the output. 
    #print out the first 5 probabilities 
    values, indices = torch.topk(probabilities, 5)
    # indices
    IMAGENET_1k_URL = 'https://storage.googleapis.com/bit_models/ilsvrc2012_wordnet_lemmas.txt'
    IMAGENET_1k_LABELS = requests.get(IMAGENET_1k_URL).text.strip().split('\n')
    labels_and_values = [{'predicted': IMAGENET_1k_LABELS[idx].split(',')[0], 'confidence': val.item()} for val, idx in zip(values, indices)]

    return json.dumps(labels_and_values)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', default="cspresnext50", help='model name is a required param.')
    parser.add_argument('--image', default="https://github.com/pytorch/hub/raw/master/images/dog.jpg", help='image name is a required param.')
    args = parser.parse_args()
    print(f"Using model {args.model} to infer image {args.image}")
    ans = inferencing_model(model=args.model, img_url =args.image)
    print(ans)