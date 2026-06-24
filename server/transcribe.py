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
    print(f"DEBUG: Script started. Arguments received: {sys.argv}")
    
    if len(sys.argv) > 1:
        video_file = sys.argv[1]
        print(f"DEBUG: Found filename: {video_file}")
        
        if os.path.exists(video_file):
            print("DEBUG: File verified as existing. Starting transcription...")
            segments = generate_captions(video_file)
            for segment in segments:
                print(f"[{segment['start']:.2f}s]: {segment['text']}")
        else:
            print(f"DEBUG ERROR: The file '{video_file}' was not found by Python.")
    else:
        print("DEBUG ERROR: No arguments were passed to the script.")
