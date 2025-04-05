import os
import random as Random


for i in range(5):
    data = Random.randint(1, 1000)
    with open("data.txt", "a") as f:
        f.write(f"{data}\n")
    os.system("git add .")
    os.system("git commit -m 'update'")
    os.system("git push origin main")
