# AudioVideoCombiner

A simple tool to merge a video file and an audio track using FFmpeg. Available both as a Windows desktop app and a Flask web app.

---

## Desktop App (Windows)

A Windows app that merges a video file (e.g., .mp4) with an audio track (e.g., .mp3, .aac, .wav) using FFmpeg — no editing skills required.

### How to Use

1. **Download & Extract**
   - Unzip the folder and run: `AudioVideoCombiner.exe
`
2. **Select Your Files**
   - Choose a video file (MP4 recommended)
   - Choose an audio file (MP3, AAC, or WAV)
3. **Click "Combine and Save"**
   - Choose where to save the new video
   - The app will merge the files using FFmpeg

### Requirements

- Windows 11 (or Windows 10 with winget installed)
- FFmpeg* (used behind the scenes)

*If FFmpeg isn’t installed, the app will:*
- Try to install it using winget
- Or download it automatically from gyan.dev

No manual setup required.

### Notes

- The app uses FFmpeg’s `-shortest` flag to trim the output to the shorter of the two inputs.
- Your original files are never modified.
- If FFmpeg is already installed and in your system PATH, the app will use it automatically.

---

## Web App (Flask)

You can also run this as a web app using Flask. The web app allows you to upload a video and audio file, then merges them server-side using FFmpeg.

### How to Use

1. **Navigate to `web-app/` directory.**
2. **Install requirements** (if needed):
   ```bash
   pip install flask
   ```
3. **Run the Flask app:**
   ```bash
   python video_audio_merger.py
   ```
4. **Open your browser and go to** [http://localhost:5000](http://localhost:5000)
5. **Upload your video and audio files, then download the merged video.**

### Structure

```
web-app/
  ├── video_audio_merger.py
  └── templates/
      └── index.html
```

Uploads and outputs are stored in `web-app/uploads/` and `web-app/outputs/`.

### Requirements

- Python 3.x
- Flask
- FFmpeg (must be in your system PATH)

---

## What's Included

- `video_audio_combiner.exe` — the Windows app
- `web-app/` — Flask web app version
- `README.md` — this file

---

## License

MIT

---
