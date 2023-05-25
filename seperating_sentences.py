import re
import pandas as pd
import spacy
from spacy import displacy
import random
nlp = spacy.load('en_core_web_sm')

from spacy.matcher import Matcher 
from spacy.tokens import Span 

import matplotlib.pyplot as plt
from tqdm import tqdm

pd.set_option('display.max_colwidth', 200)


# import wikipedia sentences
textbook_sentences = pd.read_csv("sentences.csv")
textbook_sentences.shape()
