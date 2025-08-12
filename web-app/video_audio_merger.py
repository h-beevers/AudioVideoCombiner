from flask import Flask, request, send_file, render_template
import subprocess
import os

app = Flask(__name__)

# Define upload and output folders relative to this script location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
OUTPUT_FOLDER = os.path.join(BASE_DIR, 'outputs')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        video = request.files["video"]
        audio = request.files["audio"]

        video_path = os.path.join(UPLOAD_FOLDER, video.filename)
        audio_path = os.path.join(UPLOAD_FOLDER, audio.filename)
        output_path = os.path.join(OUTPUT_FOLDER, "merged.mp4")

        # Save uploaded files
        video.save(video_path)
        audio.save(audio_path)

        # Run FFmpeg to merge video and audio
        cmd = [
            "ffmpeg", "-i", video_path, "-i", audio_path,
            "-shortest", "-c:v", "copy", "-c:a", "aac", output_path
        ]
        subprocess.run(cmd)

        # Serve the merged file for download
        return send_file(output_path, as_attachment=True)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)