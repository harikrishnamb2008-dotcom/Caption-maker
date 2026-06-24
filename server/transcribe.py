import whisper
import sys
import os

def generate_captions(video_path):
    print(f"DEBUG: Starting function with file: {video_path}")
    
    if not os.path.exists(video_path):
        print(f"DEBUG ERROR: File not found at {os.path.abspath(video_path)}")
        return None

    try:
        print("DEBUG: Loading Whisper model (this may take a minute)...")
        # 'base' model is a good balance of speed/accuracy
        model = whisper.load_model("base")
        
        print("DEBUG: Starting transcription...")
        # verbose=True will print progress to the console
        result = model.transcribe(video_path, verbose=True)
        
        print("DEBUG: Transcription process finished.")
        return result["segments"]
        
    except Exception as e:
        print(f"DEBUG ERROR: An error occurred: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        video_file = sys.argv[1]
        
        if os.path.exists(video_file):
            segments = generate_captions(video_file)
            
            if segments:
                print("\n--- TRANSCRIPTION OUTPUT ---")
                for segment in segments:
                    print(f"[{segment['start']:.2f}s]: {segment['text']}")
                print("----------------------------")
            else:
                print("DEBUG ERROR: No segments were returned. Check the debug logs above.")
        else:
            print(f"DEBUG ERROR: The file '{video_file}' was not found.")
    else:
        print("DEBUG ERROR: No video file argument provided. Usage: python server/transcribe.py <filename>")
