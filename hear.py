#Import the required packages
import speech_recognition as sr

#Initialize the recognizer
rec = sr.Recognizer()
#Record the user command; convert to text and store it in a variable
def record_text():
    #Loop in case of errors
    while(1):
        try:
            #use the microphone as source for input. 
            with sr.Microphone() as source:
                # Prepare recognizer to receive input
                rec.adjust_for_ambient_noise(source, duration=0.2)

                #listens for the user's input
                audio = rec.listen(source)

                #Using google to recognize audio
                MyText = rec.recognize_google(audio)

                return MyText

        except sr.RequestError as e:
            print("Could not request results; (0)".format(e))

        except sr.UnknownValueError:
            print("Unknown error occurred")

#Store the converted text into a .txt file
def output_text(text):
    file = open("output.txt", "a")
    file.write(text)
    file.write("\n")
    file.close()

#Main block
text="start"
while(text != "stop"):
    print("Started Recording")
    text = record_text()
    output_text(text)
    print(f"The converted text is {text}")
    print("Text converted and stored")

print("Stopped Recording")