import speech_recognition as sr
import moviepy.editor as mp
clip=mp.VideoFileClip(r"Dog_story.mp4")
clip.audio.write_audiofile(r"audio_dog.wav")
r=sr.Recognizer()
audio=sr.AudioFile('audio_dog.wav')
with audio as source:
    audio_file=r.record(source)
result=r.recognize_google(audio_file)
with open('recognized.txt',mode='w') as file:
    file.write("Recgnized Speech:")
    file.write("\n")
    file.write(result)
    print("Your text is ready")
