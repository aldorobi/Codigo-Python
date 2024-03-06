import time

def CounterDownTimer(seconds):
    while seconds > 0 : 
        mins = int(seconds/60)
        secs = int(seconds%60)
        timer = f'{mins}:{secs}'
        print(timer)
        seconds -= 0.00001
    print('Time’s over')
seconds = input('Elija tiempo de contador : ')
CounterDownTimer(int(seconds))
