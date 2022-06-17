from time import sleep

h = int(input("Enter Hours : "))
m = int(input("Enter Minutes : "))
s = int(input("Enter Seconds : "))

if s >= 60:
    m += s // 60
    s = s % 60

if m >= 60:
    h += m // 60
    m = m % 60

for H in range(h, -1, -1):
    for M in range(m, -1, -1):
        for S in range(s, -1, -1):
            print("{h:02d}:{m:02d}:{s:02d}".format(h=H, m=M, s=S))
            sleep(1)
        s = 59
    m = 59

print("\n\nTime's up..")
