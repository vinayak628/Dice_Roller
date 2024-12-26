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
    elif roll==2:
        print("""
                -------
                |*    |
                |     |
                |    *|
                -------
              """)
    elif roll==3:
        print("""
                -------
                |*    |
                |  *  |
                |    *|
                -------
              """)
    elif roll==4:
        print("""
                -------
                |*   *|
                |     |
                |*   *|
                -------
              """)
    elif roll==5:
        print("""
                -------
                |*   *|
                |  *  |
                |*   *|
                -------
              """)
    else:
        print("""
                -------
                |*   *|
                |*   *|
                |*   *|
                -------
              """)

def main():
    die_rollor()

if __name__=='__main__':
    main()