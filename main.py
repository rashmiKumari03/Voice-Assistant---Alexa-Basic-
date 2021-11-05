import speech_recognition as sr
import pyttsx3
import pywhatkit #access by alexa like...youtube,spotify or any application.
import datetime
import wikipedia
import sys
import pyjokes

listener = sr.Recognizer()

engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)       #set the male voice to female.

def engine_talk(text):        #We have defined the engine talk
                              #But to talk , we need to call the fun user_command.
    engine.say(text)

    engine.runAndWait()

def user_commands():
    try:
       with sr.Microphone() as source:
            print("Start Speaking!!!")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()       #This lowerfunction will use because, in name first letter starts with capital,
                                      # and it may create issue sometimes
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except:
        pass
    return command

#Next is to what alexa needs to do.

def run_alexa():

    engine_talk(" I am Alexa, Your Personal Assistant, How Can i help You?")
    command=user_commands()
    #listens or command is given using fun created above.

    if 'play' in command:
        song=command.replace('play',' ')
        engine_talk('Sure, Playing' +song) #this is function call.
        #As dont want that playing alexa play.... this statement we want to remove alexa word from sentence. so..
        print("Here we go playing....",song)

        pywhatkit.playonyt(song)   #play on utube is the command here , which we get from lib pywhatkit.

    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        engine_talk('The current time is' +time)

    elif 'nice'  in command:
        engine_talk('Thank you!you too  ashok sir.')


    elif 'sad'  in command:
       engine_talk('No worries i am with your dear...lets listen some songs')
       engine_talk('Which song would you like to listen...just say it!')
       command = user_commands()  # listens or command is given using fun created above.
       if 'play' in command:
           song = command.replace('play', ' ')
           engine_talk('Sure, Playing' + song)  # this is function call.
           # As dont want that playing alexa play.... this statement we want to remove alexa word from sentence. so..
           print("Here we go playing....", song)

           pywhatkit.playonyt(song)


    elif 'who' in command:
        name=command.replace('who','')
        info=wikipedia.summary(name,1)
        print(info)
        engine_talk(info)

    elif 'joke' in  command:
        print(command)
        j=pyjokes.get_joke()
        print(j)
        engine_talk(j)

    elif 'can you hear me' in command:

        print('yes i can hear you how can i help you')
        engine_talk('yes i can hear you how can i help you')
        # engine_talk('can you repeat again')
        command = user_commands()
        # listens or command is given using fun created above.
        if 'play' in command:
            song = command.replace('play', ' ')
            engine_talk('Sure, Playing' + song)  # this is function call.
            # As dont want that playing alexa play.... this statement we want to remove alexa word from sentence. so..
            print("Here we go playing....", song)

            pywhatkit.playonyt(song)  # play on utube is the command here , which we get from lib pywhatkit.

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            engine_talk('The current time is' + time)

        elif 'nice' in command:
            engine_talk('Thank you!you too  ashok sir.')


        elif 'sad' in command:
            engine_talk('No worries i am with your dear...lets listen some songs')
            engine_talk('Which song would you like to listen...just say it!')
            command = user_commands()  # listens or command is given using fun created above.
            if 'play' in command:
                song = command.replace('play', ' ')
                engine_talk('Sure, Playing' + song)  # this is function call.
                # As dont want that playing alexa play.... this statement we want to remove alexa word from sentence. so..
                print("Here we go playing....", song)

                pywhatkit.playonyt(song)


        elif 'who' in command:
            name = command.replace('who', '')
            info = wikipedia.summary(name, 1)
            print(info)

            engine_talk(info)


        elif 'joke' in command:
            print(command)
            j = pyjokes.get_joke()
            print(j)
            engine_talk(j)


        elif 'stop' in command:
            print('Here we stop')
            engine_talk(" Yeah sure, Bye, we  will  meet  soon!")
            sys.exit()



    elif 'stop' in command:
        print('Here we stop')
        engine_talk(" Yeah sure, Bye, we  will  meet  soon!")
        sys.exit()

    else:
       engine_talk(' Sorry But , I could not hear you properly!')



run_alexa()

