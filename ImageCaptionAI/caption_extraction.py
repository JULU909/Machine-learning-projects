
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import string
from pickle import load, dump
from nltk.translate.bleu_score import corpus_bleu

def caption_dictionary(raw_caption):
    """
    Input: raw_caption as retrieved from the dataset
    Return: A dictionary mapping [photo_id] -> caption_list of that photo
    """
    captions = {}
    for line in raw_caption.split('\n'):
        if len(line) < 1:
            continue
        
        tmp = line.split()
        photo_id = tmp[0].split('.')[0] #id
        caption = ' '.join(tmp[1:])
        
        if photo_id not in captions.keys():
            captions[photo_id] = []
        captions[photo_id].append(caption) #A list of captions

    return(captions)

def caption_cleaning(caption_dict):
    """
        Input: caption_directory.
        Perform text pre-processing for captions
        Return: caption_directory after pre-processing
    """
    trans_table = str.maketrans('', '', string.punctuation)
    for photo_id, caption_list in caption_dict.items():
        for i in range(len(caption_list)):
            caption = caption_list[i]
            caption = caption.lower()
            #caption = re.sub('[^\w\s]', '', caption) #remove punctuation & special character
            caption = caption.translate(trans_table) #remove punctuation only
            
            caption_list[i] = caption
            
    return(caption_dict)

if __name__ == "__main__"():
    with open("Flickr8k_text/Flickr8k.token.txt", "r") as f:
        raw_caption = f.read()

    caption_dict = caption_dictionary(raw_caption)
    caption_dict = caption_cleaning(caption_dict)

    #Save the caption_dict for future use
    with open("captions.pkl", "wb") as f:
        dump(caption_dict, f)