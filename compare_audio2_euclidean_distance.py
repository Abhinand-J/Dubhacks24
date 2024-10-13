import librosa
import numpy as np

y1, sr1 = librosa.load('./songwavs/LoveStory_TaylorSwift.wav')
y2, sr2 = librosa.load('./songwavs/LoveStory_TaylorSwift.wav')


mfcc1 = librosa.feature.mfcc(y=y1, sr=sr1)
librosa.display.specshow(mfcc1)

mfcc2 = librosa.feature.mfcc(y=y2, sr=sr2)
librosa.display.specshow(mfcc2)

#outputs value from 0 to 1, 0 being most similar and 1 being most different
def euclidean_distance_mfcc(MFCC_1, MFCC_2):
    if MFCC_1.shape != MFCC_2.shape:
        raise ValueError("MFCC matrices must have the same dimensions.")
    
    # Compute Euclidean distance for each time frame
    distances = np.sqrt(np.sum((MFCC_1 - MFCC_2)**2, axis=1))
    
    # Optionally, aggregate distances (e.g., average)
    avg_distance = np.mean(distances)
    return avg_distance

dist = euclidean_distance_mfcc(mfcc1, mfcc2)
print(dist)