from core.bytes import Bytes
from game.message.server.S_EACH_SKILL_RESULT import S_EACH_SKILL_RESULT
from util import tipo


data = Bytes([0, 0, 0, 0, 90, 54, 164, 15, 0, 128, 0, 1, 90, 54, 164, 15, 0, 128, 0, 1, 15, 39, 0, 0, 86, 131, 149, 7, 0, 0, 0, 0, 0, 0, 0, 0, 64, 153, 24, 4, 103, 30, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

p = S_EACH_SKILL_RESULT(None, None, None, data, "USA")

print(p)


