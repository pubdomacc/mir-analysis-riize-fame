# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 12:14:57 2025

@author: CrowdDana
"""

import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import os

def load_audio(path, sr=22050):
    """Load an audio file into waveform + sample rate."""
    y, sr = librosa.load(path, sr=sr)
    return y, sr


def plot_waveform(y, sr, title="Waveform"):
    plt.figure(figsize=(12, 3))
    librosa.display.waveshow(y, sr=sr)
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_rms(y, title="RMS Energy"):
    rms = librosa.feature.rms(y=y)[0]

    plt.figure(figsize=(12, 3))
    plt.plot(rms)
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_mel_spectrogram(y, sr, title="Mel Spectrogram"):
    S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
    S_dB = librosa.power_to_db(S, ref=np.max)

    plt.figure(figsize=(12, 4))
    librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
    plt.colorbar(format="%+2.0f dB")
    plt.title(title)
    plt.tight_layout()
    plt.show()


def plot_chroma(y, sr, title="Chroma Features"):
    chroma = librosa.feature.chroma_stft(y=y, sr=sr)

    plt.figure(figsize=(12, 4))
    librosa.display.specshow(chroma, x_axis='time', y_axis='chroma', sr=sr)
    plt.colorbar()
    plt.title(title)
    plt.tight_layout()
    plt.show()
