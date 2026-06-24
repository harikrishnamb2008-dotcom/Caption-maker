import whisper
import sys
import os

print("--- Debugging Start ---")

# 1. Print the arguments received
print(f"Arguments received: {sys.argv}")

# 2. Check if the file path is valid
file_path = sys.argv[1] if len(sys.argv) > 1 else "None"
print(f"Looking for file at: {os.path.abspath(file_path)}")
print(f"Does file exist? {os.path.exists(file_path)}")

# 3. Load the model
print("Loading model...")
model = whisper.load_model("base")
print("Model loaded.")

# 4. Transcribe
print("Attempting to transcribe...")
result = model.transcribe(file_path)
print("Transcription finished.")

# 5. Print text
print("Text found:", result["text"])
