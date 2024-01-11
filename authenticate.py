import speech_recognition as sr


# Function to capture user's voice
def record_user_voice():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Speak something...")
        audio = recognizer.listen(source)

    return recognizer, audio


# Function to recognize user's voice
def recognize_user_voice(recognizer, audio):
    try:
        recognized_text = recognizer.recognize_google(audio)
        return recognized_text.lower() if recognized_text else None
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
        return None
    except sr.RequestError:
        print("Failed to fetch results. Please check your internet connection.")
        return None


# Example of user authentication based on recognized text similarity
def authenticate_user(recognized_text, user_voice_pattern):
    # Compare recognized text with user's voice pattern
    similarity_threshold = 0.6  # Adjust the threshold as needed
    # Here, user_voice_pattern should contain known phrases or patterns from the specific user

    if recognized_text:
        similarity_score = similar(recognized_text, user_voice_pattern)
        if similarity_score >= similarity_threshold:
            print("User authenticated.")
            return True
        else:
            print("Voice doesn't match the user profile.")
    else:
        print("No audio input detected.")

    return False


# Function to measure similarity (e.g., using Levenshtein distance)
def similar(a, b):
    # Implement a similarity metric like Levenshtein distance or use ML-based comparison methods
    # Return a similarity score between the recognized text and user's voice pattern
    return 0.7  # Placeholder value, implement your similarity logic here


# Usage
def main():
    user_voice_pattern = "sample voice pattern"  # Placeholder, should contain known phrases from the user

    recognizer, audio = record_user_voice()
    recognized_text = recognize_user_voice(recognizer, audio)

    authenticated = authenticate_user(recognized_text, user_voice_pattern)
    if authenticated:
        # Perform actions or call the assistant function here
        print("Assistant activated.")
    else:
        print("Authentication failed.")


if __name__ == "__main__":
    main()
