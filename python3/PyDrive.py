from ev3dev.auto import *
#import time

#m1 = Motor(OUTPUT_B)
#m2 = Motor(OUTPUT_C)

#m1.run_timed(time_sp=100, speed_sp=500)
#m2.run_timed(time_sp=100, speed_sp=500)

motors = [LargeMotor(address) for address in (OUTPUT_B, OUTPUT_C)]

for m in motors:
    m.run_timed(time_sp = 1000, speed_sp = -600)