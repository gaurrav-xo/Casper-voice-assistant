# Import necessary libraries

import speech_recognition as sr    # Allows speech to be recognized and converted to text using microphone input
import webbrowser                  # Opens URLs in the default web browser (like Chrome or Firefox)
import pyttsx3                     # Converts text to speech — makes the assistant talk
import wikipedia                   # Used to fetch summaries of topics from Wikipedia
import musiclibrary                # A custom module you created that stores song names and their URLs

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()       # This object helps convert spoken audio into text
engine = pyttsx3.init()            # This initializes the text-to-speech engine so the assistant can talk

# -------------------------------------------------------------------------------------
# Function: speak(text)
# Description:
#   This function takes a string input called 'text' and speaks it out loud.
#   It is used every time Casper needs to talk (give feedback, ask questions, say goodbye, etc.)
# -------------------------------------------------------------------------------------

def speak(text):  
    engine.say(text)            # Add the text to the speech queue (stores what needs to be said)
    engine.runAndWait()         # Speak everything in the queue out loud and wait until it's finished



# Function to get and speak a brief Wikipedia summary of a topic
def get_wikipedia_summary(topic):
    try:
        # Get the summary of the topic, limited to 2 sentences
        summary = wikipedia.summary(topic, sentences=3)

        # Speak the summary aloud
        speak(summary)

    except wikipedia.exceptions.DisambiguationError:
        # Triggered if the topic is too broad and matches multiple pages
        speak("This topic is too broad. Try being more specific.")

    except wikipedia.exceptions.PageError:
        # Triggered if the topic does not match any page
        speak("I couldn't find anything on Wikipedia for that topic.")

# -------------------------------------------------------------------------------------
# Function: process_command(command)
# Description:
#   This function receives a command (spoken by the user),
#   checks what kind of instruction it is (like open Google, play music, etc.),
#   and performs the correct action — either opening a site or playing a song.
# -------------------------------------------------------------------------------------
def process_command(command):
    command = command.lower()   # Convert the spoken command to lowercase to make checking easier
    print(f"[DEBUG] Command received: {command}")  # Log the command to console for debugging

    # Match specific voice commands with actions
    if "open google" in command:
        webbrowser.open("https://google.com")      # Opens Google in default browser

    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")    # Opens Facebook

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")     # Opens YouTube

    elif "open my instagram" in command:
        webbrowser.open("https://www.instagram.com/gaurrav.nx/")  # Opens your personal Instagram profile

    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")              # Opens Instagram homepage

    elif command.startswith("play"):  
        # Extract the song name after the keyword "play"
        Play, song = command.split(" ", 1)        # Splits the command into "play" and "song name"
        link = musiclibrary.music[song]           # Looks up the song URL in your music library
        webbrowser.open(link)                     # Opens the song URL in a new browser tab


    # Check if user said "who is" or "tell me about"
    elif command.startswith("who is") or command.startswith("tell me about"):

        # Remove trigger words to extract only the topic name
        # e.g., "who is Elon Musk" → "Elon Musk"
        # e.g., "tell me about Python" → "Python"
        topic = command.replace("who is", "").replace("tell me about", "").strip()

        # Call the function to fetch and speak the Wikipedia summary
        get_wikipedia_summary(topic)


    elif "exit" in command:  
        # When user says "exit", end the assistant
        speak("Goodbye!")                         # Say goodbye using TTS
        print("[INFO] Exiting program.")          # Show exit info in the console
        exit()                                    # Exit the program


    
    else:
        # If command is not recognized, apologize
        speak("Sorry, I didn't recognize that command.")
        print("[WARN] Unrecognized command.")

    


# -------------------------------------------------------------------------------------
# Main program execution begins here
# This part runs continuously, listens for the wake word "casper", and then performs actions.
# -------------------------------------------------------------------------------------
if __name__ == "__main__":
    speak("Hello, I am Casper")   # Casper introduces itself when the program starts

    while True:  # Loop forever until "exit" command is given
        try:
            # Start listening for the wake word "casper"
            with sr.Microphone() as mic:
                print("🎤 Say 'casper' to wake me up...")
                
                # Helps the recognizer filter out background noise for clearer input
                recognizer.adjust_for_ambient_noise(mic, duration=0.8)

                # Listen to the user's speech for 3 seconds (as wake word)
                audio = recognizer.listen(mic, timeout=3, phrase_time_limit=3)

                # Try to convert the audio input into text using Google’s API
                wake_word = recognizer.recognize_google(audio)
                print(f"[TRANSCRIPT] Wake word heard: {wake_word}")

                # If wake word "casper" is detected, move to command listening
                if wake_word.lower() == "casper":
                    speak("Yes, I'm listening.")  # Casper responds to confirm it's awake
                    print("🎧 Listening for your command...")

                    try:
                        # Start a second microphone session to capture the actual command
                        with sr.Microphone() as mic2:
                            recognizer.adjust_for_ambient_noise(mic2, duration=0.5)  # Filter noise again
                            command_audio = recognizer.listen(mic2, timeout=3, phrase_time_limit=3)  # Listen to command

                            command_text = recognizer.recognize_google(command_audio)  # Convert to text
                            print(f"[TRANSCRIPT] Command heard: {command_text}")

                            process_command(command_text)  # Pass the command to be handled

                    except sr.UnknownValueError:
                        # The speech was unclear or not understood
                        print("😕 I couldn't understand your command.")
                        speak("Sorry, I didn't catch that.")

                    except sr.RequestError:
                        # Could not connect to Google services
                        print("🌐 Google speech service is unavailable.")
                        speak("I can't connect to Google services.")

        # Error Handling for the wake-word section
        except sr.UnknownValueError:
            print("😕 I couldn't understand what you said.")  # Speech was unclear

        except sr.WaitTimeoutError:
            print("⌛ Timeout: You were silent.")  # No speech detected in time

        except sr.RequestError:
            print("🌐 Google servers not reachable.")  # Internet/service unavailable
