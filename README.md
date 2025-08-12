VIDEO + AUDIO COMBINER
=======================

A simple Windows app that merges a video file (e.g. .mp4) with an audio track (e.g. .mp3, .aac, .wav) using FFmpeg — no editing skills required.

-----------------------
HOW TO USE
-----------------------

1. Download & Extract
   - Unzip the folder and run: video_audio_combiner.exe

2. Select Your Files
   - Choose a video file (MP4 recommended)
   - Choose an audio file (MP3, AAC, or WAV)

3. Click "Combine and Save"
   - Choose where to save the new video
   - The app will merge the files using FFmpeg

-----------------------
REQUIREMENTS
-----------------------

- Windows 11 (or Windows 10 with winget installed)
- FFmpeg* (used behind the scenes)

*If FFmpeg isn’t installed, the app will:
- Try to install it using winget
- Or download it automatically from gyan.dev

No manual setup required.

-----------------------
WHAT'S INCLUDED
-----------------------

- video_audio_combiner.exe — the standalone app
- README.txt — this file

-----------------------
NOTES
-----------------------

- The app uses FFmpeg’s -shortest flag to trim the output to the shorter of the two inputs.
- Your original files are never modified.
- If FFmpeg is already installed and in your system PATH, the app will use it automatically.

-----------------------
END