#!/usr/bin/env python

import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

train = pd.read_csv("train.tsv", header=0, delimiter="\t", quoting=3)

train.shape

train.columns.values
array([id, sentiment, review], dtype=object)

print train[0][0]
