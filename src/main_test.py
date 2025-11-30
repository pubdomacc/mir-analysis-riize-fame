# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 12:53:04 2025

@author: CrowdDana
"""

from src.features import load_audio, plot_waveform, plot_rms, plot_mel_spectrogram, plot_chroma

#audio_path = "audio/fame.wav"  # adjust filename if needed
audio_path = "audio/02. Fame.wav"

# Load
y, sr = load_audio(audio_path)
print("Audio loaded!")
print("Waveform shape:", y.shape)
print("Sample rate:", sr)

# Plot
plot_waveform(y, sr)
plot_rms(y)
plot_mel_spectrogram(y, sr)
plot_chroma(y, sr)
