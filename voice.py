# good tutorial - https://realpython.com/python-speech-recognition/

# https://www.geeksforgeeks.org/speech-recognition-in-python-using-google-speech-api/
import speech_recognition as sr

# Sample rate is how often values are recorded
sample_rate = 48000
# Chunk is like a buffer. It stores 2048 samples (bytes of data)
# here.
# it is advisable to use powers of 2 such as 1024 or 2048
chunk_size = 2048
# Initialize the recognizer
r = sr.Recognizer()

# id of microphone, it was 1 for me but default should be 0
device_id = 1

# use the microphone as source for input. Here, we also specify
# which device ID to specifically look for incase the microphone
# is not working, an error will pop up saying "device_id undefined"
with sr.Microphone(device_index=device_id, sample_rate=sample_rate, chunk_size=chunk_size) as source:
	# wait for a second to let the recognizer adjust the
	# energy threshold based on the surrounding noise level
	r.adjust_for_ambient_noise(source)
	print("Say Something")
	# listens for the user's input
	audio = r.listen(source)

	try:
		text = r.recognize_google(audio)
		print("you said: " + text)
		output = open("output.txt", "w")
		output.write(text)
		output.close()

	# error occurs when google could not understand what was said

	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")

	except sr.RequestError as e:
		print("Could not request results from Google Speech	Recognition	service; {0}".format(e))
