try:
    import snake
except ModuleNotFoundError:
    import os
    os.system("python lib/setup.py install")
finally:
    import snake

best = 0
with open("./score.txt", "r+") as file:
    best=file.readlines()[0]

if not best.isdigit():
    raise Exception("score is not a int")
best = int(best)

best, score = snake.play(best)

with open("./score.txt", "w+") as file:
    file.write(f"{best}")

print("You have made a great job", score)
