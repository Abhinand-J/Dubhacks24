import librosa
import librosa.display
import matplotlib.pyplot as plt
from dtw import dtw
from numpy.linalg import norm as linalg_norm
import numpy as np

def get_all_videos(filepath1, filepath2):
    y1, sr1 = librosa.load(filepath1)
    y2, sr2 = librosa.load(filepath2)

    mfcc1 = librosa.feature.mfcc(y=y1, sr=sr1)
    mfcc2 = librosa.feature.mfcc(y=y2, sr=sr2)

    mfcc1 = np.array(mfcc1[0]) 
    mfcc2 = np.array(mfcc2[0])

    alignment = dtw(mfcc1, mfcc2)
    return alignment

