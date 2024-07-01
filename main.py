import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")

    engine = pyttsx3.init()

    while True:
        x = input("Enter what you want me to speak (enter 'q' to quit): ")

        if x.lower() == 'q':
            break

        engine.say(x)
        engine.runAndWait()

    engine.stop()
    print("Goodbye!")




