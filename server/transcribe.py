import whisper
import sys

def generate_captions(video_path):
    print(f"Loading AI model and transcribing: {video_path}...")
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    
    # Print the full text found in the video
    print("\n--- Transcription Result ---")
    print(result["text"])
    print("----------------------------\n")

if __name__ == "__main__":
    # If you provide a file name when running the command, it will use it
    file_to_transcribe = sys.argv[1] if len(sys.argv) > 1 else "test.mp4"
    generate_captions(file_to_transcribe)
