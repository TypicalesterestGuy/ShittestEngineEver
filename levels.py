from Level import *
from Objects import *

level1 = Level(False, "self/Assets/Backgrounds/bg1.png", [30, 30])
test = SolidObject([500, 500], "Assets/Objects/FirstObjectEver", "FirstObjectEver.png", [50, 50])
test1 = SolidObject([550, 550], "Assets/Objects/FirstObjectEver", "FirstObjectEver.png", [50, 50])
test2 = SolidObject([500, 550], "Assets/Objects/FirstObjectEver", "FirstObjectEver.png", [50, 50])
test3 = SolidObject([400, 400], "Assets/Objects/SecondObj", "lol.png", [130, 111])
level1.addobj(test, test1, test2, test3)
levels = []
levels.append(level1)