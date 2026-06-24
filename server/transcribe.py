import whisper
import sys
import os

def generate_captions(video_path):
    print(f"DEBUG: Starting function with file: {video_path}")
    
    if not os.path.exists(video_path):
        print(f"DEBUG ERROR: File not found at {os.path.abspath(video_path)}")
        return

    print("DEBUG: Loading Whisper model...")
    try:
        model = whisper.load_model("base")
        print("DEBUG: Model loaded successfully.")
    except Exception as e:
        print(f"DEBUG ERROR: Failed to load model: {e}")
        return

    print("DEBUG: Starting transcription...")
    try:
        result = model.transcribe(video_path)
        print("DEBUG: Transcription process finished.")
        print("\n--- TRANSCRIPTION OUTPUT ---")
        print(result["text"])
        print("----------------------------")
    except Exception as e:
        print(f"DEBUG ERROR: Transcription failed: {e}")

if __name__ == "__main__":
    print("AI Transcription Service Initialized.")
    if len(sys.argv) > 1:
        generate_captions(sys.argv[1])
    else:
        print("ERROR: No filename provided.")
