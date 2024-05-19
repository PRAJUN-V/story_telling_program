from gtts import gTTS
import os
import random
from story import story_list

len_of_story_list = len(story_list)

text = story_list[random.randint(0, len_of_story_list - 1)]
tts = gTTS(text=text, lang='en')
tts.save("story.mp3")

os.system("start story.mp3")  

