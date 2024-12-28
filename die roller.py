
import pyttsx3
import random

def die_rollor():

    roll=random.randint(1,6)

    if roll==1:
        print("""
                -------
                |     |
                |  *  |
                |     |
                -------""")
        engine=pyttsx3.init()
        engine.say("its a one")
        engine.runAndWait()
    elif roll==2:
        print("""
                -------
                |*    |
                |     |
                |    *|
                -------
              """)
        engine=pyttsx3.init()
        engine.say("its a two")
        engine.runAndWait()
    elif roll==3:
        print("""
                -------
                |*    |
                |  *  |
                |    *|
                -------
              """)
        engine=pyttsx3.init()
        engine.say("its a three")
        engine.runAndWait()
    elif roll==4:
        print("""
                -------
                |*   *|
                |     |
                |*   *|
                -------
              """)
        engine=pyttsx3.init()
        engine.say("its a four")
        engine.runAndWait()
    elif roll==5:
        print("""
                -------
                |*   *|
                |  *  |
                |*   *|
                -------
              """)
        engine=pyttsx3.init()
        engine.say("its a five")
        engine.runAndWait()
    else:
        print("""
                -------
                |*   *|
                |*   *|
                |*   *|
                -------
              """)
        engine=pyttsx3.init()
        engine.say("its a six")
        engine.runAndWait()

def main():
    die_rollor()

if __name__=='__main__':
    main()