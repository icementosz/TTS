import speech_recognition as sr
import pyaudio
from gtts import gTTS
from playsound import playsound

r = sr.Recognizer()
# print(r)
# print(sr.Microphone.list_microphone_names())
mic = sr.Microphone(1)

######################## พูดตาม ###########################

# with mic as source:
#     playsound("./startsound.mp3")
#     audio = r.listen(source)
#     playsound("./stopsound.mp3")


#     text = r.recognize_google(audio,language='th')
#     print("-----------------------------------------\n",text,"\n-----------------------------------------")

#     tts = gTTS(text, lang="th")
#     tts.save("./answer.mp3")
    


# playsound("./answer.mp3")

######################## Test Script ###########################

with mic as source:
    tts = gTTS("คุณเป็นอะไรมาคะ", lang="th")
    tts.save("./answer.mp3")
    playsound("./answer.mp3")

    playsound("./startsound.mp3")
    audio = r.listen(source)
    playsound("./stopsound.mp3")

    text = r.recognize_google(audio,language='th')
    print("-----------------------------------------\n",text,"\n-----------------------------------------")
    
    tts = gTTS("เป็นมากี่วันแล้วคะ", lang="th")
    tts.save("./answer1.mp3")
    playsound("./answer1.mp3")

    playsound("./startsound.mp3")
    audio = r.listen(source)
    playsound("./stopsound.mp3")

    text = r.recognize_google(audio,language='th')
    print("-----------------------------------------\n",text,"\n-----------------------------------------")

    setanswer = {'1 วัน','2 วัน'}
    if text not in setanswer:
        tts = gTTS("ฉันไม่เข้าใจ กรุณาพูดใหม่อีกครั้ง", lang="th")
        tts.save("./answer2.mp3")
        playsound("./answer2.mp3")
        

# with mic as source:
#     tts = gTTS("คุณชื่ออะไรคะ", lang="th")
#     tts.save("./answer.mp3")
#     playsound("./answer.mp3")
    
#     playsound("./startsound.mp3")
#     audio = r.listen(source)
#     playsound("./stopsound.mp3")


#     text = r.recognize_google(audio,language='th')
#     print("-----------------------------------------\n",text,"\n-----------------------------------------")

#     tts = gTTS("คุณน่าจะต้องหล่อมากๆแน่เลย", lang="th")
#     tts.save("./answer1.mp3")
#     playsound("./answer1.mp3")
