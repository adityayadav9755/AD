# Importing
import speech_recognition as sr
import os
import subprocess
import speak

# Setup & Variables
recog = sr.Recognizer()
say = speak.Speech()
a = ""
b = []
cmd2 = ""
name = ""
keywords = ["from", "preinstalled", "installed", "pre", "install", "open", "start"]
ext = {"text": [".txt"],
    "word": [".doc", ".docx"],
    "pdf": [".pdf"],
    "image": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "audio": [".mp3", ".wav", ".flac", ".aac"],
    "video": [".mp4", ".avi", ".mkv", ".mov"],
    "spreadsheet": [".xls", ".xlsx", ".csv"],
    "presentation": [".ppt", ".pptx"],
    "code": [".py", ".java", ".cpp", ".html", ".css"],
    "archive": [".zip", ".tar", ".rar"],
    "executable": [".exe", ".app"],
    "database": [".db", ".sqlite", ".dbf"]}


class Function:

    def recognize(self):
        with sr.Microphone() as source:
            say.speak(speech="Welcome Adi!")
            audio = recog.listen(source, timeout=3, phrase_time_limit=10)
        try:
            a = recog.recognize_google(audio)
            say.speak(speech=f"You said:{a}")

            for x in range(a.count(" ")):
                b.append(a[0:a.index(" ")])
                a = a[a.index(" ") + 1:len(a)]
            b.append(a)

        except sr.UnknownValueError:
            say.speak(speech="Couldn't hear that!")

        return b

    def path(self, cmnd):
        path = ""
        terminate = 0
        ind = cmnd.index("from")
        path = path + f"{cmnd[ind + 1]}:"
        for x in cmnd:
            if x in keywords:
                if x != "from":
                    terminate = cmnd.index(x)

        for x in range(ind + 2, terminate):
            path = path + f"{cmnd[x]}\\"
        return path

    def process(self, cmnd, func):
        if cmnd[0] == "start":
            apptype = cmnd[1]
            appname = cmnd[-1]
            func.start(appname, apptype)

        if cmnd[0] == "from":
            path = func.path(cmnd)
            if "open" in cmnd:
                fname = path + cmnd[cmnd.index("open") + 1]
                ftype = cmnd[-1].lower()
                func.open(fname, ftype)

        if cmnd[0] == "open":
            fname = cmnd[1]
            ftype = cmnd[2]
            func.open(fname, ftype)


    def start(self, appname, apptype):
        if apptype == "preinstalled" or apptype == "pre" or apptype == "preinstall":
            subprocess.run(["start", f"ms-{appname}:"], shell=True)
            say.speak(speech="Starting application...")
        elif apptype == "installed" or apptype == "install":
            os.system(f"start {appname}")
            say.speak(speech="Starting application...")
        else:
            say.speak(speech="Please specify app type as 'preinstalled' or 'installed' as 2nd argument.")

    def open(self, fname, ftype):
        for x in range(len(ext[ftype])):
            try:
                os.startfile(fname + ext[ftype][x])
            except FileNotFoundError:
                continue
            except ValueError:
                say.speak(speech="Please specify file type as 2nd argument.")
            else:
                say.speak(speech="Opening file...")
                break
            say.speak(speech="Mentioned file doesn't exist.")
    

