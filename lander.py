# Andy Zeyher
# Section 068

# fix negative altitude issue

import sys

# Initial Values
G = -1.622  # Pull of Gravity (m/s^2)
A = 50  # Altitude (m)
V = 0  # Velocity (m/s)
F = 150  # Units of Fuel
s = 0  # Number of seconds passed
T = 0.1  # Thruster Acceleration (m/s^2)
L = 1  # Level Number
valid = False  # def ask_fuel while loop condition
valid1 = False  # level_start while loop condition


# def function asking user for fuel
def ask_fuel(current_fuel):
    valid = False
    while valid == False:
        current_fuel = input('Enter units of fuel to use:')
        try:
            current_fuel = int(current_fuel)
            if (current_fuel < 0) or (current_fuel > F):
                print('Please make sure units of fuel entered is positive and less than or equal to'
                      ' amount of fuel left.')
                continue
            if (current_fuel >= 0) and (current_fuel <= F):
                valid = True
                return current_fuel
        except ValueError:
            print('Please enter an integer.')


# def function to play level with desired name, gravity, and units of fuel
def play_level(name, gravity, fuel):
    global G, A, V, F, s, T, L
    A = 50
    V = 0
    s = 0
    F = fuel
    print('Entering Level', L)
    print('Landing on', name)
    print('Gravity is', gravity, 'm/s^2')
    print('Initial Altitude:', A, 'meters')
    print('Initial Velocity:', V, 'm/s')
    print('Burning a unit of fuel causes', T, 'm/s slowdown.')
    print('Initial Fuel Level:', fuel, 'units\n')
    print('GO')
    while A > 0:
        f = ask_fuel(current_fuel=0)
        F = F - f
        V = V + gravity + (T * f)
        A = A + V
        s += 1
        print('After', s, 'seconds Altitude is', A, 'meters, velocity is', V, 'm/s')
        print('Remaining Fuel:', F, 'units.')
    while A <= 0:
        if (-2 <= V) and (V <= 2):
            print('Landed Successfully.')
            L += 1
            break
        else:
            print('Crashed!')
            break


# def function to ask whether or not the user would like to play the next level
def level_start(answer):
    global L
    valid1 = False
    while valid1 == False:
        answer = input()
        if answer == 'yes':
            valid1 = True
        elif answer == 'no':
            print('You made it past', L-1, 'levels.')
            print('Thank you for playing.')
            sys.exit()
        else:
            print('Please only enter "yes" or "no".')


# main program
print('Welcome to the Lunar Landing Game')
print('Do you want to play level', L, '? (yes/no)')
level_start(answer=' ')
play_level('the Moon', -1.622, 150)
while L == 1:
    print('Do you want to play level', L, '? (yes/no)')
    level_start(answer=' ')
    play_level('Moon', -1.622, 150)
while L == 2:
    print('Do you want to play level', L, '? (yes/no)')
    level_start(answer=' ')
    play_level('Earth', -9.81, 5000)
while L == 3:
    print('Do you want to play level', L, '? (yes/no)')
    level_start(answer=' ')
    play_level('Pluto', -0.42, 1000)
while L == 4:
    print('Do you want to play level', L, '? (yes/no)')
    level_start(answer=' ')
    play_level('Neptune', -14.07, 1000)
while L == 5:
    print('Do you want to play level', L, '? (yes/no)')
    level_start(answer=' ')
    play_level('Uranus', -10.67, 1000)
while L == 6:
    print('Do you want to play level', L, '? (yes/no)')
    level_start(answer=' ')
    play_level('Saturn', -11.08, 1000)
while L == 7:
    print('Do you want to play level', L, '? (yes/no)')
    level_start(answer=' ')
    play_level('Jupiter', -25.95, 1000)
while L == 8:
    print('Do you want to play level', L, '? (yes/no)')
    level_start(answer=' ')
    play_level('Mars', -3.77, 1000)
while L == 9:
    print('Do you want to play level', L, '? (yes/no)')
    level_start(answer=' ')
    play_level('Venus', -8.87, 1000)
while L == 10:
    print('Do you want to play level', L, '? (yes/no)')
    level_start(answer=' ')
    play_level('Mercury', -3.59, 1000)
while L == 11:
    print('Do you want to play level', L, '? (yes/no)')
    level_start(answer=' ')
    play_level('the Sun', -274.13, 50000)
    break
