# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 12:14:57 2025

@author: CrowdDana
"""

import librosa

# Load file
y, sr = librosa.load("audio/02. Fame.wav")
print("Audio loaded!")
print("Waveform shape:", y.shape)
print("Sample rate:", sr)
