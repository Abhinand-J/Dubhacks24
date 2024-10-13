import librosa
import numpy as np

y1, sr1 = librosa.load('./songwavs/LoveStory_TaylorSwift.wav')
y2, sr2 = librosa.load('./songwavs/LoveStory_TaylorSwift.wav')


mfcc1 = librosa.feature.mfcc(y=y1, sr=sr1)
librosa.display.specshow(mfcc1)

mfcc2 = librosa.feature.mfcc(y=y2, sr=sr2)
librosa.display.specshow(mfcc2)

# outputs value from 0 to 1, 0 being least similar and 1 being most similar
def cosine_similarity_mfcc(MFCC_1, MFCC_2):
    # Take the mean of each MFCC over the time axis (axis=1)
    mean_mfcc1 = np.mean(mfcc1, axis=1)
    mean_mfcc2 = np.mean(mfcc2, axis=1)

    # Normalize the MFCCs
    norm_mfcc1 = mean_mfcc1 / np.linalg.norm(mean_mfcc1)
    norm_mfcc2 = mean_mfcc2 / np.linalg.norm(mean_mfcc2)

    # Compute the cosine similarity
    cosine_similarity = np.dot(norm_mfcc1, norm_mfcc2)
    return cosine_similarity


dist = cosine_similarity_mfcc(mfcc1, mfcc2)
print(dist)