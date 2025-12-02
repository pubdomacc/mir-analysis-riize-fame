MIR Analysis – RIIZE “Fame” (Work-in-Progress)

This project is a hands-on exploration of basic Music Information Retrieval (MIR) 
techniques using Python, Librosa, and Jupyter Notebook.
The goal is to understand and visualize key audio features such as waveform, spectrograms, 
chroma patterns, and dynamic characteristics from the song “Fame” by RIIZE.

The notebook is designed to be educational, transparent, and reproducible, making it 
suitable for portfolio use.

## ✨ What This Project Includes
Implemented so far

Jupyter notebook for step-by-step analysis

Environment setup using Python virtual environments

Audio loading and waveform visualization

Spectrogram (STFT) computation

Mel-Spectrogram

RMS Energy plot

Basic project structure + Git version control

Preliminary README

Upcoming additions (near-term)

Chromagram analysis

Onset strength envelope

MFCC features

Audio preprocessing (mono conversion, normalization)

More structured interpretations & commentary

Exporting plots for a mini portfolio

## 🔧 Environment Setup
1. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

2. Install required packages
pip install librosa matplotlib numpy soundfile

3. Launch Jupyter Notebook
jupyter notebook

## 📁 Project Structure
mir-analysis-riize-fame/
│
├── venv/                  # Local environment (ignored by Git)
├── .gitignore
├── README.md
├── notebook.ipynb
└── audio/                 # Local audio samples (not uploaded to repo)

## 🎯 Goals of This Project

Build a clean, self-explanatory MIR notebook suitable for portfolio submission

Develop deeper understanding of spectral, rhythmic, and harmonic features

Gradually extend toward a general DSP/MIR skillset

Prepare a micro-project template for future ML+DSP work

## 🚧 Status

This project is currently in active development, with new analysis features being added 
incrementally.
The next milestone adds chroma features and clearer commentary for each visualization.

## 📜 License

Open source for personal, educational, and portfolio use.
