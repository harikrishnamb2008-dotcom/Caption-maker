from fastapi import FastAPI, UploadFile, File
import whisper
import shutil
import os

# --- IMPORTANT: Ensure this path matches your actual ffmpeg.exe location ---
FFMPEG_PATH = r"C:\ffmpeg\bin\ffmpeg.exe"

# Point the system to the folder containing ffmpeg
if os.path.exists(FFMPEG_PATH):
    os.environ["PATH"] += os.pathsep + os.path.dirname(FFMPEG_PATH)
else:
    print(f"WARNING: FFmpeg not found at {FFMPEG_PATH}. Transcription might fail.")

app = FastAPI()

# Load the model once when the server starts so it's ready for requests
print("DEBUG: Loading Whisper model...")
model = whisper.load_model("base")
print("DEBUG: Model loaded and ready.")

@app.post("/transcribe")
async def transcribe_video(file: UploadFile = File(...)):
    # Create a temporary file to save the uploaded video
    temp_filename = f"temp_{file.filename}"
    
    with open(temp_filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    try:
        # Run the transcription
        result = model.transcribe(temp_filename)
        transcribed_text = result["text"]
    finally:
        # Always delete the temporary file, even if an error occurs
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
    
    return {"text": transcribed_text}

