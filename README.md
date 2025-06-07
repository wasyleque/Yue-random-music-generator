# Yue-random-music-generator
Simple script to generate music in loop with random genre, instruments, moods, gender, timbre

# AI Music Generation with YuE

This repository provides a Python script (`generate_now.py`) for generating AI-composed music using the [YuE](https://github.com/multimodal-art-projection/YuE) model. The script automates the process by randomizing musical attributes and lyrics.

## Installation

To use this script, first install **YuE** following the instructions in its [GitHub repository](https://github.com/multimodal-art-projection/YuE).

### Dependencies

Ensure you have Python installed along with the required dependencies:

```bash
pip install -r requirements_now.txt
```
Setup
+ Clone the YuE repository and set up the model as instructed.
+ Place generate_now.py inside the inference/ folder.
+ Download top_200_tags.json  from [here](https://github.com/multimodal-art-projection/YuE/blob/main/top_200_tags.json) and place it in the inference/ folder.
+ Ensure your prompt_egs/ folder contains various .txt lyric files.

Usage

Run the script to generate AI-composed music:
```
python generate_now.py
```
The script executes the YuE inference process 10 times, each with a randomized genre, instruments, mood, gender, and timbre, ensuring unique compositions.
How It Works ?
+ Randomly selects lyrics from the prompt_egs/ folder.
+ Creates a genre.txt file containing:  1 genre, 3-5 instruments, 1 mood, 1 gender, 1 timbre from top_200_tags.json.
+ Calls the YuE inference model.

Acknowledgments

This project utilizes the fantastic Yue model, created by [multimodal-art-projection](https://github.com/multimodal-art-projection). 
Huge thanks to its developers for enabling AI-driven music composition!

This README provides clear instructions, installation steps, usage, and proper attribution. Let me know if you'd like any tweaks! 🚀🎧
