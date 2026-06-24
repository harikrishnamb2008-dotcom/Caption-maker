import whisper
import sys
import os

# --- IMPORTANT: UPDATE THIS PATH TO WHERE FFMPEG IS ON YOUR PC ---
FFMPEG_LOCATION = r"C:\ffmpeg\bin\ffmpeg.exe"
# -----------------------------------------------------------------

def generate_captions(video_path):
    # Verify FFmpeg exists
    if not os.path.exists(FFMPEG_LOCATION):
        print(f"ERROR: Could not find ffmpeg.exe at {FFMPEG_LOCATION}")
        print("Please install FFmpeg and update the FFMPEG_LOCATION path in this script.")
        return

    # Point the script to the folder containing ffmpeg
    os.environ["PATH"] += os.pathsep + os.path.dirname(FFMPEG_LOCATION)

    print("DEBUG: Loading Whisper model (this may take a minute)...")
    try:
        model = whisper.load_model("base")
        print("DEBUG: Starting transcription...")
        
        # 'verbose=True' prints the progress bars to your terminal
        result = model.transcribe(video_path, verbose=True)
        
        print("\n--- TRANSCRIPTION OUTPUT ---")
        print(result["text"])
        print("----------------------------")
        
    except Exception as e:
        print(f"DEBUG ERROR: Transcription failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_file = sys.argv[1]
        if os.path.exists(video_file):
            generate_captions(video_file)
        else:
            print(f"ERROR: File '{video_file}' not found.")
    else:
        print("Usage: python transcribe.py <path_to_video>")
