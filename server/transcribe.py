# /server/transcribe.py
import whisper

def generate_captions(video_path):
    # Load the Whisper model
    model = whisper.load_model("base")
    
    # Transcribe the video
    result = model.transcribe(video_path)
    
    # Return the text and timestamps
    return result["segments"]

# Example usage (Placeholder)
if __name__ == "__main__":
    print("AI Transcription Service Initialized.")
