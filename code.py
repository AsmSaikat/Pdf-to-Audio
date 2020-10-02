import pyttsx3
import PyPDF2

book = open(input("Please type you book's name with extension: ") + ".pdf", "rb")
# rb: Opens the file as read-only in binary format and starts reading from the beginning of the file

pdf = PyPDF2.PdfFileReader(book)

# init function to get an engine instance for the speech synthesis
engine = pyttsx3.init()

print("Please choose pages you want to create audiobook with:")
start = input("Start: ")
end = input("End: ")

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

    # say method on the engine that passing input text to be spoken.
    engine.say(text_extractor)

    # run and wait method, it processes the voice commands.
    engine.runAndWait()
