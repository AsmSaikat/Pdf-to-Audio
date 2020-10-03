import pyttsx3
import PyPDF2

book = open(input("Please type you book's name: ") + ".pdf", "rb")
# rb: Opens the file as read-only in binary format and starts reading from the beginning of the file.

# this will initialize the PdfFileReader object.
pdf = PyPDF2.PdfFileReader(book)

# using init function to get an engine instance for the speech synthesis.
engine = pyttsx3.init()

print("Please choose pages you want to create audiobook with-")
start = input("Start: ")
end = input("End: ")

# now we will try verifying whether the start or end input is valid or not.
try:
    int(start) and int(end)
except ValueError:
    print("Please enter a valid number by running the program again.")
    exit()

# creating a loop to specify the start and end range of the book's pages.
for num in range(int(start), int(end)):
    # using getPage() method to get specific pages.
    page = pdf.getPage(num)

    # using extractText() to extract texts from pages.
    text_extractor = page.extractText()

    # retrieving the value and selecting the WPM(Words Per Minute) rate of voices.
    voices = engine.getProperty("voices")
    rate = engine.setProperty("rate", int(input("Please select WPM: ")))
    
    # selecting voice.
    print("Which voice would you prefer?")
    select = input("Type M for Male Voice or Type F for Female Voice: ")
    if select == "M" or select == "m":
        engine.setProperty("voice", voices[0].id)
    elif select == "F" or select == "f":
        engine.setProperty("voice", voices[1].id)
    else:
        print("Please use a valid input by running the program again.")
        break

    # say method on the engine that passing input text to be spoken.
    engine.say(text_extractor)

    # run and wait method, it processes the voice commands.
    engine.runAndWait()
