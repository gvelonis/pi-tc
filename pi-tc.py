import libpitc

print("Expect 11 captures")
count = libpitc.timelapse2(1, 10, rotation=270)
if count == None:
    print("Error occured")
else:
    print("Captured ", count, " images.")
