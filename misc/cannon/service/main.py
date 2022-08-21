#!/usr/bin/python3

from secrets import randbelow
from random import random
from decimal import Decimal, getcontext

getcontext().prec = 30

FLAG = "greyhats{please_dont_randomly_fire_cannon_ball_nIm4TzR4jfEdrf6C}"

rounds = 100
g = Decimal(-9.8)

art = """
     .-._______
  .={ . }..--"" -   -.      
 [/"`._.'    fsc          . 
 ---------------------|       .
| |        |        | |          .
| |        |        | |            .
| |        |        | |              .
| |        |        | |               O
| |        |        | |        .-. _______|
| |        |        | |        |=|/     /  \\
| |        |        | |        | |_____|_""_|
| |        |        | |        |_|_[X]_|____|
 ---------------------|          

"""

def menu():
    print(art)
    print("NUS Greyhats is under attack by NUS Hackers! (JK Btw :p) They are using cannons to attack our base")
    print("Their cannons can fire from any location in the 3D Space")
    print("We need to find the location of the cannons and destroy them\n")
    print("Fortunately, we have a detection system that can tell us the exact position of a cannon ball\n")
    print("2 coordinates for a cannon ball at different time t_i (in seconds since the moment of fire) will be provided to you")
    print("Your task is to find the exact coordinates of the cannon and the impact velocity of the cannon ball\n")
    print("The input will be in the following format:")
    print("(x1, y1, z1, t1) -- position of the cannon ball at time t1")
    print("(x2, y2, z2, t2) -- position of the cannon ball at time t2")
    print("You should output:")
    print("(x, y, z) -- location of the cannon")
    print("(v_x, v_y, v_z) -- impact velocity of the cannon ball\n")
    print("Note:")
    print("1. z entry in the coordinate represents the height. (Must be non-negative)")
    print("2. Ignore air resistance and take g = -9.8 m/s^2")
    print("3. The impact velocity means the velocity of the cannonball when z = 0 at t > 0")
    print("4. Your answer must be within 0.00001 of error\n")
    print(f"If you answer correctly for {rounds} times, then we will give you the flag\n")

def randomSign():
    return 1 if randbelow(2) == 0 else -1

def gen():
    x = randomSign() * randbelow(10000)
    y = randomSign() * randbelow(10000)
    z = randbelow(10000)

    vx = randomSign() * randbelow(10000)
    vy = randomSign() * randbelow(10000)
    vz = randbelow(10000)

    maxT = (-vz - Decimal(vz * vz - 2 * g * z).sqrt()) / g
    
    t1 = Decimal(random()) * maxT
    t2 = Decimal(random()) * maxT

    s1 = (x + vx * t1, y + vy * t1, z + vz * t1 + g * t1 * t1 / 2, t1)
    s2 = (x + vx * t2, y + vy * t2, z + vz * t2 + g * t2 * t2 / 2, t2)

    return ((s1, s2), (x, y, z), (vx, vy, vz + g * maxT))

def main():
    menu()
    for round in range(rounds):
        print("Round", round + 1)
        output, coord, velocity = gen()
        for i in range(2):
            t = list(map(lambda x : "{:.15f}".format(x), output[i]))
            print(f"({t[0]}, {t[1]}, {t[2]}, {t[3]})")
        print()
        
        try:
            inCoorRaw = input("Cannon coordinate: ")
            inVelocityRaw = input("Impact velocity: ")
            assert inCoorRaw[0] == '(' and inCoorRaw[-1] == ')'
            assert inVelocityRaw[0] == '(' and inVelocityRaw[-1] == ')'
            inCoor = list(map(lambda x : Decimal(x.strip()), inCoorRaw[1:-1].split(",")))
            inVelocity = list(map(lambda x : Decimal(x.strip()), inVelocityRaw[1:-1].split(",")))
            assert len(inCoor) == 3
            assert len(inVelocity) == 3
        except:
            print("Input Format Incorrect!")
            exit(0)

        for i in range(3):
            if (abs(inCoor[i] - coord[i]) >= 0.00001):
                print("We dont find any cannon there, your coordinate is incorrect")
                print("The correct answer should be", f"({coord[0]}, {coord[1]}, {coord[2]})")
                exit(0)

        for i in range(3):
            if (abs(inVelocity[i] - velocity[i]) >= 0.00001):
                print("Incorrect Velocity")
                print("The correct velocity should be", f"({velocity[0]}, {velocity[1]}, {'{:.6f}'.format(velocity[2])})")
                exit(0)

    print(f"Well done! Here's your flag {FLAG}")

if __name__ == "__main__":
    main()

