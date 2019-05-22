import time

time_in = input("Enter the cooking time in seconds:")
time_int = int(time_in)

print(" Time set for boling eggs is:", time_int)
print("Put the egg in boiling water now:")

time.sleep(time_int)

print("Take the egg out now")
