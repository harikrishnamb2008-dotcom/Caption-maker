import whisper
import sys
import os

def generate_captions(video_path):
    # Check if the file actually exists
    if not os.path.exists(video_path):
        print(f"Error: Could not find the file '{video_path}'")
        return

    print(f"Loading AI model... (this may take a moment)")
    model = whisper.load_model("base")
    
    print(f"Transcribing: {video_path}...")
    result = model.transcribe(video_path)
    
    print("\n--- Transcription Result ---")
    print(result["text"])
    print("----------------------------\n")

if __name__ == "__main__":
    # Get the file from the command line argument
    if len(sys.argv) > 1:
        file_to_transcribe = sys.argv[1]
        generate_captions(file_to_transcribe)
    else:
        print("Please provide a video file path. Example: python server/transcribe.py vid.mp4")
